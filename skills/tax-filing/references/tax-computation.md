# Tax Computation Reference (2024)

## Federal Tax Brackets (2024) - Single

| Taxable Income | Rate | Tax on Lower | Of Amount Over |
|----------------|------|--------------|----------------|
| $0 - $11,600 | 10% | $0 | $0 |
| $11,601 - $47,150 | 12% | $1,160 | $11,600 |
| $47,151 - $100,525 | 22% | $5,426 | $47,150 |
| $100,526 - $191,950 | 24% | $17,168.50 | $100,525 |
| $191,951 - $243,725 | 32% | $39,110.50 | $191,950 |
| $243,726 - $609,350 | 35% | $55,678.50 | $243,725 |
| Over $609,350 | 37% | $183,647.25 | $609,350 |

### Federal Tax Brackets - Married Filing Jointly

| Taxable Income | Rate | Tax on Lower | Of Amount Over |
|----------------|------|--------------|----------------|
| $0 - $23,200 | 10% | $0 | $0 |
| $23,201 - $94,300 | 12% | $2,320 | $23,200 |
| $94,301 - $201,050 | 22% | $10,852 | $94,300 |
| $201,051 - $383,900 | 24% | $34,337 | $201,050 |
| $383,901 - $487,450 | 32% | $78,221 | $383,900 |
| $487,451 - $731,200 | 35% | $111,357 | $487,450 |
| Over $731,200 | 37% | $196,669.50 | $731,200 |

## Standard Deductions (2024)

| Filing Status | Amount |
|---------------|--------|
| Single | $14,600 |
| Married Filing Jointly | $29,200 |
| Married Filing Separately | $14,600 |
| Head of Household | $21,900 |

## QDCG Tax Worksheet (Qualified Dividends and Capital Gain Tax)

Use this when the taxpayer has qualified dividends (1040 Line 3a > 0) or net capital gain (Schedule D Line 15 > 0, or Line 16 > 0).

### Steps:
1. **Line 1**: Taxable income (Form 1040 Line 15)
2. **Line 2**: Qualified dividends (Form 1040 Line 3a)
3. **Line 3**: Schedule D Line 15 (if > 0), else capital gain from 1040 Line 7 (if > 0), else 0
4. **Line 4**: Add lines 2 + 3
5. **Line 5**: Investment interest expense deduction (if applicable, usually 0)
6. **Line 6**: Subtract line 5 from line 4
7. **Line 7**: Subtract line 6 from line 1 (this is ordinary income)
8. **Line 8**: Enter $47,025 (single) or $94,050 (MFJ) — 0% capital gains threshold
9. **Line 9**: Smaller of line 1 or line 8
10. **Line 10**: Smaller of line 7 or line 9
11. **Line 11**: Subtract line 10 from line 9 (taxed at 0%)
12. **Line 12**: Smaller of line 1 or line 6
13. **Line 13**: Line 11
14. **Line 14**: Subtract line 13 from line 12
15. **Line 15**: Enter $518,900 (single) or $583,750 (MFJ) — 15% capital gains threshold
16. **Line 16**: Smaller of line 1 or line 15
17. **Line 17**: Add lines 7 + 11
18. **Line 18**: Subtract line 17 from line 16 (if ≤ 0, enter 0)
19. **Line 19**: Smaller of line 14 or line 18
20. **Line 20**: Multiply line 19 by 15%
21. **Line 21**: Subtract line 19 from line 14
22. **Line 22**: Multiply line 21 by 20%
23. **Line 23**: Tax on line 7 (ordinary income) using regular brackets
24. **Line 24**: Add lines 20 + 22 + 23
25. **Line 25**: Tax on line 1 using regular brackets (full taxable income)
26. **Line 26**: **Tax = smaller of line 24 or line 25**

### Example (2024, Single, $40,764 taxable, $834 qualified dividends):
- Line 1: $40,764
- Line 2: $834 (qualified dividends)
- Line 3: $0 (net capital loss, so 0)
- Line 6: $834
- Line 7: $39,930 (ordinary)
- Line 9: $40,764 (smaller of 40,764 or 47,025)
- Line 10: $39,930
- Line 11: $834 (taxed at 0%)
- Line 12: $834
- Line 14: $0
- Tax on $39,930 ordinary = $1,160 + 12% × ($39,930 - $11,600) = $1,160 + $3,399.60 = $4,559.60 → $4,559
- QDCG tax: $4,559

## Capital Loss Rules

- **Annual deduction limit**: $3,000 ($1,500 if MFS) against ordinary income
- **Carryover**: Excess losses carry forward indefinitely
- **Carryover character**: Short-term losses offset short-term gains first; long-term losses offset long-term gains first
- **Netting order**:
  1. Net short-term gains/losses within Part I
  2. Net long-term gains/losses within Part II
  3. Combine on Schedule D Line 16
  4. If net loss > $3,000, limit to -$3,000 on Line 21
  5. Carryover = total net loss - $3,000

### Carryover Calculation Example:
- Net short-term gain: +$1,024
- Net long-term loss: -$7,812
- Combined: -$6,788
- Allowed deduction: -$3,000
- Carryover to next year: $6,788 - $3,000 = $3,788 (long-term)

## California Tax Brackets (2024) - Single

| Taxable Income | Rate |
|----------------|------|
| $0 - $10,412 | 1% |
| $10,413 - $24,684 | 2% |
| $24,685 - $38,959 | 4% |
| $38,960 - $54,081 | 6% |
| $54,082 - $68,350 | 8% |
| $68,351 - $349,137 | 9.3% |
| $349,138 - $418,961 | 10.3% |
| $418,962 - $698,271 | 11.3% |
| $698,272 - $1,000,000 | 12.3% |
| Over $1,000,000 | 13.3% (includes 1% mental health tax) |

### CA Tax Computation Example (Single, $49,824):
- 1% on first $10,412 = $104.12
- 2% on $10,413-$24,684 = $285.44
- 4% on $24,685-$38,959 = $570.96
- 6% on $38,960-$49,824 = $651.84
- Total = $1,612.36 → $1,612 (from tax table)

## California Standard Deductions (2024)

| Filing Status | Amount |
|---------------|--------|
| Single | $5,540 |
| Married Filing Jointly | $11,080 |
| Married Filing Separately | $5,540 |
| Head of Household | $11,080 |

## California Exemption Credits (2024)

| Type | Amount |
|------|--------|
| Personal (each) | $149 |
| Dependent (each) | $449 |
| Blind (each) | $149 |
| Senior 65+ (each) | $149 |

**Note**: These are credits (subtracted from tax), not deductions.

## Key Thresholds (2024)

| Item | Single | MFJ |
|------|--------|-----|
| Federal standard deduction | $14,600 | $29,200 |
| 0% LTCG rate threshold | $47,025 | $94,050 |
| 15% LTCG rate threshold | $518,900 | $583,750 |
| CA standard deduction | $5,540 | $11,080 |
| CA mental health tax | >$1,000,000 | >$1,000,000 |
