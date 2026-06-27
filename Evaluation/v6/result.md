# Extraction Evaluation Results

Evaluated **3 documents** against ground truth.

---

## Summary

| Doc | GT | Extracted | Count | Weighted Acc | Cost USD | Duration |
|---|---|---|---|---|---|---|
| doc_001 | 50 | 50 | ✓ | 100.0% | $0.0963 | 45.59s |
| doc_003 | 1 | 1 | ✓ | 71.4% | $0.0805 | 29.24s |
| doc_008 | 100 | 75 | ✗ | 3.4% | $0.2212 | 41.73s |

**Total cost:** $0.3980  
**Total tokens:** 152,863 (input 137,484 / output 15,379)  
**Total wall-clock:** 116.6s

---

## Field Accuracy by Document

| Doc | date | cpt | total$ | ins$ | adj | pmts | bal | prov | insrs | 3p | desc |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doc_001 | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% |
| doc_003 | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% | ✓100% | ✗0% | ✗0% | ✗0% |
| doc_008 | ✗10% | ✗0% | ✗0% | ✗0% | ✗0% | ✗8% | ✗0% | ✗4% | ✗4% | ✗10% | ✗4% |

---

## Error Details per Document

### doc_001

Record count matches GT.

No errors. Perfect field match.

### doc_003

Record count matches GT.

**Field mismatches (4):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `balance` | 01/04/2023 - 12/31/2024 | extracted=None  expected=0.0 |
| 0 | `insurers` | 01/04/2023 - 12/31/2024 | extra=['allwin', 'cigna', 'paramount'] |
| 0 | `third_parties` | 01/04/2023 - 12/31/2024 | missing=['allwin', 'cigna healthspring', 'omnisys immunizations', 'paramount lonestar']  extra=['amanda sfs', 'health pbm', 'lonestar', 'omnisys'] |
| 0 | `description` | 01/04/2023 - 12/31/2024 | extracted='SRS PATIENT PROFILE'  expected='Pharmacy Record' |

### doc_008

**Count mismatch** — GT: 100, extracted: 75.

**Missing records (90):**
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
- GT[30] `05/26/2021 - 12/12/2024` — No extracted record found with this treatment_date
- GT[31] `02/20/2021 - 11/15/2024` — No extracted record found with this treatment_date
- GT[32] `01/06/2021 - 11/28/2024` — No extracted record found with this treatment_date
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
- GT[56] `02/23/2021 - 08/18/2024` — No extracted record found with this treatment_date
- GT[57] `05/03/2021 - 06/29/2024` — No extracted record found with this treatment_date
- GT[58] `03/23/2021 - 10/07/2024` — No extracted record found with this treatment_date
- GT[59] `01/22/2021 - 12/05/2024` — No extracted record found with this treatment_date
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

