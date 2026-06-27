# Extraction Evaluation Results

Evaluated **12 documents** against ground truth.

---

## Summary

| Doc | GT | Extracted | Count | Weighted Acc | Cost USD | Duration |
|---|---|---|---|---|---|---|
| doc_001 | 50 | 50 | ✓ | 100.0% | $0.0963 | 45.59s |
| doc_002 | 40 | 21 | ✗ | 4.0% | $0.0685 | 22.19s |
| doc_003 | 1 | 1 | ✓ | 89.3% | $0.0790 | 6.48s |
| doc_004 | 1 | 1 | ✓ | 67.9% | $0.0674 | 8.62s |
| doc_005 | 80 | 14 | ✗ | 16.9% | $0.1249 | 15.72s |
| doc_006 | 33 | 33 | ✓ | 85.7% | $0.1201 | 36.49s |
| doc_007 | 400 | 23 | ✗ | 5.5% | $0.4189 | 40.37s |
| doc_008 | 100 | 26 | ✗ | 0.6% | $0.1703 | 25.71s |
| doc_009 | 1 | 89 | ✗ | 46.4% | $0.6573 | 58.44s |
| doc_010 | 1 | 20 | ✗ | 39.3% | $0.5340 | 24.54s |
| doc_011 | 150 | 17 | ✗ | 7.0% | $0.5456 | 44.57s |
| doc_012 | 120 | 29 | ✗ | 20.7% | $0.3521 | 45.76s |

**Total cost:** $3.2344  
**Total tokens:** 1,470,345 (input 1,421,385 / output 48,960)  
**Total wall-clock:** 374.5s

---

## Field Accuracy by Document

| Doc | date | cpt | total$ | ins$ | adj | pmts | bal | prov | insrs | 3p | desc |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doc_001 | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% |
| doc_002 | ✗10% | ✗0% | ✗0% | ✗0% | ✗0% | ✗8% | ✗0% | ✗10% | ✗10% | ✗10% | ✗0% |
| doc_003 | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% | ✗0% |
| doc_004 | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% | ✓100% | ✗0% | ✓100% | ✓100% | ✗0% | ✗0% |
| doc_005 | ✗18% | ✗18% | ✗18% | ✗18% | ✗18% | ✗18% | ✗18% | ✗18% | ✗18% | ✗18% | ✗0% |
| doc_006 | ✓100% | ✗0% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% |
| doc_007 | ✗7% | ✗6% | ✗6% | ✗6% | ✗6% | ✗5% | ✗4% | ✗4% | ✗6% | ✗7% | ✗7% |
| doc_008 | ✗2% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗2% | ✗2% | ✗2% | ✗0% |
| doc_009 | ✓100% | ✓100% | ✗0% | ✗0% | ✓100% | ✗0% | ✗0% | ✓100% | ✓100% | ✗0% | ✗0% |
| doc_010 | ✓100% | ✓100% | ✗0% | ✗0% | ✗0% | ✗0% | ✓100% | ✓100% | ✗0% | ✗0% | ✗0% |
| doc_011 | ✗11% | ✗11% | ✗11% | ✗11% | ✗11% | ✗0% | ✗0% | ✗3% | ✗3% | ✗11% | ✗0% |
| doc_012 | ✗24% | ✗0% | ✗24% | ✗24% | ✗24% | ✗24% | ✗24% | ✗24% | ✗24% | ✗24% | ✗0% |

---

## Error Details per Document

### doc_001

Record count matches GT.

No errors. Perfect field match.

### doc_002

**Count mismatch** — GT: 40, extracted: 21.

**Missing records (36):**
- GT[3] `02/16/2023 - 10/01/2024` — No extracted record found with this treatment_date
- GT[4] `11/17/2023 - 12/02/2024` — No extracted record found with this treatment_date
- GT[5] `03/17/2023 - 09/30/2024` — No extracted record found with this treatment_date
- GT[6] `03/05/2023 - 12/18/2024` — No extracted record found with this treatment_date
- GT[7] `05/21/2023 - 11/23/2024` — No extracted record found with this treatment_date
- GT[8] `02/07/2023 - 10/23/2024` — No extracted record found with this treatment_date
- GT[9] `03/25/2023 - 12/21/2024` — No extracted record found with this treatment_date
- GT[10] `03/05/2023 - 08/20/2024` — No extracted record found with this treatment_date
- GT[11] `08/17/2023 - 10/18/2024` — No extracted record found with this treatment_date
- GT[12] `02/19/2023 - 11/07/2024` — No extracted record found with this treatment_date
- GT[13] `03/01/2023 - 10/20/2024` — No extracted record found with this treatment_date
- GT[14] `01/16/2023 - 11/20/2024` — No extracted record found with this treatment_date
- GT[15] `06/23/2023 - 12/25/2024` — No extracted record found with this treatment_date
- GT[16] `02/27/2023 - 12/09/2024` — No extracted record found with this treatment_date
- GT[17] `03/22/2023 - 08/22/2024` — No extracted record found with this treatment_date
- GT[19] `06/07/2023 - 12/26/2024` — No extracted record found with this treatment_date
- GT[20] `05/26/2023 - 05/09/2024` — No extracted record found with this treatment_date
- GT[21] `05/25/2023 - 11/20/2024` — No extracted record found with this treatment_date
- GT[22] `02/03/2023 - 12/28/2024` — No extracted record found with this treatment_date
- GT[23] `03/02/2023 - 12/29/2024` — No extracted record found with this treatment_date
- GT[24] `02/23/2023 - 07/30/2024` — No extracted record found with this treatment_date
- GT[25] `01/13/2023 - 10/20/2024` — No extracted record found with this treatment_date
- GT[26] `01/13/2023 - 10/04/2024` — No extracted record found with this treatment_date
- GT[27] `03/05/2023 - 12/18/2024` — No extracted record found with this treatment_date
- GT[28] `03/18/2023 - 12/03/2024` — No extracted record found with this treatment_date
- GT[29] `03/08/2023 - 12/31/2024` — No extracted record found with this treatment_date
- GT[30] `01/31/2023 - 12/18/2024` — No extracted record found with this treatment_date
- GT[31] `03/02/2023 - 12/26/2024` — No extracted record found with this treatment_date
- GT[32] `07/14/2023 - 12/04/2024` — No extracted record found with this treatment_date
- GT[33] `09/27/2023 - 12/14/2024` — No extracted record found with this treatment_date
- GT[34] `03/10/2023 - 11/01/2024` — No extracted record found with this treatment_date
- GT[35] `03/01/2023 - 12/06/2024` — No extracted record found with this treatment_date
- GT[36] `04/15/2023 - 10/29/2024` — No extracted record found with this treatment_date
- GT[37] `06/22/2023 - 11/28/2024` — No extracted record found with this treatment_date
- GT[38] `02/08/2023 - 12/04/2024` — No extracted record found with this treatment_date
- GT[39] `01/10/2023 - 11/24/2024` — No extracted record found with this treatment_date

**Extra extracted records (17):**
- `01/31/2024` — Extracted record has no GT counterpart
- `06/15/2024` — Extracted record has no GT counterpart
- `09/08/2024` — Extracted record has no GT counterpart
- `11/07/2024` — Extracted record has no GT counterpart
- `12/07/2024` — Extracted record has no GT counterpart
- `03/21/2024` — Extracted record has no GT counterpart
- `11/18/2024` — Extracted record has no GT counterpart
- `05/10/2023` — Extracted record has no GT counterpart
- `08/03/2024` — Extracted record has no GT counterpart
- `09/13/2023` — Extracted record has no GT counterpart
- `09/26/2023` — Extracted record has no GT counterpart
- `12/11/2024` — Extracted record has no GT counterpart
- `11/14/2024` — Extracted record has no GT counterpart
- `11/04/2023` — Extracted record has no GT counterpart
- `01/06/2024` — Extracted record has no GT counterpart
- `01/05/2024` — Extracted record has no GT counterpart
- `06/22/2024` — Extracted record has no GT counterpart

**Field mismatches (25):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `cpt_codes` | 02/01/2023 - 12/07/2024 | missing=['71048', '72100', '72110', '72158', '73100', '73110', '73562', '74177', '76700'] |
| 0 | `total_charges` | 02/01/2023 - 12/07/2024 | extracted=778.94  expected=6181.07  diff=5402.13 |
| 0 | `ins_paid` | 02/01/2023 - 12/07/2024 | extracted=521.52  expected=3968.12  diff=3446.60 |
| 0 | `adjustment` | 02/01/2023 - 12/07/2024 | extracted=257.42  expected=2129.5  diff=1872.08 |
| 0 | `balance` | 02/01/2023 - 12/07/2024 | extracted=0.0  expected=83.45  diff=83.45 |
| 0 | `description` | 02/01/2023 - 12/07/2024 | extracted='MRI lumbar spine without contrast'  expected=None |
| 1 | `cpt_codes` | 06/26/2023 - 12/11/2024 | missing=['72158', '73100', '73564', '76705', '76830'] |
| 1 | `total_charges` | 06/26/2023 - 12/11/2024 | extracted=897.81  expected=3437.65  diff=2539.84 |
| 1 | `ins_paid` | 06/26/2023 - 12/11/2024 | extracted=630.83  expected=2260.95  diff=1630.12 |
| 1 | `adjustment` | 06/26/2023 - 12/11/2024 | extracted=133.48  expected=1022.61  diff=889.13 |
| 1 | `payments` | 06/26/2023 - 12/11/2024 | extracted=133.5  expected=None |
| 1 | `balance` | 06/26/2023 - 12/11/2024 | extracted=0.0  expected=154.09  diff=154.09 |
| 1 | `description` | 06/26/2023 - 12/11/2024 | extracted='Ultrasound abdomen, complete'  expected=None |
| 2 | `cpt_codes` | 03/30/2023 - 07/18/2024 | missing=['72158', '74178', '77067'] |
| 2 | `total_charges` | 03/30/2023 - 07/18/2024 | extracted=347.43  expected=2794.79  diff=2447.36 |
| 2 | `ins_paid` | 03/30/2023 - 07/18/2024 | extracted=260.54  expected=1797.88  diff=1537.34 |
| 2 | `adjustment` | 03/30/2023 - 07/18/2024 | extracted=86.89  expected=961.77  diff=874.88 |
| 2 | `balance` | 03/30/2023 - 07/18/2024 | extracted=0.0  expected=35.14  diff=35.14 |
| 2 | `description` | 03/30/2023 - 07/18/2024 | extracted='X-ray spine, lumbosacral, 2-3 views'  expected=None |
| 18 | `cpt_codes` | 03/20/2023 - 09/03/2024 | missing=['72100', '73030', '73562', '73564', '74177', '74178', '77067'] |
| 18 | `total_charges` | 03/20/2023 - 09/03/2024 | extracted=523.57  expected=3977.92  diff=3454.35 |
| 18 | `ins_paid` | 03/20/2023 - 09/03/2024 | extracted=313.88  expected=2355.13  diff=2041.25 |
| 18 | `adjustment` | 03/20/2023 - 09/03/2024 | extracted=209.69  expected=1550.1  diff=1340.41 |
| 18 | `balance` | 03/20/2023 - 09/03/2024 | extracted=0.0  expected=72.69  diff=72.69 |
| 18 | `description` | 03/20/2023 - 09/03/2024 | extracted='MRI lumbar spine without contrast'  expected=None |

### doc_003

Record count matches GT.

**Field mismatches (2):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `third_parties` | 01/04/2023 - 12/31/2024 | missing=['allwin', 'omnisys immunizations', 'paramount lonestar']  extra=['allwin (usflu)', 'health pbm', 'immunizations', 'lonestar', 'paramount'] |
| 0 | `description` | 01/04/2023 - 12/31/2024 | extracted=None  expected='Pharmacy Record' |

### doc_004

Record count matches GT.

**Field mismatches (4):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `adjustment` | 01/04/2023 - 12/31/2024 | extracted=None  expected=55776.23 |
| 0 | `balance` | 01/04/2023 - 12/31/2024 | extracted=None  expected=0.0 |
| 0 | `third_parties` | 01/04/2023 - 12/31/2024 | missing=['allwin']  extra=['allwin usflu)'] |
| 0 | `description` | 01/04/2023 - 12/31/2024 | extracted=None  expected='Pharmacy Expense Report' |

### doc_005

**Count mismatch** — GT: 80, extracted: 14.

**Missing records (66):**
- GT[14] `09/14/2022 - 09/21/2022` — No extracted record found with this treatment_date
- GT[15] `05/02/2024 - 05/07/2024` — No extracted record found with this treatment_date
- GT[16] `09/18/2021 - 09/25/2021` — No extracted record found with this treatment_date
- GT[17] `03/08/2023 - 03/13/2023` — No extracted record found with this treatment_date
- GT[18] `05/11/2022 - 05/18/2022` — No extracted record found with this treatment_date
- GT[19] `02/01/2022 - 02/04/2022` — No extracted record found with this treatment_date
- GT[20] `10/09/2024 - 10/13/2024` — No extracted record found with this treatment_date
- GT[21] `10/05/2022 - 10/06/2022` — No extracted record found with this treatment_date
- GT[22] `11/01/2021 - 11/07/2021` — No extracted record found with this treatment_date
- GT[23] `12/19/2024 - 12/23/2024` — No extracted record found with this treatment_date
- GT[24] `04/15/2022 - 04/21/2022` — No extracted record found with this treatment_date
- GT[25] `11/23/2022 - 11/24/2022` — No extracted record found with this treatment_date
- GT[26] `06/26/2022 - 07/03/2022` — No extracted record found with this treatment_date
- GT[27] `10/06/2024 - 10/08/2024` — No extracted record found with this treatment_date
- GT[28] `08/08/2023 - 08/10/2023` — No extracted record found with this treatment_date
- GT[29] `05/09/2021 - 05/14/2021` — No extracted record found with this treatment_date
- GT[30] `01/24/2021 - 01/29/2021` — No extracted record found with this treatment_date
- GT[31] `07/10/2023 - 07/12/2023` — No extracted record found with this treatment_date
- GT[32] `11/23/2024 - 11/25/2024` — No extracted record found with this treatment_date
- GT[33] `10/03/2022 - 10/07/2022` — No extracted record found with this treatment_date
- GT[34] `01/11/2021 - 01/14/2021` — No extracted record found with this treatment_date
- GT[35] `04/08/2022 - 04/14/2022` — No extracted record found with this treatment_date
- GT[36] `08/26/2023 - 09/01/2023` — No extracted record found with this treatment_date
- GT[37] `04/24/2021 - 04/29/2021` — No extracted record found with this treatment_date
- GT[38] `08/29/2022 - 08/31/2022` — No extracted record found with this treatment_date
- GT[39] `10/08/2024 - 10/15/2024` — No extracted record found with this treatment_date
- GT[40] `06/22/2023 - 06/26/2023` — No extracted record found with this treatment_date
- GT[41] `12/12/2021 - 12/19/2021` — No extracted record found with this treatment_date
- GT[42] `10/12/2024 - 10/14/2024` — No extracted record found with this treatment_date
- GT[43] `06/13/2023 - 06/18/2023` — No extracted record found with this treatment_date
- GT[44] `06/18/2022 - 06/19/2022` — No extracted record found with this treatment_date
- GT[45] `12/22/2021 - 12/25/2021` — No extracted record found with this treatment_date
- GT[46] `06/19/2021 - 06/26/2021` — No extracted record found with this treatment_date
- GT[47] `08/24/2023 - 08/28/2023` — No extracted record found with this treatment_date
- GT[48] `07/26/2021 - 08/01/2021` — No extracted record found with this treatment_date
- GT[49] `11/20/2024 - 11/26/2024` — No extracted record found with this treatment_date
- GT[50] `01/30/2022 - 02/03/2022` — No extracted record found with this treatment_date
- GT[51] `06/03/2023 - 06/07/2023` — No extracted record found with this treatment_date
- GT[52] `08/15/2021 - 08/16/2021` — No extracted record found with this treatment_date
- GT[53] `12/25/2021 - 12/26/2021` — No extracted record found with this treatment_date
- GT[54] `11/08/2022 - 11/14/2022` — No extracted record found with this treatment_date
- GT[55] `08/07/2023 - 08/12/2023` — No extracted record found with this treatment_date
- GT[56] `07/09/2024 - 07/12/2024` — No extracted record found with this treatment_date
- GT[57] `11/20/2021 - 11/25/2021` — No extracted record found with this treatment_date
- GT[58] `07/18/2022 - 07/23/2022` — No extracted record found with this treatment_date
- GT[59] `06/16/2024 - 06/17/2024` — No extracted record found with this treatment_date
- GT[60] `02/16/2023 - 02/20/2023` — No extracted record found with this treatment_date
- GT[61] `01/27/2023 - 01/30/2023` — No extracted record found with this treatment_date
- GT[62] `01/25/2023 - 01/28/2023` — No extracted record found with this treatment_date
- GT[63] `10/28/2022 - 11/03/2022` — No extracted record found with this treatment_date
- GT[64] `11/20/2023 - 11/27/2023` — No extracted record found with this treatment_date
- GT[65] `12/26/2021 - 12/27/2021` — No extracted record found with this treatment_date
- GT[66] `06/16/2023 - 06/23/2023` — No extracted record found with this treatment_date
- GT[67] `08/02/2023 - 08/06/2023` — No extracted record found with this treatment_date
- GT[68] `08/28/2024 - 09/04/2024` — No extracted record found with this treatment_date
- GT[69] `07/26/2022 - 07/30/2022` — No extracted record found with this treatment_date
- GT[70] `10/28/2024 - 11/01/2024` — No extracted record found with this treatment_date
- GT[71] `02/21/2022 - 02/27/2022` — No extracted record found with this treatment_date
- GT[72] `10/25/2024 - 10/27/2024` — No extracted record found with this treatment_date
- GT[73] `11/17/2022 - 11/21/2022` — No extracted record found with this treatment_date
- GT[74] `11/29/2021 - 11/30/2021` — No extracted record found with this treatment_date
- GT[75] `07/25/2023 - 07/29/2023` — No extracted record found with this treatment_date
- GT[76] `03/20/2022 - 03/27/2022` — No extracted record found with this treatment_date
- GT[77] `02/13/2022 - 02/16/2022` — No extracted record found with this treatment_date
- GT[78] `06/16/2022 - 06/19/2022` — No extracted record found with this treatment_date
- GT[79] `09/03/2021 - 09/07/2021` — No extracted record found with this treatment_date

