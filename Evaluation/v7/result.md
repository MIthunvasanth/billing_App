# Extraction Evaluation Results

Evaluated **12 documents** against ground truth.

---

## Summary

| Doc | GT | Extracted | Count | Weighted Acc | Cost USD | Duration |
|---|---|---|---|---|---|---|
| doc_001 | 50 | 50 | ✓ | 100.0% | $0.0963 | 45.59s |
| doc_002 | 40 | 40 | ✓ | 33.5% | $0.1045 | 37.12s |
| doc_003 | 1 | 1 | ✓ | 78.6% | $0.0802 | 19.28s |
| doc_004 | 1 | 1 | ✓ | 78.6% | $0.0678 | 7.69s |
| doc_005 | 80 | 72 | ✗ | 82.0% | $0.1979 | 65.49s |
| doc_006 | 33 | 33 | ✓ | 85.7% | $0.1037 | 118.71s |
| doc_007 | 400 | 405 | ✗ | 89.9% | $0.9000 | 88.55s |
| doc_008 | 100 | 83 | ✗ | 5.1% | $0.2965 | 35.11s |
| doc_009 | 1 | 1 | ✓ | 28.6% | $1.0073 | 66.43s |
| doc_010 | 1 | 1 | ✓ | 42.9% | $0.7867 | 53.49s |
| doc_011 | 150 | 201 | ✗ | 60.6% | $0.7837 | 133.9s |
| doc_012 | 120 | 47 | ✗ | 28.7% | $0.2301 | 26.24s |

**Total cost:** $4.6546  
**Total tokens:** 1,715,474 (input 1,511,537 / output 203,937)  
**Total wall-clock:** 697.6s

---

## Field Accuracy by Document

| Doc | date | cpt | total$ | ins$ | adj | pmts | bal | prov | insrs | 3p | desc |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doc_001 | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% |
| doc_002 | ✗45% | ✗35% | ✗42% | ✗42% | ✗42% | ✗0% | ✗0% | ✗45% | ✗45% | ✗45% | ✗45% |
| doc_003 | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% | ✗0% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% |
| doc_004 | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% | ✓100% | ✗0% | ✓100% | ✓100% | ✓100% | ✓100% |
| doc_005 | ~89% | ~89% | ~75% | ~75% | ~75% | ~89% | ~88% | ~74% | ~74% | ~89% | ~86% |
| doc_006 | ✓100% | ✗0% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% |
| doc_007 | ✓100% | ✓98% | ✓98% | ✓98% | ✓98% | ~87% | ~93% | ✗9% | ~89% | ✓100% | ✓100% |
| doc_008 | ✗8% | ✗4% | ✗6% | ✗6% | ✗6% | ✗2% | ✗0% | ✗6% | ✗6% | ✗8% | ✗6% |
| doc_009 | ✓100% | ✓100% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✓100% | ✗0% | ✗0% | ✗0% |
| doc_010 | ✓100% | ✓100% | ✗0% | ✗0% | ✗0% | ✗0% | ✓100% | ✓100% | ✗0% | ✗0% | ✓100% |
| doc_011 | ✓100% | ✓100% | ~82% | ~82% | ~82% | ✗3% | ✗0% | ✗17% | ✗17% | ✓100% | ~82% |
| doc_012 | ✗38% | ✗0% | ✗37% | ✗22% | ✗22% | ✗38% | ✗38% | ✗38% | ✗38% | ✗38% | ✗0% |

---

## Error Details per Document

### doc_001

Record count matches GT.

No errors. Perfect field match.

### doc_002

Record count matches GT.

**Missing records (22):**
- GT[0] `02/01/2023 - 12/07/2024` — No extracted record found with this treatment_date
- GT[5] `03/17/2023 - 09/30/2024` — No extracted record found with this treatment_date
- GT[7] `05/21/2023 - 11/23/2024` — No extracted record found with this treatment_date
- GT[8] `02/07/2023 - 10/23/2024` — No extracted record found with this treatment_date
- GT[11] `08/17/2023 - 10/18/2024` — No extracted record found with this treatment_date
- GT[12] `02/19/2023 - 11/07/2024` — No extracted record found with this treatment_date
- GT[13] `03/01/2023 - 10/20/2024` — No extracted record found with this treatment_date
- GT[15] `06/23/2023 - 12/25/2024` — No extracted record found with this treatment_date
- GT[17] `03/22/2023 - 08/22/2024` — No extracted record found with this treatment_date
- GT[19] `06/07/2023 - 12/26/2024` — No extracted record found with this treatment_date
- GT[20] `05/26/2023 - 05/09/2024` — No extracted record found with this treatment_date
- GT[22] `02/03/2023 - 12/28/2024` — No extracted record found with this treatment_date
- GT[24] `02/23/2023 - 07/30/2024` — No extracted record found with this treatment_date
- GT[28] `03/18/2023 - 12/03/2024` — No extracted record found with this treatment_date
- GT[29] `03/08/2023 - 12/31/2024` — No extracted record found with this treatment_date
- GT[31] `03/02/2023 - 12/26/2024` — No extracted record found with this treatment_date
- GT[32] `07/14/2023 - 12/04/2024` — No extracted record found with this treatment_date
- GT[33] `09/27/2023 - 12/14/2024` — No extracted record found with this treatment_date
- GT[36] `04/15/2023 - 10/29/2024` — No extracted record found with this treatment_date
- GT[37] `06/22/2023 - 11/28/2024` — No extracted record found with this treatment_date
- GT[38] `02/08/2023 - 12/04/2024` — No extracted record found with this treatment_date
- GT[39] `01/10/2023 - 11/24/2024` — No extracted record found with this treatment_date

**Extra extracted records (23):**
- `01/05/2024 - 12/07/2024` — Extracted record has no GT counterpart
- `03/17/2023 - 12/14/2023` — Extracted record has no GT counterpart
- `02/09/2024 - 11/23/2024` — Extracted record has no GT counterpart
- `02/07/2023 - 10/24/2024` — Extracted record has no GT counterpart
- `08/17/2023 - 04/28/2024` — Extracted record has no GT counterpart
- `03/10/2023 - 11/07/2024` — Extracted record has no GT counterpart
- `02/02/2024 - 10/20/2024` — Extracted record has no GT counterpart
- `07/03/2023 - 09/26/2024` — Extracted record has no GT counterpart
- `02/03/2023 - 08/22/2024` — Extracted record has no GT counterpart
- `02/15/2024 - 12/26/2024` — Extracted record has no GT counterpart
- `05/09/2024 - 12/18/2023` — Extracted record has no GT counterpart
- `05/01/2023 - 12/28/2024` — Extracted record has no GT counterpart
- `01/05/2024 - 08/20/2023` — Extracted record has no GT counterpart
- `03/05/2023 - 07/30/2023` — Extracted record has no GT counterpart
- `02/19/2023 - 12/03/2024` — Extracted record has no GT counterpart
- `01/17/2024 - 08/02/2024` — Extracted record has no GT counterpart
- `03/02/2023 - 12/31/2024` — Extracted record has no GT counterpart
- `07/13/2024 - 10/29/2024` — Extracted record has no GT counterpart
- `04/29/2024 - 08/26/2024` — Extracted record has no GT counterpart
- `04/15/2023 - 10/24/2024` — Extracted record has no GT counterpart
- `06/22/2023 - 12/10/2023` — Extracted record has no GT counterpart
- `02/08/2023 - 10/10/2024` — Extracted record has no GT counterpart
- `02/19/2023 - 11/08/2024` — Extracted record has no GT counterpart

**Field mismatches (43):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 1 | `payments` | 06/26/2023 - 12/11/2024 | extracted=154.09  expected=None |
| 1 | `balance` | 06/26/2023 - 12/11/2024 | extracted=0.0  expected=154.09  diff=154.09 |
| 2 | `payments` | 03/30/2023 - 07/18/2024 | extracted=35.14  expected=None |
| 2 | `balance` | 03/30/2023 - 07/18/2024 | extracted=0.0  expected=35.14  diff=35.14 |
| 3 | `payments` | 02/16/2023 - 10/01/2024 | extracted=65.76  expected=None |
| 3 | `balance` | 02/16/2023 - 10/01/2024 | extracted=0.0  expected=65.76  diff=65.76 |
| 4 | `payments` | 11/17/2023 - 12/02/2024 | extracted=43.37  expected=None |
| 4 | `balance` | 11/17/2023 - 12/02/2024 | extracted=0.0  expected=43.37  diff=43.37 |
| 6 | `cpt_codes` | 03/05/2023 - 12/18/2024 | missing=['72110', '74177'] |
| 6 | `payments` | 03/05/2023 - 12/18/2024 | extracted=109.17  expected=None |
| 6 | `balance` | 03/05/2023 - 12/18/2024 | extracted=0.0  expected=109.17  diff=109.17 |
| 9 | `cpt_codes` | 03/25/2023 - 12/21/2024 | missing=['76830'] |
| 9 | `payments` | 03/25/2023 - 12/21/2024 | extracted=88.51  expected=None |
| 9 | `balance` | 03/25/2023 - 12/21/2024 | extracted=0.0  expected=88.51  diff=88.51 |
| 10 | `payments` | 03/05/2023 - 08/20/2024 | extracted=16.46  expected=None |
| 10 | `balance` | 03/05/2023 - 08/20/2024 | extracted=0.0  expected=16.46  diff=16.46 |
| 14 | `payments` | 01/16/2023 - 11/20/2024 | extracted=131.29  expected=None |
| 14 | `balance` | 01/16/2023 - 11/20/2024 | extracted=0.0  expected=131.29  diff=131.29 |
| 16 | `payments` | 02/27/2023 - 12/09/2024 | extracted=120.67  expected=None |
| 16 | `balance` | 02/27/2023 - 12/09/2024 | extracted=0.0  expected=120.67  diff=120.67 |
| 18 | `payments` | 03/20/2023 - 09/03/2024 | extracted=72.69  expected=None |
| 18 | `balance` | 03/20/2023 - 09/03/2024 | extracted=0.0  expected=72.69  diff=72.69 |
| 21 | `payments` | 05/25/2023 - 11/20/2024 | extracted=168.39  expected=None |
| 21 | `balance` | 05/25/2023 - 11/20/2024 | extracted=0.0  expected=168.39  diff=168.39 |
| 23 | `payments` | 03/02/2023 - 12/29/2024 | extracted=211.07  expected=None |
| 23 | `balance` | 03/02/2023 - 12/29/2024 | extracted=0.0  expected=211.07  diff=211.07 |
| 25 | `payments` | 01/13/2023 - 10/20/2024 | extracted=372.14  expected=None |
| 25 | `balance` | 01/13/2023 - 10/20/2024 | extracted=0.0  expected=372.14  diff=372.14 |
| 26 | `payments` | 01/13/2023 - 10/04/2024 | extracted=108.64  expected=None |
| 26 | `balance` | 01/13/2023 - 10/04/2024 | extracted=0.0  expected=108.64  diff=108.64 |
| 27 | `cpt_codes` | 03/05/2023 - 12/18/2024 | missing=['73100', '73564', '74177', '76830']  extra=['71046', '73030', '73060', '73110', '73562', '76700'] |
| 27 | `total_charges` | 03/05/2023 - 12/18/2024 | extracted=5535.97  expected=3427.99  diff=2107.98 |
| 27 | `ins_paid` | 03/05/2023 - 12/18/2024 | extracted=3510.0  expected=2136.63  diff=1373.37 |
| 27 | `adjustment` | 03/05/2023 - 12/18/2024 | extracted=1916.8  expected=1142.99  diff=773.81 |
| 27 | `payments` | 03/05/2023 - 12/18/2024 | extracted=109.17  expected=None |
| 27 | `balance` | 03/05/2023 - 12/18/2024 | extracted=0.0  expected=148.37  diff=148.37 |
| 30 | `payments` | 01/31/2023 - 12/18/2024 | extracted=65.28  expected=None |
| 30 | `balance` | 01/31/2023 - 12/18/2024 | extracted=0.0  expected=65.28  diff=65.28 |
| 34 | `payments` | 03/10/2023 - 11/01/2024 | extracted=307.7  expected=None |
| 34 | `balance` | 03/10/2023 - 11/01/2024 | extracted=0.0  expected=307.7  diff=307.70 |
| 35 | `cpt_codes` | 03/01/2023 - 12/06/2024 | missing=['73060'] |
| 35 | `payments` | 03/01/2023 - 12/06/2024 | extracted=107.8  expected=None |
| 35 | `balance` | 03/01/2023 - 12/06/2024 | extracted=0.0  expected=107.8  diff=107.80 |

### doc_003

Record count matches GT.

**Field mismatches (2):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `adjustment` | 01/04/2023 - 12/31/2024 | extracted=31072.93  expected=None |
| 0 | `payments` | 01/04/2023 - 12/31/2024 | extracted=None  expected=31072.93 |

### doc_004

Record count matches GT.

**Field mismatches (2):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `adjustment` | 01/04/2023 - 12/31/2024 | extracted=None  expected=55776.23 |
| 0 | `balance` | 01/04/2023 - 12/31/2024 | extracted=None  expected=0.0 |

### doc_005

**Count mismatch** — GT: 80, extracted: 72.

**Missing records (9):**
- GT[61] `01/27/2023 - 01/30/2023` — No extracted record found with this treatment_date
- GT[72] `10/25/2024 - 10/27/2024` — No extracted record found with this treatment_date
- GT[73] `11/17/2022 - 11/21/2022` — No extracted record found with this treatment_date
- GT[74] `11/29/2021 - 11/30/2021` — No extracted record found with this treatment_date
- GT[75] `07/25/2023 - 07/29/2023` — No extracted record found with this treatment_date
- GT[76] `03/20/2022 - 03/27/2022` — No extracted record found with this treatment_date
- GT[77] `02/13/2022 - 02/16/2022` — No extracted record found with this treatment_date
- GT[78] `06/16/2022 - 06/19/2022` — No extracted record found with this treatment_date
- GT[79] `09/03/2021 - 09/07/2021` — No extracted record found with this treatment_date

**Extra extracted records (1):**
- `07/19/2022 - 07/23/2022` — Extracted record has no GT counterpart

**Field mismatches (60):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 58 | `total_charges` | 07/18/2022 - 07/23/2022 | extracted=50157.0  expected=79005.76  diff=28848.76 |
| 58 | `ins_paid` | 07/18/2022 - 07/23/2022 | extracted=None  expected=48694.68 |
| 58 | `adjustment` | 07/18/2022 - 07/23/2022 | extracted=None  expected=30311.08 |
| 58 | `balance` | 07/18/2022 - 07/23/2022 | extracted=None  expected=0.0 |
| 59 | `provider` | 06/16/2024 - 06/17/2024 | extracted='Unknown'  expected='Dyer Healthcare' |
| 59 | `insurers` | 06/16/2024 - 06/17/2024 | missing=['amerihealth'] |
| 59 | `description` | 06/16/2024 - 06/17/2024 | extracted='Acute myocardial infarction'  expected='Pulmonary embolism' |
| 60 | `provider` | 02/16/2023 - 02/20/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 60 | `insurers` | 02/16/2023 - 02/20/2023 | missing=['amerihealth'] |
| 60 | `description` | 02/16/2023 - 02/20/2023 | extracted='Cellulitis of lower leg'  expected='Acute myocardial infarction' |
| 62 | `total_charges` | 01/25/2023 - 01/28/2023 | extracted=180150.55  expected=109043.14  diff=71107.41 |
| 62 | `ins_paid` | 01/25/2023 - 01/28/2023 | extracted=111034.59  expected=67208.01  diff=43826.58 |
| 62 | `adjustment` | 01/25/2023 - 01/28/2023 | extracted=69115.96  expected=41835.13  diff=27280.83 |
| 62 | `provider` | 01/25/2023 - 01/28/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 62 | `insurers` | 01/25/2023 - 01/28/2023 | missing=['amerihealth'] |
| 63 | `total_charges` | 10/28/2022 - 11/03/2022 | extracted=109043.14  expected=121768.36  diff=12725.22 |
| 63 | `ins_paid` | 10/28/2022 - 11/03/2022 | extracted=67208.01  expected=75051.12  diff=7843.11 |
| 63 | `adjustment` | 10/28/2022 - 11/03/2022 | extracted=41835.13  expected=46717.24  diff=4882.11 |
| 63 | `provider` | 10/28/2022 - 11/03/2022 | extracted='Unknown'  expected='Dyer Healthcare' |
| 63 | `insurers` | 10/28/2022 - 11/03/2022 | missing=['amerihealth'] |
| 64 | `total_charges` | 11/20/2023 - 11/27/2023 | extracted=121768.36  expected=61825.46  diff=59942.90 |
| 64 | `ins_paid` | 11/20/2023 - 11/27/2023 | extracted=75051.12  expected=38105.71  diff=36945.41 |
| 64 | `adjustment` | 11/20/2023 - 11/27/2023 | extracted=46717.24  expected=23719.75  diff=22997.49 |
| 64 | `provider` | 11/20/2023 - 11/27/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 64 | `insurers` | 11/20/2023 - 11/27/2023 | missing=['amerihealth'] |
| 65 | `total_charges` | 12/26/2021 - 12/27/2021 | extracted=61825.46  expected=92110.01  diff=30284.55 |
| 65 | `ins_paid` | 12/26/2021 - 12/27/2021 | extracted=38105.71  expected=56771.39  diff=18665.68 |
| 65 | `adjustment` | 12/26/2021 - 12/27/2021 | extracted=23719.75  expected=35338.62  diff=11618.87 |
| 65 | `provider` | 12/26/2021 - 12/27/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 65 | `insurers` | 12/26/2021 - 12/27/2021 | missing=['amerihealth'] |
| 66 | `total_charges` | 06/16/2023 - 06/23/2023 | extracted=92110.01  expected=145282.34  diff=53172.33 |
| 66 | `ins_paid` | 06/16/2023 - 06/23/2023 | extracted=56771.39  expected=89543.81  diff=32772.42 |
| 66 | `adjustment` | 06/16/2023 - 06/23/2023 | extracted=35338.62  expected=55738.53  diff=20399.91 |
| 66 | `provider` | 06/16/2023 - 06/23/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 66 | `insurers` | 06/16/2023 - 06/23/2023 | missing=['amerihealth'] |
| 67 | `total_charges` | 08/02/2023 - 08/06/2023 | extracted=145282.34  expected=143293.47  diff=1988.87 |
| 67 | `ins_paid` | 08/02/2023 - 08/06/2023 | extracted=89543.81  expected=88317.98  diff=1225.83 |
| 67 | `adjustment` | 08/02/2023 - 08/06/2023 | extracted=55738.53  expected=54975.49  diff=763.04 |
| 67 | `provider` | 08/02/2023 - 08/06/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 67 | `insurers` | 08/02/2023 - 08/06/2023 | missing=['amerihealth'] |
| 68 | `total_charges` | 08/28/2024 - 09/04/2024 | extracted=143293.47  expected=99037.33  diff=44256.14 |
| 68 | `ins_paid` | 08/28/2024 - 09/04/2024 | extracted=88317.98  expected=61041.0  diff=27276.98 |
| 68 | `adjustment` | 08/28/2024 - 09/04/2024 | extracted=54975.49  expected=37996.33  diff=16979.16 |
| 68 | `provider` | 08/28/2024 - 09/04/2024 | extracted='Unknown'  expected='Dyer Healthcare' |
| 68 | `insurers` | 08/28/2024 - 09/04/2024 | missing=['amerihealth'] |
| 69 | `total_charges` | 07/26/2022 - 07/30/2022 | extracted=99037.33  expected=143781.79  diff=44744.46 |
| 69 | `ins_paid` | 07/26/2022 - 07/30/2022 | extracted=61041.0  expected=88618.95  diff=27577.95 |
| 69 | `adjustment` | 07/26/2022 - 07/30/2022 | extracted=37996.33  expected=55162.84  diff=17166.51 |
| 69 | `provider` | 07/26/2022 - 07/30/2022 | extracted='Unknown'  expected='Dyer Healthcare' |
| 69 | `insurers` | 07/26/2022 - 07/30/2022 | missing=['amerihealth'] |
| 70 | `total_charges` | 10/28/2024 - 11/01/2024 | extracted=143781.79  expected=113640.22  diff=30141.57 |
| 70 | `ins_paid` | 10/28/2024 - 11/01/2024 | extracted=88618.95  expected=70041.39  diff=18577.56 |
| 70 | `adjustment` | 10/28/2024 - 11/01/2024 | extracted=55162.84  expected=43598.83  diff=11564.01 |
| 70 | `provider` | 10/28/2024 - 11/01/2024 | extracted='Unknown'  expected='Dyer Healthcare' |
| 70 | `insurers` | 10/28/2024 - 11/01/2024 | missing=['amerihealth'] |
| 71 | `total_charges` | 02/21/2022 - 02/27/2022 | extracted=113640.22  expected=78544.41  diff=35095.81 |
| 71 | `ins_paid` | 02/21/2022 - 02/27/2022 | extracted=70041.39  expected=48410.33  diff=21631.06 |
| 71 | `adjustment` | 02/21/2022 - 02/27/2022 | extracted=43598.83  expected=30134.08  diff=13464.75 |
| 71 | `provider` | 02/21/2022 - 02/27/2022 | extracted='Unknown'  expected='Dyer Healthcare' |
| 71 | `insurers` | 02/21/2022 - 02/27/2022 | missing=['amerihealth'] |

