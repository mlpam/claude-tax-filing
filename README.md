# Tax Filing Skill for Claude Code

A Claude Code skill that prepares federal (IRS) and state (CA) income tax returns end-to-end:

1. **Reads** your W-2, 1099-INT, 1099-DIV, 1099-B, and brokerage CSVs
2. **Computes** federal 1040, Schedule D, Form 8949, and CA Form 540
3. **Fills** the official IRS/FTB PDF forms programmatically
4. **Verifies** every field and presents a checklist of what was checked

## What It Handles

- W-2 wages and withholding
- Interest and dividend income (1099-INT, 1099-DIV)
- Stock and option sales (1099-B / Form 8949 / Schedule D)
- Capital loss carryovers from prior years
- Qualified Dividends and Capital Gain Tax Worksheet
- California Form 540 with state brackets and exemption credits
- Standard or itemized deductions

## Installation

### Claude Code CLI

```bash
# Add as a plugin marketplace, then install
/plugin marketplace add youruser/claude-tax-filing
/plugin install tax-filing
```

### Manual

Copy the `skills/tax-filing/` directory into your project or user `.claude/skills/` folder:

```bash
cp -r skills/tax-filing ~/.claude/skills/
```

## Usage

In Claude Code, say any of:
- "do my taxes"
- "prepare tax return"
- "fill tax forms"

The skill will walk you through gathering documents, confirming filing details, computing everything, and filling the PDFs.

## Requirements

- Python 3.10+
- `pypdf` — for filling all PDF forms
- `PyMuPDF` (`fitz`) — for discovering IRS XFA field names

```bash
pip install pypdf PyMuPDF
```

## Disclaimer

This skill is a tax preparation aid, not professional tax advice. Always review the filled forms carefully and consult a tax professional if you have questions about your specific situation.