**Field mismatches (14):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `description` | 12/22/2023 - 12/24/2023 | extracted=None  expected='Lumbar spine fusion' |
| 1 | `description` | 05/16/2021 - 05/19/2021 | extracted=None  expected='Bowel obstruction' |
| 2 | `description` | 07/02/2024 - 07/03/2024 | extracted=None  expected='Acute pancreatitis' |
| 3 | `description` | 11/30/2022 - 12/07/2022 | extracted=None  expected='Bowel obstruction' |
| 4 | `description` | 03/23/2022 - 03/27/2022 | extracted=None  expected='Acute kidney injury' |
| 5 | `description` | 05/18/2021 - 05/21/2021 | extracted=None  expected='Major depressive disorder, recurrent' |
| 6 | `description` | 09/20/2023 - 09/23/2023 | extracted=None  expected='Bowel obstruction' |
| 7 | `description` | 11/07/2021 - 11/08/2021 | extracted=None  expected='Schizophrenia, acute exacerbation' |
| 8 | `description` | 06/29/2022 - 07/04/2022 | extracted=None  expected='Urinary tract infection' |
| 9 | `description` | 09/11/2022 - 09/13/2022 | extracted=None  expected='Acute kidney injury' |
| 10 | `description` | 12/03/2021 - 12/04/2021 | extracted=None  expected='Stroke, ischemic' |
| 11 | `description` | 05/18/2021 - 05/21/2021 | extracted=None  expected='Type 2 diabetes mellitus with ketoacidosis' |
| 12 | `description` | 07/14/2021 - 07/15/2021 | extracted=None  expected='Chronic obstructive pulmonary disease with acute exacerbation' |
| 13 | `description` | 07/27/2021 - 07/29/2021 | extracted=None  expected='Chronic obstructive pulmonary disease with acute exacerbation' |

### doc_006

Record count matches GT.

**Field mismatches (66):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `cpt_codes` | 01/01/2021 - 01/27/2021 | extra=['82565', '84100', '84132', '84295', '90937', '93975', '99213', 'A4690', 'A4706', 'G0491', 'J0885', 'J2916'] |
| 0 | `description` | 01/01/2021 - 01/27/2021 | extracted=None  expected='Dialysis — 10 treatments' |
| 1 | `cpt_codes` | 01/28/2021 - 02/22/2021 | extra=['83540', '90937', '99213', 'A4690', 'A4750', 'A4755', 'A4802', 'A4860', 'A4920', 'J2916', 'J3370'] |
| 1 | `description` | 01/28/2021 - 02/22/2021 | extracted=None  expected='Dialysis — 9 treatments' |
| 2 | `cpt_codes` | 02/23/2021 - 03/20/2021 | extra=['36821', '36831', '86000', '90937', 'A4755', 'A4860', 'J0885', 'J3370'] |
| 2 | `description` | 02/23/2021 - 03/20/2021 | extracted=None  expected='Dialysis — 10 treatments' |
| 3 | `cpt_codes` | 03/21/2021 - 04/19/2021 | extra=['83036', '90937', '90940', 'A4690', 'A4706', 'A4730', 'A4750', 'A4802', 'G0491', 'J3370'] |
| 3 | `description` | 03/21/2021 - 04/19/2021 | extracted=None  expected='Dialysis — 13 treatments' |
| 4 | `cpt_codes` | 04/20/2021 - 05/21/2021 | extra=['36831', '83036', '83540', '84100', '84132', '85025', '90937', '99213', 'A4690', 'A4730', 'A4802', 'J0885'] |
| 4 | `description` | 04/20/2021 - 05/21/2021 | extracted=None  expected='Dialysis — 11 treatments' |
| 5 | `cpt_codes` | 05/22/2021 - 06/20/2021 | extra=['82565', '82728', '83540', '84100', '93975', 'A4690', 'A4706', 'A4730', 'G0491', 'J2916'] |
| 5 | `description` | 05/22/2021 - 06/20/2021 | extracted=None  expected='Dialysis — 12 treatments' |
| 6 | `cpt_codes` | 06/21/2021 - 07/21/2021 | extra=['82310', '82728', '90937', '99213', 'A4690', 'A4706', 'A4730', 'J2916'] |
| 6 | `description` | 06/21/2021 - 07/21/2021 | extracted=None  expected='Dialysis — 8 treatments' |
| 7 | `cpt_codes` | 07/22/2021 - 08/16/2021 | extra=['83540', '84100', '90935', '90940', 'A4860', 'G0491', 'J2916'] |
| 7 | `description` | 07/22/2021 - 08/16/2021 | extracted=None  expected='Dialysis — 8 treatments' |
| 8 | `cpt_codes` | 08/17/2021 - 09/16/2021 | extra=['36821', '83036', '83540', 'A4750', 'A4860', 'G0491', 'J2916'] |
| 8 | `description` | 08/17/2021 - 09/16/2021 | extracted=None  expected='Dialysis — 10 treatments' |
| 9 | `cpt_codes` | 09/17/2021 - 10/15/2021 | extra=['36831', '83036', '84295', '90935', 'A4750', 'A4802', 'A4860', 'A4920', 'J2916'] |
| 9 | `description` | 09/17/2021 - 10/15/2021 | extracted=None  expected='Dialysis — 13 treatments' |
| 10 | `cpt_codes` | 10/16/2021 - 11/16/2021 | extra=['82565', '82728', '86000', '90937', '99213', 'A4730', 'A4755', 'A4860', 'G0491', 'J0885'] |
| 10 | `description` | 10/16/2021 - 11/16/2021 | extracted=None  expected='Dialysis — 12 treatments' |
| 11 | `cpt_codes` | 11/17/2021 - 12/15/2021 | extra=['36831', '82310', '84100', '85025', '90935', '90940', '99213', 'A4706', 'A4750', 'A4802', 'G0491'] |
| 11 | `description` | 11/17/2021 - 12/15/2021 | extracted=None  expected='Dialysis — 12 treatments' |
| 12 | `cpt_codes` | 05/02/2022 - 05/28/2022 | extra=['36831', '82310', '84295', '86000', '90935', '90937', '90940', '99213', 'A4750', 'A4860', 'A4920', 'J0885', 'J3370'] |
| 12 | `description` | 05/02/2022 - 05/28/2022 | extracted=None  expected='Dialysis — 10 treatments' |
| 13 | `cpt_codes` | 05/29/2022 - 06/30/2022 | extra=['82310', '82565', '82728', '84132', '84295', '90940', 'A4706', 'A4750', 'A4920', 'J2916', 'J3370'] |
| 13 | `description` | 05/29/2022 - 06/30/2022 | extracted=None  expected='Dialysis — 8 treatments' |
| 14 | `cpt_codes` | 07/01/2022 - 08/02/2022 | extra=['36831', '82310', '90937', '99213', 'A4750', 'A4920', 'J2916', 'J3370'] |
| 14 | `description` | 07/01/2022 - 08/02/2022 | extracted=None  expected='Dialysis — 13 treatments' |
| 15 | `cpt_codes` | 08/03/2022 - 09/01/2022 | extra=['36821', '82310', '82728', '85025', '90937', '93975', '99213', 'A4750', 'A4802', 'A4860', 'A4920', 'J0885'] |
| 15 | `description` | 08/03/2022 - 09/01/2022 | extracted=None  expected='Dialysis — 8 treatments' |
| 16 | `cpt_codes` | 09/02/2022 - 09/29/2022 | extra=['84295', '85025', '86000', '90935', '90940', '99213', 'A4706', 'A4802', 'A4920', 'J2916', 'J3370'] |
| 16 | `description` | 09/02/2022 - 09/29/2022 | extracted=None  expected='Dialysis — 11 treatments' |
| 17 | `cpt_codes` | 09/30/2022 - 10/31/2022 | extra=['84100', '84295', '86000', '90935', '99213', 'A4730', 'A4750', 'A4755', 'A4860', 'G0491', 'J2916'] |
| 17 | `description` | 09/30/2022 - 10/31/2022 | extracted=None  expected='Dialysis — 12 treatments' |
| 18 | `cpt_codes` | 11/01/2022 - 12/01/2022 | extra=['36831', '83540', '84100', '84295', '85025', '90937', '90940', 'A4730', 'A4755', 'A4860', 'A4920', 'J2916', 'J3370'] |
| 18 | `description` | 11/01/2022 - 12/01/2022 | extracted=None  expected='Dialysis — 12 treatments' |
| 19 | `cpt_codes` | 12/02/2022 - 01/03/2023 | extra=['36821', '36831', '82728', '83540', '90935', '90940', 'G0491', 'J2916'] |
| 19 | `description` | 12/02/2022 - 01/03/2023 | extracted=None  expected='Dialysis — 10 treatments' |
| 20 | `cpt_codes` | 01/04/2023 - 02/01/2023 | extra=['82310', '82565', '82728', '84132', '85025', '90935', '90940', 'A4706', 'A4730', 'A4750', 'A4755', 'A4802', 'A4860'] |
| 20 | `description` | 01/04/2023 - 02/01/2023 | extracted=None  expected='Dialysis — 10 treatments' |
| 21 | `cpt_codes` | 02/02/2023 - 02/28/2023 | extra=['86000', '93975', '99213', 'A4690', 'A4706', 'A4755', 'A4860', 'A4920', 'G0491', 'J2916'] |
| 21 | `description` | 02/02/2023 - 02/28/2023 | extracted=None  expected='Dialysis — 9 treatments' |
| 22 | `cpt_codes` | 03/01/2023 - 03/26/2023 | extra=['82728', '83036', '84295', '90935', '90940', '93975', 'A4690', 'A4750', 'G0491', 'J0885', 'J2916', 'J3370'] |
| 22 | `description` | 03/01/2023 - 03/26/2023 | extracted=None  expected='Dialysis — 12 treatments' |
| 23 | `cpt_codes` | 08/31/2023 - 09/30/2023 | extra=['36831', '82728', '84132', '85025', '86000', '93975', '99213', 'A4706', 'A4802', 'G0491', 'J0885', 'J2916'] |
| 23 | `description` | 08/31/2023 - 09/30/2023 | extracted=None  expected='Dialysis — 13 treatments' |
| 24 | `cpt_codes` | 10/01/2023 - 10/30/2023 | extra=['83036', '84132', '84295', '93975', '99213', 'A4706', 'A4750', 'A4755', 'J2916'] |
| 24 | `description` | 10/01/2023 - 10/30/2023 | extracted=None  expected='Dialysis — 11 treatments' |
| 25 | `cpt_codes` | 10/31/2023 - 11/28/2023 | extra=['83540', '84100', '85025', '99213', 'A4730', 'A4802', 'A4860', 'G0491', 'J0885', 'J2916'] |
| 25 | `description` | 10/31/2023 - 11/28/2023 | extracted=None  expected='Dialysis — 10 treatments' |
| 26 | `cpt_codes` | 11/29/2023 - 12/25/2023 | extra=['82728', '85025', '90935', 'A4802', 'A4860', 'G0491', 'J0885', 'J2916'] |
| 26 | `description` | 11/29/2023 - 12/25/2023 | extracted=None  expected='Dialysis — 12 treatments' |
| 27 | `cpt_codes` | 12/26/2023 - 01/26/2024 | extra=['82565', '83036', '84100', '85025', '86000', '90937', '99213', 'A4690', 'A4706', 'A4802', 'G0491', 'J2916'] |
| 27 | `description` | 12/26/2023 - 01/26/2024 | extracted=None  expected='Dialysis — 13 treatments' |
| 28 | `cpt_codes` | 01/27/2024 - 02/28/2024 | extra=['36831', '82728', '83036', '83540', '84100', '85025', '86000', 'A4706', 'A4860', 'J2916'] |
| 28 | `description` | 01/27/2024 - 02/28/2024 | extracted=None  expected='Dialysis — 8 treatments' |
| 29 | `cpt_codes` | 02/29/2024 - 04/01/2024 | extra=['36821', '82565', '83540', '84100', '84132', '85025', '90937', '99213', 'A4750', 'A4920', 'G0491', 'J3370'] |
| 29 | `description` | 02/29/2024 - 04/01/2024 | extracted=None  expected='Dialysis — 9 treatments' |
| 30 | `cpt_codes` | 04/02/2024 - 05/03/2024 | extra=['36831', '82728', '83036', '84295', '86000', '90937', 'A4730', 'A4755', 'J3370'] |
| 30 | `description` | 04/02/2024 - 05/03/2024 | extracted=None  expected='Dialysis — 10 treatments' |
| 31 | `cpt_codes` | 05/04/2024 - 06/03/2024 | extra=['36821', '90935', '93975', 'A4730', 'A4750', 'A4755', 'A4802', 'A4860'] |
| 31 | `description` | 05/04/2024 - 06/03/2024 | extracted=None  expected='Dialysis — 8 treatments' |
| 32 | `cpt_codes` | 06/04/2024 - 07/05/2024 | extra=['82728', '83036', '84100', '84132', '84295', '99213', 'A4706', 'A4750', 'A4860', 'G0491'] |
| 32 | `description` | 06/04/2024 - 07/05/2024 | extracted=None  expected='Dialysis — 9 treatments' |