### doc_006

Record count matches GT.

**Field mismatches (66):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `cpt_codes` | 01/01/2021 - 01/27/2021 | extra=['90937'] |
| 0 | `description` | 01/01/2021 - 01/27/2021 | extracted='10 Treatments'  expected='Dialysis — 10 treatments' |
| 1 | `cpt_codes` | 01/28/2021 - 02/22/2021 | extra=['90937'] |
| 1 | `description` | 01/28/2021 - 02/22/2021 | extracted='9 Treatments'  expected='Dialysis — 9 treatments' |
| 2 | `cpt_codes` | 02/23/2021 - 03/20/2021 | extra=['90937'] |
| 2 | `description` | 02/23/2021 - 03/20/2021 | extracted='10 Treatments'  expected='Dialysis — 10 treatments' |
| 3 | `cpt_codes` | 03/21/2021 - 04/19/2021 | extra=['90937'] |
| 3 | `description` | 03/21/2021 - 04/19/2021 | extracted='13 Treatments'  expected='Dialysis — 13 treatments' |
| 4 | `cpt_codes` | 04/20/2021 - 05/21/2021 | extra=['90937'] |
| 4 | `description` | 04/20/2021 - 05/21/2021 | extracted='11 Treatments'  expected='Dialysis — 11 treatments' |
| 5 | `cpt_codes` | 05/22/2021 - 06/20/2021 | extra=['G0491'] |
| 5 | `description` | 05/22/2021 - 06/20/2021 | extracted='12 Treatments'  expected='Dialysis — 12 treatments' |
| 6 | `cpt_codes` | 06/21/2021 - 07/21/2021 | extra=['90937'] |
| 6 | `description` | 06/21/2021 - 07/21/2021 | extracted='8 Treatments'  expected='Dialysis — 8 treatments' |
| 7 | `cpt_codes` | 07/22/2021 - 08/16/2021 | extra=['G0491'] |
| 7 | `description` | 07/22/2021 - 08/16/2021 | extracted='8 Treatments'  expected='Dialysis — 8 treatments' |
| 8 | `cpt_codes` | 08/17/2021 - 09/16/2021 | extra=['G0491'] |
| 8 | `description` | 08/17/2021 - 09/16/2021 | extracted='10 Treatments'  expected='Dialysis — 10 treatments' |
| 9 | `cpt_codes` | 09/17/2021 - 10/15/2021 | extra=['90935'] |
| 9 | `description` | 09/17/2021 - 10/15/2021 | extracted='13 Treatments'  expected='Dialysis — 13 treatments' |
| 10 | `cpt_codes` | 10/16/2021 - 11/16/2021 | extra=['G0491'] |
| 10 | `description` | 10/16/2021 - 11/16/2021 | extracted='12 Treatments'  expected='Dialysis — 12 treatments' |
| 11 | `cpt_codes` | 11/17/2021 - 12/15/2021 | extra=['G0491'] |
| 11 | `description` | 11/17/2021 - 12/15/2021 | extracted='12 Treatments'  expected='Dialysis — 12 treatments' |
| 12 | `cpt_codes` | 05/02/2022 - 05/28/2022 | extra=['90937'] |
| 12 | `description` | 05/02/2022 - 05/28/2022 | extracted='10 Treatments'  expected='Dialysis — 10 treatments' |
| 13 | `cpt_codes` | 05/29/2022 - 06/30/2022 | extra=['90940'] |
| 13 | `description` | 05/29/2022 - 06/30/2022 | extracted='8 Treatments'  expected='Dialysis — 8 treatments' |
| 14 | `cpt_codes` | 07/01/2022 - 08/02/2022 | extra=['90937'] |
| 14 | `description` | 07/01/2022 - 08/02/2022 | extracted='13 Treatments'  expected='Dialysis — 13 treatments' |
| 15 | `cpt_codes` | 08/03/2022 - 09/01/2022 | extra=['90937'] |
| 15 | `description` | 08/03/2022 - 09/01/2022 | extracted='8 Treatments'  expected='Dialysis — 8 treatments' |
| 16 | `cpt_codes` | 09/02/2022 - 09/29/2022 | extra=['90935'] |
| 16 | `description` | 09/02/2022 - 09/29/2022 | extracted='11 Treatments'  expected='Dialysis — 11 treatments' |
| 17 | `cpt_codes` | 09/30/2022 - 10/31/2022 | extra=['G0491'] |
| 17 | `description` | 09/30/2022 - 10/31/2022 | extracted='12 Treatments'  expected='Dialysis — 12 treatments' |
| 18 | `cpt_codes` | 11/01/2022 - 12/01/2022 | extra=['90937'] |
| 18 | `description` | 11/01/2022 - 12/01/2022 | extracted='12 Treatments'  expected='Dialysis — 12 treatments' |
| 19 | `cpt_codes` | 12/02/2022 - 01/03/2023 | extra=['G0491'] |
| 19 | `description` | 12/02/2022 - 01/03/2023 | extracted='10 Treatments'  expected='Dialysis — 10 treatments' |
| 20 | `cpt_codes` | 01/04/2023 - 02/01/2023 | extra=['90935'] |
| 20 | `description` | 01/04/2023 - 02/01/2023 | extracted='10 Treatments'  expected='Dialysis — 10 treatments' |
| 21 | `cpt_codes` | 02/02/2023 - 02/28/2023 | extra=['G0491'] |
| 21 | `description` | 02/02/2023 - 02/28/2023 | extracted='9 Treatments'  expected='Dialysis — 9 treatments' |
| 22 | `cpt_codes` | 03/01/2023 - 03/26/2023 | extra=['G0491'] |
| 22 | `description` | 03/01/2023 - 03/26/2023 | extracted='12 Treatments'  expected='Dialysis — 12 treatments' |
| 23 | `cpt_codes` | 08/31/2023 - 09/30/2023 | extra=['G0491'] |
| 23 | `description` | 08/31/2023 - 09/30/2023 | extracted='13 Treatments'  expected='Dialysis — 13 treatments' |
| 24 | `cpt_codes` | 10/01/2023 - 10/30/2023 | extra=['90935'] |
| 24 | `description` | 10/01/2023 - 10/30/2023 | extracted='11 Treatments'  expected='Dialysis — 11 treatments' |
| 25 | `cpt_codes` | 10/31/2023 - 11/28/2023 | extra=['G0491'] |
| 25 | `description` | 10/31/2023 - 11/28/2023 | extracted='10 Treatments'  expected='Dialysis — 10 treatments' |
| 26 | `cpt_codes` | 11/29/2023 - 12/25/2023 | extra=['G0491'] |
| 26 | `description` | 11/29/2023 - 12/25/2023 | extracted='12 Treatments'  expected='Dialysis — 12 treatments' |
| 27 | `cpt_codes` | 12/26/2023 - 01/26/2024 | extra=['G0491'] |
| 27 | `description` | 12/26/2023 - 01/26/2024 | extracted='13 Treatments'  expected='Dialysis — 13 treatments' |
| 28 | `cpt_codes` | 01/27/2024 - 02/28/2024 | extra=['90935'] |
| 28 | `description` | 01/27/2024 - 02/28/2024 | extracted='8 Treatments'  expected='Dialysis — 8 treatments' |
| 29 | `cpt_codes` | 02/29/2024 - 04/01/2024 | extra=['G0491'] |
| 29 | `description` | 02/29/2024 - 04/01/2024 | extracted='9 Treatments'  expected='Dialysis — 9 treatments' |
| 30 | `cpt_codes` | 04/02/2024 - 05/03/2024 | extra=['90937'] |
| 30 | `description` | 04/02/2024 - 05/03/2024 | extracted='10 Treatments'  expected='Dialysis — 10 treatments' |
| 31 | `cpt_codes` | 05/04/2024 - 06/03/2024 | extra=['90935'] |
| 31 | `description` | 05/04/2024 - 06/03/2024 | extracted='8 Treatments'  expected='Dialysis — 8 treatments' |
| 32 | `cpt_codes` | 06/04/2024 - 07/05/2024 | extra=['G0491'] |
| 32 | `description` | 06/04/2024 - 07/05/2024 | extracted='9 Treatments'  expected='Dialysis — 9 treatments' |

### doc_007

**Count mismatch** — GT: 400, extracted: 405.

**Extra extracted records (5):**
- `01/18/2023` — Extracted record has no GT counterpart
- `10/08/2023` — Extracted record has no GT counterpart
- `01/15/2024` — Extracted record has no GT counterpart
- `12/28/2022` — Extracted record has no GT counterpart
- `01/08/2021` — Extracted record has no GT counterpart