**Extra extracted records (67):**
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
- `11/29/2023` — Extracted record has no GT counterpart
- `12/02/2022` — Extracted record has no GT counterpart
- `08/15/2022` — Extracted record has no GT counterpart
- `11/15/2021` — Extracted record has no GT counterpart
- `01/08/2021` — Extracted record has no GT counterpart
- `11/28/2021` — Extracted record has no GT counterpart
- `08/07/2021` — Extracted record has no GT counterpart
- `07/14/2023` — Extracted record has no GT counterpart
- `05/04/2022` — Extracted record has no GT counterpart
- `06/28/2024` — Extracted record has no GT counterpart
- `05/16/2023` — Extracted record has no GT counterpart
- `07/10/2024` — Extracted record has no GT counterpart
- `01/13/2024` — Extracted record has no GT counterpart
- `04/03/2024` — Extracted record has no GT counterpart
- `03/11/2021` — Extracted record has no GT counterpart
- `01/17/2022` — Extracted record has no GT counterpart
- `09/13/2021` — Extracted record has no GT counterpart
- `11/22/2022` — Extracted record has no GT counterpart
- `03/10/2022` — Extracted record has no GT counterpart
- `07/22/2023` — Extracted record has no GT counterpart
- `06/19/2024` — Extracted record has no GT counterpart
- `09/24/2023` — Extracted record has no GT counterpart
- `09/23/2023` — Extracted record has no GT counterpart
- `12/22/2023` — Extracted record has no GT counterpart
- `08/30/2021` — Extracted record has no GT counterpart
- `04/03/2024` — Extracted record has no GT counterpart
- `12/03/2021` — Extracted record has no GT counterpart
- `08/10/2022` — Extracted record has no GT counterpart
- `01/19/2022` — Extracted record has no GT counterpart
- `05/28/2022` — Extracted record has no GT counterpart
- `05/07/2023` — Extracted record has no GT counterpart
- `09/29/2022` — Extracted record has no GT counterpart
- `03/15/2024` — Extracted record has no GT counterpart
- `08/28/2023` — Extracted record has no GT counterpart
- `05/26/2023` — Extracted record has no GT counterpart
- `06/28/2022` — Extracted record has no GT counterpart
- `09/14/2024` — Extracted record has no GT counterpart
- `02/26/2022` — Extracted record has no GT counterpart
- `07/13/2023` — Extracted record has no GT counterpart
- `10/29/2022` — Extracted record has no GT counterpart
- `03/16/2023` — Extracted record has no GT counterpart
- `05/24/2024` — Extracted record has no GT counterpart
- `11/21/2022` — Extracted record has no GT counterpart