### doc_007

**Count mismatch** — GT: 400, extracted: 23.

**Missing records (373):**
- GT[10] `06/22/2022` — No extracted record found with this treatment_date
- GT[11] `10/20/2021` — No extracted record found with this treatment_date
- GT[12] `12/04/2024` — No extracted record found with this treatment_date
- GT[13] `05/12/2021` — No extracted record found with this treatment_date
- GT[14] `06/30/2024` — No extracted record found with this treatment_date
- GT[15] `07/24/2021` — No extracted record found with this treatment_date
- GT[16] `01/11/2021` — No extracted record found with this treatment_date
- GT[17] `04/03/2022` — No extracted record found with this treatment_date
- GT[18] `10/22/2022` — No extracted record found with this treatment_date
- GT[19] `12/27/2023` — No extracted record found with this treatment_date
- GT[20] `03/05/2021` — No extracted record found with this treatment_date
- GT[21] `11/28/2022` — No extracted record found with this treatment_date
- GT[22] `10/06/2024` — No extracted record found with this treatment_date
- GT[23] `05/16/2021` — No extracted record found with this treatment_date
- GT[24] `07/24/2021` — No extracted record found with this treatment_date
- GT[25] `04/28/2023` — No extracted record found with this treatment_date
- GT[26] `09/30/2022` — No extracted record found with this treatment_date
- GT[27] `05/17/2024` — No extracted record found with this treatment_date
- GT[28] `04/07/2024` — No extracted record found with this treatment_date
- GT[29] `07/07/2024` — No extracted record found with this treatment_date
- GT[30] `12/06/2021` — No extracted record found with this treatment_date
- GT[31] `01/03/2024` — No extracted record found with this treatment_date
- GT[32] `06/11/2023` — No extracted record found with this treatment_date
- GT[33] `06/17/2024` — No extracted record found with this treatment_date
- GT[34] `04/12/2024` — No extracted record found with this treatment_date
- GT[35] `03/18/2024` — No extracted record found with this treatment_date
- GT[36] `08/16/2022` — No extracted record found with this treatment_date
- GT[38] `12/18/2024` — No extracted record found with this treatment_date
- GT[39] `09/11/2023` — No extracted record found with this treatment_date
- GT[40] `08/22/2021` — No extracted record found with this treatment_date
- GT[41] `10/23/2024` — No extracted record found with this treatment_date
- GT[42] `06/27/2024` — No extracted record found with this treatment_date
- GT[43] `06/30/2022` — No extracted record found with this treatment_date
- GT[44] `09/18/2021` — No extracted record found with this treatment_date
- GT[45] `10/29/2021` — No extracted record found with this treatment_date
- GT[46] `03/02/2022` — No extracted record found with this treatment_date
- GT[47] `09/29/2024` — No extracted record found with this treatment_date
- GT[48] `12/14/2021` — No extracted record found with this treatment_date
- GT[49] `07/25/2021` — No extracted record found with this treatment_date
- GT[50] `05/18/2024` — No extracted record found with this treatment_date
- GT[51] `10/28/2024` — No extracted record found with this treatment_date
- GT[52] `09/08/2024` — No extracted record found with this treatment_date
- GT[53] `04/13/2023` — No extracted record found with this treatment_date
- GT[54] `01/06/2023` — No extracted record found with this treatment_date
- GT[55] `06/19/2021` — No extracted record found with this treatment_date
- GT[56] `04/18/2023` — No extracted record found with this treatment_date
- GT[57] `02/10/2024` — No extracted record found with this treatment_date
- GT[58] `01/16/2021` — No extracted record found with this treatment_date
- GT[59] `07/15/2021` — No extracted record found with this treatment_date
- GT[60] `02/06/2024` — No extracted record found with this treatment_date
- GT[61] `11/11/2022` — No extracted record found with this treatment_date
- GT[62] `01/05/2022` — No extracted record found with this treatment_date
- GT[63] `11/29/2021` — No extracted record found with this treatment_date
- GT[64] `12/12/2023` — No extracted record found with this treatment_date
- GT[65] `11/02/2024` — No extracted record found with this treatment_date
- GT[66] `05/06/2022` — No extracted record found with this treatment_date
- GT[67] `06/19/2021` — No extracted record found with this treatment_date
- GT[68] `12/29/2021` — No extracted record found with this treatment_date
- GT[69] `11/18/2022` — No extracted record found with this treatment_date
- GT[70] `07/18/2023` — No extracted record found with this treatment_date
- GT[71] `03/07/2022` — No extracted record found with this treatment_date
- GT[72] `10/09/2024` — No extracted record found with this treatment_date
- GT[73] `05/06/2023` — No extracted record found with this treatment_date
- GT[75] `10/06/2024` — No extracted record found with this treatment_date
- GT[76] `10/15/2024` — No extracted record found with this treatment_date
- GT[77] `03/17/2022` — No extracted record found with this treatment_date
- GT[78] `07/17/2022` — No extracted record found with this treatment_date
- GT[79] `07/06/2021` — No extracted record found with this treatment_date
- GT[80] `06/24/2021` — No extracted record found with this treatment_date
- GT[81] `04/19/2024` — No extracted record found with this treatment_date
- GT[82] `11/18/2022` — No extracted record found with this treatment_date
- GT[83] `08/07/2021` — No extracted record found with this treatment_date
- GT[84] `10/27/2021` — No extracted record found with this treatment_date
- GT[85] `09/04/2021` — No extracted record found with this treatment_date
- GT[86] `04/01/2024` — No extracted record found with this treatment_date
- GT[87] `03/31/2021` — No extracted record found with this treatment_date
- GT[88] `10/22/2023` — No extracted record found with this treatment_date
- GT[89] `10/03/2024` — No extracted record found with this treatment_date
- GT[90] `05/10/2024` — No extracted record found with this treatment_date
- GT[91] `07/21/2024` — No extracted record found with this treatment_date
- GT[92] `01/08/2021` — No extracted record found with this treatment_date
- GT[93] `04/11/2023` — No extracted record found with this treatment_date
- GT[94] `08/03/2024` — No extracted record found with this treatment_date
- GT[95] `10/25/2022` — No extracted record found with this treatment_date
- GT[96] `02/04/2024` — No extracted record found with this treatment_date
- GT[97] `10/17/2021` — No extracted record found with this treatment_date
- GT[98] `04/11/2022` — No extracted record found with this treatment_date
- GT[99] `08/20/2023` — No extracted record found with this treatment_date
- GT[100] `05/15/2021` — No extracted record found with this treatment_date
- GT[101] `11/12/2021` — No extracted record found with this treatment_date
- GT[102] `01/02/2024` — No extracted record found with this treatment_date
- GT[103] `07/07/2022` — No extracted record found with this treatment_date
- GT[104] `04/04/2022` — No extracted record found with this treatment_date
- GT[106] `01/19/2024` — No extracted record found with this treatment_date
- GT[107] `11/19/2023` — No extracted record found with this treatment_date
- GT[108] `09/29/2022` — No extracted record found with this treatment_date
- GT[109] `03/20/2021` — No extracted record found with this treatment_date
- GT[110] `06/12/2023` — No extracted record found with this treatment_date
- GT[111] `08/17/2021` — No extracted record found with this treatment_date
- GT[112] `01/13/2021` — No extracted record found with this treatment_date
- GT[113] `11/03/2024` — No extracted record found with this treatment_date
- GT[114] `02/08/2022` — No extracted record found with this treatment_date
- GT[115] `01/18/2023` — No extracted record found with this treatment_date
- GT[116] `05/22/2023` — No extracted record found with this treatment_date
- GT[117] `09/28/2024` — No extracted record found with this treatment_date
- GT[118] `09/09/2023` — No extracted record found with this treatment_date
- GT[119] `12/18/2024` — No extracted record found with this treatment_date
- GT[120] `07/04/2023` — No extracted record found with this treatment_date
- GT[121] `10/02/2023` — No extracted record found with this treatment_date
- GT[122] `05/14/2022` — No extracted record found with this treatment_date
- GT[123] `12/14/2022` — No extracted record found with this treatment_date
- GT[124] `04/15/2024` — No extracted record found with this treatment_date
- GT[125] `02/11/2024` — No extracted record found with this treatment_date
- GT[126] `01/08/2024` — No extracted record found with this treatment_date
- GT[127] `08/16/2024` — No extracted record found with this treatment_date
- GT[128] `11/19/2021` — No extracted record found with this treatment_date
- GT[129] `07/31/2021` — No extracted record found with this treatment_date
- GT[130] `07/22/2024` — No extracted record found with this treatment_date
- GT[131] `05/31/2024` — No extracted record found with this treatment_date
- GT[132] `02/20/2023` — No extracted record found with this treatment_date
- GT[133] `11/01/2022` — No extracted record found with this treatment_date
- GT[134] `01/09/2024` — No extracted record found with this treatment_date
- GT[135] `09/18/2024` — No extracted record found with this treatment_date
- GT[136] `04/18/2024` — No extracted record found with this treatment_date
- GT[137] `02/14/2021` — No extracted record found with this treatment_date
- GT[138] `11/02/2022` — No extracted record found with this treatment_date
- GT[139] `08/04/2023` — No extracted record found with this treatment_date
- GT[140] `06/04/2022` — No extracted record found with this treatment_date
- GT[141] `02/03/2023` — No extracted record found with this treatment_date
- GT[142] `04/12/2024` — No extracted record found with this treatment_date
- GT[143] `07/29/2022` — No extracted record found with this treatment_date
- GT[144] `12/13/2024` — No extracted record found with this treatment_date
- GT[145] `10/08/2024` — No extracted record found with this treatment_date
- GT[146] `05/07/2023` — No extracted record found with this treatment_date
- GT[147] `08/02/2023` — No extracted record found with this treatment_date
- GT[148] `07/28/2021` — No extracted record found with this treatment_date
- GT[149] `10/17/2022` — No extracted record found with this treatment_date
- GT[150] `08/05/2024` — No extracted record found with this treatment_date
- GT[151] `01/08/2021` — No extracted record found with this treatment_date
- GT[152] `10/08/2023` — No extracted record found with this treatment_date
- GT[153] `06/11/2022` — No extracted record found with this treatment_date
- GT[154] `05/22/2023` — No extracted record found with this treatment_date
- GT[155] `06/10/2022` — No extracted record found with this treatment_date
- GT[156] `07/10/2021` — No extracted record found with this treatment_date
- GT[157] `12/04/2021` — No extracted record found with this treatment_date
- GT[158] `12/07/2022` — No extracted record found with this treatment_date
- GT[159] `08/06/2024` — No extracted record found with this treatment_date
- GT[160] `07/30/2022` — No extracted record found with this treatment_date
- GT[161] `03/16/2023` — No extracted record found with this treatment_date
- GT[162] `03/29/2021` — No extracted record found with this treatment_date
- GT[163] `09/12/2023` — No extracted record found with this treatment_date
- GT[164] `06/23/2024` — No extracted record found with this treatment_date
- GT[165] `01/06/2021` — No extracted record found with this treatment_date
- GT[166] `11/22/2024` — No extracted record found with this treatment_date
- GT[167] `12/06/2022` — No extracted record found with this treatment_date
- GT[168] `08/19/2022` — No extracted record found with this treatment_date
- GT[169] `06/17/2023` — No extracted record found with this treatment_date
- GT[170] `04/13/2024` — No extracted record found with this treatment_date
- GT[171] `10/05/2022` — No extracted record found with this treatment_date
- GT[172] `01/07/2022` — No extracted record found with this treatment_date
- GT[173] `09/19/2022` — No extracted record found with this treatment_date
- GT[174] `01/05/2024` — No extracted record found with this treatment_date
- GT[175] `03/09/2023` — No extracted record found with this treatment_date
- GT[176] `11/12/2024` — No extracted record found with this treatment_date
- GT[177] `10/28/2024` — No extracted record found with this treatment_date
- GT[178] `10/15/2021` — No extracted record found with this treatment_date
- GT[179] `08/01/2024` — No extracted record found with this treatment_date
- GT[180] `10/07/2023` — No extracted record found with this treatment_date
- GT[181] `04/24/2024` — No extracted record found with this treatment_date
- GT[182] `11/14/2022` — No extracted record found with this treatment_date
- GT[183] `08/09/2021` — No extracted record found with this treatment_date
- GT[184] `07/04/2022` — No extracted record found with this treatment_date
- GT[185] `06/19/2023` — No extracted record found with this treatment_date
- GT[186] `04/17/2021` — No extracted record found with this treatment_date
- GT[187] `10/24/2022` — No extracted record found with this treatment_date
- GT[188] `05/23/2022` — No extracted record found with this treatment_date
- GT[189] `02/22/2024` — No extracted record found with this treatment_date
- GT[190] `02/03/2022` — No extracted record found with this treatment_date
- GT[191] `03/27/2023` — No extracted record found with this treatment_date
- GT[192] `04/16/2022` — No extracted record found with this treatment_date
- GT[193] `06/16/2022` — No extracted record found with this treatment_date
- GT[194] `09/17/2023` — No extracted record found with this treatment_date
- GT[195] `06/20/2021` — No extracted record found with this treatment_date
- GT[196] `12/18/2021` — No extracted record found with this treatment_date
- GT[197] `07/07/2024` — No extracted record found with this treatment_date
- GT[198] `05/01/2024` — No extracted record found with this treatment_date
- GT[199] `01/24/2021` — No extracted record found with this treatment_date
- GT[200] `09/04/2023` — No extracted record found with this treatment_date
- GT[201] `10/14/2022` — No extracted record found with this treatment_date
- GT[202] `12/24/2021` — No extracted record found with this treatment_date
- GT[203] `02/06/2023` — No extracted record found with this treatment_date
- GT[204] `04/22/2022` — No extracted record found with this treatment_date
- GT[205] `06/05/2023` — No extracted record found with this treatment_date
- GT[206] `07/02/2023` — No extracted record found with this treatment_date
- GT[207] `07/01/2021` — No extracted record found with this treatment_date
- GT[208] `11/13/2021` — No extracted record found with this treatment_date
- GT[209] `03/01/2024` — No extracted record found with this treatment_date
- GT[210] `12/17/2022` — No extracted record found with this treatment_date
- GT[211] `07/31/2021` — No extracted record found with this treatment_date
- GT[212] `03/09/2024` — No extracted record found with this treatment_date
- GT[213] `06/20/2024` — No extracted record found with this treatment_date
- GT[214] `08/11/2022` — No extracted record found with this treatment_date
- GT[215] `01/04/2022` — No extracted record found with this treatment_date
- GT[216] `11/15/2021` — No extracted record found with this treatment_date
- GT[217] `05/25/2022` — No extracted record found with this treatment_date
- GT[218] `07/21/2024` — No extracted record found with this treatment_date
- GT[219] `07/05/2022` — No extracted record found with this treatment_date
- GT[220] `12/14/2022` — No extracted record found with this treatment_date
- GT[221] `08/19/2022` — No extracted record found with this treatment_date
- GT[222] `06/01/2021` — No extracted record found with this treatment_date
- GT[223] `09/13/2022` — No extracted record found with this treatment_date
- GT[224] `11/04/2023` — No extracted record found with this treatment_date
- GT[225] `08/06/2023` — No extracted record found with this treatment_date
- GT[226] `05/02/2022` — No extracted record found with this treatment_date
- GT[227] `01/03/2021` — No extracted record found with this treatment_date
- GT[228] `01/14/2023` — No extracted record found with this treatment_date
- GT[229] `07/05/2024` — No extracted record found with this treatment_date
- GT[230] `10/20/2022` — No extracted record found with this treatment_date
- GT[231] `08/04/2024` — No extracted record found with this treatment_date
- GT[232] `03/21/2023` — No extracted record found with this treatment_date
- GT[233] `10/29/2024` — No extracted record found with this treatment_date
- GT[234] `03/29/2024` — No extracted record found with this treatment_date
- GT[235] `01/06/2021` — No extracted record found with this treatment_date
- GT[236] `11/11/2022` — No extracted record found with this treatment_date
- GT[237] `08/03/2024` — No extracted record found with this treatment_date
- GT[238] `05/25/2022` — No extracted record found with this treatment_date
- GT[239] `09/05/2024` — No extracted record found with this treatment_date
- GT[240] `11/24/2021` — No extracted record found with this treatment_date
- GT[241] `10/17/2022` — No extracted record found with this treatment_date
- GT[242] `09/26/2021` — No extracted record found with this treatment_date
- GT[256] `10/14/2022` — No extracted record found with this treatment_date
- GT[257] `03/26/2023` — No extracted record found with this treatment_date
- GT[258] `02/10/2021` — No extracted record found with this treatment_date
- GT[259] `10/17/2024` — No extracted record found with this treatment_date
- GT[260] `12/26/2021` — No extracted record found with this treatment_date
- GT[261] `06/22/2023` — No extracted record found with this treatment_date
- GT[262] `12/22/2023` — No extracted record found with this treatment_date
- GT[263] `10/28/2023` — No extracted record found with this treatment_date
- GT[264] `04/21/2023` — No extracted record found with this treatment_date
- GT[265] `11/17/2022` — No extracted record found with this treatment_date
- GT[266] `07/23/2023` — No extracted record found with this treatment_date
- GT[267] `01/15/2024` — No extracted record found with this treatment_date
- GT[268] `11/10/2021` — No extracted record found with this treatment_date
- GT[269] `08/12/2023` — No extracted record found with this treatment_date
- GT[270] `08/06/2022` — No extracted record found with this treatment_date
- GT[271] `11/18/2023` — No extracted record found with this treatment_date
- GT[272] `12/26/2021` — No extracted record found with this treatment_date
- GT[273] `01/22/2024` — No extracted record found with this treatment_date
- GT[274] `01/31/2022` — No extracted record found with this treatment_date
- GT[275] `06/06/2022` — No extracted record found with this treatment_date
- GT[276] `07/29/2024` — No extracted record found with this treatment_date
- GT[277] `11/28/2021` — No extracted record found with this treatment_date
- GT[278] `01/28/2024` — No extracted record found with this treatment_date
- GT[279] `03/09/2024` — No extracted record found with this treatment_date
- GT[280] `07/18/2023` — No extracted record found with this treatment_date
- GT[281] `06/29/2024` — No extracted record found with this treatment_date
- GT[282] `01/11/2023` — No extracted record found with this treatment_date
- GT[283] `02/22/2022` — No extracted record found with this treatment_date
- GT[284] `11/05/2021` — No extracted record found with this treatment_date
- GT[285] `02/17/2023` — No extracted record found with this treatment_date
- GT[286] `11/15/2024` — No extracted record found with this treatment_date
- GT[287] `04/29/2021` — No extracted record found with this treatment_date
- GT[288] `06/07/2024` — No extracted record found with this treatment_date
- GT[289] `03/04/2021` — No extracted record found with this treatment_date
- GT[290] `11/23/2022` — No extracted record found with this treatment_date
- GT[291] `07/21/2021` — No extracted record found with this treatment_date
- GT[292] `05/29/2021` — No extracted record found with this treatment_date
- GT[293] `06/13/2022` — No extracted record found with this treatment_date
- GT[294] `05/15/2024` — No extracted record found with this treatment_date
- GT[295] `04/04/2024` — No extracted record found with this treatment_date
- GT[296] `07/10/2024` — No extracted record found with this treatment_date
- GT[297] `08/20/2024` — No extracted record found with this treatment_date
- GT[298] `05/26/2024` — No extracted record found with this treatment_date
- GT[299] `02/18/2022` — No extracted record found with this treatment_date
- GT[300] `10/31/2023` — No extracted record found with this treatment_date
- GT[301] `03/05/2021` — No extracted record found with this treatment_date
- GT[302] `12/17/2023` — No extracted record found with this treatment_date
- GT[303] `09/16/2022` — No extracted record found with this treatment_date
- GT[304] `03/25/2023` — No extracted record found with this treatment_date
- GT[305] `10/28/2021` — No extracted record found with this treatment_date
- GT[306] `12/28/2022` — No extracted record found with this treatment_date
- GT[307] `03/08/2022` — No extracted record found with this treatment_date
- GT[308] `08/08/2023` — No extracted record found with this treatment_date
- GT[309] `10/18/2024` — No extracted record found with this treatment_date
- GT[310] `09/02/2022` — No extracted record found with this treatment_date
- GT[311] `03/19/2024` — No extracted record found with this treatment_date
- GT[312] `08/16/2023` — No extracted record found with this treatment_date
- GT[313] `03/10/2021` — No extracted record found with this treatment_date
- GT[314] `01/14/2023` — No extracted record found with this treatment_date
- GT[315] `03/08/2023` — No extracted record found with this treatment_date
- GT[316] `04/03/2021` — No extracted record found with this treatment_date
- GT[317] `06/27/2024` — No extracted record found with this treatment_date
- GT[318] `07/31/2024` — No extracted record found with this treatment_date
- GT[319] `12/09/2021` — No extracted record found with this treatment_date
- GT[320] `03/09/2024` — No extracted record found with this treatment_date
- GT[321] `05/14/2024` — No extracted record found with this treatment_date
- GT[322] `08/23/2023` — No extracted record found with this treatment_date
- GT[323] `05/02/2021` — No extracted record found with this treatment_date
- GT[324] `02/05/2022` — No extracted record found with this treatment_date
- GT[325] `03/14/2024` — No extracted record found with this treatment_date
- GT[326] `06/03/2022` — No extracted record found with this treatment_date
- GT[327] `04/24/2024` — No extracted record found with this treatment_date
- GT[328] `09/09/2024` — No extracted record found with this treatment_date
- GT[329] `09/23/2021` — No extracted record found with this treatment_date
- GT[330] `09/28/2021` — No extracted record found with this treatment_date
- GT[331] `11/21/2023` — No extracted record found with this treatment_date
- GT[332] `06/13/2022` — No extracted record found with this treatment_date
- GT[333] `10/05/2023` — No extracted record found with this treatment_date
- GT[334] `05/05/2023` — No extracted record found with this treatment_date
- GT[335] `01/18/2022` — No extracted record found with this treatment_date
- GT[336] `09/12/2023` — No extracted record found with this treatment_date
- GT[337] `02/24/2022` — No extracted record found with this treatment_date
- GT[338] `02/04/2024` — No extracted record found with this treatment_date
- GT[339] `06/25/2022` — No extracted record found with this treatment_date
- GT[341] `03/08/2021` — No extracted record found with this treatment_date
- GT[342] `02/10/2023` — No extracted record found with this treatment_date
- GT[343] `11/21/2022` — No extracted record found with this treatment_date
- GT[344] `10/23/2024` — No extracted record found with this treatment_date
- GT[345] `06/20/2022` — No extracted record found with this treatment_date
- GT[346] `02/21/2023` — No extracted record found with this treatment_date
- GT[347] `03/04/2024` — No extracted record found with this treatment_date
- GT[348] `03/13/2021` — No extracted record found with this treatment_date
- GT[349] `12/11/2021` — No extracted record found with this treatment_date
- GT[350] `12/16/2022` — No extracted record found with this treatment_date
- GT[351] `02/25/2021` — No extracted record found with this treatment_date
- GT[352] `07/17/2022` — No extracted record found with this treatment_date
- GT[353] `02/18/2022` — No extracted record found with this treatment_date
- GT[354] `08/04/2022` — No extracted record found with this treatment_date
- GT[355] `04/20/2023` — No extracted record found with this treatment_date
- GT[356] `08/13/2021` — No extracted record found with this treatment_date
- GT[357] `06/23/2023` — No extracted record found with this treatment_date
- GT[358] `06/19/2021` — No extracted record found with this treatment_date
- GT[359] `04/21/2021` — No extracted record found with this treatment_date
- GT[360] `10/31/2022` — No extracted record found with this treatment_date
- GT[361] `07/09/2022` — No extracted record found with this treatment_date
- GT[362] `12/14/2023` — No extracted record found with this treatment_date
- GT[363] `06/28/2023` — No extracted record found with this treatment_date
- GT[364] `02/02/2023` — No extracted record found with this treatment_date
- GT[365] `05/24/2023` — No extracted record found with this treatment_date
- GT[366] `04/25/2021` — No extracted record found with this treatment_date
- GT[367] `02/21/2022` — No extracted record found with this treatment_date
- GT[368] `10/20/2022` — No extracted record found with this treatment_date
- GT[369] `12/21/2024` — No extracted record found with this treatment_date
- GT[370] `08/26/2022` — No extracted record found with this treatment_date
- GT[371] `07/10/2021` — No extracted record found with this treatment_date
- GT[372] `05/11/2021` — No extracted record found with this treatment_date
- GT[373] `10/15/2024` — No extracted record found with this treatment_date
- GT[374] `12/30/2021` — No extracted record found with this treatment_date
- GT[375] `07/05/2024` — No extracted record found with this treatment_date
- GT[376] `01/28/2024` — No extracted record found with this treatment_date
- GT[377] `08/27/2023` — No extracted record found with this treatment_date
- GT[378] `08/11/2021` — No extracted record found with this treatment_date
- GT[379] `04/28/2023` — No extracted record found with this treatment_date
- GT[380] `08/19/2021` — No extracted record found with this treatment_date
- GT[381] `12/06/2024` — No extracted record found with this treatment_date
- GT[382] `01/18/2023` — No extracted record found with this treatment_date
- GT[383] `12/14/2021` — No extracted record found with this treatment_date
- GT[384] `08/11/2024` — No extracted record found with this treatment_date
- GT[385] `07/11/2023` — No extracted record found with this treatment_date
- GT[386] `01/08/2021` — No extracted record found with this treatment_date
- GT[387] `02/19/2022` — No extracted record found with this treatment_date
- GT[388] `01/23/2022` — No extracted record found with this treatment_date
- GT[389] `06/05/2022` — No extracted record found with this treatment_date
- GT[390] `04/20/2021` — No extracted record found with this treatment_date
- GT[391] `11/19/2022` — No extracted record found with this treatment_date
- GT[392] `04/13/2021` — No extracted record found with this treatment_date
- GT[393] `08/10/2024` — No extracted record found with this treatment_date
- GT[394] `07/22/2024` — No extracted record found with this treatment_date
- GT[395] `06/30/2023` — No extracted record found with this treatment_date
- GT[396] `06/24/2023` — No extracted record found with this treatment_date
- GT[397] `11/23/2022` — No extracted record found with this treatment_date
- GT[398] `08/25/2024` — No extracted record found with this treatment_date
- GT[399] `01/12/2021` — No extracted record found with this treatment_date