**Field mismatches (515):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 6 | `insurers` | 05/04/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 9 | `insurers` | 10/13/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 11 | `insurers` | 10/20/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 13 | `insurers` | 05/12/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 19 | `insurers` | 12/27/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 36 | `cpt_codes` | 08/16/2022 | missing=['45378'] |
| 36 | `total_charges` | 08/16/2022 | extracted=788.29  expected=1077.79  diff=289.50 |
| 36 | `ins_paid` | 08/16/2022 | extracted=306.22  expected=569.27  diff=263.05 |
| 36 | `adjustment` | 08/16/2022 | extracted=323.87  expected=500.6  diff=176.73 |
| 36 | `payments` | 08/16/2022 | extracted=7.92  expected=None |
| 36 | `balance` | 08/16/2022 | extracted=150.28  expected=7.92  diff=142.36 |
| 36 | `provider` | 08/16/2022 | extracted='HORN STACY'  expected='Smith Medical, PC' |
| 37 | `provider` | 06/22/2021 | extracted='GONZALEZ ELIZABETH'  expected='Smith Medical, PC' |
| 38 | `provider` | 12/18/2024 | extracted='LITTLE DANIELLE'  expected='Smith Medical, PC' |
| 39 | `provider` | 09/11/2023 | extracted='DAVIS DANIEL'  expected='Smith Medical, PC' |
| 40 | `provider` | 08/22/2021 | extracted='HENDRIX RAYMOND'  expected='Smith Medical, PC' |
| 41 | `provider` | 10/23/2024 | extracted='HANSEN ZACHARY'  expected='Smith Medical, PC' |
| 42 | `provider` | 06/27/2024 | extracted='HUMPHREY EMMA'  expected='Smith Medical, PC' |
| 43 | `provider` | 06/30/2022 | extracted='SPENCER KEVIN'  expected='Smith Medical, PC' |
| 44 | `provider` | 09/18/2021 | extracted='HENRY PATRICIA'  expected='Smith Medical, PC' |
| 45 | `provider` | 10/29/2021 | extracted='HERNANDEZ EMILY'  expected='Smith Medical, PC' |
| 46 | `provider` | 03/02/2022 | extracted='VELAZQUEZ YOLANDA'  expected='Smith Medical, PC' |
| 46 | `insurers` | 03/02/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 47 | `provider` | 09/29/2024 | extracted='BROWN ADAM'  expected='Smith Medical, PC' |
| 48 | `provider` | 12/14/2021 | extracted='MOORE JENNIFER'  expected='Smith Medical, PC' |
| 49 | `provider` | 07/25/2021 | extracted='VELAZQUEZ MATTHEW'  expected='Smith Medical, PC' |
| 50 | `provider` | 05/18/2024 | extracted='LEWIS BRIAN'  expected='Smith Medical, PC' |
| 50 | `insurers` | 05/18/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 51 | `provider` | 10/28/2024 | extracted='MITCHELL ROGER'  expected='Smith Medical, PC' |
| 52 | `provider` | 09/08/2024 | extracted='MARTIN ALEJANDRA'  expected='Smith Medical, PC' |
| 53 | `provider` | 04/13/2023 | extracted='PEREZ JAMES'  expected='Smith Medical, PC' |
| 54 | `provider` | 01/06/2023 | extracted='CORDOVA ROBERT'  expected='Smith Medical, PC' |
| 55 | `provider` | 06/19/2021 | extracted='GREENE TRACEY'  expected='Smith Medical, PC' |
| 56 | `provider` | 04/18/2023 | extracted='PETERS BARRY'  expected='Smith Medical, PC' |
| 57 | `provider` | 02/10/2024 | extracted='REED LYNN'  expected='Smith Medical, PC' |
| 58 | `provider` | 01/16/2021 | extracted='KIDD BRADLEY'  expected='Smith Medical, PC' |
| 59 | `provider` | 07/15/2021 | extracted='CONNER JOHN'  expected='Smith Medical, PC' |
| 60 | `provider` | 02/06/2024 | extracted='PETTY MICHAEL'  expected='Smith Medical, PC' |
| 61 | `provider` | 11/11/2022 | extracted='FREDERICK MICHELLE'  expected='Smith Medical, PC' |
| 62 | `provider` | 01/05/2022 | extracted='JOHNSON MARK'  expected='Smith Medical, PC' |
| 63 | `provider` | 11/29/2021 | extracted='SPENCER JAMES'  expected='Smith Medical, PC' |
| 64 | `provider` | 12/12/2023 | extracted='DAVIS DIANE'  expected='Smith Medical, PC' |
| 64 | `insurers` | 12/12/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 65 | `provider` | 11/02/2024 | extracted='CHARLES JOSHUA'  expected='Smith Medical, PC' |
| 65 | `insurers` | 11/02/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 66 | `provider` | 05/06/2022 | extracted='MOORE COURTNEY'  expected='Smith Medical, PC' |
| 66 | `insurers` | 05/06/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 67 | `provider` | 06/19/2021 | extracted='LUCERO BRIANNA'  expected='Smith Medical, PC' |
| 68 | `provider` | 12/29/2021 | extracted='NELSON SHARON'  expected='Smith Medical, PC' |
| 69 | `provider` | 11/18/2022 | extracted='SMITH JENNA'  expected='Smith Medical, PC' |
| 70 | `provider` | 07/18/2023 | extracted='KNAPP DEBRA'  expected='Smith Medical, PC' |
| 71 | `provider` | 03/07/2022 | extracted='SCHNEIDER FREDERICK'  expected='Smith Medical, PC' |
| 72 | `provider` | 10/09/2024 | extracted='RILEY KRISTIN'  expected='Smith Medical, PC' |
| 72 | `insurers` | 10/09/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 73 | `provider` | 05/06/2023 | extracted='DIAZ RANDALL'  expected='Smith Medical, PC' |
| 74 | `provider` | 10/08/2021 | extracted='WHEELER FRANK'  expected='Smith Medical, PC' |
| 75 | `cpt_codes` | 10/06/2024 | missing=['99239'] |
| 75 | `provider` | 10/06/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 76 | `provider` | 10/15/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 77 | `provider` | 03/17/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 78 | `provider` | 07/17/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 79 | `provider` | 07/06/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 80 | `provider` | 06/24/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 81 | `provider` | 04/19/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 82 | `provider` | 11/18/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 83 | `provider` | 08/07/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 84 | `provider` | 10/27/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 85 | `provider` | 09/04/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 85 | `insurers` | 09/04/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 86 | `provider` | 04/01/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 87 | `provider` | 03/31/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 88 | `provider` | 10/22/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 89 | `provider` | 10/03/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 90 | `provider` | 05/10/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 91 | `provider` | 07/21/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 92 | `provider` | 01/08/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 93 | `provider` | 04/11/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 94 | `provider` | 08/03/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 95 | `provider` | 10/25/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 95 | `insurers` | 10/25/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 96 | `provider` | 02/04/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 97 | `provider` | 10/17/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 98 | `provider` | 04/11/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 99 | `provider` | 08/20/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 100 | `provider` | 05/15/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 101 | `provider` | 11/12/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 102 | `provider` | 01/02/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 103 | `provider` | 07/07/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 104 | `provider` | 04/04/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 105 | `provider` | 10/13/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 105 | `insurers` | 10/13/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 106 | `provider` | 01/19/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 107 | `provider` | 11/19/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 108 | `provider` | 09/29/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 109 | `provider` | 03/20/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 110 | `provider` | 06/12/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 111 | `provider` | 08/17/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 112 | `provider` | 01/13/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 113 | `provider` | 11/03/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 114 | `provider` | 02/08/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 115 | `cpt_codes` | 01/18/2023 | missing=['99201'] |
| 115 | `provider` | 01/18/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 116 | `provider` | 05/22/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 117 | `provider` | 09/28/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 118 | `provider` | 09/09/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 119 | `provider` | 12/18/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 120 | `provider` | 07/04/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 120 | `insurers` | 07/04/2023 | missing=['insurance payment'] |
| 121 | `provider` | 10/02/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 122 | `provider` | 05/14/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 123 | `provider` | 12/14/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 124 | `provider` | 04/15/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 125 | `provider` | 02/11/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 126 | `provider` | 01/08/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 127 | `provider` | 08/16/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 128 | `provider` | 11/19/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 129 | `provider` | 07/31/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 130 | `provider` | 07/22/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 131 | `provider` | 05/31/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 131 | `insurers` | 05/31/2024 | missing=['molina healthcare of ny'] |
| 132 | `provider` | 02/20/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 133 | `provider` | 11/01/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 134 | `provider` | 01/09/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 135 | `provider` | 09/18/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 136 | `provider` | 04/18/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 137 | `provider` | 02/14/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 138 | `provider` | 11/02/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 139 | `provider` | 08/04/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 140 | `provider` | 06/04/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 141 | `provider` | 02/03/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 142 | `provider` | 04/12/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 143 | `provider` | 07/29/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 144 | `provider` | 12/13/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 145 | `provider` | 10/08/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 146 | `provider` | 05/07/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 147 | `provider` | 08/02/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 147 | `insurers` | 08/02/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 148 | `provider` | 07/28/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 149 | `provider` | 10/17/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 150 | `provider` | 08/05/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 151 | `provider` | 01/08/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 152 | `cpt_codes` | 10/08/2023 | missing=['99281', 'J9000'] |
| 152 | `provider` | 10/08/2023 | extracted='REAVES CAROL'  expected='Smith Medical, PC' |
| 153 | `provider` | 06/11/2022 | extracted='CARROLL PAUL'  expected='Smith Medical, PC' |
| 154 | `provider` | 05/22/2023 | extracted='GONZALEZ NANCY'  expected='Smith Medical, PC' |
| 155 | `provider` | 06/10/2022 | extracted='LUTZ ANNA'  expected='Smith Medical, PC' |
| 156 | `provider` | 07/10/2021 | extracted='KELLY JACOB'  expected='Smith Medical, PC' |
| 157 | `provider` | 12/04/2021 | extracted='PEARSON FRANCES'  expected='Smith Medical, PC' |
| 158 | `provider` | 12/07/2022 | extracted='SULLIVAN MITCHELL'  expected='Smith Medical, PC' |
| 159 | `provider` | 08/06/2024 | extracted='SUAREZ JAMES'  expected='Smith Medical, PC' |
| 160 | `provider` | 07/30/2022 | extracted='ROSE BRIANNA'  expected='Smith Medical, PC' |
| 161 | `provider` | 03/16/2023 | extracted='RODRIGUEZ PAUL'  expected='Smith Medical, PC' |
| 162 | `provider` | 03/29/2021 | extracted='JOHNSON MARY'  expected='Smith Medical, PC' |
| 163 | `provider` | 09/12/2023 | extracted='CARTER WILLIAM'  expected='Smith Medical, PC' |
| 164 | `provider` | 06/23/2024 | extracted='TURNER ANNA'  expected='Smith Medical, PC' |
| 165 | `provider` | 01/06/2021 | extracted='GARCIA ANTHONY'  expected='Smith Medical, PC' |
| 166 | `provider` | 11/22/2024 | extracted='VALDEZ STEPHANIE'  expected='Smith Medical, PC' |
| 167 | `provider` | 12/06/2022 | extracted='COLLINS SHANE'  expected='Smith Medical, PC' |
| 167 | `insurers` | 12/06/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 168 | `provider` | 08/19/2022 | extracted='DAVIS AUSTIN'  expected='Smith Medical, PC' |
| 169 | `provider` | 06/17/2023 | extracted='BENSON ELIZABETH'  expected='Smith Medical, PC' |
| 170 | `provider` | 04/13/2024 | extracted='JOHNSON ANGELA'  expected='Smith Medical, PC' |
| 171 | `provider` | 10/05/2022 | extracted='SHAW GARY'  expected='Smith Medical, PC' |
| 172 | `provider` | 01/07/2022 | extracted='SANCHEZ MICHAEL'  expected='Smith Medical, PC' |
| 173 | `provider` | 09/19/2022 | extracted='VANG RHONDA'  expected='Smith Medical, PC' |
| 173 | `insurers` | 09/19/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 174 | `provider` | 01/05/2024 | extracted='LOPEZ NATHANIEL'  expected='Smith Medical, PC' |
| 174 | `insurers` | 01/05/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 175 | `provider` | 03/09/2023 | extracted='JOHNSON JULIE'  expected='Smith Medical, PC' |
| 176 | `provider` | 11/12/2024 | extracted='HERRERA MARGARET'  expected='Smith Medical, PC' |
| 177 | `provider` | 10/28/2024 | extracted='ROMERO DEVIN'  expected='Smith Medical, PC' |
| 178 | `provider` | 10/15/2021 | extracted='TURNER WILLIAM'  expected='Smith Medical, PC' |
| 179 | `provider` | 08/01/2024 | extracted='WARD STACEY'  expected='Smith Medical, PC' |
| 180 | `provider` | 10/07/2023 | extracted='MOORE JASON'  expected='Smith Medical, PC' |
| 181 | `provider` | 04/24/2024 | extracted='DUNLAP JACOB'  expected='Smith Medical, PC' |
| 182 | `provider` | 11/14/2022 | extracted='MILLER PATTY'  expected='Smith Medical, PC' |
| 183 | `provider` | 08/09/2021 | extracted='DELACRUZ JOSEPH'  expected='Smith Medical, PC' |
| 184 | `provider` | 07/04/2022 | extracted='COLEMAN MICHELE'  expected='Smith Medical, PC' |
| 185 | `provider` | 06/19/2023 | extracted='THOMPSON JILL'  expected='Smith Medical, PC' |
| 186 | `provider` | 04/17/2021 | extracted='ALLEN STEPHANIE'  expected='Smith Medical, PC' |
| 187 | `provider` | 10/24/2022 | extracted='FIELDS EMILY'  expected='Smith Medical, PC' |
| 188 | `provider` | 05/23/2022 | extracted='MOORE KEVIN'  expected='Smith Medical, PC' |
| 189 | `provider` | 02/22/2024 | extracted='EDWARDS JOHN'  expected='Smith Medical, PC' |
| 190 | `total_charges` | 02/03/2022 | extracted=None  expected=1447.81 |
| 190 | `ins_paid` | 02/03/2022 | extracted=None  expected=739.31 |
| 190 | `adjustment` | 02/03/2022 | extracted=None  expected=708.5 |
| 190 | `balance` | 02/03/2022 | extracted=None  expected=0.0 |
| 190 | `provider` | 02/03/2022 | extracted='WARE SAMANTHA'  expected='Smith Medical, PC' |
| 190 | `insurers` | 02/03/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 191 | `total_charges` | 03/27/2023 | extracted=1447.81  expected=1154.55  diff=293.26 |
| 191 | `ins_paid` | 03/27/2023 | extracted=739.31  expected=683.98  diff=55.33 |
| 191 | `adjustment` | 03/27/2023 | extracted=708.5  expected=470.57  diff=237.93 |
| 191 | `provider` | 03/27/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 192 | `total_charges` | 04/16/2022 | extracted=1154.55  expected=529.54  diff=625.01 |
| 192 | `ins_paid` | 04/16/2022 | extracted=683.98  expected=319.51  diff=364.47 |
| 192 | `adjustment` | 04/16/2022 | extracted=470.57  expected=210.03  diff=260.54 |
| 192 | `provider` | 04/16/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 193 | `provider` | 06/16/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 194 | `provider` | 09/17/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 194 | `insurers` | 09/17/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 195 | `provider` | 06/20/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 196 | `provider` | 12/18/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 197 | `provider` | 07/07/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 198 | `provider` | 05/01/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 199 | `provider` | 01/24/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 200 | `provider` | 09/04/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 201 | `provider` | 10/14/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 202 | `provider` | 12/24/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 203 | `provider` | 02/06/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 204 | `provider` | 04/22/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 205 | `provider` | 06/05/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 206 | `provider` | 07/02/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 207 | `provider` | 07/01/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 208 | `provider` | 11/13/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 209 | `provider` | 03/01/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 210 | `provider` | 12/17/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 211 | `provider` | 07/31/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 212 | `provider` | 03/09/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 212 | `insurers` | 03/09/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 213 | `provider` | 06/20/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 214 | `provider` | 08/11/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 215 | `provider` | 01/04/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 216 | `provider` | 11/15/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 217 | `provider` | 05/25/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 218 | `provider` | 07/21/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 219 | `provider` | 07/05/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 220 | `provider` | 12/14/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 221 | `provider` | 08/19/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 222 | `provider` | 06/01/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 223 | `provider` | 09/13/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 224 | `provider` | 11/04/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 225 | `provider` | 08/06/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 226 | `provider` | 05/02/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 227 | `provider` | 01/03/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 228 | `provider` | 01/14/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 229 | `provider` | 07/05/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 230 | `provider` | 10/20/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 231 | `provider` | 08/04/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 232 | `provider` | 03/21/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 232 | `insurers` | 03/21/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 233 | `provider` | 10/29/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 234 | `provider` | 03/29/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 235 | `provider` | 01/06/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 236 | `provider` | 11/11/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 237 | `provider` | 08/03/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 238 | `provider` | 05/25/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 239 | `provider` | 09/05/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 240 | `provider` | 11/24/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 241 | `provider` | 10/17/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 241 | `insurers` | 10/17/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 242 | `provider` | 09/26/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 243 | `provider` | 06/25/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 244 | `provider` | 05/05/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 244 | `insurers` | 05/05/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 245 | `provider` | 01/13/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 246 | `provider` | 07/22/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 247 | `provider` | 08/05/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 248 | `provider` | 08/28/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 249 | `provider` | 10/08/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 250 | `provider` | 05/31/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 251 | `provider` | 08/30/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 252 | `provider` | 12/31/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 253 | `provider` | 02/23/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 254 | `provider` | 04/23/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 255 | `provider` | 10/09/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 256 | `provider` | 10/14/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 257 | `provider` | 03/26/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 258 | `provider` | 02/10/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 259 | `provider` | 10/17/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 260 | `provider` | 12/26/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 261 | `provider` | 06/22/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 262 | `provider` | 12/22/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 263 | `provider` | 10/28/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 264 | `provider` | 04/21/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 265 | `provider` | 11/17/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 266 | `provider` | 07/23/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 267 | `cpt_codes` | 01/15/2024 | missing=['72148', '74177', '97750'] |
| 267 | `provider` | 01/15/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 268 | `provider` | 11/10/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 269 | `provider` | 08/12/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 270 | `provider` | 08/06/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 271 | `provider` | 11/18/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 272 | `provider` | 12/26/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 273 | `provider` | 01/22/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 274 | `provider` | 01/31/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 275 | `provider` | 06/06/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 276 | `provider` | 07/29/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 277 | `provider` | 11/28/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 278 | `provider` | 01/28/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 279 | `provider` | 03/09/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 280 | `provider` | 07/18/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 281 | `provider` | 06/29/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 281 | `insurers` | 06/29/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 282 | `provider` | 01/11/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 283 | `provider` | 02/22/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 283 | `insurers` | 02/22/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 284 | `provider` | 11/05/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 285 | `provider` | 02/17/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 286 | `provider` | 11/15/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 287 | `provider` | 04/29/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 288 | `provider` | 06/07/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 289 | `provider` | 03/04/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 290 | `provider` | 11/23/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 291 | `provider` | 07/21/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 292 | `provider` | 05/29/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 293 | `provider` | 06/13/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 294 | `provider` | 05/15/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 295 | `provider` | 04/04/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 295 | `insurers` | 04/04/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 296 | `provider` | 07/10/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 297 | `provider` | 08/20/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 298 | `provider` | 05/26/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 299 | `provider` | 02/18/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 300 | `provider` | 10/31/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 301 | `provider` | 03/05/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 302 | `provider` | 12/17/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 303 | `provider` | 09/16/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 304 | `provider` | 03/25/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 305 | `provider` | 10/28/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 306 | `cpt_codes` | 12/28/2022 | missing=['90960'] |
| 306 | `total_charges` | 12/28/2022 | extracted=None  expected=1701.71 |
| 306 | `ins_paid` | 12/28/2022 | extracted=None  expected=947.26 |
| 306 | `adjustment` | 12/28/2022 | extracted=None  expected=754.45 |
| 306 | `balance` | 12/28/2022 | extracted=None  expected=0.0 |
| 306 | `provider` | 12/28/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 307 | `provider` | 03/08/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 308 | `payments` | 08/08/2023 | extracted=13.12  expected=None |
| 308 | `balance` | 08/08/2023 | extracted=0.0  expected=13.12  diff=13.12 |
| 308 | `provider` | 08/08/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 308 | `insurers` | 08/08/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 309 | `payments` | 10/18/2024 | extracted=34.57  expected=None |
| 309 | `balance` | 10/18/2024 | extracted=0.0  expected=34.57  diff=34.57 |
| 309 | `provider` | 10/18/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 310 | `provider` | 09/02/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 311 | `provider` | 03/19/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 312 | `payments` | 08/16/2023 | extracted=12.42  expected=None |
| 312 | `balance` | 08/16/2023 | extracted=0.0  expected=12.42  diff=12.42 |
| 312 | `provider` | 08/16/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 313 | `provider` | 03/10/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 314 | `payments` | 01/14/2023 | extracted=78.61  expected=None |
| 314 | `balance` | 01/14/2023 | extracted=0.0  expected=78.61  diff=78.61 |
| 314 | `provider` | 01/14/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 315 | `payments` | 03/08/2023 | extracted=24.6  expected=None |
| 315 | `balance` | 03/08/2023 | extracted=0.0  expected=24.6  diff=24.60 |
| 315 | `provider` | 03/08/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 316 | `payments` | 04/03/2021 | extracted=30.99  expected=None |
| 316 | `balance` | 04/03/2021 | extracted=0.0  expected=30.99  diff=30.99 |
| 316 | `provider` | 04/03/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 317 | `payments` | 06/27/2024 | extracted=3.57  expected=None |
| 317 | `balance` | 06/27/2024 | extracted=0.0  expected=3.57  diff=3.57 |
| 317 | `provider` | 06/27/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 318 | `provider` | 07/31/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 319 | `payments` | 12/09/2021 | extracted=6.15  expected=None |
| 319 | `balance` | 12/09/2021 | extracted=0.0  expected=6.15  diff=6.15 |
| 319 | `provider` | 12/09/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 320 | `payments` | 03/09/2024 | extracted=65.78  expected=None |
| 320 | `balance` | 03/09/2024 | extracted=0.0  expected=65.78  diff=65.78 |
| 320 | `provider` | 03/09/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 321 | `payments` | 05/14/2024 | extracted=28.12  expected=None |
| 321 | `balance` | 05/14/2024 | extracted=0.0  expected=28.12  diff=28.12 |
| 321 | `provider` | 05/14/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 321 | `insurers` | 05/14/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 322 | `provider` | 08/23/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 323 | `provider` | 05/02/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 324 | `payments` | 02/05/2022 | extracted=6.99  expected=None |
| 324 | `balance` | 02/05/2022 | extracted=0.0  expected=6.99  diff=6.99 |
| 324 | `provider` | 02/05/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 325 | `provider` | 03/14/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 326 | `payments` | 06/03/2022 | extracted=2.91  expected=None |
| 326 | `balance` | 06/03/2022 | extracted=0.0  expected=2.91  diff=2.91 |
| 326 | `provider` | 06/03/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 327 | `payments` | 04/24/2024 | extracted=5.4  expected=None |
| 327 | `balance` | 04/24/2024 | extracted=0.0  expected=5.4  diff=5.40 |
| 327 | `provider` | 04/24/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 328 | `payments` | 09/09/2024 | extracted=5.6  expected=None |
| 328 | `balance` | 09/09/2024 | extracted=0.0  expected=5.6  diff=5.60 |
| 328 | `provider` | 09/09/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 328 | `insurers` | 09/09/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 329 | `provider` | 09/23/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 330 | `provider` | 09/28/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 331 | `provider` | 11/21/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 331 | `insurers` | 11/21/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 332 | `payments` | 06/13/2022 | extracted=2.4  expected=None |
| 332 | `balance` | 06/13/2022 | extracted=0.0  expected=2.4  diff=2.40 |
| 332 | `provider` | 06/13/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 333 | `payments` | 10/05/2023 | extracted=10.44  expected=None |
| 333 | `balance` | 10/05/2023 | extracted=0.0  expected=10.44  diff=10.44 |
| 333 | `provider` | 10/05/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 333 | `insurers` | 10/05/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 334 | `payments` | 05/05/2023 | extracted=15.71  expected=None |
| 334 | `balance` | 05/05/2023 | extracted=0.0  expected=15.71  diff=15.71 |
| 334 | `provider` | 05/05/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 335 | `payments` | 01/18/2022 | extracted=12.65  expected=None |
| 335 | `balance` | 01/18/2022 | extracted=0.0  expected=12.65  diff=12.65 |
| 335 | `provider` | 01/18/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 336 | `provider` | 09/12/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 337 | `provider` | 02/24/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 337 | `insurers` | 02/24/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 338 | `payments` | 02/04/2024 | extracted=43.09  expected=None |
| 338 | `balance` | 02/04/2024 | extracted=0.0  expected=43.09  diff=43.09 |
| 338 | `provider` | 02/04/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 339 | `payments` | 06/25/2022 | extracted=8.76  expected=None |
| 339 | `balance` | 06/25/2022 | extracted=0.0  expected=8.76  diff=8.76 |
| 339 | `provider` | 06/25/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 340 | `payments` | 10/13/2021 | extracted=32.69  expected=None |
| 340 | `balance` | 10/13/2021 | extracted=0.0  expected=32.69  diff=32.69 |
| 340 | `provider` | 10/13/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 341 | `payments` | 03/08/2021 | extracted=7.58  expected=None |
| 341 | `balance` | 03/08/2021 | extracted=0.0  expected=7.58  diff=7.58 |
| 341 | `provider` | 03/08/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 341 | `insurers` | 03/08/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 342 | `payments` | 02/10/2023 | extracted=14.46  expected=None |
| 342 | `balance` | 02/10/2023 | extracted=0.0  expected=14.46  diff=14.46 |
| 342 | `provider` | 02/10/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 342 | `insurers` | 02/10/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 343 | `payments` | 11/21/2022 | extracted=3.65  expected=None |
| 343 | `balance` | 11/21/2022 | extracted=0.0  expected=3.65  diff=3.65 |
| 343 | `provider` | 11/21/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 344 | `provider` | 10/23/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 344 | `insurers` | 10/23/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 345 | `payments` | 06/20/2022 | extracted=50.98  expected=None |
| 345 | `balance` | 06/20/2022 | extracted=0.0  expected=50.98  diff=50.98 |
| 345 | `provider` | 06/20/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 346 | `provider` | 02/21/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 346 | `insurers` | 02/21/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 347 | `total_charges` | 03/04/2024 | extracted=None  expected=2461.26 |
| 347 | `ins_paid` | 03/04/2024 | extracted=None  expected=1277.34 |
| 347 | `adjustment` | 03/04/2024 | extracted=None  expected=1135.4 |
| 347 | `balance` | 03/04/2024 | extracted=None  expected=48.52 |
| 347 | `provider` | 03/04/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 347 | `insurers` | 03/04/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 348 | `payments` | 03/13/2021 | extracted=54.98  expected=None |
| 348 | `provider` | 03/13/2021 | extracted='VALENTINE TARA'  expected='Smith Medical, PC' |
| 349 | `payments` | 12/11/2021 | extracted=35.61  expected=None |
| 349 | `provider` | 12/11/2021 | extracted='THOMAS JACOB'  expected='Smith Medical, PC' |
| 350 | `payments` | 12/16/2022 | extracted=22.94  expected=None |
| 350 | `provider` | 12/16/2022 | extracted='SLOAN HEATHER'  expected='Smith Medical, PC' |
| 351 | `provider` | 02/25/2021 | extracted='HALL JENNIFER'  expected='Smith Medical, PC' |
| 352 | `payments` | 07/17/2022 | extracted=18.99  expected=None |
| 352 | `provider` | 07/17/2022 | extracted='SHAFFER VINCENT'  expected='Smith Medical, PC' |
| 353 | `payments` | 02/18/2022 | extracted=53.39  expected=None |
| 353 | `provider` | 02/18/2022 | extracted='MCKEE NANCY'  expected='Smith Medical, PC' |
| 354 | `payments` | 08/04/2022 | extracted=29.34  expected=None |
| 354 | `provider` | 08/04/2022 | extracted='HOOPER CATHERINE'  expected='Smith Medical, PC' |
| 355 | `provider` | 04/20/2023 | extracted='RICHMOND CURTIS'  expected='Smith Medical, PC' |
| 356 | `payments` | 08/13/2021 | extracted=38.45  expected=None |
| 356 | `provider` | 08/13/2021 | extracted='BARRETT ALEXANDER'  expected='Smith Medical, PC' |
| 357 | `payments` | 06/23/2023 | extracted=9.63  expected=None |
| 357 | `provider` | 06/23/2023 | extracted='DOMINGUEZ ALEXANDER'  expected='Smith Medical, PC' |
| 358 | `payments` | 06/19/2021 | extracted=35.19  expected=None |
| 358 | `provider` | 06/19/2021 | extracted='NORTON NATHAN'  expected='Smith Medical, PC' |
| 359 | `payments` | 04/21/2021 | extracted=15.89  expected=None |
| 359 | `provider` | 04/21/2021 | extracted='JOHNSON MATTHEW'  expected='Smith Medical, PC' |
| 360 | `provider` | 10/31/2022 | extracted='PARKER ALISON'  expected='Smith Medical, PC' |
| 361 | `payments` | 07/09/2022 | extracted=28.9  expected=None |
| 361 | `provider` | 07/09/2022 | extracted='MAY MICHAEL'  expected='Smith Medical, PC' |
| 362 | `payments` | 12/14/2023 | extracted=17.43  expected=None |
| 362 | `provider` | 12/14/2023 | extracted='ADAMS TONYA'  expected='Smith Medical, PC' |
| 362 | `insurers` | 12/14/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 363 | `provider` | 06/28/2023 | extracted='GARRETT ERIC'  expected='Smith Medical, PC' |
| 364 | `payments` | 02/02/2023 | extracted=47.26  expected=None |
| 364 | `provider` | 02/02/2023 | extracted='WHITE DAWN'  expected='Smith Medical, PC' |
| 364 | `insurers` | 02/02/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 365 | `payments` | 05/24/2023 | extracted=44.17  expected=None |
| 365 | `provider` | 05/24/2023 | extracted='WILLIAMS GEORGE'  expected='Smith Medical, PC' |
| 366 | `provider` | 04/25/2021 | extracted='GOMEZ TRACY'  expected='Smith Medical, PC' |
| 366 | `insurers` | 04/25/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 367 | `provider` | 02/21/2022 | extracted='BURNS VALERIE'  expected='Smith Medical, PC' |
| 367 | `insurers` | 02/21/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 368 | `payments` | 10/20/2022 | extracted=25.16  expected=None |
| 368 | `provider` | 10/20/2022 | extracted='BROWN MICHELLE'  expected='Smith Medical, PC' |
| 369 | `payments` | 12/21/2024 | extracted=32.42  expected=None |
| 369 | `provider` | 12/21/2024 | extracted='RICHARDSON JEFFERY'  expected='Smith Medical, PC' |
| 370 | `provider` | 08/26/2022 | extracted='BOYD AMANDA'  expected='Smith Medical, PC' |
| 371 | `payments` | 07/10/2021 | extracted=38.17  expected=None |
| 371 | `provider` | 07/10/2021 | extracted='WILSON MELISSA'  expected='Smith Medical, PC' |
| 372 | `payments` | 05/11/2021 | extracted=21.47  expected=None |
| 372 | `provider` | 05/11/2021 | extracted='GONZALEZ RYAN'  expected='Smith Medical, PC' |
| 373 | `payments` | 10/15/2024 | extracted=15.45  expected=None |
| 373 | `provider` | 10/15/2024 | extracted='HOFFMAN ASHLEY'  expected='Smith Medical, PC' |
| 374 | `payments` | 12/30/2021 | extracted=6.96  expected=None |
| 374 | `provider` | 12/30/2021 | extracted='YORK SHEILA'  expected='Smith Medical, PC' |
| 375 | `provider` | 07/05/2024 | extracted='STEWART STEPHEN'  expected='Smith Medical, PC' |
| 376 | `provider` | 01/28/2024 | extracted='BOOKER ROBERT'  expected='Smith Medical, PC' |
| 377 | `payments` | 08/27/2023 | extracted=17.57  expected=None |
| 377 | `provider` | 08/27/2023 | extracted='BROWN JACOB'  expected='Smith Medical, PC' |
| 378 | `payments` | 08/11/2021 | extracted=4.91  expected=None |
| 378 | `provider` | 08/11/2021 | extracted='SANCHEZ TERESA'  expected='Smith Medical, PC' |
| 379 | `provider` | 04/28/2023 | extracted='DAVIS AMY'  expected='Smith Medical, PC' |
| 380 | `payments` | 08/19/2021 | extracted=21.11  expected=None |
| 380 | `provider` | 08/19/2021 | extracted='HARRIS LAWRENCE'  expected='Smith Medical, PC' |
| 381 | `payments` | 12/06/2024 | extracted=27.23  expected=None |
| 381 | `provider` | 12/06/2024 | extracted='DAVIS GEORGE'  expected='Smith Medical, PC' |
| 382 | `payments` | 01/18/2023 | extracted=15.8  expected=None |
| 382 | `provider` | 01/18/2023 | extracted='STEPHENS JOSHUA'  expected='Smith Medical, PC' |
| 383 | `provider` | 12/14/2021 | extracted='FISHER CHEYENNE'  expected='Smith Medical, PC' |
| 384 | `payments` | 08/11/2024 | extracted=69.66  expected=None |
| 384 | `provider` | 08/11/2024 | extracted='JACOBS KAREN'  expected='Smith Medical, PC' |
| 385 | `provider` | 07/11/2023 | extracted='ALLEN KELLY'  expected='Smith Medical, PC' |
| 386 | `cpt_codes` | 01/08/2021 | missing=['85027', '97010', '97018', '99221'] |
| 386 | `provider` | 01/08/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 387 | `provider` | 02/19/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 388 | `provider` | 01/23/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 389 | `provider` | 06/05/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 390 | `provider` | 04/20/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 391 | `provider` | 11/19/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 392 | `provider` | 04/13/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 393 | `provider` | 08/10/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 394 | `provider` | 07/22/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 395 | `provider` | 06/30/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 396 | `provider` | 06/24/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 396 | `insurers` | 06/24/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 397 | `provider` | 11/23/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 398 | `provider` | 08/25/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 399 | `provider` | 01/12/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |

### doc_008

**Count mismatch** — GT: 100, extracted: 83.

**Missing records (92):**
- GT[4] `03/30/2022 - 07/30/2024` — No extracted record found with this treatment_date
- GT[5] `07/12/2021 - 05/01/2024` — No extracted record found with this treatment_date
- GT[6] `04/12/2021 - 10/11/2024` — No extracted record found with this treatment_date
- GT[7] `04/08/2021 - 06/20/2024` — No extracted record found with this treatment_date
- GT[9] `04/03/2021 - 11/04/2024` — No extracted record found with this treatment_date
- GT[10] `01/29/2021 - 10/20/2024` — No extracted record found with this treatment_date
- GT[11] `01/15/2021 - 09/02/2024` — No extracted record found with this treatment_date
- GT[12] `01/02/2021 - 10/22/2024` — No extracted record found with this treatment_date
- GT[13] `04/11/2021 - 12/21/2024` — No extracted record found with this treatment_date
- GT[14] `01/07/2021 - 12/13/2024` — No extracted record found with this treatment_date
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

**Extra extracted records (76):**
- `03/30/2022 - 04/19/2024` — Extracted record has no GT counterpart
- `07/20/2021 - 12/06/2023` — Extracted record has no GT counterpart
- `01/07/2024 - 10/19/2021` — Extracted record has no GT counterpart
- `01/24/2024 - 11/14/2021` — Extracted record has no GT counterpart
- `04/03/2021 - 10/26/2024` — Extracted record has no GT counterpart
- `01/29/2021 - 11/24/2023` — Extracted record has no GT counterpart
- `01/15/2021 - 02/14/2024` — Extracted record has no GT counterpart
- `01/02/2021 - 08/24/2024` — Extracted record has no GT counterpart
- `04/11/2021 - 12/13/2024` — Extracted record has no GT counterpart
- `01/07/2021 - 02/03/2022` — Extracted record has no GT counterpart
- `04/19/2021 - 09/09/2023` — Extracted record has no GT counterpart
- `02/10/2022 - 06/13/2024` — Extracted record has no GT counterpart
- `03/24/2023 - 06/14/2024` — Extracted record has no GT counterpart
- `01/12/2023 - 08/17/2024` — Extracted record has no GT counterpart
- `02/03/2022 - 04/15/2022` — Extracted record has no GT counterpart
- `10/28/2024 - 03/20/2023` — Extracted record has no GT counterpart
- `05/01/2023 - 12/08/2022` — Extracted record has no GT counterpart
- `01/10/2021 - 07/20/2024` — Extracted record has no GT counterpart
- `03/11/2022 - 06/13/2022` — Extracted record has no GT counterpart
- `01/02/2024 - 09/22/2022` — Extracted record has no GT counterpart
- `03/12/2024 - 04/02/2024` — Extracted record has no GT counterpart
- `04/29/2021 - 04/21/2024` — Extracted record has no GT counterpart
- `11/13/2021 - 01/31/2023` — Extracted record has no GT counterpart
- `12/28/2024 - 08/13/2024` — Extracted record has no GT counterpart
- `03/09/2024 - 05/02/2023` — Extracted record has no GT counterpart
- `10/02/2024 - 07/20/2023` — Extracted record has no GT counterpart
- `09/18/2024 - 10/17/2024` — Extracted record has no GT counterpart
- `10/29/2024 - 12/12/2024` — Extracted record has no GT counterpart
- `03/12/2022 - 12/07/2022` — Extracted record has no GT counterpart
- `08/13/2024 - 11/28/2024` — Extracted record has no GT counterpart
- `03/19/2024 - 12/25/2024` — Extracted record has no GT counterpart
- `07/05/2022 - 02/26/2024` — Extracted record has no GT counterpart
- `06/18/2022 - 11/16/2024` — Extracted record has no GT counterpart
- `07/06/2023 - 11/16/2022` — Extracted record has no GT counterpart
- `10/01/2024 - 08/20/2022` — Extracted record has no GT counterpart
- `11/14/2021 - 12/03/2024` — Extracted record has no GT counterpart
- `06/12/2023 - 09/03/2021` — Extracted record has no GT counterpart
- `03/03/2021 - 02/28/2024` — Extracted record has no GT counterpart
- `01/31/2023` — Extracted record has no GT counterpart
- `03/23/2021 - 09/07/2023` — Extracted record has no GT counterpart
- `04/10/2024` — Extracted record has no GT counterpart
- `10/07/2024` — Extracted record has no GT counterpart
- `03/08/2022 - 09/18/2023` — Extracted record has no GT counterpart
- `02/18/2023` — Extracted record has no GT counterpart
- `03/22/2022` — Extracted record has no GT counterpart
- `08/06/2021` — Extracted record has no GT counterpart
- `01/12/2022 - 12/05/2024` — Extracted record has no GT counterpart
- `03/13/2024` — Extracted record has no GT counterpart
- `11/08/2022 - 02/05/2024` — Extracted record has no GT counterpart
- `06/02/2021 - 08/14/2022` — Extracted record has no GT counterpart
- `12/31/2021 - 09/22/2024` — Extracted record has no GT counterpart
- `08/29/2021` — Extracted record has no GT counterpart
- `02/24/2022 - 01/09/2024` — Extracted record has no GT counterpart
- `02/17/2021` — Extracted record has no GT counterpart
- `10/17/2023 - 01/08/2024` — Extracted record has no GT counterpart
- `12/15/2021` — Extracted record has no GT counterpart
- `12/26/2021 - 08/03/2024` — Extracted record has no GT counterpart
- `07/20/2024` — Extracted record has no GT counterpart
- `06/25/2023` — Extracted record has no GT counterpart
- `08/14/2022 - 07/28/2024` — Extracted record has no GT counterpart
- `10/15/2021 - 11/01/2022` — Extracted record has no GT counterpart
- `11/28/2023 - 02/10/2024` — Extracted record has no GT counterpart
- `06/07/2024 - 12/23/2024` — Extracted record has no GT counterpart
- `04/30/2023 - 03/03/2021` — Extracted record has no GT counterpart
- `10/31/2022 - 09/04/2024` — Extracted record has no GT counterpart
- `08/27/2022 - 02/17/2024` — Extracted record has no GT counterpart
- `08/27/2024 - 12/08/2022` — Extracted record has no GT counterpart
- `09/08/2021 - 08/02/2024` — Extracted record has no GT counterpart
- `08/05/2021 - 10/17/2021` — Extracted record has no GT counterpart
- `08/24/2022 - 11/24/2024` — Extracted record has no GT counterpart
- `07/18/2021 - 08/07/2023` — Extracted record has no GT counterpart
- `04/30/2021 - 09/13/2024` — Extracted record has no GT counterpart
- `12/24/2023 - 05/24/2023` — Extracted record has no GT counterpart
- `09/12/2024 - 06/30/2022` — Extracted record has no GT counterpart
- `11/27/2022 - 06/25/2024` — Extracted record has no GT counterpart
- `11/18/2021 - 11/08/2024` — Extracted record has no GT counterpart

**Field mismatches (30):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `payments` | 06/04/2021 - 11/30/2024 | extracted=365.0  expected=None |
| 0 | `balance` | 06/04/2021 - 11/30/2024 | extracted=0.0  expected=365.0  diff=365.00 |
| 1 | `payments` | 01/25/2021 - 10/20/2024 | extracted=260.57  expected=None |
| 1 | `balance` | 01/25/2021 - 10/20/2024 | extracted=0.0  expected=260.57  diff=260.57 |
| 2 | `payments` | 01/08/2021 - 11/19/2024 | extracted=209.85  expected=None |
| 2 | `balance` | 01/08/2021 - 11/19/2024 | extracted=0.0  expected=209.85  diff=209.85 |
| 3 | `payments` | 05/23/2021 - 11/04/2024 | extracted=236.5  expected=None |
| 3 | `balance` | 05/23/2021 - 11/04/2024 | extracted=0.0  expected=236.5  diff=236.50 |
| 8 | `cpt_codes` | 03/13/2021 - 12/18/2024 |  |
| 8 | `payments` | 03/13/2021 - 12/18/2024 | extracted=165.46  expected=None |
| 8 | `balance` | 03/13/2021 - 12/18/2024 | extracted=0.0  expected=165.46  diff=165.46 |
| 15 | `cpt_codes` | 02/15/2021 - 10/14/2024 |  |
| 15 | `payments` | 02/15/2021 - 10/14/2024 | extracted=459.47  expected=None |
| 15 | `balance` | 02/15/2021 - 10/14/2024 | extracted=0.0  expected=459.47  diff=459.47 |
| 40 | `cpt_codes` | 01/22/2021 - 09/03/2024 | missing=['72110', '73100', '73110', '73562', '73564', '74178', '76705', 'J1644', 'J3480']  extra=['A4245'] |
| 40 | `total_charges` | 01/22/2021 - 09/03/2024 | extracted=421.87  expected=5604.51  diff=5182.64 |
| 40 | `ins_paid` | 01/22/2021 - 09/03/2024 | extracted=224.67  expected=3594.14  diff=3369.47 |
| 40 | `adjustment` | 01/22/2021 - 09/03/2024 | extracted=197.2  expected=1874.28  diff=1677.08 |
| 40 | `balance` | 01/22/2021 - 09/03/2024 | extracted=0.0  expected=136.09  diff=136.09 |
| 40 | `provider` | 01/22/2021 - 09/03/2024 | extracted=''  expected='Hudson Medical, PC' |
| 40 | `insurers` | 01/22/2021 - 09/03/2024 | missing=['tricare'] |
| 40 | `description` | 01/22/2021 - 09/03/2024 | extracted='Alcohol wipes, per box'  expected=None |
| 59 | `cpt_codes` | 01/22/2021 - 12/05/2024 | missing=['72100', '72110', '72148', '73100', '73564', '74177', '74178', '76700', '76705', '76830', 'A4207', 'A4246'] |
| 59 | `total_charges` | 01/22/2021 - 12/05/2024 | extracted=421.87  expected=9587.28  diff=9165.41 |
| 59 | `ins_paid` | 01/22/2021 - 12/05/2024 | extracted=224.67  expected=6029.89  diff=5805.22 |
| 59 | `adjustment` | 01/22/2021 - 12/05/2024 | extracted=197.2  expected=3357.02  diff=3159.82 |
| 59 | `balance` | 01/22/2021 - 12/05/2024 | extracted=0.0  expected=200.37  diff=200.37 |
| 59 | `provider` | 01/22/2021 - 12/05/2024 | extracted=''  expected='Hudson Medical, PC' |
| 59 | `insurers` | 01/22/2021 - 12/05/2024 | missing=['tricare'] |
| 59 | `description` | 01/22/2021 - 12/05/2024 | extracted='Alcohol wipes, per box'  expected=None |

### doc_009

Record count matches GT.

**Field mismatches (8):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `total_charges` | 01/01/2017 - 12/31/2024 | extracted=1699901.27  expected=1262450.18  diff=437451.09 |
| 0 | `ins_paid` | 01/01/2017 - 12/31/2024 | extracted=972275.83  expected=948201.11  diff=24074.72 |
| 0 | `adjustment` | 01/01/2017 - 12/31/2024 | extracted=314249.07  expected=None |
| 0 | `payments` | 01/01/2017 - 12/31/2024 | extracted=61315.16  expected=314249.07  diff=252933.91 |
| 0 | `balance` | 01/01/2017 - 12/31/2024 | extracted=88116.62  expected=0.0  diff=88116.62 |
| 0 | `insurers` | 01/01/2017 - 12/31/2024 | extra=['allwin', 'argus', 'blink health', 'caremark', 'cigna', 'cigna healthspring', 'express scripts', 'goodrx', 'healthspring', 'hurst', 'immunizations', 'lonestar', 'my rx card', 'omnisys immunizations', 'paramount', 'pbm program', 'scriptcycle', 'sfs', 'supplemental', 'supplemental coverage', 'third party', 'third party program'] |
| 0 | `third_parties` | 01/01/2017 - 12/31/2024 | extra=['argus discount', 'discount', 'healthspring', 'hurst', 'mckesson health pbm hurst', 'pbm', 'pbm christopher', 'pbm program hurst', 'program', 'third party', 'third party program hurst'] |
| 0 | `description` | 01/01/2017 - 12/31/2024 | extracted='Pharmacy Patient Profile'  expected='Pharmacy Record' |

### doc_010

Record count matches GT.

**Field mismatches (6):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `total_charges` | 01/01/2017 - 12/29/2024 | extracted=1428563.85  expected=1247488.96  diff=181074.89 |
| 0 | `ins_paid` | 01/01/2017 - 12/29/2024 | extracted=509222.5  expected=373214.66  diff=136007.84 |
| 0 | `adjustment` | 01/01/2017 - 12/29/2024 | extracted=None  expected=562959.56 |
| 0 | `payments` | 01/01/2017 - 12/29/2024 | extracted=356381.79  expected=311314.74  diff=45067.05 |
| 0 | `insurers` | 01/01/2017 - 12/29/2024 | extra=['allwin', 'argus', 'blink health', 'caremark', 'cigna', 'cigna healthspring', 'express scripts', 'goodrx', 'mckesson health pbm', 'medco health', 'my rx card', 'omnisys immunizations', 'optumrx', 'paramount lonestar', 'scriptcycle', 'sfs'] |
| 0 | `third_parties` | 01/01/2017 - 12/29/2024 | extra=['healthspring'] |

### doc_011

**Count mismatch** — GT: 150, extracted: 201.

**Extra extracted records (51):**
- `04/18/2021 - 04/22/2021` — Extracted record has no GT counterpart
- `11/03/2020 – 11/01/2020` — Extracted record has no GT counterpart
- `12/03/2018` — Extracted record has no GT counterpart
- `12/04/2018` — Extracted record has no GT counterpart
- `12/08/2018` — Extracted record has no GT counterpart
- `12/04/2018` — Extracted record has no GT counterpart
- `12/02/2018` — Extracted record has no GT counterpart
- `12/07/2018` — Extracted record has no GT counterpart
- `12/01/2018` — Extracted record has no GT counterpart
- `12/05/2018` — Extracted record has no GT counterpart
- `12/05/2018` — Extracted record has no GT counterpart
- `12/05/2018` — Extracted record has no GT counterpart
- `12/02/2018` — Extracted record has no GT counterpart
- `12/02/2018` — Extracted record has no GT counterpart
- `12/01/2018` — Extracted record has no GT counterpart
- `12/04/2018` — Extracted record has no GT counterpart
- `12/01/2018` — Extracted record has no GT counterpart
- `12/05/2018` — Extracted record has no GT counterpart
- `12/04/2018` — Extracted record has no GT counterpart
- `12/08/2018` — Extracted record has no GT counterpart
- `12/06/2018` — Extracted record has no GT counterpart
- `12/08/2018` — Extracted record has no GT counterpart
- `12/02/2018` — Extracted record has no GT counterpart
- `12/08/2018` — Extracted record has no GT counterpart
- `12/01/2018` — Extracted record has no GT counterpart
- `12/06/2018` — Extracted record has no GT counterpart
- `12/03/2018` — Extracted record has no GT counterpart
- `12/06/2018` — Extracted record has no GT counterpart
- `12/06/2018` — Extracted record has no GT counterpart
- `12/03/2018` — Extracted record has no GT counterpart
- `12/08/2018` — Extracted record has no GT counterpart
- `12/02/2018` — Extracted record has no GT counterpart
- `12/04/2018` — Extracted record has no GT counterpart
- `12/06/2018` — Extracted record has no GT counterpart
- `Inpatient Episode: 11/13/2022 – 11/15/2022` — Extracted record has no GT counterpart
- `11/14/2022` — Extracted record has no GT counterpart
- `11/15/2022` — Extracted record has no GT counterpart
- `11/14/2022` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `11/14/2022` — Extracted record has no GT counterpart
- `11/14/2022` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `11/15/2022` — Extracted record has no GT counterpart
- `11/15/2022` — Extracted record has no GT counterpart
- `11/15/2022` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `11/15/2022` — Extracted record has no GT counterpart

