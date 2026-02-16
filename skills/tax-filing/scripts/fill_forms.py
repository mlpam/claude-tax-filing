#!/usr/bin/env python3
"""Reusable PDF form-filling engine for tax forms.

Usage:
    from fill_forms import fill_pdf

    fill_pdf("blank.pdf", "filled.pdf",
             {"field_name": "value"},
             {"checkbox_name": True})
"""

from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    NameObject, BooleanObject, DictionaryObject
)


def fill_pdf(input_path, output_path, field_values, checkbox_values=None):
    """Fill a PDF form with given field values and checkbox states.

    Args:
        input_path: Path to blank PDF form
        output_path: Path to write filled PDF
        field_values: Dict of {field_name: string_value} for text fields
        checkbox_values: Dict of {field_name: bool} for checkboxes
    """
    reader = PdfReader(input_path)
    writer = PdfWriter()
    writer.append(reader)

    # Remove XFA to force AcroForm rendering
    if "/AcroForm" in writer._root_object:
        acroform = writer._root_object["/AcroForm"]
        if isinstance(acroform, DictionaryObject) and "/XFA" in acroform:
            del acroform["/XFA"]

    # Fill text fields
    for page in writer.pages:
        writer.update_page_form_field_values(
            page, field_values, auto_regenerate=False
        )

    # Handle checkboxes
    if checkbox_values:
        for page in writer.pages:
            annots = page.get("/Annots")
            if not annots:
                continue
            for annot_ref in annots:
                annot = annot_ref.get_object()
                field_name = _get_full_name(annot)
                if field_name in checkbox_values:
                    val = checkbox_values[field_name]
                    if val:
                        annot.update({
                            NameObject("/V"): NameObject("/1"),
                            NameObject("/AS"): NameObject("/1"),
                        })
                    else:
                        annot.update({
                            NameObject("/V"): NameObject("/Off"),
                            NameObject("/AS"): NameObject("/Off"),
                        })

    # Set NeedAppearances so PDF viewer regenerates appearance
    if "/AcroForm" in writer._root_object:
        writer._root_object["/AcroForm"].update({
            NameObject("/NeedAppearances"): BooleanObject(True)
        })

    writer.write(output_path)
    print(f"  Written: {output_path}")


def _get_full_name(annot):
    """Get full field name by walking the /Parent chain."""
    parts = []
    obj = annot
    while obj:
        t = obj.get("/T", "")
        if t:
            parts.insert(0, str(t))
        parent = obj.get("/Parent")
        if parent:
            obj = parent.get_object()
        else:
            break
    return ".".join(parts)