**Field mismatches (52):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 6 | `insurers` | 05/04/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 9 | `insurers` | 10/13/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 37 | `cpt_codes` | 06/22/2021 | missing=['95921', '97018', '99201', '99214,25', 'J0205']  extra=['72158', '73100', '90834', '99213'] |
| 37 | `total_charges` | 06/22/2021 | extracted=1820.15  expected=1526.83  diff=293.32 |
| 37 | `ins_paid` | 06/22/2021 | extracted=983.52  expected=862.76  diff=120.76 |
| 37 | `adjustment` | 06/22/2021 | extracted=827.04  expected=664.07  diff=162.97 |
| 37 | `balance` | 06/22/2021 | extracted=9.59  expected=0.0  diff=9.59 |
| 74 | `cpt_codes` | 10/08/2021 | missing=['72110', '73564', '76700', '90472', '99281', '99282']  extra=['90960', '97010', '97035', '99284', 'A4246', 'A4616', 'J1040'] |
| 74 | `total_charges` | 10/08/2021 | extracted=1747.47  expected=2078.23  diff=330.76 |
| 74 | `ins_paid` | 10/08/2021 | extracted=950.39  expected=1242.08  diff=291.69 |
| 74 | `adjustment` | 10/08/2021 | extracted=776.18  expected=806.64  diff=30.46 |
| 74 | `balance` | 10/08/2021 | extracted=20.9  expected=29.51  diff=8.61 |
| 105 | `cpt_codes` | 10/13/2023 | missing=['76705', '85025', '97140', '99211', 'Q0169']  extra=['71048', '97012', '97110', 'Q4100'] |
| 105 | `total_charges` | 10/13/2023 | extracted=1251.41  expected=1909.65  diff=658.24 |
| 105 | `ins_paid` | 10/13/2023 | extracted=802.89  expected=1097.66  diff=294.77 |
| 105 | `adjustment` | 10/13/2023 | extracted=448.52  expected=791.58  diff=343.06 |
| 105 | `balance` | 10/13/2023 | extracted=0.0  expected=20.41  diff=20.41 |
| 105 | `insurers` | 10/13/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 243 | `cpt_codes` | 06/25/2023 | missing=['97116', '99201'] |
| 243 | `payments` | 06/25/2023 | extracted=48.22  expected=None |
| 243 | `balance` | 06/25/2023 | extracted=0.0  expected=48.22  diff=48.22 |
| 243 | `provider` | 06/25/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 244 | `payments` | 05/05/2021 | extracted=54.08  expected=None |
| 244 | `balance` | 05/05/2021 | extracted=0.0  expected=54.08  diff=54.08 |
| 244 | `provider` | 05/05/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 244 | `insurers` | 05/05/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 245 | `provider` | 01/13/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 246 | `payments` | 07/22/2022 | extracted=31.96  expected=None |
| 246 | `balance` | 07/22/2022 | extracted=0.0  expected=31.96  diff=31.96 |
| 246 | `provider` | 07/22/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 247 | `payments` | 08/05/2023 | extracted=50.28  expected=None |
| 247 | `balance` | 08/05/2023 | extracted=0.0  expected=50.28  diff=50.28 |
| 247 | `provider` | 08/05/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 248 | `provider` | 08/28/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 249 | `provider` | 10/08/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 250 | `payments` | 05/31/2022 | extracted=16.75  expected=None |
| 250 | `balance` | 05/31/2022 | extracted=0.0  expected=16.75  diff=16.75 |
| 250 | `provider` | 05/31/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 251 | `payments` | 08/30/2022 | extracted=19.06  expected=None |
| 251 | `balance` | 08/30/2022 | extracted=0.0  expected=19.06  diff=19.06 |
| 251 | `provider` | 08/30/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 252 | `provider` | 12/31/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 253 | `provider` | 02/23/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 254 | `provider` | 04/23/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 255 | `payments` | 10/09/2021 | extracted=17.63  expected=None |
| 255 | `balance` | 10/09/2021 | extracted=0.0  expected=17.63  diff=17.63 |
| 255 | `provider` | 10/09/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 340 | `cpt_codes` | 10/13/2021 | missing=['86592', '93306', '97022', '97530', '99233', '99284']  extra=['72100', '90472', '90935', '99214', 'J1055', 'J9060'] |
| 340 | `total_charges` | 10/13/2021 | extracted=1882.58  expected=1615.5  diff=267.08 |
| 340 | `ins_paid` | 10/13/2021 | extracted=844.46  expected=1000.03  diff=155.57 |
| 340 | `adjustment` | 10/13/2021 | extracted=1038.12  expected=582.78  diff=455.34 |
| 340 | `balance` | 10/13/2021 | extracted=0.0  expected=32.69  diff=32.69 |