**Field mismatches (653):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `payments` | 01/25/2023 - 01/26/2023 | extracted=16802.06  expected=None |
| 0 | `balance` | 01/25/2023 - 01/26/2023 | extracted=0.0  expected=16802.06  diff=16802.06 |
| 1 | `payments` | 09/13/2023 - 09/19/2023 | extracted=24725.09  expected=None |
| 1 | `balance` | 09/13/2023 - 09/19/2023 | extracted=0.0  expected=24725.09  diff=24725.09 |
| 2 | `payments` | 02/27/2023 - 03/05/2023 | extracted=18230.58  expected=None |
| 2 | `balance` | 02/27/2023 - 03/05/2023 | extracted=0.0  expected=18230.58  diff=18230.58 |
| 3 | `payments` | 07/21/2017 - 07/28/2017 | extracted=20570.21  expected=None |
| 3 | `balance` | 07/21/2017 - 07/28/2017 | extracted=0.0  expected=20570.21  diff=20570.21 |
| 4 | `payments` | 04/18/2023 - 04/22/2023 | extracted=13846.82  expected=None |
| 4 | `balance` | 04/18/2023 - 04/22/2023 | extracted=0.0  expected=13846.82  diff=13846.82 |
| 5 | `payments` | 08/08/2022 - 08/11/2022 | extracted=20308.98  expected=None |
| 5 | `balance` | 08/08/2022 - 08/11/2022 | extracted=0.0  expected=20308.98  diff=20308.98 |
| 6 | `payments` | 10/12/2020 - 10/13/2020 | extracted=25650.39  expected=None |
| 6 | `balance` | 10/12/2020 - 10/13/2020 | extracted=0.0  expected=25650.39  diff=25650.39 |
| 7 | `payments` | 05/07/2022 - 05/08/2022 | extracted=19153.05  expected=None |
| 7 | `balance` | 05/07/2022 - 05/08/2022 | extracted=0.0  expected=19153.05  diff=19153.05 |
| 8 | `payments` | 07/16/2017 - 07/17/2017 | extracted=19547.52  expected=None |
| 8 | `balance` | 07/16/2017 - 07/17/2017 | extracted=0.0  expected=19547.52  diff=19547.52 |
| 9 | `payments` | 11/02/2019 - 11/06/2019 | extracted=13486.54  expected=None |
| 9 | `balance` | 11/02/2019 - 11/06/2019 | extracted=0.0  expected=13486.54  diff=13486.54 |
| 10 | `payments` | 10/03/2020 - 10/06/2020 | extracted=27817.19  expected=None |
| 10 | `balance` | 10/03/2020 - 10/06/2020 | extracted=0.0  expected=27817.19  diff=27817.19 |
| 11 | `payments` | 05/09/2022 - 05/10/2022 | extracted=17467.8  expected=None |
| 11 | `balance` | 05/09/2022 - 05/10/2022 | extracted=0.0  expected=17467.8  diff=17467.80 |
| 12 | `payments` | 01/17/2018 - 01/24/2018 | extracted=16177.43  expected=None |
| 12 | `balance` | 01/17/2018 - 01/24/2018 | extracted=0.0  expected=16177.43  diff=16177.43 |
| 13 | `payments` | 12/29/2019 - 01/05/2020 | extracted=21530.69  expected=None |
| 13 | `balance` | 12/29/2019 - 01/05/2020 | extracted=0.0  expected=21530.69  diff=21530.69 |
| 14 | `payments` | 05/28/2024 - 06/01/2024 | extracted=18143.4  expected=None |
| 14 | `balance` | 05/28/2024 - 06/01/2024 | extracted=0.0  expected=18143.4  diff=18143.40 |
| 15 | `payments` | 06/16/2021 - 06/23/2021 | extracted=22926.63  expected=None |
| 15 | `balance` | 06/16/2021 - 06/23/2021 | extracted=0.0  expected=22926.63  diff=22926.63 |
| 16 | `payments` | 02/03/2023 - 02/09/2023 | extracted=14427.58  expected=None |
| 16 | `balance` | 02/03/2023 - 02/09/2023 | extracted=0.0  expected=14427.58  diff=14427.58 |
| 17 | `payments` | 05/04/2021 - 05/08/2021 | extracted=15878.74  expected=None |
| 17 | `balance` | 05/04/2021 - 05/08/2021 | extracted=0.0  expected=15878.74  diff=15878.74 |
| 18 | `payments` | 09/21/2019 - 09/26/2019 | extracted=25196.84  expected=None |
| 18 | `balance` | 09/21/2019 - 09/26/2019 | extracted=0.0  expected=25196.84  diff=25196.84 |
| 19 | `payments` | 07/06/2018 - 07/07/2018 | extracted=17904.72  expected=None |
| 19 | `balance` | 07/06/2018 - 07/07/2018 | extracted=0.0  expected=17904.72  diff=17904.72 |
| 20 | `payments` | 09/15/2022 - 09/22/2022 | extracted=20237.77  expected=None |
| 20 | `balance` | 09/15/2022 - 09/22/2022 | extracted=0.0  expected=20237.77  diff=20237.77 |
| 21 | `payments` | 10/28/2021 - 11/03/2021 | extracted=16866.56  expected=None |
| 21 | `balance` | 10/28/2021 - 11/03/2021 | extracted=0.0  expected=16866.56  diff=16866.56 |
| 22 | `payments` | 07/14/2024 - 07/16/2024 | extracted=12561.64  expected=None |
| 22 | `balance` | 07/14/2024 - 07/16/2024 | extracted=0.0  expected=12561.64  diff=12561.64 |
| 23 | `payments` | 12/16/2022 - 12/20/2022 | extracted=13331.91  expected=None |
| 23 | `balance` | 12/16/2022 - 12/20/2022 | extracted=0.0  expected=13331.91  diff=13331.91 |
| 24 | `total_charges` | 04/16/2021 - 04/23/2021 | extracted=270886.44  expected=351524.69  diff=80638.25 |
| 24 | `ins_paid` | 04/16/2021 - 04/23/2021 | extracted=133123.66  expected=169561.02  diff=36437.36 |
| 24 | `adjustment` | 04/16/2021 - 04/23/2021 | extracted=124481.8  expected=159536.39  diff=35054.59 |
| 24 | `balance` | 04/16/2021 - 04/23/2021 | extracted=13381.01  expected=22427.28  diff=9046.27 |
| 25 | `payments` | 08/21/2022 - 08/28/2022 | extracted=25723.55  expected=None |
| 25 | `balance` | 08/21/2022 - 08/28/2022 | extracted=0.0  expected=25723.55  diff=25723.55 |
| 25 | `provider` | 08/21/2022 - 08/28/2022 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 25 | `insurers` | 08/21/2022 - 08/28/2022 | missing=['medicaid'] |
| 25 | `description` | 08/21/2022 - 08/28/2022 | extracted='Diagnosis: Urinary tract infection'  expected='Urinary tract infection' |
| 26 | `payments` | 01/26/2023 - 02/02/2023 | extracted=27219.37  expected=None |
| 26 | `balance` | 01/26/2023 - 02/02/2023 | extracted=0.0  expected=27219.37  diff=27219.37 |
| 26 | `provider` | 01/26/2023 - 02/02/2023 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 26 | `insurers` | 01/26/2023 - 02/02/2023 | missing=['medicaid'] |
| 26 | `description` | 01/26/2023 - 02/02/2023 | extracted='Diagnosis: Acute myocardial infarction'  expected='Acute myocardial infarction' |
| 27 | `payments` | 03/12/2018 - 03/15/2018 | extracted=16389.43  expected=None |
| 27 | `balance` | 03/12/2018 - 03/15/2018 | extracted=0.0  expected=16389.43  diff=16389.43 |
| 27 | `provider` | 03/12/2018 - 03/15/2018 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 27 | `insurers` | 03/12/2018 - 03/15/2018 | missing=['medicaid'] |
| 27 | `description` | 03/12/2018 - 03/15/2018 | extracted='Diagnosis: Pneumonia, unspecified organism'  expected='Pneumonia, unspecified organism' |
| 28 | `payments` | 11/09/2020 - 11/15/2020 | extracted=16140.46  expected=None |
| 28 | `balance` | 11/09/2020 - 11/15/2020 | extracted=0.0  expected=16140.46  diff=16140.46 |
| 28 | `provider` | 11/09/2020 - 11/15/2020 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 28 | `insurers` | 11/09/2020 - 11/15/2020 | missing=['medicaid'] |
| 28 | `description` | 11/09/2020 - 11/15/2020 | extracted='Diagnosis: Bowel obstruction'  expected='Bowel obstruction' |
| 29 | `payments` | 12/13/2022 - 12/16/2022 | extracted=20601.25  expected=None |
| 29 | `balance` | 12/13/2022 - 12/16/2022 | extracted=0.0  expected=20601.25  diff=20601.25 |
| 29 | `provider` | 12/13/2022 - 12/16/2022 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 29 | `insurers` | 12/13/2022 - 12/16/2022 | missing=['medicaid'] |
| 29 | `description` | 12/13/2022 - 12/16/2022 | extracted='Diagnosis: Hip fracture, right femur'  expected='Hip fracture, right femur' |
| 30 | `payments` | 03/22/2023 - 03/23/2023 | extracted=22281.49  expected=None |
| 30 | `balance` | 03/22/2023 - 03/23/2023 | extracted=0.0  expected=22281.49  diff=22281.49 |
| 30 | `provider` | 03/22/2023 - 03/23/2023 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 30 | `insurers` | 03/22/2023 - 03/23/2023 | missing=['medicaid'] |
| 30 | `description` | 03/22/2023 - 03/23/2023 | extracted='Diagnosis: Gastrointestinal hemorrhage'  expected='Gastrointestinal hemorrhage' |
| 31 | `payments` | 10/08/2021 - 10/14/2021 | extracted=15615.27  expected=None |
| 31 | `balance` | 10/08/2021 - 10/14/2021 | extracted=0.0  expected=15615.27  diff=15615.27 |
| 31 | `provider` | 10/08/2021 - 10/14/2021 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 31 | `insurers` | 10/08/2021 - 10/14/2021 | missing=['medicaid'] |
| 31 | `description` | 10/08/2021 - 10/14/2021 | extracted='Diagnosis: Gastrointestinal hemorrhage'  expected='Gastrointestinal hemorrhage' |
| 32 | `payments` | 10/24/2024 - 10/28/2024 | extracted=25167.12  expected=None |
| 32 | `balance` | 10/24/2024 - 10/28/2024 | extracted=0.0  expected=25167.12  diff=25167.12 |
| 32 | `provider` | 10/24/2024 - 10/28/2024 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 32 | `insurers` | 10/24/2024 - 10/28/2024 | missing=['medicaid'] |
| 32 | `description` | 10/24/2024 - 10/28/2024 | extracted='Diagnosis: Total knee arthroplasty'  expected='Total knee arthroplasty' |
| 33 | `payments` | 10/10/2024 - 10/11/2024 | extracted=23656.92  expected=None |
| 33 | `balance` | 10/10/2024 - 10/11/2024 | extracted=0.0  expected=23656.92  diff=23656.92 |
| 33 | `provider` | 10/10/2024 - 10/11/2024 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 33 | `insurers` | 10/10/2024 - 10/11/2024 | missing=['medicaid'] |
| 33 | `description` | 10/10/2024 - 10/11/2024 | extracted='Diagnosis: Acute kidney injury'  expected='Acute kidney injury' |
| 34 | `payments` | 01/30/2019 - 02/03/2019 | extracted=18015.28  expected=None |
| 34 | `balance` | 01/30/2019 - 02/03/2019 | extracted=0.0  expected=18015.28  diff=18015.28 |
| 34 | `provider` | 01/30/2019 - 02/03/2019 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 34 | `insurers` | 01/30/2019 - 02/03/2019 | missing=['medicaid'] |
| 34 | `description` | 01/30/2019 - 02/03/2019 | extracted='Diagnosis: Urinary tract infection'  expected='Urinary tract infection' |
| 35 | `payments` | 05/11/2017 - 05/14/2017 | extracted=19815.67  expected=None |
| 35 | `balance` | 05/11/2017 - 05/14/2017 | extracted=0.0  expected=19815.67  diff=19815.67 |
| 35 | `provider` | 05/11/2017 - 05/14/2017 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 35 | `insurers` | 05/11/2017 - 05/14/2017 | missing=['medicaid'] |
| 35 | `description` | 05/11/2017 - 05/14/2017 | extracted='Diagnosis: Bowel obstruction'  expected='Bowel obstruction' |
| 36 | `payments` | 03/20/2021 - 03/24/2021 | extracted=17129.77  expected=None |
| 36 | `balance` | 03/20/2021 - 03/24/2021 | extracted=0.0  expected=17129.77  diff=17129.77 |
| 36 | `provider` | 03/20/2021 - 03/24/2021 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 36 | `insurers` | 03/20/2021 - 03/24/2021 | missing=['medicaid'] |
| 36 | `description` | 03/20/2021 - 03/24/2021 | extracted='Diagnosis: Schizophrenia, acute exacerbation'  expected='Schizophrenia, acute exacerbation' |
| 37 | `payments` | 05/17/2020 - 05/20/2020 | extracted=25958.32  expected=None |
| 37 | `balance` | 05/17/2020 - 05/20/2020 | extracted=0.0  expected=25958.32  diff=25958.32 |
| 37 | `provider` | 05/17/2020 - 05/20/2020 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 37 | `insurers` | 05/17/2020 - 05/20/2020 | missing=['medicaid'] |
| 37 | `description` | 05/17/2020 - 05/20/2020 | extracted='Diagnosis: Heart failure, unspecified'  expected='Heart failure, unspecified' |
| 38 | `payments` | 12/19/2022 - 12/21/2022 | extracted=21455.21  expected=None |
| 38 | `balance` | 12/19/2022 - 12/21/2022 | extracted=0.0  expected=21455.21  diff=21455.21 |
| 38 | `provider` | 12/19/2022 - 12/21/2022 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 38 | `insurers` | 12/19/2022 - 12/21/2022 | missing=['medicaid'] |
| 38 | `description` | 12/19/2022 - 12/21/2022 | extracted='Diagnosis: Bowel obstruction'  expected='Bowel obstruction' |
| 39 | `payments` | 08/06/2020 - 08/07/2020 | extracted=19020.69  expected=None |
| 39 | `balance` | 08/06/2020 - 08/07/2020 | extracted=0.0  expected=19020.69  diff=19020.69 |
| 39 | `provider` | 08/06/2020 - 08/07/2020 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 39 | `insurers` | 08/06/2020 - 08/07/2020 | missing=['medicaid'] |
| 39 | `description` | 08/06/2020 - 08/07/2020 | extracted='Diagnosis: Gastrointestinal hemorrhage'  expected='Gastrointestinal hemorrhage' |
| 40 | `payments` | 04/09/2017 - 04/13/2017 | extracted=19340.89  expected=None |
| 40 | `balance` | 04/09/2017 - 04/13/2017 | extracted=0.0  expected=19340.89  diff=19340.89 |
| 40 | `provider` | 04/09/2017 - 04/13/2017 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 40 | `insurers` | 04/09/2017 - 04/13/2017 | missing=['medicaid'] |
| 40 | `description` | 04/09/2017 - 04/13/2017 | extracted='Diagnosis: Pulmonary embolism'  expected='Pulmonary embolism' |
| 41 | `payments` | 07/25/2023 - 07/30/2023 | extracted=23705.95  expected=None |
| 41 | `balance` | 07/25/2023 - 07/30/2023 | extracted=0.0  expected=23705.95  diff=23705.95 |
| 41 | `provider` | 07/25/2023 - 07/30/2023 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 41 | `insurers` | 07/25/2023 - 07/30/2023 | missing=['medicaid'] |
| 41 | `description` | 07/25/2023 - 07/30/2023 | extracted='Diagnosis: Total knee arthroplasty'  expected='Total knee arthroplasty' |
| 42 | `payments` | 07/15/2019 - 07/18/2019 | extracted=15259.96  expected=None |
| 42 | `balance` | 07/15/2019 - 07/18/2019 | extracted=0.0  expected=15259.96  diff=15259.96 |
| 42 | `provider` | 07/15/2019 - 07/18/2019 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 42 | `insurers` | 07/15/2019 - 07/18/2019 | missing=['medicaid'] |
| 42 | `description` | 07/15/2019 - 07/18/2019 | extracted='Diagnosis: Lumbar spine fusion'  expected='Lumbar spine fusion' |
| 43 | `payments` | 07/28/2022 - 08/04/2022 | extracted=12127.85  expected=None |
| 43 | `balance` | 07/28/2022 - 08/04/2022 | extracted=0.0  expected=12127.85  diff=12127.85 |
| 43 | `provider` | 07/28/2022 - 08/04/2022 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 43 | `insurers` | 07/28/2022 - 08/04/2022 | missing=['medicaid'] |
| 43 | `description` | 07/28/2022 - 08/04/2022 | extracted='Diagnosis: Acute pancreatitis'  expected='Acute pancreatitis' |
| 44 | `payments` | 12/25/2019 - 12/27/2019 | extracted=18799.08  expected=None |
| 44 | `balance` | 12/25/2019 - 12/27/2019 | extracted=0.0  expected=18799.08  diff=18799.08 |
| 44 | `provider` | 12/25/2019 - 12/27/2019 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 44 | `insurers` | 12/25/2019 - 12/27/2019 | missing=['medicaid'] |
| 44 | `description` | 12/25/2019 - 12/27/2019 | extracted='Diagnosis: Alcohol withdrawal syndrome'  expected='Alcohol withdrawal syndrome' |
| 45 | `payments` | 01/01/2019 - 01/08/2019 | extracted=13491.95  expected=None |
| 45 | `balance` | 01/01/2019 - 01/08/2019 | extracted=0.0  expected=13491.95  diff=13491.95 |
| 45 | `provider` | 01/01/2019 - 01/08/2019 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 45 | `insurers` | 01/01/2019 - 01/08/2019 | missing=['medicaid'] |
| 45 | `description` | 01/01/2019 - 01/08/2019 | extracted='Diagnosis: Urinary tract infection'  expected='Urinary tract infection' |
| 46 | `payments` | 10/11/2023 - 10/14/2023 | extracted=17934.49  expected=None |
| 46 | `balance` | 10/11/2023 - 10/14/2023 | extracted=0.0  expected=17934.49  diff=17934.49 |
| 46 | `provider` | 10/11/2023 - 10/14/2023 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 46 | `insurers` | 10/11/2023 - 10/14/2023 | missing=['medicaid'] |
| 46 | `description` | 10/11/2023 - 10/14/2023 | extracted='Diagnosis: Gastrointestinal hemorrhage'  expected='Gastrointestinal hemorrhage' |
| 47 | `payments` | 05/04/2021 - 05/06/2021 | extracted=21407.0  expected=None |
| 47 | `balance` | 05/04/2021 - 05/06/2021 | extracted=0.0  expected=21407.0  diff=21407.00 |
| 47 | `provider` | 05/04/2021 - 05/06/2021 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 47 | `insurers` | 05/04/2021 - 05/06/2021 | missing=['medicaid'] |
| 47 | `description` | 05/04/2021 - 05/06/2021 | extracted='Diagnosis: Acute pancreatitis'  expected='Acute pancreatitis' |
| 48 | `payments` | 09/10/2017 - 09/14/2017 | extracted=14044.89  expected=None |
| 48 | `balance` | 09/10/2017 - 09/14/2017 | extracted=0.0  expected=14044.89  diff=14044.89 |
| 48 | `provider` | 09/10/2017 - 09/14/2017 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 48 | `insurers` | 09/10/2017 - 09/14/2017 | missing=['medicaid'] |
| 48 | `description` | 09/10/2017 - 09/14/2017 | extracted='Diagnosis: Heart failure, unspecified'  expected='Heart failure, unspecified' |
| 49 | `payments` | 07/08/2022 - 07/10/2022 | extracted=19341.42  expected=None |
| 49 | `balance` | 07/08/2022 - 07/10/2022 | extracted=0.0  expected=19341.42  diff=19341.42 |
| 49 | `provider` | 07/08/2022 - 07/10/2022 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 49 | `insurers` | 07/08/2022 - 07/10/2022 | missing=['medicaid'] |
| 49 | `description` | 07/08/2022 - 07/10/2022 | extracted='Diagnosis: Heart failure, unspecified'  expected='Heart failure, unspecified' |
| 50 | `total_charges` | 08/08/2022 - 08/12/2022 | extracted=None  expected=251492.85 |
| 50 | `ins_paid` | 08/08/2022 - 08/12/2022 | extracted=None  expected=121309.78 |
| 50 | `adjustment` | 08/08/2022 - 08/12/2022 | extracted=None  expected=114137.83 |
| 50 | `balance` | 08/08/2022 - 08/12/2022 | extracted=None  expected=16045.24 |
| 50 | `provider` | 08/08/2022 - 08/12/2022 | extracted='Unknown Hospital'  expected='South Patrickmouth General Hospital' |
| 50 | `insurers` | 08/08/2022 - 08/12/2022 | missing=['medicaid'] |
| 50 | `description` | 08/08/2022 - 08/12/2022 | extracted='Diagnosis: Urinary tract infection'  expected='Urinary tract infection' |
| 51 | `total_charges` | 08/05/2023 - 08/11/2023 | extracted=251492.85  expected=388757.26  diff=137264.41 |
| 51 | `ins_paid` | 08/05/2023 - 08/11/2023 | extracted=121309.78  expected=187520.48  diff=66210.70 |
| 51 | `adjustment` | 08/05/2023 - 08/11/2023 | extracted=114137.83  expected=176434.07  diff=62296.24 |
| 51 | `payments` | 08/05/2023 - 08/11/2023 | extracted=16045.24  expected=None |
| 51 | `balance` | 08/05/2023 - 08/11/2023 | extracted=0.0  expected=24802.71  diff=24802.71 |
| 51 | `provider` | 08/05/2023 - 08/11/2023 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 51 | `insurers` | 08/05/2023 - 08/11/2023 | missing=['medicaid'] |
| 52 | `total_charges` | 02/23/2020 - 02/28/2020 | extracted=388757.26  expected=208128.86  diff=180628.40 |
| 52 | `ins_paid` | 02/23/2020 - 02/28/2020 | extracted=187520.48  expected=100392.78  diff=87127.70 |
| 52 | `adjustment` | 02/23/2020 - 02/28/2020 | extracted=176434.07  expected=94457.46  diff=81976.61 |
| 52 | `payments` | 02/23/2020 - 02/28/2020 | extracted=24802.71  expected=None |
| 52 | `balance` | 02/23/2020 - 02/28/2020 | extracted=0.0  expected=13278.62  diff=13278.62 |
| 52 | `provider` | 02/23/2020 - 02/28/2020 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 52 | `insurers` | 02/23/2020 - 02/28/2020 | missing=['medicaid'] |
| 53 | `total_charges` | 03/12/2019 - 03/14/2019 | extracted=208128.86  expected=411876.7  diff=203747.84 |
| 53 | `ins_paid` | 03/12/2019 - 03/14/2019 | extracted=100392.78  expected=198672.34  diff=98279.56 |
| 53 | `adjustment` | 03/12/2019 - 03/14/2019 | extracted=94457.46  expected=186926.63  diff=92469.17 |
| 53 | `payments` | 03/12/2019 - 03/14/2019 | extracted=13278.62  expected=None |
| 53 | `balance` | 03/12/2019 - 03/14/2019 | extracted=0.0  expected=26277.73  diff=26277.73 |
| 53 | `provider` | 03/12/2019 - 03/14/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 53 | `insurers` | 03/12/2019 - 03/14/2019 | missing=['medicaid'] |
| 54 | `total_charges` | 12/20/2021 - 12/27/2021 | extracted=411876.7  expected=321766.43  diff=90110.27 |
| 54 | `ins_paid` | 12/20/2021 - 12/27/2021 | extracted=198672.34  expected=155206.86  diff=43465.48 |
| 54 | `adjustment` | 12/20/2021 - 12/27/2021 | extracted=186926.63  expected=146030.87  diff=40895.76 |
| 54 | `payments` | 12/20/2021 - 12/27/2021 | extracted=26277.73  expected=None |
| 54 | `balance` | 12/20/2021 - 12/27/2021 | extracted=0.0  expected=20528.7  diff=20528.70 |
| 54 | `provider` | 12/20/2021 - 12/27/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 54 | `insurers` | 12/20/2021 - 12/27/2021 | missing=['medicaid'] |
| 55 | `total_charges` | 10/15/2020 - 10/16/2020 | extracted=321766.43  expected=282145.91  diff=39620.52 |
| 55 | `ins_paid` | 10/15/2020 - 10/16/2020 | extracted=155206.86  expected=136095.56  diff=19111.30 |
| 55 | `adjustment` | 10/15/2020 - 10/16/2020 | extracted=146030.87  expected=128049.44  diff=17981.43 |
| 55 | `payments` | 10/15/2020 - 10/16/2020 | extracted=20528.7  expected=None |
| 55 | `balance` | 10/15/2020 - 10/16/2020 | extracted=0.0  expected=18000.91  diff=18000.91 |
| 55 | `provider` | 10/15/2020 - 10/16/2020 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 55 | `insurers` | 10/15/2020 - 10/16/2020 | missing=['medicaid'] |
| 56 | `total_charges` | 12/10/2021 - 12/12/2021 | extracted=282145.91  expected=332446.67  diff=50300.76 |
| 56 | `ins_paid` | 12/10/2021 - 12/12/2021 | extracted=136095.56  expected=160358.57  diff=24263.01 |
| 56 | `adjustment` | 12/10/2021 - 12/12/2021 | extracted=128049.44  expected=150878.0  diff=22828.56 |
| 56 | `payments` | 12/10/2021 - 12/12/2021 | extracted=18000.91  expected=None |
| 56 | `balance` | 12/10/2021 - 12/12/2021 | extracted=0.0  expected=21210.1  diff=21210.10 |
| 56 | `provider` | 12/10/2021 - 12/12/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 56 | `insurers` | 12/10/2021 - 12/12/2021 | missing=['medicaid'] |
| 57 | `total_charges` | 07/11/2019 - 07/12/2019 | extracted=332446.67  expected=407296.42  diff=74849.75 |
| 57 | `ins_paid` | 07/11/2019 - 07/12/2019 | extracted=160358.57  expected=196463.0  diff=36104.43 |
| 57 | `adjustment` | 07/11/2019 - 07/12/2019 | extracted=150878.0  expected=184847.91  diff=33969.91 |
| 57 | `payments` | 07/11/2019 - 07/12/2019 | extracted=21210.1  expected=None |
| 57 | `balance` | 07/11/2019 - 07/12/2019 | extracted=0.0  expected=25985.51  diff=25985.51 |
| 57 | `provider` | 07/11/2019 - 07/12/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 57 | `insurers` | 07/11/2019 - 07/12/2019 | missing=['medicaid'] |
| 58 | `total_charges` | 01/27/2021 - 02/02/2021 | extracted=407296.42  expected=331797.33  diff=75499.09 |
| 58 | `ins_paid` | 01/27/2021 - 02/02/2021 | extracted=196463.0  expected=160045.35  diff=36417.65 |
| 58 | `adjustment` | 01/27/2021 - 02/02/2021 | extracted=184847.91  expected=150583.31  diff=34264.60 |
| 58 | `payments` | 01/27/2021 - 02/02/2021 | extracted=25985.51  expected=None |
| 58 | `balance` | 01/27/2021 - 02/02/2021 | extracted=0.0  expected=21168.67  diff=21168.67 |
| 58 | `provider` | 01/27/2021 - 02/02/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 58 | `insurers` | 01/27/2021 - 02/02/2021 | missing=['medicaid'] |
| 59 | `total_charges` | 10/15/2022 - 10/16/2022 | extracted=331797.33  expected=310963.97  diff=20833.36 |
| 59 | `ins_paid` | 10/15/2022 - 10/16/2022 | extracted=160045.35  expected=149996.2  diff=10049.15 |
| 59 | `adjustment` | 10/15/2022 - 10/16/2022 | extracted=150583.31  expected=141128.27  diff=9455.04 |
| 59 | `payments` | 10/15/2022 - 10/16/2022 | extracted=21168.67  expected=None |
| 59 | `balance` | 10/15/2022 - 10/16/2022 | extracted=0.0  expected=19839.5  diff=19839.50 |
| 59 | `provider` | 10/15/2022 - 10/16/2022 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 59 | `insurers` | 10/15/2022 - 10/16/2022 | missing=['medicaid'] |
| 60 | `total_charges` | 05/08/2017 - 05/10/2017 | extracted=310963.97  expected=393601.99  diff=82638.02 |
| 60 | `ins_paid` | 05/08/2017 - 05/10/2017 | extracted=149996.2  expected=189857.37  diff=39861.17 |
| 60 | `adjustment` | 05/08/2017 - 05/10/2017 | extracted=141128.27  expected=178632.81  diff=37504.54 |
| 60 | `payments` | 05/08/2017 - 05/10/2017 | extracted=19839.5  expected=None |
| 60 | `balance` | 05/08/2017 - 05/10/2017 | extracted=0.0  expected=25111.81  diff=25111.81 |
| 60 | `provider` | 05/08/2017 - 05/10/2017 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 60 | `insurers` | 05/08/2017 - 05/10/2017 | missing=['medicaid'] |
| 61 | `total_charges` | 01/26/2022 - 01/31/2022 | extracted=393601.99  expected=343860.84  diff=49741.15 |
| 61 | `ins_paid` | 01/26/2022 - 01/31/2022 | extracted=189857.37  expected=165864.29  diff=23993.08 |
| 61 | `adjustment` | 01/26/2022 - 01/31/2022 | extracted=178632.81  expected=156058.23  diff=22574.58 |
| 61 | `payments` | 01/26/2022 - 01/31/2022 | extracted=25111.81  expected=None |
| 61 | `balance` | 01/26/2022 - 01/31/2022 | extracted=0.0  expected=21938.32  diff=21938.32 |
| 61 | `provider` | 01/26/2022 - 01/31/2022 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 61 | `insurers` | 01/26/2022 - 01/31/2022 | missing=['medicaid'] |
| 62 | `total_charges` | 05/01/2024 - 05/02/2024 | extracted=343860.84  expected=349773.54  diff=5912.70 |
| 62 | `ins_paid` | 05/01/2024 - 05/02/2024 | extracted=165864.29  expected=168716.34  diff=2852.05 |
| 62 | `adjustment` | 05/01/2024 - 05/02/2024 | extracted=156058.23  expected=158741.65  diff=2683.42 |
| 62 | `payments` | 05/01/2024 - 05/02/2024 | extracted=21938.32  expected=None |
| 62 | `balance` | 05/01/2024 - 05/02/2024 | extracted=0.0  expected=22315.55  diff=22315.55 |
| 62 | `provider` | 05/01/2024 - 05/02/2024 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 62 | `insurers` | 05/01/2024 - 05/02/2024 | missing=['medicaid'] |
| 63 | `total_charges` | 04/07/2017 - 04/11/2017 | extracted=349773.54  expected=263607.14  diff=86166.40 |
| 63 | `ins_paid` | 04/07/2017 - 04/11/2017 | extracted=168716.34  expected=127153.22  diff=41563.12 |
| 63 | `adjustment` | 04/07/2017 - 04/11/2017 | extracted=158741.65  expected=119635.78  diff=39105.87 |
| 63 | `payments` | 04/07/2017 - 04/11/2017 | extracted=22315.55  expected=None |
| 63 | `balance` | 04/07/2017 - 04/11/2017 | extracted=0.0  expected=16818.14  diff=16818.14 |
| 63 | `provider` | 04/07/2017 - 04/11/2017 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 63 | `insurers` | 04/07/2017 - 04/11/2017 | missing=['medicaid'] |
| 64 | `total_charges` | 03/27/2024 - 04/03/2024 | extracted=263607.14  expected=321676.6  diff=58069.46 |
| 64 | `ins_paid` | 03/27/2024 - 04/03/2024 | extracted=127153.22  expected=155163.53  diff=28010.31 |
| 64 | `adjustment` | 03/27/2024 - 04/03/2024 | extracted=119635.78  expected=145990.1  diff=26354.32 |
| 64 | `payments` | 03/27/2024 - 04/03/2024 | extracted=16818.14  expected=None |
| 64 | `balance` | 03/27/2024 - 04/03/2024 | extracted=0.0  expected=20522.97  diff=20522.97 |
| 64 | `provider` | 03/27/2024 - 04/03/2024 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 64 | `insurers` | 03/27/2024 - 04/03/2024 | missing=['medicaid'] |
| 65 | `total_charges` | 10/03/2019 - 10/08/2019 | extracted=321676.6  expected=209060.97  diff=112615.63 |
| 65 | `ins_paid` | 10/03/2019 - 10/08/2019 | extracted=155163.53  expected=100842.39  diff=54321.14 |
| 65 | `adjustment` | 10/03/2019 - 10/08/2019 | extracted=145990.1  expected=94880.49  diff=51109.61 |
| 65 | `payments` | 10/03/2019 - 10/08/2019 | extracted=20522.97  expected=None |
| 65 | `balance` | 10/03/2019 - 10/08/2019 | extracted=0.0  expected=13338.09  diff=13338.09 |
| 65 | `provider` | 10/03/2019 - 10/08/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 65 | `insurers` | 10/03/2019 - 10/08/2019 | missing=['medicaid'] |
| 66 | `total_charges` | 05/05/2024 - 05/12/2024 | extracted=209060.97  expected=389096.76  diff=180035.79 |
| 66 | `ins_paid` | 05/05/2024 - 05/12/2024 | extracted=100842.39  expected=187684.24  diff=86841.85 |
| 66 | `adjustment` | 05/05/2024 - 05/12/2024 | extracted=94880.49  expected=176588.15  diff=81707.66 |
| 66 | `payments` | 05/05/2024 - 05/12/2024 | extracted=13338.09  expected=None |
| 66 | `balance` | 05/05/2024 - 05/12/2024 | extracted=0.0  expected=24824.37  diff=24824.37 |
| 66 | `provider` | 05/05/2024 - 05/12/2024 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 66 | `insurers` | 05/05/2024 - 05/12/2024 | missing=['medicaid'] |
| 67 | `total_charges` | 03/30/2021 - 04/01/2021 | extracted=389096.76  expected=362095.41  diff=27001.35 |
| 67 | `ins_paid` | 03/30/2021 - 04/01/2021 | extracted=187684.24  expected=174659.9  diff=13024.34 |
| 67 | `adjustment` | 03/30/2021 - 04/01/2021 | extracted=176588.15  expected=164333.82  diff=12254.33 |
| 67 | `payments` | 03/30/2021 - 04/01/2021 | extracted=24824.37  expected=None |
| 67 | `balance` | 03/30/2021 - 04/01/2021 | extracted=0.0  expected=23101.69  diff=23101.69 |
| 67 | `provider` | 03/30/2021 - 04/01/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 67 | `insurers` | 03/30/2021 - 04/01/2021 | missing=['medicaid'] |
| 68 | `total_charges` | 02/03/2024 - 02/04/2024 | extracted=362095.41  expected=343185.37  diff=18910.04 |
| 68 | `ins_paid` | 02/03/2024 - 02/04/2024 | extracted=174659.9  expected=165538.48  diff=9121.42 |
| 68 | `adjustment` | 02/03/2024 - 02/04/2024 | extracted=164333.82  expected=155751.66  diff=8582.16 |
| 68 | `payments` | 02/03/2024 - 02/04/2024 | extracted=23101.69  expected=None |
| 68 | `balance` | 02/03/2024 - 02/04/2024 | extracted=0.0  expected=21895.23  diff=21895.23 |
| 68 | `provider` | 02/03/2024 - 02/04/2024 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 68 | `insurers` | 02/03/2024 - 02/04/2024 | missing=['medicaid'] |
| 69 | `total_charges` | 10/14/2017 - 10/20/2017 | extracted=343185.37  expected=175042.86  diff=168142.51 |
| 69 | `ins_paid` | 10/14/2017 - 10/20/2017 | extracted=165538.48  expected=84433.46  diff=81105.02 |
| 69 | `adjustment` | 10/14/2017 - 10/20/2017 | extracted=155751.66  expected=79441.67  diff=76309.99 |
| 69 | `payments` | 10/14/2017 - 10/20/2017 | extracted=21895.23  expected=None |
| 69 | `balance` | 10/14/2017 - 10/20/2017 | extracted=0.0  expected=11167.73  diff=11167.73 |
| 69 | `provider` | 10/14/2017 - 10/20/2017 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 69 | `insurers` | 10/14/2017 - 10/20/2017 | missing=['medicaid'] |
| 70 | `total_charges` | 08/14/2023 - 08/21/2023 | extracted=175042.86  expected=338905.9  diff=163863.04 |
| 70 | `ins_paid` | 08/14/2023 - 08/21/2023 | extracted=84433.46  expected=163474.24  diff=79040.78 |
| 70 | `adjustment` | 08/14/2023 - 08/21/2023 | extracted=79441.67  expected=153809.46  diff=74367.79 |
| 70 | `payments` | 08/14/2023 - 08/21/2023 | extracted=11167.73  expected=None |
| 70 | `balance` | 08/14/2023 - 08/21/2023 | extracted=0.0  expected=21622.2  diff=21622.20 |
| 70 | `provider` | 08/14/2023 - 08/21/2023 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 70 | `insurers` | 08/14/2023 - 08/21/2023 | missing=['medicaid'] |
| 71 | `total_charges` | 09/29/2023 - 10/06/2023 | extracted=338905.9  expected=367146.88  diff=28240.98 |
| 71 | `ins_paid` | 09/29/2023 - 10/06/2023 | extracted=163474.24  expected=177096.52  diff=13622.28 |
| 71 | `adjustment` | 09/29/2023 - 10/06/2023 | extracted=153809.46  expected=166626.39  diff=12816.93 |
| 71 | `payments` | 09/29/2023 - 10/06/2023 | extracted=21622.2  expected=None |
| 71 | `balance` | 09/29/2023 - 10/06/2023 | extracted=0.0  expected=23423.97  diff=23423.97 |
| 71 | `provider` | 09/29/2023 - 10/06/2023 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 71 | `insurers` | 09/29/2023 - 10/06/2023 | missing=['medicaid'] |
| 72 | `total_charges` | 03/10/2019 - 03/15/2019 | extracted=367146.88  expected=385904.85  diff=18757.97 |
| 72 | `ins_paid` | 03/10/2019 - 03/15/2019 | extracted=177096.52  expected=186144.59  diff=9048.07 |
| 72 | `adjustment` | 03/10/2019 - 03/15/2019 | extracted=166626.39  expected=175139.53  diff=8513.14 |
| 72 | `payments` | 03/10/2019 - 03/15/2019 | extracted=23423.97  expected=None |
| 72 | `balance` | 03/10/2019 - 03/15/2019 | extracted=0.0  expected=24620.73  diff=24620.73 |
| 72 | `provider` | 03/10/2019 - 03/15/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 72 | `insurers` | 03/10/2019 - 03/15/2019 | missing=['medicaid'] |
| 73 | `total_charges` | 11/01/2020 - 11/03/2020 | extracted=385904.85  expected=204720.12  diff=181184.73 |
| 73 | `ins_paid` | 11/01/2020 - 11/03/2020 | extracted=186144.59  expected=98748.55  diff=87396.04 |
| 73 | `adjustment` | 11/01/2020 - 11/03/2020 | extracted=175139.53  expected=92910.43  diff=82229.10 |
| 73 | `payments` | 11/01/2020 - 11/03/2020 | extracted=24620.73  expected=None |
| 73 | `balance` | 11/01/2020 - 11/03/2020 | extracted=0.0  expected=13061.14  diff=13061.14 |
| 73 | `provider` | 11/01/2020 - 11/03/2020 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 73 | `insurers` | 11/01/2020 - 11/03/2020 | missing=['medicaid'] |
| 74 | `payments` | 09/22/2018 - 09/24/2018 | extracted=24105.48  expected=None |
| 74 | `balance` | 09/22/2018 - 09/24/2018 | extracted=0.0  expected=24105.48  diff=24105.48 |
| 74 | `provider` | 09/22/2018 - 09/24/2018 | extracted=''  expected='South Patrickmouth General Hospital' |
| 74 | `insurers` | 09/22/2018 - 09/24/2018 | missing=['medicaid'] |
| 75 | `payments` | 02/26/2021 - 03/05/2021 | extracted=18867.13  expected=None |
| 75 | `balance` | 02/26/2021 - 03/05/2021 | extracted=0.0  expected=18867.13  diff=18867.13 |
| 75 | `provider` | 02/26/2021 - 03/05/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 75 | `insurers` | 02/26/2021 - 03/05/2021 | missing=['medicaid'] |
| 76 | `payments` | 06/11/2021 - 06/17/2021 | extracted=20616.64  expected=None |
| 76 | `balance` | 06/11/2021 - 06/17/2021 | extracted=0.0  expected=20616.64  diff=20616.64 |
| 76 | `provider` | 06/11/2021 - 06/17/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 76 | `insurers` | 06/11/2021 - 06/17/2021 | missing=['medicaid'] |
| 77 | `payments` | 04/05/2018 - 04/07/2018 | extracted=21750.44  expected=None |
| 77 | `balance` | 04/05/2018 - 04/07/2018 | extracted=0.0  expected=21750.44  diff=21750.44 |
| 77 | `provider` | 04/05/2018 - 04/07/2018 | extracted=''  expected='South Patrickmouth General Hospital' |
| 77 | `insurers` | 04/05/2018 - 04/07/2018 | missing=['medicaid'] |
| 78 | `payments` | 12/17/2018 - 12/23/2018 | extracted=19797.34  expected=None |
| 78 | `balance` | 12/17/2018 - 12/23/2018 | extracted=0.0  expected=19797.34  diff=19797.34 |
| 78 | `provider` | 12/17/2018 - 12/23/2018 | extracted=''  expected='South Patrickmouth General Hospital' |
| 78 | `insurers` | 12/17/2018 - 12/23/2018 | missing=['medicaid'] |
| 79 | `payments` | 03/12/2019 - 03/15/2019 | extracted=21595.04  expected=None |
| 79 | `balance` | 03/12/2019 - 03/15/2019 | extracted=0.0  expected=21595.04  diff=21595.04 |
| 79 | `provider` | 03/12/2019 - 03/15/2019 | extracted=''  expected='South Patrickmouth General Hospital' |
| 79 | `insurers` | 03/12/2019 - 03/15/2019 | missing=['medicaid'] |
| 80 | `payments` | 06/18/2020 - 06/20/2020 | extracted=20592.69  expected=None |
| 80 | `balance` | 06/18/2020 - 06/20/2020 | extracted=0.0  expected=20592.69  diff=20592.69 |
| 80 | `provider` | 06/18/2020 - 06/20/2020 | extracted=''  expected='South Patrickmouth General Hospital' |
| 80 | `insurers` | 06/18/2020 - 06/20/2020 | missing=['medicaid'] |
| 81 | `payments` | 03/13/2024 - 03/15/2024 | extracted=21689.11  expected=None |
| 81 | `balance` | 03/13/2024 - 03/15/2024 | extracted=0.0  expected=21689.11  diff=21689.11 |
| 81 | `provider` | 03/13/2024 - 03/15/2024 | extracted=''  expected='South Patrickmouth General Hospital' |
| 81 | `insurers` | 03/13/2024 - 03/15/2024 | missing=['medicaid'] |
| 82 | `payments` | 06/20/2020 - 06/27/2020 | extracted=20879.61  expected=None |
| 82 | `balance` | 06/20/2020 - 06/27/2020 | extracted=0.0  expected=20879.61  diff=20879.61 |
| 82 | `provider` | 06/20/2020 - 06/27/2020 | extracted=''  expected='South Patrickmouth General Hospital' |
| 82 | `insurers` | 06/20/2020 - 06/27/2020 | missing=['medicaid'] |
| 83 | `payments` | 01/12/2017 - 01/13/2017 | extracted=21751.41  expected=None |
| 83 | `balance` | 01/12/2017 - 01/13/2017 | extracted=0.0  expected=21751.41  diff=21751.41 |
| 83 | `provider` | 01/12/2017 - 01/13/2017 | extracted=''  expected='South Patrickmouth General Hospital' |
| 83 | `insurers` | 01/12/2017 - 01/13/2017 | missing=['medicaid'] |
| 84 | `payments` | 06/17/2020 - 06/21/2020 | extracted=31034.51  expected=None |
| 84 | `balance` | 06/17/2020 - 06/21/2020 | extracted=0.0  expected=31034.51  diff=31034.51 |
| 84 | `provider` | 06/17/2020 - 06/21/2020 | extracted=''  expected='South Patrickmouth General Hospital' |
| 84 | `insurers` | 06/17/2020 - 06/21/2020 | missing=['medicaid'] |
| 85 | `payments` | 02/24/2019 - 02/28/2019 | extracted=14609.98  expected=None |
| 85 | `balance` | 02/24/2019 - 02/28/2019 | extracted=0.0  expected=14609.98  diff=14609.98 |
| 85 | `provider` | 02/24/2019 - 02/28/2019 | extracted=''  expected='South Patrickmouth General Hospital' |
| 85 | `insurers` | 02/24/2019 - 02/28/2019 | missing=['medicaid'] |
| 86 | `payments` | 02/06/2017 - 02/11/2017 | extracted=18635.03  expected=None |
| 86 | `balance` | 02/06/2017 - 02/11/2017 | extracted=0.0  expected=18635.03  diff=18635.03 |
| 86 | `provider` | 02/06/2017 - 02/11/2017 | extracted=''  expected='South Patrickmouth General Hospital' |
| 86 | `insurers` | 02/06/2017 - 02/11/2017 | missing=['medicaid'] |
| 87 | `payments` | 11/26/2021 - 11/28/2021 | extracted=26884.97  expected=None |
| 87 | `balance` | 11/26/2021 - 11/28/2021 | extracted=0.0  expected=26884.97  diff=26884.97 |
| 87 | `provider` | 11/26/2021 - 11/28/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 87 | `insurers` | 11/26/2021 - 11/28/2021 | missing=['medicaid'] |
| 88 | `payments` | 12/07/2021 - 12/14/2021 | extracted=21602.65  expected=None |
| 88 | `balance` | 12/07/2021 - 12/14/2021 | extracted=0.0  expected=21602.65  diff=21602.65 |
| 88 | `provider` | 12/07/2021 - 12/14/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 88 | `insurers` | 12/07/2021 - 12/14/2021 | missing=['medicaid'] |
| 89 | `payments` | 12/16/2024 - 12/17/2024 | extracted=14246.55  expected=None |
| 89 | `balance` | 12/16/2024 - 12/17/2024 | extracted=0.0  expected=14246.55  diff=14246.55 |
| 89 | `provider` | 12/16/2024 - 12/17/2024 | extracted=''  expected='South Patrickmouth General Hospital' |
| 89 | `insurers` | 12/16/2024 - 12/17/2024 | missing=['medicaid'] |
| 90 | `payments` | 09/16/2022 - 09/20/2022 | extracted=11491.79  expected=None |
| 90 | `balance` | 09/16/2022 - 09/20/2022 | extracted=0.0  expected=11491.79  diff=11491.79 |
| 90 | `provider` | 09/16/2022 - 09/20/2022 | extracted=''  expected='South Patrickmouth General Hospital' |
| 90 | `insurers` | 09/16/2022 - 09/20/2022 | missing=['medicaid'] |
| 91 | `payments` | 11/20/2022 - 11/21/2022 | extracted=24740.24  expected=None |
| 91 | `balance` | 11/20/2022 - 11/21/2022 | extracted=0.0  expected=24740.24  diff=24740.24 |
| 91 | `provider` | 11/20/2022 - 11/21/2022 | extracted=''  expected='South Patrickmouth General Hospital' |
| 91 | `insurers` | 11/20/2022 - 11/21/2022 | missing=['medicaid'] |
| 92 | `payments` | 09/16/2020 - 09/22/2020 | extracted=13196.5  expected=None |
| 92 | `balance` | 09/16/2020 - 09/22/2020 | extracted=0.0  expected=13196.5  diff=13196.50 |
| 92 | `provider` | 09/16/2020 - 09/22/2020 | extracted=''  expected='South Patrickmouth General Hospital' |
| 92 | `insurers` | 09/16/2020 - 09/22/2020 | missing=['medicaid'] |
| 93 | `payments` | 11/28/2023 - 11/30/2023 | extracted=16576.05  expected=None |
| 93 | `balance` | 11/28/2023 - 11/30/2023 | extracted=0.0  expected=16576.05  diff=16576.05 |
| 93 | `provider` | 11/28/2023 - 11/30/2023 | extracted=''  expected='South Patrickmouth General Hospital' |
| 93 | `insurers` | 11/28/2023 - 11/30/2023 | missing=['medicaid'] |
| 94 | `payments` | 09/03/2023 - 09/06/2023 | extracted=12828.97  expected=None |
| 94 | `balance` | 09/03/2023 - 09/06/2023 | extracted=0.0  expected=12828.97  diff=12828.97 |
| 94 | `provider` | 09/03/2023 - 09/06/2023 | extracted=''  expected='South Patrickmouth General Hospital' |
| 94 | `insurers` | 09/03/2023 - 09/06/2023 | missing=['medicaid'] |
| 95 | `payments` | 09/25/2024 - 10/01/2024 | extracted=14703.7  expected=None |
| 95 | `balance` | 09/25/2024 - 10/01/2024 | extracted=0.0  expected=14703.7  diff=14703.70 |
| 95 | `provider` | 09/25/2024 - 10/01/2024 | extracted=''  expected='South Patrickmouth General Hospital' |
| 95 | `insurers` | 09/25/2024 - 10/01/2024 | missing=['medicaid'] |
| 96 | `payments` | 06/18/2019 - 06/20/2019 | extracted=24040.21  expected=None |
| 96 | `balance` | 06/18/2019 - 06/20/2019 | extracted=0.0  expected=24040.21  diff=24040.21 |
| 96 | `provider` | 06/18/2019 - 06/20/2019 | extracted=''  expected='South Patrickmouth General Hospital' |
| 96 | `insurers` | 06/18/2019 - 06/20/2019 | missing=['medicaid'] |
| 97 | `payments` | 07/26/2019 - 08/01/2019 | extracted=13636.3  expected=None |
| 97 | `balance` | 07/26/2019 - 08/01/2019 | extracted=0.0  expected=13636.3  diff=13636.30 |
| 97 | `provider` | 07/26/2019 - 08/01/2019 | extracted=''  expected='South Patrickmouth General Hospital' |
| 97 | `insurers` | 07/26/2019 - 08/01/2019 | missing=['medicaid'] |
| 98 | `payments` | 01/15/2019 - 01/17/2019 | extracted=14460.88  expected=None |
| 98 | `balance` | 01/15/2019 - 01/17/2019 | extracted=0.0  expected=14460.88  diff=14460.88 |
| 98 | `provider` | 01/15/2019 - 01/17/2019 | extracted=''  expected='South Patrickmouth General Hospital' |
| 98 | `insurers` | 01/15/2019 - 01/17/2019 | missing=['medicaid'] |
| 99 | `payments` | 03/03/2023 - 03/06/2023 | extracted=12038.18  expected=None |
| 99 | `balance` | 03/03/2023 - 03/06/2023 | extracted=0.0  expected=12038.18  diff=12038.18 |
| 99 | `provider` | 03/03/2023 - 03/06/2023 | extracted=''  expected='South Patrickmouth General Hospital' |
| 99 | `insurers` | 03/03/2023 - 03/06/2023 | missing=['medicaid'] |
| 100 | `payments` | 11/30/2021 - 12/02/2021 | extracted=17788.93  expected=None |
| 100 | `balance` | 11/30/2021 - 12/02/2021 | extracted=0.0  expected=17788.93  diff=17788.93 |
| 100 | `provider` | 11/30/2021 - 12/02/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 100 | `insurers` | 11/30/2021 - 12/02/2021 | missing=['medicaid'] |
| 101 | `payments` | 06/27/2021 - 07/02/2021 | extracted=16844.11  expected=None |
| 101 | `balance` | 06/27/2021 - 07/02/2021 | extracted=0.0  expected=16844.11  diff=16844.11 |
| 101 | `provider` | 06/27/2021 - 07/02/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 101 | `insurers` | 06/27/2021 - 07/02/2021 | missing=['medicaid'] |
| 102 | `payments` | 06/16/2019 - 06/22/2019 | extracted=16690.62  expected=None |
| 102 | `balance` | 06/16/2019 - 06/22/2019 | extracted=0.0  expected=16690.62  diff=16690.62 |
| 102 | `provider` | 06/16/2019 - 06/22/2019 | extracted=''  expected='South Patrickmouth General Hospital' |
| 102 | `insurers` | 06/16/2019 - 06/22/2019 | missing=['medicaid'] |
| 103 | `payments` | 01/09/2024 - 01/12/2024 | extracted=23049.57  expected=None |
| 103 | `balance` | 01/09/2024 - 01/12/2024 | extracted=0.0  expected=23049.57  diff=23049.57 |
| 103 | `provider` | 01/09/2024 - 01/12/2024 | extracted=''  expected='South Patrickmouth General Hospital' |
| 103 | `insurers` | 01/09/2024 - 01/12/2024 | missing=['medicaid'] |
| 104 | `payments` | 10/25/2020 - 10/29/2020 | extracted=24173.12  expected=None |
| 104 | `balance` | 10/25/2020 - 10/29/2020 | extracted=0.0  expected=24173.12  diff=24173.12 |
| 104 | `provider` | 10/25/2020 - 10/29/2020 | extracted=''  expected='South Patrickmouth General Hospital' |
| 104 | `insurers` | 10/25/2020 - 10/29/2020 | missing=['medicaid'] |
| 105 | `payments` | 07/30/2021 - 08/02/2021 | extracted=17809.21  expected=None |
| 105 | `balance` | 07/30/2021 - 08/02/2021 | extracted=0.0  expected=17809.21  diff=17809.21 |
| 105 | `provider` | 07/30/2021 - 08/02/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 105 | `insurers` | 07/30/2021 - 08/02/2021 | missing=['medicaid'] |
| 106 | `payments` | 09/09/2021 - 09/15/2021 | extracted=18205.45  expected=None |
| 106 | `balance` | 09/09/2021 - 09/15/2021 | extracted=0.0  expected=18205.45  diff=18205.45 |
| 106 | `provider` | 09/09/2021 - 09/15/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 106 | `insurers` | 09/09/2021 - 09/15/2021 | missing=['medicaid'] |
| 107 | `payments` | 03/20/2020 - 03/27/2020 | extracted=16690.52  expected=None |
| 107 | `balance` | 03/20/2020 - 03/27/2020 | extracted=0.0  expected=16690.52  diff=16690.52 |
| 107 | `provider` | 03/20/2020 - 03/27/2020 | extracted=''  expected='South Patrickmouth General Hospital' |
| 107 | `insurers` | 03/20/2020 - 03/27/2020 | missing=['medicaid'] |
| 108 | `payments` | 08/28/2017 - 09/04/2017 | extracted=16937.63  expected=None |
| 108 | `balance` | 08/28/2017 - 09/04/2017 | extracted=0.0  expected=16937.63  diff=16937.63 |
| 108 | `provider` | 08/28/2017 - 09/04/2017 | extracted=''  expected='South Patrickmouth General Hospital' |
| 108 | `insurers` | 08/28/2017 - 09/04/2017 | missing=['medicaid'] |
| 109 | `payments` | 02/10/2023 - 02/16/2023 | extracted=14340.9  expected=None |
| 109 | `balance` | 02/10/2023 - 02/16/2023 | extracted=0.0  expected=14340.9  diff=14340.90 |
| 109 | `provider` | 02/10/2023 - 02/16/2023 | extracted=''  expected='South Patrickmouth General Hospital' |
| 109 | `insurers` | 02/10/2023 - 02/16/2023 | missing=['medicaid'] |
| 110 | `payments` | 06/24/2018 - 06/26/2018 | extracted=27717.87  expected=None |
| 110 | `balance` | 06/24/2018 - 06/26/2018 | extracted=0.0  expected=27717.87  diff=27717.87 |
| 110 | `provider` | 06/24/2018 - 06/26/2018 | extracted=''  expected='South Patrickmouth General Hospital' |
| 110 | `insurers` | 06/24/2018 - 06/26/2018 | missing=['medicaid'] |
| 111 | `payments` | 04/12/2021 - 04/15/2021 | extracted=19186.73  expected=None |
| 111 | `balance` | 04/12/2021 - 04/15/2021 | extracted=0.0  expected=19186.73  diff=19186.73 |
| 111 | `provider` | 04/12/2021 - 04/15/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 111 | `insurers` | 04/12/2021 - 04/15/2021 | missing=['medicaid'] |
| 112 | `payments` | 02/22/2023 - 03/01/2023 | extracted=17922.72  expected=None |
| 112 | `balance` | 02/22/2023 - 03/01/2023 | extracted=0.0  expected=17922.72  diff=17922.72 |
| 112 | `provider` | 02/22/2023 - 03/01/2023 | extracted=''  expected='South Patrickmouth General Hospital' |
| 112 | `insurers` | 02/22/2023 - 03/01/2023 | missing=['medicaid'] |
| 113 | `payments` | 07/28/2021 - 07/29/2021 | extracted=23832.03  expected=None |
| 113 | `balance` | 07/28/2021 - 07/29/2021 | extracted=0.0  expected=23832.03  diff=23832.03 |
| 113 | `provider` | 07/28/2021 - 07/29/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 113 | `insurers` | 07/28/2021 - 07/29/2021 | missing=['medicaid'] |
| 114 | `payments` | 11/22/2022 - 11/26/2022 | extracted=14456.75  expected=None |
| 114 | `balance` | 11/22/2022 - 11/26/2022 | extracted=0.0  expected=14456.75  diff=14456.75 |
| 114 | `provider` | 11/22/2022 - 11/26/2022 | extracted=''  expected='South Patrickmouth General Hospital' |
| 114 | `insurers` | 11/22/2022 - 11/26/2022 | missing=['medicaid'] |
| 115 | `payments` | 01/11/2024 - 01/18/2024 | extracted=25476.06  expected=None |
| 115 | `balance` | 01/11/2024 - 01/18/2024 | extracted=0.0  expected=25476.06  diff=25476.06 |
| 115 | `provider` | 01/11/2024 - 01/18/2024 | extracted=''  expected='South Patrickmouth General Hospital' |
| 115 | `insurers` | 01/11/2024 - 01/18/2024 | missing=['medicaid'] |
| 116 | `payments` | 02/07/2022 - 02/14/2022 | extracted=19978.54  expected=None |
| 116 | `balance` | 02/07/2022 - 02/14/2022 | extracted=0.0  expected=19978.54  diff=19978.54 |
| 116 | `provider` | 02/07/2022 - 02/14/2022 | extracted=''  expected='South Patrickmouth General Hospital' |
| 116 | `insurers` | 02/07/2022 - 02/14/2022 | missing=['medicaid'] |
| 117 | `payments` | 04/27/2023 - 05/02/2023 | extracted=20147.44  expected=None |
| 117 | `balance` | 04/27/2023 - 05/02/2023 | extracted=0.0  expected=20147.44  diff=20147.44 |
| 117 | `provider` | 04/27/2023 - 05/02/2023 | extracted=''  expected='South Patrickmouth General Hospital' |
| 117 | `insurers` | 04/27/2023 - 05/02/2023 | missing=['medicaid'] |
| 118 | `payments` | 12/15/2018 - 12/17/2018 | extracted=20740.83  expected=None |
| 118 | `balance` | 12/15/2018 - 12/17/2018 | extracted=0.0  expected=20740.83  diff=20740.83 |
| 118 | `provider` | 12/15/2018 - 12/17/2018 | extracted=''  expected='South Patrickmouth General Hospital' |
| 118 | `insurers` | 12/15/2018 - 12/17/2018 | missing=['medicaid'] |
| 119 | `payments` | 09/06/2017 - 09/10/2017 | extracted=17070.82  expected=None |
| 119 | `balance` | 09/06/2017 - 09/10/2017 | extracted=0.0  expected=17070.82  diff=17070.82 |
| 119 | `provider` | 09/06/2017 - 09/10/2017 | extracted=''  expected='South Patrickmouth General Hospital' |
| 119 | `insurers` | 09/06/2017 - 09/10/2017 | missing=['medicaid'] |
| 120 | `payments` | 01/16/2024 - 01/21/2024 | extracted=16253.14  expected=None |
| 120 | `balance` | 01/16/2024 - 01/21/2024 | extracted=0.0  expected=16253.14  diff=16253.14 |
| 120 | `provider` | 01/16/2024 - 01/21/2024 | extracted=''  expected='South Patrickmouth General Hospital' |
| 120 | `insurers` | 01/16/2024 - 01/21/2024 | missing=['medicaid'] |
| 121 | `payments` | 07/17/2018 - 07/22/2018 | extracted=22418.15  expected=None |
| 121 | `balance` | 07/17/2018 - 07/22/2018 | extracted=0.0  expected=22418.15  diff=22418.15 |
| 121 | `provider` | 07/17/2018 - 07/22/2018 | extracted=''  expected='South Patrickmouth General Hospital' |
| 121 | `insurers` | 07/17/2018 - 07/22/2018 | missing=['medicaid'] |
| 122 | `balance` | 04/28/2024 - 05/02/2024 | extracted=16473.04  expected=16373.04  diff=100.00 |
| 122 | `provider` | 04/28/2024 - 05/02/2024 | extracted=''  expected='South Patrickmouth General Hospital' |
| 122 | `insurers` | 04/28/2024 - 05/02/2024 | missing=['medicaid'] |
| 123 | `payments` | 10/06/2017 - 10/09/2017 | extracted=18940.85  expected=None |
| 123 | `balance` | 10/06/2017 - 10/09/2017 | extracted=0.0  expected=18940.85  diff=18940.85 |
| 123 | `provider` | 10/06/2017 - 10/09/2017 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 123 | `insurers` | 10/06/2017 - 10/09/2017 | missing=['medicaid'] |
| 124 | `payments` | 03/27/2020 - 03/30/2020 | extracted=13849.45  expected=None |
| 124 | `balance` | 03/27/2020 - 03/30/2020 | extracted=0.0  expected=13849.45  diff=13849.45 |
| 124 | `provider` | 03/27/2020 - 03/30/2020 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 124 | `insurers` | 03/27/2020 - 03/30/2020 | missing=['medicaid'] |
| 125 | `payments` | 08/22/2024 - 08/27/2024 | extracted=16978.46  expected=None |
| 125 | `balance` | 08/22/2024 - 08/27/2024 | extracted=0.0  expected=16978.46  diff=16978.46 |
| 125 | `provider` | 08/22/2024 - 08/27/2024 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 125 | `insurers` | 08/22/2024 - 08/27/2024 | missing=['medicaid'] |
| 126 | `payments` | 06/14/2021 - 06/17/2021 | extracted=17580.42  expected=None |
| 126 | `balance` | 06/14/2021 - 06/17/2021 | extracted=0.0  expected=17580.42  diff=17580.42 |
| 126 | `provider` | 06/14/2021 - 06/17/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 126 | `insurers` | 06/14/2021 - 06/17/2021 | missing=['medicaid'] |
| 127 | `payments` | 09/26/2021 - 10/03/2021 | extracted=23957.03  expected=None |
| 127 | `balance` | 09/26/2021 - 10/03/2021 | extracted=0.0  expected=23957.03  diff=23957.03 |
| 127 | `provider` | 09/26/2021 - 10/03/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 127 | `insurers` | 09/26/2021 - 10/03/2021 | missing=['medicaid'] |
| 128 | `payments` | 03/10/2019 - 03/13/2019 | extracted=27244.56  expected=None |
| 128 | `balance` | 03/10/2019 - 03/13/2019 | extracted=0.0  expected=27244.56  diff=27244.56 |
| 128 | `provider` | 03/10/2019 - 03/13/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 128 | `insurers` | 03/10/2019 - 03/13/2019 | missing=['medicaid'] |
| 129 | `payments` | 10/05/2021 - 10/11/2021 | extracted=20969.26  expected=None |
| 129 | `balance` | 10/05/2021 - 10/11/2021 | extracted=0.0  expected=20969.26  diff=20969.26 |
| 129 | `provider` | 10/05/2021 - 10/11/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 129 | `insurers` | 10/05/2021 - 10/11/2021 | missing=['medicaid'] |
| 130 | `payments` | 09/08/2024 - 09/14/2024 | extracted=17607.18  expected=None |
| 130 | `balance` | 09/08/2024 - 09/14/2024 | extracted=0.0  expected=17607.18  diff=17607.18 |
| 130 | `provider` | 09/08/2024 - 09/14/2024 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 130 | `insurers` | 09/08/2024 - 09/14/2024 | missing=['medicaid'] |
| 131 | `payments` | 05/12/2021 - 05/13/2021 | extracted=26994.56  expected=None |
| 131 | `balance` | 05/12/2021 - 05/13/2021 | extracted=0.0  expected=26994.56  diff=26994.56 |
| 131 | `provider` | 05/12/2021 - 05/13/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 131 | `insurers` | 05/12/2021 - 05/13/2021 | missing=['medicaid'] |
| 132 | `payments` | 08/31/2024 - 09/07/2024 | extracted=12335.79  expected=None |
| 132 | `balance` | 08/31/2024 - 09/07/2024 | extracted=0.0  expected=12335.79  diff=12335.79 |
| 132 | `provider` | 08/31/2024 - 09/07/2024 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 132 | `insurers` | 08/31/2024 - 09/07/2024 | missing=['medicaid'] |
| 133 | `payments` | 12/08/2019 - 12/12/2019 | extracted=15766.0  expected=None |
| 133 | `balance` | 12/08/2019 - 12/12/2019 | extracted=0.0  expected=15766.0  diff=15766.00 |
| 133 | `provider` | 12/08/2019 - 12/12/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 133 | `insurers` | 12/08/2019 - 12/12/2019 | missing=['medicaid'] |
| 134 | `payments` | 06/09/2020 - 06/10/2020 | extracted=16234.87  expected=None |
| 134 | `balance` | 06/09/2020 - 06/10/2020 | extracted=0.0  expected=16234.87  diff=16234.87 |
| 134 | `provider` | 06/09/2020 - 06/10/2020 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 134 | `insurers` | 06/09/2020 - 06/10/2020 | missing=['medicaid'] |
| 135 | `payments` | 07/11/2017 - 07/12/2017 | extracted=17480.88  expected=None |
| 135 | `balance` | 07/11/2017 - 07/12/2017 | extracted=0.0  expected=17480.88  diff=17480.88 |
| 135 | `provider` | 07/11/2017 - 07/12/2017 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 135 | `insurers` | 07/11/2017 - 07/12/2017 | missing=['medicaid'] |
| 136 | `payments` | 11/06/2019 - 11/07/2019 | extracted=18059.33  expected=None |
| 136 | `balance` | 11/06/2019 - 11/07/2019 | extracted=0.0  expected=18059.33  diff=18059.33 |
| 136 | `provider` | 11/06/2019 - 11/07/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 136 | `insurers` | 11/06/2019 - 11/07/2019 | missing=['medicaid'] |
| 137 | `payments` | 09/16/2021 - 09/17/2021 | extracted=12181.78  expected=None |
| 137 | `balance` | 09/16/2021 - 09/17/2021 | extracted=0.0  expected=12181.78  diff=12181.78 |
| 137 | `provider` | 09/16/2021 - 09/17/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 137 | `insurers` | 09/16/2021 - 09/17/2021 | missing=['medicaid'] |
| 138 | `payments` | 12/02/2017 - 12/08/2017 | extracted=24619.77  expected=None |
| 138 | `balance` | 12/02/2017 - 12/08/2017 | extracted=0.0  expected=24619.77  diff=24619.77 |
| 138 | `provider` | 12/02/2017 - 12/08/2017 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 138 | `insurers` | 12/02/2017 - 12/08/2017 | missing=['medicaid'] |
| 139 | `payments` | 05/29/2019 - 06/05/2019 | extracted=24879.46  expected=None |
| 139 | `balance` | 05/29/2019 - 06/05/2019 | extracted=0.0  expected=24879.46  diff=24879.46 |
| 139 | `provider` | 05/29/2019 - 06/05/2019 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 139 | `insurers` | 05/29/2019 - 06/05/2019 | missing=['medicaid'] |
| 140 | `payments` | 10/05/2018 - 10/08/2018 | extracted=21923.31  expected=None |
| 140 | `balance` | 10/05/2018 - 10/08/2018 | extracted=0.0  expected=21923.31  diff=21923.31 |
| 140 | `provider` | 10/05/2018 - 10/08/2018 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 140 | `insurers` | 10/05/2018 - 10/08/2018 | missing=['medicaid'] |
| 141 | `payments` | 05/25/2017 - 06/01/2017 | extracted=18647.34  expected=None |
| 141 | `balance` | 05/25/2017 - 06/01/2017 | extracted=0.0  expected=18647.34  diff=18647.34 |
| 141 | `provider` | 05/25/2017 - 06/01/2017 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 141 | `insurers` | 05/25/2017 - 06/01/2017 | missing=['medicaid'] |
| 142 | `payments` | 07/15/2022 - 07/16/2022 | extracted=24802.28  expected=None |
| 142 | `balance` | 07/15/2022 - 07/16/2022 | extracted=0.0  expected=24802.28  diff=24802.28 |
| 142 | `provider` | 07/15/2022 - 07/16/2022 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 142 | `insurers` | 07/15/2022 - 07/16/2022 | missing=['medicaid'] |
| 143 | `payments` | 07/11/2021 - 07/12/2021 | extracted=24830.66  expected=None |
| 143 | `balance` | 07/11/2021 - 07/12/2021 | extracted=0.0  expected=24830.66  diff=24830.66 |
| 143 | `provider` | 07/11/2021 - 07/12/2021 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 143 | `insurers` | 07/11/2021 - 07/12/2021 | missing=['medicaid'] |
| 144 | `payments` | 05/02/2017 - 05/07/2017 | extracted=17588.77  expected=None |
| 144 | `balance` | 05/02/2017 - 05/07/2017 | extracted=0.0  expected=17588.77  diff=17588.77 |
| 144 | `provider` | 05/02/2017 - 05/07/2017 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 144 | `insurers` | 05/02/2017 - 05/07/2017 | missing=['medicaid'] |
| 145 | `payments` | 11/13/2018 - 11/14/2018 | extracted=23379.92  expected=None |
| 145 | `balance` | 11/13/2018 - 11/14/2018 | extracted=0.0  expected=23379.92  diff=23379.92 |
| 145 | `provider` | 11/13/2018 - 11/14/2018 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 145 | `insurers` | 11/13/2018 - 11/14/2018 | missing=['medicaid'] |
| 146 | `payments` | 04/07/2022 - 04/13/2022 | extracted=20822.33  expected=None |
| 146 | `balance` | 04/07/2022 - 04/13/2022 | extracted=0.0  expected=20822.33  diff=20822.33 |
| 146 | `provider` | 04/07/2022 - 04/13/2022 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 146 | `insurers` | 04/07/2022 - 04/13/2022 | missing=['medicaid'] |
| 147 | `payments` | 05/23/2024 - 05/30/2024 | extracted=19529.89  expected=None |
| 147 | `balance` | 05/23/2024 - 05/30/2024 | extracted=0.0  expected=19529.89  diff=19529.89 |
| 147 | `provider` | 05/23/2024 - 05/30/2024 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 147 | `insurers` | 05/23/2024 - 05/30/2024 | missing=['medicaid'] |
| 148 | `total_charges` | 12/01/2018 - 12/08/2018 | extracted=0.0  expected=354058.17  diff=354058.17 |
| 148 | `ins_paid` | 12/01/2018 - 12/08/2018 | extracted=None  expected=170783.07 |
| 148 | `adjustment` | 12/01/2018 - 12/08/2018 | extracted=None  expected=160686.19 |
| 148 | `balance` | 12/01/2018 - 12/08/2018 | extracted=None  expected=22588.91 |
| 148 | `provider` | 12/01/2018 - 12/08/2018 | extracted='Unknown'  expected='South Patrickmouth General Hospital' |
| 148 | `insurers` | 12/01/2018 - 12/08/2018 | missing=['medicaid'] |
| 149 | `total_charges` | 11/13/2022 - 11/15/2022 | extracted=8800.24  expected=345130.58  diff=336330.34 |
| 149 | `ins_paid` | 11/13/2022 - 11/15/2022 | extracted=None  expected=166476.76 |
| 149 | `adjustment` | 11/13/2022 - 11/15/2022 | extracted=None  expected=156634.49 |
| 149 | `balance` | 11/13/2022 - 11/15/2022 | extracted=None  expected=22019.33 |
| 149 | `provider` | 11/13/2022 - 11/15/2022 | extracted=''  expected='South Patrickmouth General Hospital' |
| 149 | `insurers` | 11/13/2022 - 11/15/2022 | missing=['medicaid'] |
| 149 | `description` | 11/13/2022 - 11/15/2022 | extracted='Professional Fees, Speech Pathology'  expected='Pneumonia, unspecified organism' |