**Field mismatches (70):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `cpt_codes` | 06/04/2021 - 11/30/2024 | missing=['71046', '72100', '73030', '73060', '73110', '73564', '76705', '77067'] |
| 0 | `total_charges` | 06/04/2021 - 11/30/2024 | extracted=663.56  expected=5342.73  diff=4679.17 |
| 0 | `ins_paid` | 06/04/2021 - 11/30/2024 | extracted=440.39  expected=3373.28  diff=2932.89 |
| 0 | `adjustment` | 06/04/2021 - 11/30/2024 | extracted=124.7  expected=1604.45  diff=1479.75 |
| 0 | `payments` | 06/04/2021 - 11/30/2024 | extracted=98.47  expected=None |
| 0 | `balance` | 06/04/2021 - 11/30/2024 | extracted=0.0  expected=365.0  diff=365.00 |
| 1 | `cpt_codes` | 01/25/2021 - 10/20/2024 | missing=['71048', '72158', '73100', '73110', '73562', '74177', '76700', '76705', '76830', 'A4570', 'A4614', 'Q9920'] |
| 1 | `total_charges` | 01/25/2021 - 10/20/2024 | extracted=871.76  expected=7766.86  diff=6895.10 |
| 1 | `ins_paid` | 01/25/2021 - 10/20/2024 | extracted=579.02  expected=4658.49  diff=4079.47 |
| 1 | `adjustment` | 01/25/2021 - 10/20/2024 | extracted=181.85  expected=2847.8  diff=2665.95 |
| 1 | `payments` | 01/25/2021 - 10/20/2024 | extracted=110.89  expected=None |
| 1 | `balance` | 01/25/2021 - 10/20/2024 | extracted=0.0  expected=260.57  diff=260.57 |
| 2 | `cpt_codes` | 01/08/2021 - 11/19/2024 | missing=['71046', '72100', '72158', '73030', '73060', '74177', '76705', '76830', 'J0205', 'J2720', 'J3480', 'J9060'] |
| 2 | `total_charges` | 01/08/2021 - 11/19/2024 | extracted=179.57  expected=7351.46  diff=7171.89 |
| 2 | `ins_paid` | 01/08/2021 - 11/19/2024 | extracted=116.53  expected=4342.54  diff=4226.01 |
| 2 | `adjustment` | 01/08/2021 - 11/19/2024 | extracted=63.04  expected=2799.07  diff=2736.03 |
| 2 | `balance` | 01/08/2021 - 11/19/2024 | extracted=0.0  expected=209.85  diff=209.85 |
| 29 | `cpt_codes` | 06/26/2021 - 10/17/2024 | missing=['72158', '73030', '73100', '73110', '73564', '76830', '77067', 'J2001'] |
| 29 | `total_charges` | 06/26/2021 - 10/17/2024 | extracted=568.12  expected=5429.05  diff=4860.93 |
| 29 | `ins_paid` | 06/26/2021 - 10/17/2024 | extracted=288.52  expected=3268.05  diff=2979.53 |
| 29 | `adjustment` | 06/26/2021 - 10/17/2024 | extracted=279.6  expected=2019.01  diff=1739.41 |
| 29 | `balance` | 06/26/2021 - 10/17/2024 | extracted=0.0  expected=141.99  diff=141.99 |
| 29 | `provider` | 06/26/2021 - 10/17/2024 | extracted=''  expected='Hudson Medical, PC' |
| 29 | `insurers` | 06/26/2021 - 10/17/2024 | missing=['tricare'] |
| 29 | `description` | 06/26/2021 - 10/17/2024 | extracted='X-ray spine, lumbosacral, 2-3 views'  expected=None |
| 33 | `cpt_codes` | 03/10/2021 - 12/25/2024 | missing=['71048', '72148', '73030', '73100', '73562', '74177', '74178', '76700', '76705', 'A4244', 'A4630']  extra=['72158'] |
| 33 | `total_charges` | 03/10/2021 - 12/25/2024 | extracted=126.55  expected=7034.09  diff=6907.54 |
| 33 | `ins_paid` | 03/10/2021 - 12/25/2024 | extracted=81.3  expected=4187.26  diff=4105.96 |
| 33 | `adjustment` | 03/10/2021 - 12/25/2024 | extracted=45.25  expected=2820.69  diff=2775.44 |
| 33 | `balance` | 03/10/2021 - 12/25/2024 | extracted=0.0  expected=26.14  diff=26.14 |
| 33 | `provider` | 03/10/2021 - 12/25/2024 | extracted=''  expected='Hudson Medical, PC' |
| 33 | `insurers` | 03/10/2021 - 12/25/2024 | missing=['tricare'] |
| 33 | `description` | 03/10/2021 - 12/25/2024 | extracted='MRI lumbar spine without and with contrast'  expected=None |
| 55 | `cpt_codes` | 10/04/2021 - 09/16/2024 | missing=['72158', '73030', '73100', '73110', '74177', '74178', '76830', '77067', 'J0171'] |
| 55 | `total_charges` | 10/04/2021 - 09/16/2024 | extracted=118.94  expected=4085.52  diff=3966.58 |
| 55 | `ins_paid` | 10/04/2021 - 09/16/2024 | extracted=63.25  expected=2432.48  diff=2369.23 |
| 55 | `adjustment` | 10/04/2021 - 09/16/2024 | extracted=55.69  expected=1560.39  diff=1504.70 |
| 55 | `balance` | 10/04/2021 - 09/16/2024 | extracted=0.0  expected=92.65  diff=92.65 |
| 55 | `provider` | 10/04/2021 - 09/16/2024 | extracted=''  expected='Hudson Medical, PC' |
| 55 | `insurers` | 10/04/2021 - 09/16/2024 | missing=['tricare'] |
| 55 | `description` | 10/04/2021 - 09/16/2024 | extracted='MRI lumbar spine without contrast'  expected=None |
| 60 | `cpt_codes` | 01/08/2021 - 07/20/2024 | missing=['71046', '71048', '72110', '72148', '72158', '73030', '73060', '73100', '73564', '74178', '76830', '77067', 'A4209', 'A4657'] |
| 60 | `total_charges` | 01/08/2021 - 07/20/2024 | extracted=179.57  expected=9589.68  diff=9410.11 |
| 60 | `ins_paid` | 01/08/2021 - 07/20/2024 | extracted=116.53  expected=5933.0  diff=5816.47 |
| 60 | `adjustment` | 01/08/2021 - 07/20/2024 | extracted=63.04  expected=3570.71  diff=3507.67 |
| 60 | `balance` | 01/08/2021 - 07/20/2024 | extracted=0.0  expected=85.97  diff=85.97 |
| 61 | `cpt_codes` | 03/10/2021 - 06/19/2024 | missing=['72110', '73100', '73110', '73562', '74177', '76700', '76830', 'J0290', 'Q0163'] |
| 61 | `total_charges` | 03/10/2021 - 06/19/2024 | extracted=126.55  expected=6414.64  diff=6288.09 |
| 61 | `ins_paid` | 03/10/2021 - 06/19/2024 | extracted=81.3  expected=4049.51  diff=3968.21 |
| 61 | `adjustment` | 03/10/2021 - 06/19/2024 | extracted=45.25  expected=2107.19  diff=2061.94 |
| 61 | `balance` | 03/10/2021 - 06/19/2024 | extracted=0.0  expected=257.94  diff=257.94 |
| 61 | `provider` | 03/10/2021 - 06/19/2024 | extracted=''  expected='Hudson Medical, PC' |
| 61 | `insurers` | 03/10/2021 - 06/19/2024 | missing=['tricare'] |
| 61 | `description` | 03/10/2021 - 06/19/2024 | extracted='MRI lumbar spine without and with contrast'  expected=None |
| 62 | `cpt_codes` | 06/08/2021 - 09/14/2024 | missing=['72100', '72110', '72148', '73030', '73060', '73562', '74178', '76705', '76830', 'A4627', 'J0270', 'J1040', 'J9000', 'Q9920'] |
| 62 | `total_charges` | 06/08/2021 - 09/14/2024 | extracted=590.13  expected=8552.72  diff=7962.59 |
| 62 | `ins_paid` | 06/08/2021 - 09/14/2024 | extracted=404.87  expected=5250.97  diff=4846.10 |
| 62 | `adjustment` | 06/08/2021 - 09/14/2024 | extracted=185.26  expected=3260.12  diff=3074.86 |
| 62 | `balance` | 06/08/2021 - 09/14/2024 | extracted=0.0  expected=41.63  diff=41.63 |
| 62 | `provider` | 06/08/2021 - 09/14/2024 | extracted=''  expected='Hudson Medical, PC' |
| 62 | `insurers` | 06/08/2021 - 09/14/2024 | missing=['tricare'] |
| 62 | `description` | 06/08/2021 - 09/14/2024 | extracted='CT abdomen & pelvis with contrast'  expected=None |
| 85 | `cpt_codes` | 04/06/2021 - 11/30/2024 | missing=['71046', '73060', '73564', '74177', '74178', '76700', '76705', 'A4209', 'A4550', 'J0153', 'Q0163']  extra=['73110'] |
| 85 | `total_charges` | 04/06/2021 - 11/30/2024 | extracted=273.59  expected=6419.81  diff=6146.22 |
| 85 | `ins_paid` | 04/06/2021 - 11/30/2024 | extracted=190.83  expected=3965.87  diff=3775.04 |
| 85 | `adjustment` | 04/06/2021 - 11/30/2024 | extracted=82.76  expected=2350.49  diff=2267.73 |
| 85 | `balance` | 04/06/2021 - 11/30/2024 | extracted=0.0  expected=103.45  diff=103.45 |
| 85 | `provider` | 04/06/2021 - 11/30/2024 | extracted=''  expected='Hudson Medical, PC' |
| 85 | `insurers` | 04/06/2021 - 11/30/2024 | missing=['tricare'] |
| 85 | `description` | 04/06/2021 - 11/30/2024 | extracted='X-ray wrist, minimum 3 views'  expected=None |

---

_Generated by `scripts/eval_extraction.py`_