### doc_008

**Count mismatch** — GT: 100, extracted: 26.

**Missing records (98):**
- GT[2] `01/08/2021 - 11/19/2024` — No extracted record found with this treatment_date
- GT[3] `05/23/2021 - 11/04/2024` — No extracted record found with this treatment_date
- GT[4] `03/30/2022 - 07/30/2024` — No extracted record found with this treatment_date
- GT[5] `07/12/2021 - 05/01/2024` — No extracted record found with this treatment_date
- GT[6] `04/12/2021 - 10/11/2024` — No extracted record found with this treatment_date
- GT[7] `04/08/2021 - 06/20/2024` — No extracted record found with this treatment_date
- GT[8] `03/13/2021 - 12/18/2024` — No extracted record found with this treatment_date
- GT[9] `04/03/2021 - 11/04/2024` — No extracted record found with this treatment_date
- GT[10] `01/29/2021 - 10/20/2024` — No extracted record found with this treatment_date
- GT[11] `01/15/2021 - 09/02/2024` — No extracted record found with this treatment_date
- GT[12] `01/02/2021 - 10/22/2024` — No extracted record found with this treatment_date
- GT[13] `04/11/2021 - 12/21/2024` — No extracted record found with this treatment_date
- GT[14] `01/07/2021 - 12/13/2024` — No extracted record found with this treatment_date
- GT[15] `02/15/2021 - 10/14/2024` — No extracted record found with this treatment_date
- GT[16] `02/08/2021 - 06/05/2024` — No extracted record found with this treatment_date
- GT[17] `03/04/2021 - 11/24/2024` — No extracted record found with this treatment_date
- GT[18] `10/15/2021 - 08/17/2024` — No extracted record found with this treatment_date
- GT[19] `02/04/2021 - 12/23/2024` — No extracted record found with this treatment_date
- GT[20] `01/31/2021 - 10/28/2024` — No extracted record found with this treatment_date
- GT[21] `02/19/2021 - 11/23/2024` — No extracted record found with this treatment_date
- GT[22] `01/10/2021 - 11/04/2024` — No extracted record found with this treatment_date
- GT[23] `09/21/2021 - 09/12/2024` — No extracted record found with this treatment_date
- GT[24] `03/03/2021 - 11/25/2024` — No extracted record found with this treatment_date
- GT[25] `04/29/2021 - 12/12/2024` — No extracted record found with this treatment_date
- GT[26] `12/24/2022 - 12/28/2024` — No extracted record found with this treatment_date
- GT[27] `07/18/2021 - 11/23/2024` — No extracted record found with this treatment_date
- GT[28] `01/15/2021 - 10/02/2024` — No extracted record found with this treatment_date
- GT[29] `06/26/2021 - 10/17/2024` — No extracted record found with this treatment_date
- GT[30] `05/26/2021 - 12/12/2024` — No extracted record found with this treatment_date
- GT[31] `02/20/2021 - 11/15/2024` — No extracted record found with this treatment_date
- GT[32] `01/06/2021 - 11/28/2024` — No extracted record found with this treatment_date
- GT[33] `03/10/2021 - 12/25/2024` — No extracted record found with this treatment_date
- GT[34] `08/26/2021 - 02/26/2024` — No extracted record found with this treatment_date
- GT[35] `04/12/2021 - 12/28/2024` — No extracted record found with this treatment_date
- GT[36] `03/23/2021 - 05/05/2024` — No extracted record found with this treatment_date
- GT[37] `02/27/2021 - 12/03/2024` — No extracted record found with this treatment_date
- GT[38] `03/14/2021 - 10/31/2024` — No extracted record found with this treatment_date
- GT[39] `01/19/2021 - 11/04/2024` — No extracted record found with this treatment_date
- GT[40] `01/22/2021 - 09/03/2024` — No extracted record found with this treatment_date
- GT[41] `05/01/2021 - 12/24/2024` — No extracted record found with this treatment_date
- GT[42] `02/03/2021 - 10/28/2024` — No extracted record found with this treatment_date
- GT[43] `03/25/2021 - 09/23/2024` — No extracted record found with this treatment_date
- GT[44] `02/07/2021 - 10/07/2024` — No extracted record found with this treatment_date
- GT[45] `01/10/2021 - 04/18/2024` — No extracted record found with this treatment_date
- GT[46] `02/04/2021 - 12/21/2024` — No extracted record found with this treatment_date
- GT[47] `05/12/2021 - 12/03/2024` — No extracted record found with this treatment_date
- GT[48] `06/07/2022 - 09/18/2024` — No extracted record found with this treatment_date
- GT[49] `02/23/2021 - 08/30/2024` — No extracted record found with this treatment_date
- GT[50] `08/28/2021 - 10/02/2024` — No extracted record found with this treatment_date
- GT[51] `02/07/2021 - 10/19/2024` — No extracted record found with this treatment_date
- GT[52] `01/13/2021 - 09/09/2024` — No extracted record found with this treatment_date
- GT[53] `03/01/2021 - 09/17/2024` — No extracted record found with this treatment_date
- GT[54] `05/29/2021 - 09/14/2024` — No extracted record found with this treatment_date
- GT[55] `10/04/2021 - 09/16/2024` — No extracted record found with this treatment_date
- GT[56] `02/23/2021 - 08/18/2024` — No extracted record found with this treatment_date
- GT[57] `05/03/2021 - 06/29/2024` — No extracted record found with this treatment_date
- GT[58] `03/23/2021 - 10/07/2024` — No extracted record found with this treatment_date
- GT[59] `01/22/2021 - 12/05/2024` — No extracted record found with this treatment_date
- GT[60] `01/08/2021 - 07/20/2024` — No extracted record found with this treatment_date
- GT[61] `03/10/2021 - 06/19/2024` — No extracted record found with this treatment_date
- GT[62] `06/08/2021 - 09/14/2024` — No extracted record found with this treatment_date
- GT[63] `10/21/2021 - 08/12/2024` — No extracted record found with this treatment_date
- GT[64] `02/02/2021 - 12/26/2024` — No extracted record found with this treatment_date
- GT[65] `04/22/2021 - 05/07/2024` — No extracted record found with this treatment_date
- GT[66] `02/27/2021 - 11/06/2024` — No extracted record found with this treatment_date
- GT[67] `06/24/2021 - 09/30/2024` — No extracted record found with this treatment_date
- GT[68] `01/09/2021 - 11/14/2024` — No extracted record found with this treatment_date
- GT[69] `03/09/2021 - 11/18/2024` — No extracted record found with this treatment_date
- GT[70] `02/27/2021 - 06/26/2024` — No extracted record found with this treatment_date
- GT[71] `04/19/2021 - 06/09/2024` — No extracted record found with this treatment_date
- GT[72] `01/13/2021 - 12/11/2024` — No extracted record found with this treatment_date
- GT[73] `02/20/2021 - 12/09/2024` — No extracted record found with this treatment_date
- GT[74] `01/13/2021 - 11/16/2024` — No extracted record found with this treatment_date
- GT[75] `04/07/2021 - 09/21/2024` — No extracted record found with this treatment_date
- GT[76] `01/26/2021 - 12/04/2024` — No extracted record found with this treatment_date
- GT[77] `02/04/2021 - 10/23/2024` — No extracted record found with this treatment_date
- GT[78] `01/05/2021 - 11/20/2024` — No extracted record found with this treatment_date
- GT[79] `04/14/2021 - 12/18/2024` — No extracted record found with this treatment_date
- GT[80] `02/04/2021 - 12/17/2024` — No extracted record found with this treatment_date
- GT[81] `04/23/2021 - 11/26/2024` — No extracted record found with this treatment_date
- GT[82] `01/04/2021 - 12/16/2024` — No extracted record found with this treatment_date
- GT[83] `06/09/2021 - 12/29/2024` — No extracted record found with this treatment_date
- GT[84] `02/12/2021 - 09/21/2024` — No extracted record found with this treatment_date
- GT[85] `04/06/2021 - 11/30/2024` — No extracted record found with this treatment_date
- GT[86] `05/05/2021 - 11/19/2024` — No extracted record found with this treatment_date
- GT[87] `01/30/2021 - 07/28/2024` — No extracted record found with this treatment_date
- GT[88] `06/06/2021 - 06/15/2024` — No extracted record found with this treatment_date
- GT[89] `11/13/2021 - 07/29/2024` — No extracted record found with this treatment_date
- GT[90] `03/03/2021 - 12/23/2024` — No extracted record found with this treatment_date
- GT[91] `01/11/2021 - 09/04/2024` — No extracted record found with this treatment_date
- GT[92] `04/15/2021 - 12/22/2024` — No extracted record found with this treatment_date
- GT[93] `01/18/2021 - 08/27/2024` — No extracted record found with this treatment_date
- GT[94] `05/24/2021 - 07/18/2024` — No extracted record found with this treatment_date
- GT[95] `01/21/2021 - 11/24/2024` — No extracted record found with this treatment_date
- GT[96] `04/30/2021 - 10/11/2024` — No extracted record found with this treatment_date
- GT[97] `01/17/2021 - 07/17/2024` — No extracted record found with this treatment_date
- GT[98] `05/14/2021 - 09/12/2024` — No extracted record found with this treatment_date
- GT[99] `08/18/2021 - 11/08/2024` — No extracted record found with this treatment_date

**Extra extracted records (24):**
- `01/23/2023` — Extracted record has no GT counterpart
- `10/22/2021` — Extracted record has no GT counterpart
- `02/04/2023` — Extracted record has no GT counterpart
- `07/10/2023` — Extracted record has no GT counterpart
- `07/15/2021` — Extracted record has no GT counterpart
- `11/30/2024` — Extracted record has no GT counterpart
- `09/26/2023` — Extracted record has no GT counterpart
- `01/06/2024` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `11/08/2022` — Extracted record has no GT counterpart
- `08/14/2024` — Extracted record has no GT counterpart
- `11/21/2021` — Extracted record has no GT counterpart
- `06/10/2022` — Extracted record has no GT counterpart
- `03/03/2023` — Extracted record has no GT counterpart
- `10/20/2024` — Extracted record has no GT counterpart
- `08/28/2024` — Extracted record has no GT counterpart
- `02/27/2023` — Extracted record has no GT counterpart
- `05/25/2021` — Extracted record has no GT counterpart
- `09/19/2022` — Extracted record has no GT counterpart
- `08/05/2021` — Extracted record has no GT counterpart
- `01/08/2023` — Extracted record has no GT counterpart
- `05/01/2023` — Extracted record has no GT counterpart
- `06/10/2024` — Extracted record has no GT counterpart
- `12/19/2023` — Extracted record has no GT counterpart

**Field mismatches (14):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `cpt_codes` | 06/04/2021 - 11/30/2024 | missing=['71046', '72100', '73030', '73060', '73110', '73564', '76705', '77067'] |
| 0 | `total_charges` | 06/04/2021 - 11/30/2024 | extracted=663.56  expected=5342.73  diff=4679.17 |
| 0 | `ins_paid` | 06/04/2021 - 11/30/2024 | extracted=440.39  expected=3373.28  diff=2932.89 |
| 0 | `adjustment` | 06/04/2021 - 11/30/2024 | extracted=124.7  expected=1604.45  diff=1479.75 |
| 0 | `payments` | 06/04/2021 - 11/30/2024 | extracted=98.47  expected=None |
| 0 | `balance` | 06/04/2021 - 11/30/2024 | extracted=0.0  expected=365.0  diff=365.00 |
| 0 | `description` | 06/04/2021 - 11/30/2024 | extracted='MRI lumbar spine without and with contrast'  expected=None |
| 1 | `cpt_codes` | 01/25/2021 - 10/20/2024 | missing=['71048', '72158', '73100', '73110', '73562', '74177', '76700', '76705', '76830', 'A4570', 'A4614', 'Q9920'] |
| 1 | `total_charges` | 01/25/2021 - 10/20/2024 | extracted=871.76  expected=7766.86  diff=6895.10 |
| 1 | `ins_paid` | 01/25/2021 - 10/20/2024 | extracted=579.02  expected=4658.49  diff=4079.47 |
| 1 | `adjustment` | 01/25/2021 - 10/20/2024 | extracted=181.85  expected=2847.8  diff=2665.95 |
| 1 | `payments` | 01/25/2021 - 10/20/2024 | extracted=110.89  expected=None |
| 1 | `balance` | 01/25/2021 - 10/20/2024 | extracted=0.0  expected=260.57  diff=260.57 |
| 1 | `description` | 01/25/2021 - 10/20/2024 | extracted='Screening mammography, bilateral'  expected=None |

### doc_009

**Count mismatch** — GT: 1, extracted: 89.