### doc_012

**Count mismatch** — GT: 120, extracted: 47.

**Missing records (75):**
- GT[6] `06/06/2017 - 07/04/2017` — No extracted record found with this treatment_date
- GT[7] `07/05/2017 - 07/13/2017` — No extracted record found with this treatment_date
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
- GT[92] `02/10/2023 - 03/12/2023` — No extracted record found with this treatment_date
- GT[93] `03/13/2023 - 04/14/2023` — No extracted record found with this treatment_date
- GT[95] `05/15/2023 - 05/17/2023` — No extracted record found with this treatment_date
- GT[108] `03/04/2024 - 04/05/2024` — No extracted record found with this treatment_date
- GT[109] `04/06/2024 - 05/05/2024` — No extracted record found with this treatment_date
- GT[111] `06/06/2024 - 06/08/2024` — No extracted record found with this treatment_date

**Extra extracted records (2):**
- `03/15/2023 - 04/14/2023` — Extracted record has no GT counterpart
- `04/07/2024 - 05/05/2024` — Extracted record has no GT counterpart

**Field mismatches (129):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `cpt_codes` | 01/01/2017 - 01/30/2017 | extra=['90935'] |
| 0 | `description` | 01/01/2017 - 01/30/2017 | extracted='10 treatments'  expected='Dialysis — 10 treatments' |
| 1 | `cpt_codes` | 01/31/2017 - 03/02/2017 | extra=['90935'] |
| 1 | `ins_paid` | 01/31/2017 - 03/02/2017 | extracted=10546.42  expected=8129.03  diff=2417.39 |
| 1 | `adjustment` | 01/31/2017 - 03/02/2017 | extracted=0.0  expected=2417.39  diff=2417.39 |
| 1 | `description` | 01/31/2017 - 03/02/2017 | extracted='13 treatments'  expected='Dialysis — 13 treatments' |
| 2 | `cpt_codes` | 03/03/2017 - 04/04/2017 | extra=['90935'] |
| 2 | `ins_paid` | 03/03/2017 - 04/04/2017 | extracted=7733.93  expected=5961.2  diff=1772.73 |
| 2 | `adjustment` | 03/03/2017 - 04/04/2017 | extracted=0.0  expected=1772.73  diff=1772.73 |
| 2 | `description` | 03/03/2017 - 04/04/2017 | extracted='8 treatments'  expected='Dialysis — 8 treatments' |
| 3 | `cpt_codes` | 04/05/2017 - 04/07/2017 | extra=['90935'] |
| 3 | `ins_paid` | 04/05/2017 - 04/07/2017 | extracted=10223.09  expected=7879.81  diff=2343.28 |
| 3 | `adjustment` | 04/05/2017 - 04/07/2017 | extracted=0.0  expected=2343.28  diff=2343.28 |
| 3 | `description` | 04/05/2017 - 04/07/2017 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 4 | `cpt_codes` | 04/08/2017 - 05/03/2017 | extra=['90937'] |
| 4 | `description` | 04/08/2017 - 05/03/2017 | extracted='12 treatments'  expected='Dialysis — 12 treatments' |
| 5 | `cpt_codes` | 05/04/2017 - 06/05/2017 | extra=['90935'] |
| 5 | `ins_paid` | 05/04/2017 - 06/05/2017 | extracted=14925.93  expected=11504.69  diff=3421.24 |
| 5 | `adjustment` | 05/04/2017 - 06/05/2017 | extracted=0.0  expected=3421.24  diff=3421.24 |
| 5 | `description` | 05/04/2017 - 06/05/2017 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 8 | `cpt_codes` | 07/14/2017 - 08/12/2017 | extra=['90935'] |
| 8 | `description` | 07/14/2017 - 08/12/2017 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 9 | `cpt_codes` | 08/13/2017 - 09/08/2017 | extra=['90935'] |
| 9 | `ins_paid` | 08/13/2017 - 09/08/2017 | extracted=13115.68  expected=10109.38  diff=3006.30 |
| 9 | `adjustment` | 08/13/2017 - 09/08/2017 | extracted=0.0  expected=3006.3  diff=3006.30 |
| 9 | `description` | 08/13/2017 - 09/08/2017 | extracted='13 treatments'  expected='Dialysis — 13 treatments' |
| 10 | `cpt_codes` | 09/09/2017 - 10/09/2017 | extra=['90935'] |
| 10 | `ins_paid` | 09/09/2017 - 10/09/2017 | extracted=12177.23  expected=9386.03  diff=2791.20 |
| 10 | `adjustment` | 09/09/2017 - 10/09/2017 | extracted=0.0  expected=2791.2  diff=2791.20 |
| 10 | `description` | 09/09/2017 - 10/09/2017 | extracted='12 treatments'  expected='Dialysis — 12 treatments' |
| 11 | `cpt_codes` | 10/10/2017 - 10/18/2017 | extra=['90935'] |
| 11 | `ins_paid` | 10/10/2017 - 10/18/2017 | extracted=14332.08  expected=11046.96  diff=3285.12 |
| 11 | `adjustment` | 10/10/2017 - 10/18/2017 | extracted=0.0  expected=3285.12  diff=3285.12 |
| 11 | `description` | 10/10/2017 - 10/18/2017 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 12 | `cpt_codes` | 10/19/2017 - 11/15/2017 | extra=['90935'] |
| 12 | `description` | 10/19/2017 - 11/15/2017 | extracted='13 treatments'  expected='Dialysis — 13 treatments' |
| 13 | `cpt_codes` | 11/16/2017 - 12/11/2017 | extra=['90935'] |
| 13 | `ins_paid` | 11/16/2017 - 12/11/2017 | extracted=15946.74  expected=12291.52  diff=3655.22 |
| 13 | `adjustment` | 11/16/2017 - 12/11/2017 | extracted=0.0  expected=3655.22  diff=3655.22 |
| 13 | `description` | 11/16/2017 - 12/11/2017 | extracted='11 treatments'  expected='Dialysis — 11 treatments' |
| 14 | `cpt_codes` | 12/12/2017 - 01/12/2018 | extra=['90935'] |
| 14 | `ins_paid` | 12/12/2017 - 01/12/2018 | extracted=19153.25  expected=14763.05  diff=4390.20 |
| 14 | `adjustment` | 12/12/2017 - 01/12/2018 | extracted=0.0  expected=4390.2  diff=4390.20 |
| 14 | `description` | 12/12/2017 - 01/12/2018 | extracted='11 treatments'  expected='Dialysis — 11 treatments' |
| 15 | `cpt_codes` | 01/13/2018 - 01/23/2018 | extra=['90935'] |
| 15 | `ins_paid` | 01/13/2018 - 01/23/2018 | extracted=9639.89  expected=7430.29  diff=2209.60 |
| 15 | `adjustment` | 01/13/2018 - 01/23/2018 | extracted=0.0  expected=2209.6  diff=2209.60 |
| 15 | `description` | 01/13/2018 - 01/23/2018 | extracted='11 treatments'  expected='Dialysis — 11 treatments' |
| 16 | `cpt_codes` | 01/24/2018 - 02/22/2018 | extra=['G0491'] |
| 16 | `description` | 01/24/2018 - 02/22/2018 | extracted='11 treatments'  expected='Dialysis — 11 treatments' |
| 17 | `cpt_codes` | 02/23/2018 - 03/23/2018 | extra=['G0491'] |
| 17 | `ins_paid` | 02/23/2018 - 03/23/2018 | extracted=16059.6  expected=12378.51  diff=3681.09 |
| 17 | `adjustment` | 02/23/2018 - 03/23/2018 | extracted=0.0  expected=3681.09  diff=3681.09 |
| 17 | `description` | 02/23/2018 - 03/23/2018 | extracted='13 treatments'  expected='Dialysis — 13 treatments' |
| 18 | `cpt_codes` | 03/24/2018 - 04/25/2018 | extra=['G0491'] |
| 18 | `ins_paid` | 03/24/2018 - 04/25/2018 | extracted=10769.1  expected=8300.67  diff=2468.43 |
| 18 | `adjustment` | 03/24/2018 - 04/25/2018 | extracted=0.0  expected=2468.43  diff=2468.43 |
| 18 | `description` | 03/24/2018 - 04/25/2018 | extracted='10 treatments'  expected='Dialysis — 10 treatments' |
| 19 | `cpt_codes` | 04/26/2018 - 04/30/2018 | extra=['G0491'] |
| 19 | `ins_paid` | 04/26/2018 - 04/30/2018 | extracted=9391.21  expected=7238.61  diff=2152.60 |
| 19 | `adjustment` | 04/26/2018 - 04/30/2018 | extracted=0.0  expected=2152.6  diff=2152.60 |
| 19 | `description` | 04/26/2018 - 04/30/2018 | extracted='10 treatments'  expected='Dialysis — 10 treatments' |
| 87 | `cpt_codes` | 10/27/2022 - 11/04/2022 | extra=['90937'] |
| 87 | `total_charges` | 10/27/2022 - 11/04/2022 | extracted=12976.34  expected=11888.27  diff=1088.07 |
| 87 | `ins_paid` | 10/27/2022 - 11/04/2022 | extracted=10001.98  expected=9163.31  diff=838.67 |
| 87 | `adjustment` | 10/27/2022 - 11/04/2022 | extracted=2974.36  expected=2724.96  diff=249.40 |
| 87 | `description` | 10/27/2022 - 11/04/2022 | extracted='10 treatments'  expected='Dialysis — 10 treatments' |
| 88 | `cpt_codes` | 11/05/2022 - 12/05/2022 | extra=['90937'] |
| 88 | `description` | 11/05/2022 - 12/05/2022 | extracted='8 treatments'  expected='Dialysis — 8 treatments' |
| 89 | `cpt_codes` | 12/06/2022 - 01/06/2023 | extra=['90937'] |
| 89 | `ins_paid` | 12/06/2022 - 01/06/2023 | extracted=15863.39  expected=12227.27  diff=3636.12 |
| 89 | `adjustment` | 12/06/2022 - 01/06/2023 | extracted=0.0  expected=3636.12  diff=3636.12 |
| 89 | `description` | 12/06/2022 - 01/06/2023 | extracted='13 treatments'  expected='Dialysis — 13 treatments' |
| 90 | `cpt_codes` | 01/07/2023 - 02/02/2023 | extra=['90937'] |
| 90 | `description` | 01/07/2023 - 02/02/2023 | extracted='8 treatments'  expected='Dialysis — 8 treatments' |
| 91 | `cpt_codes` | 02/03/2023 - 02/09/2023 | extra=['90935'] |
| 91 | `description` | 02/03/2023 - 02/09/2023 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 94 | `cpt_codes` | 04/15/2023 - 05/14/2023 | extra=['90937'] |
| 94 | `description` | 04/15/2023 - 05/14/2023 | extracted='11 treatments'  expected='Dialysis — 11 treatments' |
| 96 | `cpt_codes` | 05/18/2023 - 06/16/2023 | extra=['G0491'] |
| 96 | `description` | 05/18/2023 - 06/16/2023 | extracted='10 treatments'  expected='Dialysis — 10 treatments' |
| 97 | `cpt_codes` | 06/17/2023 - 07/18/2023 | extra=['90937'] |
| 97 | `ins_paid` | 06/17/2023 - 07/18/2023 | extracted=15932.27  expected=12280.37  diff=3651.90 |
| 97 | `adjustment` | 06/17/2023 - 07/18/2023 | extracted=0.0  expected=3651.9  diff=3651.90 |
| 97 | `description` | 06/17/2023 - 07/18/2023 | extracted='8 treatments'  expected='Dialysis — 8 treatments' |
| 98 | `cpt_codes` | 07/19/2023 - 08/19/2023 | extra=['90937'] |
| 98 | `description` | 07/19/2023 - 08/19/2023 | extracted='11 treatments'  expected='Dialysis — 11 treatments' |
| 99 | `cpt_codes` | 08/20/2023 - 08/22/2023 | extra=['G0491'] |
| 99 | `description` | 08/20/2023 - 08/22/2023 | extracted='12 treatments'  expected='Dialysis — 12 treatments' |
| 100 | `cpt_codes` | 08/23/2023 - 09/19/2023 | extra=['G0491'] |
| 100 | `description` | 08/23/2023 - 09/19/2023 | extracted='12 treatments'  expected='Dialysis — 12 treatments' |
| 101 | `cpt_codes` | 09/20/2023 - 10/15/2023 | extra=['G0491'] |
| 101 | `ins_paid` | 09/20/2023 - 10/15/2023 | extracted=13608.0  expected=10488.85  diff=3119.15 |
| 101 | `adjustment` | 09/20/2023 - 10/15/2023 | extracted=0.0  expected=3119.15  diff=3119.15 |
| 101 | `description` | 09/20/2023 - 10/15/2023 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 102 | `cpt_codes` | 10/16/2023 - 11/13/2023 | extra=['G0491'] |
| 102 | `description` | 10/16/2023 - 11/13/2023 | extracted='10 treatments'  expected='Dialysis — 10 treatments' |
| 103 | `cpt_codes` | 11/14/2023 - 11/27/2023 | extra=['90937'] |
| 103 | `description` | 11/14/2023 - 11/27/2023 | extracted='11 treatments'  expected='Dialysis — 11 treatments' |
| 104 | `cpt_codes` | 11/28/2023 - 12/24/2023 | extra=['90940'] |
| 104 | `description` | 11/28/2023 - 12/24/2023 | extracted='10 treatments'  expected='Dialysis — 10 treatments' |
| 105 | `cpt_codes` | 12/25/2023 - 01/25/2024 | extra=['90940'] |
| 105 | `ins_paid` | 12/25/2023 - 01/25/2024 | extracted=10071.55  expected=7763.01  diff=2308.54 |
| 105 | `adjustment` | 12/25/2023 - 01/25/2024 | extracted=0.0  expected=2308.54  diff=2308.54 |
| 105 | `description` | 12/25/2023 - 01/25/2024 | extracted='12 treatments'  expected='Dialysis — 12 treatments' |
| 106 | `cpt_codes` | 01/26/2024 - 02/23/2024 | extra=['90937'] |
| 106 | `description` | 01/26/2024 - 02/23/2024 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 107 | `cpt_codes` | 02/24/2024 - 03/03/2024 | extra=['G0491'] |
| 107 | `description` | 02/24/2024 - 03/03/2024 | extracted='10 treatments'  expected='Dialysis — 10 treatments' |
| 110 | `cpt_codes` | 05/06/2024 - 06/05/2024 | extra=['90937'] |
| 110 | `description` | 05/06/2024 - 06/05/2024 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 112 | `cpt_codes` | 06/09/2024 - 07/04/2024 | extra=['90937'] |
| 112 | `description` | 06/09/2024 - 07/04/2024 | extracted='11 treatments'  expected='Dialysis — 11 treatments' |
| 113 | `cpt_codes` | 07/05/2024 - 08/04/2024 | extra=['G0491'] |
| 113 | `ins_paid` | 07/05/2024 - 08/04/2024 | extracted=13452.66  expected=10369.12  diff=3083.54 |
| 113 | `adjustment` | 07/05/2024 - 08/04/2024 | extracted=0.0  expected=3083.54  diff=3083.54 |
| 113 | `description` | 07/05/2024 - 08/04/2024 | extracted='10 treatments'  expected='Dialysis — 10 treatments' |
| 114 | `cpt_codes` | 08/05/2024 - 09/02/2024 | extra=['G0491'] |
| 114 | `description` | 08/05/2024 - 09/02/2024 | extracted='8 treatments'  expected='Dialysis — 8 treatments' |
| 115 | `cpt_codes` | 09/03/2024 - 09/13/2024 | extra=['G0491'] |
| 115 | `description` | 09/03/2024 - 09/13/2024 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 116 | `cpt_codes` | 09/14/2024 - 10/14/2024 | extra=['G0491'] |
| 116 | `description` | 09/14/2024 - 10/14/2024 | extracted='11 treatments'  expected='Dialysis — 11 treatments' |
| 117 | `cpt_codes` | 10/15/2024 - 11/14/2024 | extra=['90937'] |
| 117 | `description` | 10/15/2024 - 11/14/2024 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 118 | `cpt_codes` | 11/15/2024 - 12/10/2024 | extra=['90937'] |
| 118 | `description` | 11/15/2024 - 12/10/2024 | extracted='9 treatments'  expected='Dialysis — 9 treatments' |
| 119 | `cpt_codes` | 12/11/2024 - 12/19/2024 | extra=['90937'] |
| 119 | `description` | 12/11/2024 - 12/19/2024 | extracted='13 treatments'  expected='Dialysis — 13 treatments' |

---

_Generated by `scripts/eval_extraction.py`_