**Extra extracted records (88):**
- `01/01/2017` — Extracted record has no GT counterpart
- `01/01/2017` — Extracted record has no GT counterpart
- `01/02/2017` — Extracted record has no GT counterpart
- `01/04/2017` — Extracted record has no GT counterpart
- `01/04/2017` — Extracted record has no GT counterpart
- `01/05/2017` — Extracted record has no GT counterpart
- `01/06/2017` — Extracted record has no GT counterpart
- `01/08/2017` — Extracted record has no GT counterpart
- `01/08/2017` — Extracted record has no GT counterpart
- `01/09/2017` — Extracted record has no GT counterpart
- `01/09/2017` — Extracted record has no GT counterpart
- `01/10/2017` — Extracted record has no GT counterpart
- `01/11/2017` — Extracted record has no GT counterpart
- `01/12/2017` — Extracted record has no GT counterpart
- `12/24/2020` — Extracted record has no GT counterpart
- `12/24/2020` — Extracted record has no GT counterpart
- `12/25/2020` — Extracted record has no GT counterpart
- `12/26/2020` — Extracted record has no GT counterpart
- `12/27/2020` — Extracted record has no GT counterpart
- `12/28/2020` — Extracted record has no GT counterpart
- `12/28/2020` — Extracted record has no GT counterpart
- `12/29/2020` — Extracted record has no GT counterpart
- `12/29/2020` — Extracted record has no GT counterpart
- `12/29/2020` — Extracted record has no GT counterpart
- `11/06/2024` — Extracted record has no GT counterpart
- `11/08/2024` — Extracted record has no GT counterpart
- `11/08/2024` — Extracted record has no GT counterpart
- `11/09/2024` — Extracted record has no GT counterpart
- `11/09/2024` — Extracted record has no GT counterpart
- `11/09/2024` — Extracted record has no GT counterpart
- `11/11/2024` — Extracted record has no GT counterpart
- `11/11/2024` — Extracted record has no GT counterpart
- `11/11/2024` — Extracted record has no GT counterpart
- `11/11/2024` — Extracted record has no GT counterpart
- `11/11/2024` — Extracted record has no GT counterpart
- `11/12/2024` — Extracted record has no GT counterpart
- `11/13/2024` — Extracted record has no GT counterpart
- `11/14/2024` — Extracted record has no GT counterpart
- `11/14/2024` — Extracted record has no GT counterpart
- `11/15/2024` — Extracted record has no GT counterpart
- `11/16/2024` — Extracted record has no GT counterpart
- `11/16/2024` — Extracted record has no GT counterpart
- `11/17/2024` — Extracted record has no GT counterpart
- `11/18/2024` — Extracted record has no GT counterpart
- `11/18/2024` — Extracted record has no GT counterpart
- `11/19/2024` — Extracted record has no GT counterpart
- `11/19/2024` — Extracted record has no GT counterpart
- `11/19/2024` — Extracted record has no GT counterpart
- `11/20/2024` — Extracted record has no GT counterpart
- `11/20/2024` — Extracted record has no GT counterpart
- `11/21/2024` — Extracted record has no GT counterpart
- `11/22/2024` — Extracted record has no GT counterpart
- `11/22/2024` — Extracted record has no GT counterpart
- `11/23/2024` — Extracted record has no GT counterpart
- `11/23/2024` — Extracted record has no GT counterpart
- `11/23/2024` — Extracted record has no GT counterpart
- `11/23/2024` — Extracted record has no GT counterpart
- `11/24/2024` — Extracted record has no GT counterpart
- `11/24/2024` — Extracted record has no GT counterpart
- `11/24/2024` — Extracted record has no GT counterpart
- `11/24/2024` — Extracted record has no GT counterpart
- `11/25/2024` — Extracted record has no GT counterpart
- `11/26/2024` — Extracted record has no GT counterpart
- `11/27/2024` — Extracted record has no GT counterpart
- `11/28/2024` — Extracted record has no GT counterpart
- `11/28/2024` — Extracted record has no GT counterpart
- `11/28/2024` — Extracted record has no GT counterpart
- `11/29/2024` — Extracted record has no GT counterpart
- `11/29/2024` — Extracted record has no GT counterpart
- `11/29/2024` — Extracted record has no GT counterpart
- `12/01/2024` — Extracted record has no GT counterpart
- `12/01/2024` — Extracted record has no GT counterpart
- `12/01/2024` — Extracted record has no GT counterpart
- `12/02/2024` — Extracted record has no GT counterpart
- `12/02/2024` — Extracted record has no GT counterpart
- `12/02/2024` — Extracted record has no GT counterpart
- `12/03/2024` — Extracted record has no GT counterpart
- `12/03/2024` — Extracted record has no GT counterpart
- `12/03/2024` — Extracted record has no GT counterpart
- `12/04/2024` — Extracted record has no GT counterpart
- `12/05/2024` — Extracted record has no GT counterpart
- `12/06/2024` — Extracted record has no GT counterpart
- `12/08/2024` — Extracted record has no GT counterpart
- `12/08/2024` — Extracted record has no GT counterpart
- `12/09/2024` — Extracted record has no GT counterpart
- `12/09/2024` — Extracted record has no GT counterpart
- `12/10/2024` — Extracted record has no GT counterpart
- `12/10/2024` — Extracted record has no GT counterpart

**Field mismatches (6):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `total_charges` | 01/01/2017 - 12/31/2024 | extracted=403.09  expected=1262450.18  diff=1262047.09 |
| 0 | `ins_paid` | 01/01/2017 - 12/31/2024 | extracted=None  expected=948201.11 |
| 0 | `payments` | 01/01/2017 - 12/31/2024 | extracted=106.7  expected=314249.07  diff=314142.37 |
| 0 | `balance` | 01/01/2017 - 12/31/2024 | extracted=296.39  expected=0.0  diff=296.39 |
| 0 | `third_parties` | 01/01/2017 - 12/31/2024 | missing=['allwin', 'argus', 'benefit plan', 'blink health', 'caremark', 'cigna healthspring', 'discount program', 'express scripts', 'goodrx', 'mckesson health pbm', 'medco health', 'my rx card', 'omnisys immunizations', 'optumrx', 'paramount lonestar', 'pbm program', 'scriptcycle', 'sfs', 'supplemental coverage', 'third party program'] |
| 0 | `description` | 01/01/2017 - 12/31/2024 | extracted=None  expected='Pharmacy Record' |

### doc_010

**Count mismatch** — GT: 1, extracted: 20.

**Extra extracted records (19):**
- `01/02/2017` — Extracted record has no GT counterpart
- `01/02/2017` — Extracted record has no GT counterpart
- `01/02/2017` — Extracted record has no GT counterpart
- `01/04/2017` — Extracted record has no GT counterpart
- `01/06/2017` — Extracted record has no GT counterpart
- `01/06/2017` — Extracted record has no GT counterpart
- `01/07/2017` — Extracted record has no GT counterpart
- `04/24/2021` — Extracted record has no GT counterpart
- `04/25/2021` — Extracted record has no GT counterpart
- `04/25/2021` — Extracted record has no GT counterpart
- `04/25/2021` — Extracted record has no GT counterpart
- `04/28/2021` — Extracted record has no GT counterpart
- `04/28/2021` — Extracted record has no GT counterpart
- `04/28/2021` — Extracted record has no GT counterpart
- `04/29/2021` — Extracted record has no GT counterpart
- `04/29/2021` — Extracted record has no GT counterpart
- `04/29/2021` — Extracted record has no GT counterpart
- `04/29/2021` — Extracted record has no GT counterpart
- `04/30/2021` — Extracted record has no GT counterpart

**Field mismatches (7):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `total_charges` | 01/01/2017 - 12/29/2024 | extracted=138.37  expected=1247488.96  diff=1247350.59 |
| 0 | `ins_paid` | 01/01/2017 - 12/29/2024 | extracted=101.28  expected=373214.66  diff=373113.38 |
| 0 | `adjustment` | 01/01/2017 - 12/29/2024 | extracted=None  expected=562959.56 |
| 0 | `payments` | 01/01/2017 - 12/29/2024 | extracted=37.09  expected=311314.74  diff=311277.65 |
| 0 | `insurers` | 01/01/2017 - 12/29/2024 | extra=['paramount'] |
| 0 | `third_parties` | 01/01/2017 - 12/29/2024 | missing=['allwin', 'argus', 'blink health', 'caremark', 'cigna healthspring', 'express scripts', 'goodrx', 'mckesson health pbm', 'medco health', 'my rx card', 'omnisys immunizations', 'optumrx', 'paramount lonestar', 'scriptcycle', 'sfs']  extra=['lonestar'] |
| 0 | `description` | 01/01/2017 - 12/29/2024 | extracted=None  expected='Pharmacy Expense Report' |

### doc_011

**Count mismatch** — GT: 150, extracted: 17.

**Missing records (134):**
- GT[5] `08/08/2022 - 08/11/2022` — No extracted record found with this treatment_date
- GT[6] `10/12/2020 - 10/13/2020` — No extracted record found with this treatment_date
- GT[7] `05/07/2022 - 05/08/2022` — No extracted record found with this treatment_date
- GT[8] `07/16/2017 - 07/17/2017` — No extracted record found with this treatment_date
- GT[9] `11/02/2019 - 11/06/2019` — No extracted record found with this treatment_date
- GT[10] `10/03/2020 - 10/06/2020` — No extracted record found with this treatment_date
- GT[11] `05/09/2022 - 05/10/2022` — No extracted record found with this treatment_date
- GT[12] `01/17/2018 - 01/24/2018` — No extracted record found with this treatment_date
- GT[13] `12/29/2019 - 01/05/2020` — No extracted record found with this treatment_date
- GT[14] `05/28/2024 - 06/01/2024` — No extracted record found with this treatment_date
- GT[15] `06/16/2021 - 06/23/2021` — No extracted record found with this treatment_date
- GT[16] `02/03/2023 - 02/09/2023` — No extracted record found with this treatment_date
- GT[17] `05/04/2021 - 05/08/2021` — No extracted record found with this treatment_date
- GT[18] `09/21/2019 - 09/26/2019` — No extracted record found with this treatment_date
- GT[19] `07/06/2018 - 07/07/2018` — No extracted record found with this treatment_date
- GT[20] `09/15/2022 - 09/22/2022` — No extracted record found with this treatment_date
- GT[21] `10/28/2021 - 11/03/2021` — No extracted record found with this treatment_date
- GT[22] `07/14/2024 - 07/16/2024` — No extracted record found with this treatment_date
- GT[23] `12/16/2022 - 12/20/2022` — No extracted record found with this treatment_date
- GT[24] `04/16/2021 - 04/23/2021` — No extracted record found with this treatment_date
- GT[25] `08/21/2022 - 08/28/2022` — No extracted record found with this treatment_date
- GT[26] `01/26/2023 - 02/02/2023` — No extracted record found with this treatment_date
- GT[27] `03/12/2018 - 03/15/2018` — No extracted record found with this treatment_date
- GT[28] `11/09/2020 - 11/15/2020` — No extracted record found with this treatment_date
- GT[29] `12/13/2022 - 12/16/2022` — No extracted record found with this treatment_date
- GT[30] `03/22/2023 - 03/23/2023` — No extracted record found with this treatment_date
- GT[31] `10/08/2021 - 10/14/2021` — No extracted record found with this treatment_date
- GT[32] `10/24/2024 - 10/28/2024` — No extracted record found with this treatment_date
- GT[33] `10/10/2024 - 10/11/2024` — No extracted record found with this treatment_date
- GT[34] `01/30/2019 - 02/03/2019` — No extracted record found with this treatment_date
- GT[35] `05/11/2017 - 05/14/2017` — No extracted record found with this treatment_date
- GT[36] `03/20/2021 - 03/24/2021` — No extracted record found with this treatment_date
- GT[37] `05/17/2020 - 05/20/2020` — No extracted record found with this treatment_date
- GT[38] `12/19/2022 - 12/21/2022` — No extracted record found with this treatment_date
- GT[39] `08/06/2020 - 08/07/2020` — No extracted record found with this treatment_date
- GT[40] `04/09/2017 - 04/13/2017` — No extracted record found with this treatment_date
- GT[41] `07/25/2023 - 07/30/2023` — No extracted record found with this treatment_date
- GT[42] `07/15/2019 - 07/18/2019` — No extracted record found with this treatment_date
- GT[43] `07/28/2022 - 08/04/2022` — No extracted record found with this treatment_date
- GT[44] `12/25/2019 - 12/27/2019` — No extracted record found with this treatment_date
- GT[45] `01/01/2019 - 01/08/2019` — No extracted record found with this treatment_date
- GT[46] `10/11/2023 - 10/14/2023` — No extracted record found with this treatment_date
- GT[47] `05/04/2021 - 05/06/2021` — No extracted record found with this treatment_date
- GT[48] `09/10/2017 - 09/14/2017` — No extracted record found with this treatment_date
- GT[49] `07/08/2022 - 07/10/2022` — No extracted record found with this treatment_date
- GT[50] `08/08/2022 - 08/12/2022` — No extracted record found with this treatment_date
- GT[51] `08/05/2023 - 08/11/2023` — No extracted record found with this treatment_date
- GT[52] `02/23/2020 - 02/28/2020` — No extracted record found with this treatment_date
- GT[53] `03/12/2019 - 03/14/2019` — No extracted record found with this treatment_date
- GT[54] `12/20/2021 - 12/27/2021` — No extracted record found with this treatment_date
- GT[55] `10/15/2020 - 10/16/2020` — No extracted record found with this treatment_date
- GT[56] `12/10/2021 - 12/12/2021` — No extracted record found with this treatment_date
- GT[57] `07/11/2019 - 07/12/2019` — No extracted record found with this treatment_date
- GT[58] `01/27/2021 - 02/02/2021` — No extracted record found with this treatment_date
- GT[59] `10/15/2022 - 10/16/2022` — No extracted record found with this treatment_date
- GT[60] `05/08/2017 - 05/10/2017` — No extracted record found with this treatment_date
- GT[61] `01/26/2022 - 01/31/2022` — No extracted record found with this treatment_date
- GT[62] `05/01/2024 - 05/02/2024` — No extracted record found with this treatment_date
- GT[63] `04/07/2017 - 04/11/2017` — No extracted record found with this treatment_date
- GT[64] `03/27/2024 - 04/03/2024` — No extracted record found with this treatment_date
- GT[65] `10/03/2019 - 10/08/2019` — No extracted record found with this treatment_date
- GT[66] `05/05/2024 - 05/12/2024` — No extracted record found with this treatment_date
- GT[67] `03/30/2021 - 04/01/2021` — No extracted record found with this treatment_date
- GT[68] `02/03/2024 - 02/04/2024` — No extracted record found with this treatment_date
- GT[69] `10/14/2017 - 10/20/2017` — No extracted record found with this treatment_date
- GT[70] `08/14/2023 - 08/21/2023` — No extracted record found with this treatment_date
- GT[71] `09/29/2023 - 10/06/2023` — No extracted record found with this treatment_date
- GT[72] `03/10/2019 - 03/15/2019` — No extracted record found with this treatment_date
- GT[73] `11/01/2020 - 11/03/2020` — No extracted record found with this treatment_date
- GT[74] `09/22/2018 - 09/24/2018` — No extracted record found with this treatment_date
- GT[86] `02/06/2017 - 02/11/2017` — No extracted record found with this treatment_date
- GT[87] `11/26/2021 - 11/28/2021` — No extracted record found with this treatment_date
- GT[88] `12/07/2021 - 12/14/2021` — No extracted record found with this treatment_date
- GT[89] `12/16/2024 - 12/17/2024` — No extracted record found with this treatment_date
- GT[90] `09/16/2022 - 09/20/2022` — No extracted record found with this treatment_date
- GT[91] `11/20/2022 - 11/21/2022` — No extracted record found with this treatment_date
- GT[92] `09/16/2020 - 09/22/2020` — No extracted record found with this treatment_date
- GT[93] `11/28/2023 - 11/30/2023` — No extracted record found with this treatment_date
- GT[94] `09/03/2023 - 09/06/2023` — No extracted record found with this treatment_date
- GT[95] `09/25/2024 - 10/01/2024` — No extracted record found with this treatment_date
- GT[96] `06/18/2019 - 06/20/2019` — No extracted record found with this treatment_date
- GT[97] `07/26/2019 - 08/01/2019` — No extracted record found with this treatment_date
- GT[98] `01/15/2019 - 01/17/2019` — No extracted record found with this treatment_date
- GT[99] `03/03/2023 - 03/06/2023` — No extracted record found with this treatment_date
- GT[100] `11/30/2021 - 12/02/2021` — No extracted record found with this treatment_date
- GT[101] `06/27/2021 - 07/02/2021` — No extracted record found with this treatment_date
- GT[102] `06/16/2019 - 06/22/2019` — No extracted record found with this treatment_date
- GT[103] `01/09/2024 - 01/12/2024` — No extracted record found with this treatment_date
- GT[104] `10/25/2020 - 10/29/2020` — No extracted record found with this treatment_date
- GT[105] `07/30/2021 - 08/02/2021` — No extracted record found with this treatment_date
- GT[106] `09/09/2021 - 09/15/2021` — No extracted record found with this treatment_date
- GT[107] `03/20/2020 - 03/27/2020` — No extracted record found with this treatment_date
- GT[108] `08/28/2017 - 09/04/2017` — No extracted record found with this treatment_date
- GT[109] `02/10/2023 - 02/16/2023` — No extracted record found with this treatment_date
- GT[110] `06/24/2018 - 06/26/2018` — No extracted record found with this treatment_date
- GT[111] `04/12/2021 - 04/15/2021` — No extracted record found with this treatment_date
- GT[112] `02/22/2023 - 03/01/2023` — No extracted record found with this treatment_date
- GT[113] `07/28/2021 - 07/29/2021` — No extracted record found with this treatment_date
- GT[114] `11/22/2022 - 11/26/2022` — No extracted record found with this treatment_date
- GT[115] `01/11/2024 - 01/18/2024` — No extracted record found with this treatment_date
- GT[116] `02/07/2022 - 02/14/2022` — No extracted record found with this treatment_date
- GT[117] `04/27/2023 - 05/02/2023` — No extracted record found with this treatment_date
- GT[118] `12/15/2018 - 12/17/2018` — No extracted record found with this treatment_date
- GT[119] `09/06/2017 - 09/10/2017` — No extracted record found with this treatment_date
- GT[120] `01/16/2024 - 01/21/2024` — No extracted record found with this treatment_date
- GT[121] `07/17/2018 - 07/22/2018` — No extracted record found with this treatment_date
- GT[122] `04/28/2024 - 05/02/2024` — No extracted record found with this treatment_date
- GT[123] `10/06/2017 - 10/09/2017` — No extracted record found with this treatment_date
- GT[124] `03/27/2020 - 03/30/2020` — No extracted record found with this treatment_date
- GT[125] `08/22/2024 - 08/27/2024` — No extracted record found with this treatment_date
- GT[126] `06/14/2021 - 06/17/2021` — No extracted record found with this treatment_date
- GT[127] `09/26/2021 - 10/03/2021` — No extracted record found with this treatment_date
- GT[128] `03/10/2019 - 03/13/2019` — No extracted record found with this treatment_date
- GT[129] `10/05/2021 - 10/11/2021` — No extracted record found with this treatment_date
- GT[130] `09/08/2024 - 09/14/2024` — No extracted record found with this treatment_date
- GT[131] `05/12/2021 - 05/13/2021` — No extracted record found with this treatment_date
- GT[132] `08/31/2024 - 09/07/2024` — No extracted record found with this treatment_date
- GT[133] `12/08/2019 - 12/12/2019` — No extracted record found with this treatment_date
- GT[134] `06/09/2020 - 06/10/2020` — No extracted record found with this treatment_date
- GT[135] `07/11/2017 - 07/12/2017` — No extracted record found with this treatment_date
- GT[136] `11/06/2019 - 11/07/2019` — No extracted record found with this treatment_date
- GT[137] `09/16/2021 - 09/17/2021` — No extracted record found with this treatment_date
- GT[138] `12/02/2017 - 12/08/2017` — No extracted record found with this treatment_date
- GT[139] `05/29/2019 - 06/05/2019` — No extracted record found with this treatment_date
- GT[140] `10/05/2018 - 10/08/2018` — No extracted record found with this treatment_date
- GT[141] `05/25/2017 - 06/01/2017` — No extracted record found with this treatment_date
- GT[142] `07/15/2022 - 07/16/2022` — No extracted record found with this treatment_date
- GT[143] `07/11/2021 - 07/12/2021` — No extracted record found with this treatment_date
- GT[144] `05/02/2017 - 05/07/2017` — No extracted record found with this treatment_date
- GT[145] `11/13/2018 - 11/14/2018` — No extracted record found with this treatment_date
- GT[146] `04/07/2022 - 04/13/2022` — No extracted record found with this treatment_date
- GT[147] `05/23/2024 - 05/30/2024` — No extracted record found with this treatment_date
- GT[148] `12/01/2018 - 12/08/2018` — No extracted record found with this treatment_date
- GT[149] `11/13/2022 - 11/15/2022` — No extracted record found with this treatment_date

**Extra extracted records (1):**
- `09/24/2018 - 09/24/2018` — Extracted record has no GT counterpart

**Field mismatches (70):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `payments` | 01/25/2023 - 01/26/2023 | extracted=16802.06  expected=None |
| 0 | `balance` | 01/25/2023 - 01/26/2023 | extracted=0.0  expected=16802.06  diff=16802.06 |
| 0 | `description` | 01/25/2023 - 01/26/2023 | extracted=None  expected='Total knee arthroplasty' |
| 1 | `payments` | 09/13/2023 - 09/19/2023 | extracted=24725.09  expected=None |
| 1 | `balance` | 09/13/2023 - 09/19/2023 | extracted=0.0  expected=24725.09  diff=24725.09 |
| 1 | `description` | 09/13/2023 - 09/19/2023 | extracted=None  expected='Pulmonary embolism' |
| 2 | `payments` | 02/27/2023 - 03/05/2023 | extracted=18230.58  expected=None |
| 2 | `balance` | 02/27/2023 - 03/05/2023 | extracted=0.0  expected=18230.58  diff=18230.58 |
| 2 | `description` | 02/27/2023 - 03/05/2023 | extracted=None  expected='Cellulitis of lower leg' |
| 3 | `payments` | 07/21/2017 - 07/28/2017 | extracted=20570.21  expected=None |
| 3 | `balance` | 07/21/2017 - 07/28/2017 | extracted=0.0  expected=20570.21  diff=20570.21 |
| 3 | `description` | 07/21/2017 - 07/28/2017 | extracted=None  expected='Total knee arthroplasty' |
| 4 | `payments` | 04/18/2023 - 04/22/2023 | extracted=13846.82  expected=None |
| 4 | `balance` | 04/18/2023 - 04/22/2023 | extracted=0.0  expected=13846.82  diff=13846.82 |
| 4 | `description` | 04/18/2023 - 04/22/2023 | extracted=None  expected='Heart failure, unspecified' |
| 75 | `payments` | 02/26/2021 - 03/05/2021 | extracted=18867.13  expected=None |
| 75 | `balance` | 02/26/2021 - 03/05/2021 | extracted=0.0  expected=18867.13  diff=18867.13 |
| 75 | `provider` | 02/26/2021 - 03/05/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 75 | `insurers` | 02/26/2021 - 03/05/2021 | missing=['medicaid'] |
| 75 | `description` | 02/26/2021 - 03/05/2021 | extracted=None  expected='Alcohol withdrawal syndrome' |
| 76 | `payments` | 06/11/2021 - 06/17/2021 | extracted=20616.64  expected=None |
| 76 | `balance` | 06/11/2021 - 06/17/2021 | extracted=0.0  expected=20616.64  diff=20616.64 |
| 76 | `provider` | 06/11/2021 - 06/17/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 76 | `insurers` | 06/11/2021 - 06/17/2021 | missing=['medicaid'] |
| 76 | `description` | 06/11/2021 - 06/17/2021 | extracted=None  expected='Pulmonary embolism' |
| 77 | `payments` | 04/05/2018 - 04/07/2018 | extracted=21750.44  expected=None |
| 77 | `balance` | 04/05/2018 - 04/07/2018 | extracted=0.0  expected=21750.44  diff=21750.44 |
| 77 | `provider` | 04/05/2018 - 04/07/2018 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 77 | `insurers` | 04/05/2018 - 04/07/2018 | missing=['medicaid'] |
| 77 | `description` | 04/05/2018 - 04/07/2018 | extracted=None  expected='Schizophrenia, acute exacerbation' |
| 78 | `payments` | 12/17/2018 - 12/23/2018 | extracted=19797.34  expected=None |
| 78 | `balance` | 12/17/2018 - 12/23/2018 | extracted=0.0  expected=19797.34  diff=19797.34 |
| 78 | `provider` | 12/17/2018 - 12/23/2018 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 78 | `insurers` | 12/17/2018 - 12/23/2018 | missing=['medicaid'] |
| 78 | `description` | 12/17/2018 - 12/23/2018 | extracted=None  expected='Stroke, ischemic' |
| 79 | `payments` | 03/12/2019 - 03/15/2019 | extracted=21595.04  expected=None |
| 79 | `balance` | 03/12/2019 - 03/15/2019 | extracted=0.0  expected=21595.04  diff=21595.04 |
| 79 | `provider` | 03/12/2019 - 03/15/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 79 | `insurers` | 03/12/2019 - 03/15/2019 | missing=['medicaid'] |
| 79 | `description` | 03/12/2019 - 03/15/2019 | extracted=None  expected='Pneumonia, unspecified organism' |
| 80 | `payments` | 06/18/2020 - 06/20/2020 | extracted=20592.69  expected=None |
| 80 | `balance` | 06/18/2020 - 06/20/2020 | extracted=0.0  expected=20592.69  diff=20592.69 |
| 80 | `provider` | 06/18/2020 - 06/20/2020 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 80 | `insurers` | 06/18/2020 - 06/20/2020 | missing=['medicaid'] |
| 80 | `description` | 06/18/2020 - 06/20/2020 | extracted=None  expected='Acute pancreatitis' |
| 81 | `payments` | 03/13/2024 - 03/15/2024 | extracted=21689.11  expected=None |
| 81 | `balance` | 03/13/2024 - 03/15/2024 | extracted=0.0  expected=21689.11  diff=21689.11 |
| 81 | `provider` | 03/13/2024 - 03/15/2024 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 81 | `insurers` | 03/13/2024 - 03/15/2024 | missing=['medicaid'] |
| 81 | `description` | 03/13/2024 - 03/15/2024 | extracted=None  expected='Cellulitis of lower leg' |
| 82 | `payments` | 06/20/2020 - 06/27/2020 | extracted=20879.61  expected=None |
| 82 | `balance` | 06/20/2020 - 06/27/2020 | extracted=0.0  expected=20879.61  diff=20879.61 |
| 82 | `provider` | 06/20/2020 - 06/27/2020 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 82 | `insurers` | 06/20/2020 - 06/27/2020 | missing=['medicaid'] |
| 82 | `description` | 06/20/2020 - 06/27/2020 | extracted=None  expected='Total knee arthroplasty' |
| 83 | `payments` | 01/12/2017 - 01/13/2017 | extracted=21751.41  expected=None |
| 83 | `balance` | 01/12/2017 - 01/13/2017 | extracted=0.0  expected=21751.41  diff=21751.41 |
| 83 | `provider` | 01/12/2017 - 01/13/2017 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 83 | `insurers` | 01/12/2017 - 01/13/2017 | missing=['medicaid'] |
| 83 | `description` | 01/12/2017 - 01/13/2017 | extracted=None  expected='Pneumonia, unspecified organism' |
| 84 | `payments` | 06/17/2020 - 06/21/2020 | extracted=31034.51  expected=None |
| 84 | `balance` | 06/17/2020 - 06/21/2020 | extracted=0.0  expected=31034.51  diff=31034.51 |
| 84 | `provider` | 06/17/2020 - 06/21/2020 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 84 | `insurers` | 06/17/2020 - 06/21/2020 | missing=['medicaid'] |
| 84 | `description` | 06/17/2020 - 06/21/2020 | extracted=None  expected='Heart failure, unspecified' |
| 85 | `payments` | 02/24/2019 - 02/28/2019 | extracted=14609.98  expected=None |
| 85 | `balance` | 02/24/2019 - 02/28/2019 | extracted=0.0  expected=14609.98  diff=14609.98 |
| 85 | `provider` | 02/24/2019 - 02/28/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 85 | `insurers` | 02/24/2019 - 02/28/2019 | missing=['medicaid'] |
| 85 | `description` | 02/24/2019 - 02/28/2019 | extracted=None  expected='Stroke, ischemic' |

### doc_012

**Count mismatch** — GT: 120, extracted: 29.

**Missing records (91):**
- GT[5] `05/04/2017 - 06/05/2017` — No extracted record found with this treatment_date
- GT[6] `06/06/2017 - 07/04/2017` — No extracted record found with this treatment_date
- GT[7] `07/05/2017 - 07/13/2017` — No extracted record found with this treatment_date
- GT[8] `07/14/2017 - 08/12/2017` — No extracted record found with this treatment_date
- GT[9] `08/13/2017 - 09/08/2017` — No extracted record found with this treatment_date
- GT[10] `09/09/2017 - 10/09/2017` — No extracted record found with this treatment_date
- GT[11] `10/10/2017 - 10/18/2017` — No extracted record found with this treatment_date
- GT[12] `10/19/2017 - 11/15/2017` — No extracted record found with this treatment_date
- GT[13] `11/16/2017 - 12/11/2017` — No extracted record found with this treatment_date
- GT[14] `12/12/2017 - 01/12/2018` — No extracted record found with this treatment_date
- GT[15] `01/13/2018 - 01/23/2018` — No extracted record found with this treatment_date
- GT[16] `01/24/2018 - 02/22/2018` — No extracted record found with this treatment_date
- GT[17] `02/23/2018 - 03/23/2018` — No extracted record found with this treatment_date
- GT[18] `03/24/2018 - 04/25/2018` — No extracted record found with this treatment_date
- GT[19] `04/26/2018 - 04/30/2018` — No extracted record found with this treatment_date
- GT[20] `05/01/2018 - 05/30/2018` — No extracted record found with this treatment_date
- GT[21] `05/31/2018 - 07/01/2018` — No extracted record found with this treatment_date
- GT[22] `07/02/2018 - 08/01/2018` — No extracted record found with this treatment_date
- GT[23] `08/02/2018 - 08/05/2018` — No extracted record found with this treatment_date
- GT[24] `08/06/2018 - 09/01/2018` — No extracted record found with this treatment_date
- GT[25] `09/02/2018 - 09/29/2018` — No extracted record found with this treatment_date
- GT[26] `09/30/2018 - 10/26/2018` — No extracted record found with this treatment_date
- GT[27] `10/27/2018 - 11/10/2018` — No extracted record found with this treatment_date
- GT[28] `11/11/2018 - 12/07/2018` — No extracted record found with this treatment_date
- GT[29] `12/08/2018 - 01/07/2019` — No extracted record found with this treatment_date
- GT[30] `01/08/2019 - 02/02/2019` — No extracted record found with this treatment_date
- GT[31] `02/03/2019 - 02/15/2019` — No extracted record found with this treatment_date
- GT[32] `02/16/2019 - 03/14/2019` — No extracted record found with this treatment_date
- GT[33] `03/15/2019 - 04/11/2019` — No extracted record found with this treatment_date
- GT[34] `04/12/2019 - 05/08/2019` — No extracted record found with this treatment_date
- GT[35] `05/09/2019 - 05/23/2019` — No extracted record found with this treatment_date
- GT[36] `05/24/2019 - 06/19/2019` — No extracted record found with this treatment_date
- GT[37] `06/20/2019 - 07/16/2019` — No extracted record found with this treatment_date
- GT[38] `07/17/2019 - 08/13/2019` — No extracted record found with this treatment_date
- GT[39] `08/14/2019 - 08/28/2019` — No extracted record found with this treatment_date
- GT[40] `08/29/2019 - 09/25/2019` — No extracted record found with this treatment_date
- GT[41] `09/26/2019 - 10/26/2019` — No extracted record found with this treatment_date
- GT[42] `10/27/2019 - 11/28/2019` — No extracted record found with this treatment_date
- GT[43] `11/29/2019 - 12/03/2019` — No extracted record found with this treatment_date
- GT[44] `12/04/2019 - 12/29/2019` — No extracted record found with this treatment_date
- GT[45] `12/30/2019 - 01/27/2020` — No extracted record found with this treatment_date
- GT[46] `01/28/2020 - 02/23/2020` — No extracted record found with this treatment_date
- GT[47] `02/24/2020 - 03/09/2020` — No extracted record found with this treatment_date
- GT[48] `03/10/2020 - 04/07/2020` — No extracted record found with this treatment_date
- GT[49] `04/08/2020 - 05/07/2020` — No extracted record found with this treatment_date
- GT[50] `05/08/2020 - 06/09/2020` — No extracted record found with this treatment_date
- GT[51] `06/10/2020 - 06/14/2020` — No extracted record found with this treatment_date
- GT[52] `06/15/2020 - 07/14/2020` — No extracted record found with this treatment_date
- GT[53] `07/15/2020 - 08/09/2020` — No extracted record found with this treatment_date
- GT[54] `08/10/2020 - 09/10/2020` — No extracted record found with this treatment_date
- GT[55] `09/11/2020 - 09/19/2020` — No extracted record found with this treatment_date
- GT[56] `09/20/2020 - 10/17/2020` — No extracted record found with this treatment_date
- GT[57] `10/18/2020 - 11/18/2020` — No extracted record found with this treatment_date
- GT[58] `11/19/2020 - 12/18/2020` — No extracted record found with this treatment_date
- GT[59] `12/19/2020 - 12/25/2020` — No extracted record found with this treatment_date
- GT[60] `12/26/2020 - 01/20/2021` — No extracted record found with this treatment_date
- GT[61] `01/21/2021 - 02/19/2021` — No extracted record found with this treatment_date
- GT[62] `02/20/2021 - 03/20/2021` — No extracted record found with this treatment_date
- GT[63] `03/21/2021 - 04/01/2021` — No extracted record found with this treatment_date
- GT[64] `04/02/2021 - 05/03/2021` — No extracted record found with this treatment_date
- GT[65] `05/04/2021 - 06/04/2021` — No extracted record found with this treatment_date
- GT[66] `06/05/2021 - 07/04/2021` — No extracted record found with this treatment_date
- GT[67] `07/05/2021 - 07/07/2021` — No extracted record found with this treatment_date
- GT[68] `07/08/2021 - 08/08/2021` — No extracted record found with this treatment_date
- GT[69] `08/09/2021 - 09/04/2021` — No extracted record found with this treatment_date
- GT[70] `09/05/2021 - 10/07/2021` — No extracted record found with this treatment_date
- GT[71] `10/08/2021 - 10/12/2021` — No extracted record found with this treatment_date
- GT[72] `10/13/2021 - 11/10/2021` — No extracted record found with this treatment_date
- GT[73] `11/11/2021 - 12/12/2021` — No extracted record found with this treatment_date
- GT[74] `12/13/2021 - 01/13/2022` — No extracted record found with this treatment_date
- GT[75] `01/14/2022 - 01/17/2022` — No extracted record found with this treatment_date
- GT[76] `01/18/2022 - 02/14/2022` — No extracted record found with this treatment_date
- GT[77] `02/15/2022 - 03/17/2022` — No extracted record found with this treatment_date
- GT[78] `03/18/2022 - 04/12/2022` — No extracted record found with this treatment_date
- GT[79] `04/13/2022 - 04/24/2022` — No extracted record found with this treatment_date
- GT[80] `04/25/2022 - 05/20/2022` — No extracted record found with this treatment_date
- GT[81] `05/21/2022 - 06/18/2022` — No extracted record found with this treatment_date
- GT[82] `06/19/2022 - 07/14/2022` — No extracted record found with this treatment_date
- GT[83] `07/15/2022 - 07/30/2022` — No extracted record found with this treatment_date
- GT[84] `07/31/2022 - 08/26/2022` — No extracted record found with this treatment_date
- GT[85] `08/27/2022 - 09/28/2022` — No extracted record found with this treatment_date
- GT[86] `09/29/2022 - 10/26/2022` — No extracted record found with this treatment_date
- GT[87] `10/27/2022 - 11/04/2022` — No extracted record found with this treatment_date
- GT[88] `11/05/2022 - 12/05/2022` — No extracted record found with this treatment_date
- GT[89] `12/06/2022 - 01/06/2023` — No extracted record found with this treatment_date
- GT[90] `01/07/2023 - 02/02/2023` — No extracted record found with this treatment_date
- GT[91] `02/03/2023 - 02/09/2023` — No extracted record found with this treatment_date
- GT[92] `02/10/2023 - 03/12/2023` — No extracted record found with this treatment_date
- GT[93] `03/13/2023 - 04/14/2023` — No extracted record found with this treatment_date
- GT[94] `04/15/2023 - 05/14/2023` — No extracted record found with this treatment_date
- GT[95] `05/15/2023 - 05/17/2023` — No extracted record found with this treatment_date

**Field mismatches (58):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `cpt_codes` | 01/01/2017 - 01/30/2017 | extra=['36831', '82565', '82728', '83540', '84132', '84295', '85025', '90935', '90940', '99213', 'A4690', 'A4706', 'A4730', 'A4750', 'A4755', 'A4920', 'J0885', 'J2916', 'J3370'] |
| 0 | `description` | 01/01/2017 - 01/30/2017 | extracted=None  expected='Dialysis — 10 treatments' |
| 1 | `cpt_codes` | 01/31/2017 - 03/02/2017 | extra=['36821', '36831', '82310', '82565', '82728', '83036', '83540', '84132', '85025', '90935', '90940', 'A4730', 'A4755', 'A4860', 'J0885', 'J2916'] |
| 1 | `description` | 01/31/2017 - 03/02/2017 | extracted=None  expected='Dialysis — 13 treatments' |
| 2 | `cpt_codes` | 03/03/2017 - 04/04/2017 | extra=['82565', '83036', '84132', '84295', '85025', '86000', '90935', '90940', '99213', 'A4690', 'A4706', 'A4750', 'A4920', 'G0491'] |
| 2 | `description` | 03/03/2017 - 04/04/2017 | extracted=None  expected='Dialysis — 8 treatments' |
| 3 | `cpt_codes` | 04/05/2017 - 04/07/2017 | extra=['36821', '36831', '82565', '82728', '84132', '85025', '93975', 'A4706', 'A4730', 'A4750', 'A4755', 'A4860', 'A4920', 'J2916', 'J3370'] |
| 3 | `description` | 04/05/2017 - 04/07/2017 | extracted=None  expected='Dialysis — 9 treatments' |
| 4 | `cpt_codes` | 04/08/2017 - 05/03/2017 | extra=['36821', '36831', '82728', '83036', '84100', '84295', '90937', 'A4690', 'A4706', 'A4750', 'A4802', 'A4920'] |
| 4 | `description` | 04/08/2017 - 05/03/2017 | extracted=None  expected='Dialysis — 12 treatments' |
| 96 | `cpt_codes` | 05/18/2023 - 06/16/2023 | extra=['36831', '84100', '84132', '85025', '86000', '90935', '90937', '90940', '93975', '99213', 'A4690', 'A4706', 'A4730', 'A4750', 'A4755', 'A4920', 'G0491', 'J0885', 'J2916', 'J3370'] |
| 96 | `description` | 05/18/2023 - 06/16/2023 | extracted=None  expected='Dialysis — 10 treatments' |
| 97 | `cpt_codes` | 06/17/2023 - 07/18/2023 | extra=['36821', '36831', '82310', '82728', '83540', '84100', '84132', '84295', '85025', '86000', '90935', '90937', '93975', 'A4690', 'A4706', 'A4730', 'A4802', 'A4920', 'G0491', 'J0885', 'J2916'] |
| 97 | `description` | 06/17/2023 - 07/18/2023 | extracted=None  expected='Dialysis — 8 treatments' |
| 98 | `cpt_codes` | 07/19/2023 - 08/19/2023 | extra=['36831', '82565', '83540', '84100', '84132', '84295', '90935', '90937', '99213', 'A4690', 'A4706', 'A4730', 'A4802', 'A4920', 'J2916', 'J3370'] |
| 98 | `description` | 07/19/2023 - 08/19/2023 | extracted=None  expected='Dialysis — 11 treatments' |
| 99 | `cpt_codes` | 08/20/2023 - 08/22/2023 | extra=['36831', '82310', '82565', '82728', '83036', '83540', '84295', '85025', '90935', '90940', '93975', 'A4690', 'A4706', 'A4755', 'A4860', 'A4920', 'G0491', 'J0885', 'J2916', 'J3370'] |
| 99 | `description` | 08/20/2023 - 08/22/2023 | extracted=None  expected='Dialysis — 12 treatments' |
| 100 | `cpt_codes` | 08/23/2023 - 09/19/2023 | extra=['36831', '82728', '83540', '84100', '84132', '84295', '85025', '86000', '90940', '93975', '99213', 'A4690', 'A4706', 'A4750', 'A4860', 'A4920', 'G0491', 'J0885', 'J3370'] |
| 100 | `description` | 08/23/2023 - 09/19/2023 | extracted=None  expected='Dialysis — 12 treatments' |
| 101 | `cpt_codes` | 09/20/2023 - 10/15/2023 | extra=['82728', '83036', '83540', '84100', '84295', '85025', '90935', '90940', '93975', '99213', 'A4690', 'A4706', 'A4750', 'A4755', 'A4920', 'G0491', 'J2916'] |
| 101 | `description` | 09/20/2023 - 10/15/2023 | extracted=None  expected='Dialysis — 9 treatments' |
| 102 | `cpt_codes` | 10/16/2023 - 11/13/2023 | extra=['36831', '82310', '82565', '82728', '83036', '83540', '84132', '84295', '85025', '90935', '90940', '99213', 'A4706', 'A4730', 'A4860', 'A4920', 'G0491', 'J0885'] |
| 102 | `description` | 10/16/2023 - 11/13/2023 | extracted=None  expected='Dialysis — 10 treatments' |
| 103 | `cpt_codes` | 11/14/2023 - 11/27/2023 | extra=['36831', '84100', '84132', '84295', '85025', '86000', '90935', '90937', '99213', 'A4690', 'A4860', 'J0885', 'J3370'] |
| 103 | `description` | 11/14/2023 - 11/27/2023 | extracted=None  expected='Dialysis — 11 treatments' |
| 104 | `cpt_codes` | 11/28/2023 - 12/24/2023 | extra=['82565', '82728', '83036', '83540', '84132', '85025', '90940', '93975', 'A4730', 'A4750', 'A4755', 'J0885', 'J2916', 'J3370'] |
| 104 | `description` | 11/28/2023 - 12/24/2023 | extracted=None  expected='Dialysis — 10 treatments' |
| 105 | `cpt_codes` | 12/25/2023 - 01/25/2024 | extra=['36821', '82310', '82565', '83036', '83540', '84100', '85025', '86000', '90935', '90940', 'A4690', 'A4706', 'A4730', 'A4750', 'A4755', 'A4802', 'A4860', 'A4920'] |
| 105 | `description` | 12/25/2023 - 01/25/2024 | extracted=None  expected='Dialysis — 12 treatments' |
| 106 | `cpt_codes` | 01/26/2024 - 02/23/2024 | extra=['36831', '82310', '82728', '83540', '84100', '84132', '85025', '86000', '90940', 'A4706', 'A4755', 'A4802', 'A4860', 'G0491', 'J0885'] |
| 106 | `description` | 01/26/2024 - 02/23/2024 | extracted=None  expected='Dialysis — 9 treatments' |
| 107 | `cpt_codes` | 02/24/2024 - 03/03/2024 | extra=['36821', '82310', '82565', '84295', '86000', '90940', '93975', '99213', 'A4690', 'A4750', 'A4802', 'G0491', 'J3370'] |
| 107 | `description` | 02/24/2024 - 03/03/2024 | extracted=None  expected='Dialysis — 10 treatments' |
| 108 | `cpt_codes` | 03/04/2024 - 04/05/2024 | extra=['36821', '36831', '83540', '84100', '85025', '93975', '99213', 'A4730', 'A4750', 'A4755', 'A4802', 'J0885', 'J2916', 'J3370'] |
| 108 | `description` | 03/04/2024 - 04/05/2024 | extracted=None  expected='Dialysis — 10 treatments' |
| 109 | `cpt_codes` | 04/06/2024 - 05/05/2024 | extra=['36831', '82310', '82728', '83036', '83540', '84100', '84295', '86000', '90937', '90940', 'A4690', 'A4706', 'A4755', 'A4920'] |
| 109 | `description` | 04/06/2024 - 05/05/2024 | extracted=None  expected='Dialysis — 11 treatments' |
| 110 | `cpt_codes` | 05/06/2024 - 06/05/2024 | extra=['36821', '36831', '82310', '82728', '83036', '84100', '84132', '90937', '90940', '99213', 'A4690', 'A4755', 'A4802', 'A4920', 'J3370'] |
| 110 | `description` | 05/06/2024 - 06/05/2024 | extracted=None  expected='Dialysis — 9 treatments' |
| 111 | `cpt_codes` | 06/06/2024 - 06/08/2024 | extra=['36821', '36831', '82565', '84132', 'A4690', 'A4730', 'A4860', 'A4920', 'G0491', 'J0885', 'J2916'] |
| 111 | `description` | 06/06/2024 - 06/08/2024 | extracted=None  expected='Dialysis — 12 treatments' |
| 112 | `cpt_codes` | 06/09/2024 - 07/04/2024 | extra=['36821', '36831', '82310', '82728', '83036', '84100', '84132', '86000', '90937', '93975', 'A4706', 'A4730', 'A4750', 'A4802', 'A4920', 'J2916', 'J3370'] |
| 112 | `description` | 06/09/2024 - 07/04/2024 | extracted=None  expected='Dialysis — 11 treatments' |
| 113 | `cpt_codes` | 07/05/2024 - 08/04/2024 | extra=['36821', '36831', '82565', '82728', '83036', '84100', '85025', '86000', '93975', '99213', 'A4750', 'A4755', 'J0885', 'J3370'] |
| 113 | `description` | 07/05/2024 - 08/04/2024 | extracted=None  expected='Dialysis — 10 treatments' |
| 114 | `cpt_codes` | 08/05/2024 - 09/02/2024 | extra=['36831', '82310', '82728', '83036', '83540', '84100', '84132', '85025', '86000', '90940', '99213', 'A4690', 'A4706', 'A4750', 'A4802', 'A4860', 'G0491', 'J2916'] |
| 114 | `description` | 08/05/2024 - 09/02/2024 | extracted=None  expected='Dialysis — 8 treatments' |
| 115 | `cpt_codes` | 09/03/2024 - 09/13/2024 | extra=['36831', '82310', '82728', '83036', '84295', '85025', '90937', '90940', '93975', 'A4706', 'A4730', 'A4755', 'A4920', 'G0491', 'J0885', 'J3370'] |
| 115 | `description` | 09/03/2024 - 09/13/2024 | extracted=None  expected='Dialysis — 9 treatments' |
| 116 | `cpt_codes` | 09/14/2024 - 10/14/2024 | extra=['36821', '82565', '82728', '83036', '83540', '84132', '86000', '90940', '99213', 'A4690', 'A4730', 'A4750', 'A4755', 'A4802', 'A4920', 'G0491', 'J2916'] |
| 116 | `description` | 09/14/2024 - 10/14/2024 | extracted=None  expected='Dialysis — 11 treatments' |
| 117 | `cpt_codes` | 10/15/2024 - 11/14/2024 | extra=['82565', '83036', '83540', '84132', '85025', '86000', '90937', '90940', 'A4690', 'A4706', 'A4750', 'A4802', 'J2916'] |
| 117 | `description` | 10/15/2024 - 11/14/2024 | extracted=None  expected='Dialysis — 9 treatments' |
| 118 | `cpt_codes` | 11/15/2024 - 12/10/2024 | extra=['36821', '36831', '82310', '82565', '82728', '83540', '84295', '86000', '90935', '90937', '99213', 'A4690', 'A4706', 'A4755', 'A4802', 'A4920', 'G0491', 'J0885'] |
| 118 | `description` | 11/15/2024 - 12/10/2024 | extracted=None  expected='Dialysis — 9 treatments' |
| 119 | `cpt_codes` | 12/11/2024 - 12/19/2024 | extra=['36831', '82728', '83036', '83540', '84100', '84132', '90937', '90940', '93975', '99213', 'A4750', 'A4755', 'A4802', 'A4860', 'J0885', 'J2916', 'J3370'] |
| 119 | `description` | 12/11/2024 - 12/19/2024 | extracted=None  expected='Dialysis — 13 treatments' |

---

_Generated by `scripts/eval_extraction.py`_
