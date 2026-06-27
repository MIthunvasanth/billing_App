# Extraction Evaluation Results

Evaluated **12 documents** against ground truth.

---

## Summary

| Doc | GT | Extracted | Count | Weighted Acc | Cost USD | Duration |
|---|---|---|---|---|---|---|
| doc_001 | 50 | 49 | ✗ | 88.4% | $0.0822 | 24.59s |
| doc_002 | 40 | 40 | ✓ | 69.3% | $0.0875 | 24.06s |
| doc_003 | 1 | 2 | ✗ | 0.0% | $0.0913 | 6.98s |
| doc_004 | 1 | 2 | ✗ | 0.0% | $0.0778 | 6.05s |
| doc_005 | 80 | 77 | ✗ | 85.7% | $0.2027 | 15.96s |
| doc_006 | 33 | 33 | ✓ | 99.0% | $0.1100 | 14.39s |
| doc_007 | 400 | 402 | ✗ | 79.5% | $0.7957 | 58.13s |
| doc_008 | 100 | 1474 | ✗ | 31.9% | $1.1314 | 151.1s |
| doc_009 | 1 | 53 | ✗ | 0.0% | $0.7507 | 22.0s |
| doc_010 | 1 | 28 | ✗ | 0.0% | $0.6453 | 19.71s |
| doc_011 | 150 | 149 | ✗ | 57.7% | $0.8062 | 32.0s |
| doc_012 | 120 | 122 | ✗ | 99.0% | $0.4420 | 20.52s |

**Total cost:** $5.2229  
**Total tokens:** 1,909,574 (input 1,675,620 / output 233,954)  
**Total wall-clock:** 395.5s

---

## Field Accuracy by Document

| Doc | date | cpt | total$ | ins$ | adj | pmts | bal | prov | insrs | 3p | desc |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doc_001 | ✓98% | ✓98% | ✓96% | ✓96% | ✓96% | ✗56% | ✗56% | ✓98% | ✓98% | ✓98% | ✓98% |
| doc_002 | ~88% | ~88% | ~88% | ~88% | ~88% | ✗2% | ✗2% | ~88% | ~88% | ~88% | ~88% |
| doc_003 | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% |
| doc_004 | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% |
| doc_005 | ✓96% | ✓96% | ~91% | ~91% | ~91% | ✓96% | ✓95% | ✗35% | ✗35% | ✓96% | ~94% |
| doc_006 | ✓100% | ✓100% | ✓100% | ✓97% | ✓97% | ✓100% | ✓97% | ✓100% | ✓100% | ✓100% | ✓100% |
| doc_007 | ✓100% | ✓98% | ✓99% | ✓99% | ✓99% | ✗38% | ✗50% | ✗9% | ~88% | ✓100% | ~90% |
| doc_008 | ✓100% | ✗0% | ✗0% | ✗0% | ✗0% | ✗63% | ✗2% | ✗46% | ✗46% | ✓100% | ✗13% |
| doc_009 | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% |
| doc_010 | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% |
| doc_011 | ✓97% | ✓97% | ~81% | ~81% | ~81% | ✗0% | ✗0% | ✗7% | ✗7% | ✓97% | ~81% |
| doc_012 | ✓100% | ✓100% | ✓100% | ✓98% | ✓97% | ✓99% | ✓98% | ✓100% | ✓100% | ✓100% | ✓100% |

---

## Error Details per Document

### doc_001

**Count mismatch** — GT: 50, extracted: 49.

**Missing records (1):**
- GT[0] `07/28/2024` — No extracted record found with this treatment_date

**Field mismatches (45):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 2 | `payments` | 01/06/2024 | extracted=21.87  expected=None |
| 2 | `balance` | 01/06/2024 | extracted=0.0  expected=21.87  diff=21.87 |
| 3 | `payments` | 02/27/2023 | extracted=6.36  expected=None |
| 3 | `balance` | 02/27/2023 | extracted=0.0  expected=6.36  diff=6.36 |
| 5 | `total_charges` | 10/28/2023 | extracted=641.46  expected=148.26  diff=493.20 |
| 5 | `ins_paid` | 10/28/2023 | extracted=424.45  expected=106.66  diff=317.79 |
| 5 | `adjustment` | 10/28/2023 | extracted=211.54  expected=36.13  diff=175.41 |
| 5 | `payments` | 10/28/2023 | extracted=5.47  expected=None |
| 5 | `balance` | 10/28/2023 | extracted=0.0  expected=5.47  diff=5.47 |
| 6 | `payments` | 09/15/2024 | extracted=42.5  expected=None |
| 6 | `balance` | 09/15/2024 | extracted=0.0  expected=42.5  diff=42.50 |
| 9 | `payments` | 08/13/2024 | extracted=2.54  expected=None |
| 9 | `balance` | 08/13/2024 | extracted=0.0  expected=2.54  diff=2.54 |
| 11 | `payments` | 03/04/2023 | extracted=4.06  expected=None |
| 11 | `balance` | 03/04/2023 | extracted=0.0  expected=4.06  diff=4.06 |
| 15 | `payments` | 01/02/2024 | extracted=18.33  expected=None |
| 15 | `balance` | 01/02/2024 | extracted=0.0  expected=18.33  diff=18.33 |
| 16 | `payments` | 02/27/2024 | extracted=42.17  expected=None |
| 16 | `balance` | 02/27/2024 | extracted=0.0  expected=42.17  diff=42.17 |
| 17 | `payments` | 08/17/2023 | extracted=7.78  expected=None |
| 17 | `balance` | 08/17/2023 | extracted=0.0  expected=7.78  diff=7.78 |
| 18 | `payments` | 02/09/2023 | extracted=25.73  expected=None |
| 18 | `balance` | 02/09/2023 | extracted=0.0  expected=25.73  diff=25.73 |
| 24 | `payments` | 07/09/2024 | extracted=29.29  expected=None |
| 24 | `balance` | 07/09/2024 | extracted=0.0  expected=29.29  diff=29.29 |
| 26 | `payments` | 12/12/2023 | extracted=2.52  expected=None |
| 26 | `balance` | 12/12/2023 | extracted=0.0  expected=2.52  diff=2.52 |
| 33 | `payments` | 05/10/2023 | extracted=42.8  expected=None |
| 33 | `balance` | 05/10/2023 | extracted=0.0  expected=42.8  diff=42.80 |
| 35 | `payments` | 12/24/2024 | extracted=42.99  expected=None |
| 35 | `balance` | 12/24/2024 | extracted=0.0  expected=42.99  diff=42.99 |
| 37 | `payments` | 10/12/2024 | extracted=9.58  expected=None |
| 37 | `balance` | 10/12/2024 | extracted=0.0  expected=9.58  diff=9.58 |
| 38 | `payments` | 04/18/2024 | extracted=20.29  expected=None |
| 38 | `balance` | 04/18/2024 | extracted=0.0  expected=20.29  diff=20.29 |
| 39 | `payments` | 03/01/2024 | extracted=48.91  expected=None |
| 39 | `balance` | 03/01/2024 | extracted=0.0  expected=48.91  diff=48.91 |
| 40 | `payments` | 08/16/2024 | extracted=48.96  expected=None |
| 40 | `balance` | 08/16/2024 | extracted=0.0  expected=48.96  diff=48.96 |
| 45 | `payments` | 07/23/2023 | extracted=71.71  expected=None |
| 45 | `balance` | 07/23/2023 | extracted=0.0  expected=71.71  diff=71.71 |
| 47 | `payments` | 12/01/2023 | extracted=98.62  expected=None |
| 47 | `balance` | 12/01/2023 | extracted=0.0  expected=98.62  diff=98.62 |
| 48 | `payments` | 07/24/2024 | extracted=35.35  expected=None |
| 48 | `balance` | 07/24/2024 | extracted=0.0  expected=35.35  diff=35.35 |

### doc_002

Record count matches GT.

**Missing records (5):**
- GT[19] `06/07/2023 - 12/26/2024` — No extracted record found with this treatment_date
- GT[23] `03/02/2023 - 12/29/2024` — No extracted record found with this treatment_date
- GT[24] `02/23/2023 - 07/30/2024` — No extracted record found with this treatment_date
- GT[32] `07/14/2023 - 12/04/2024` — No extracted record found with this treatment_date
- GT[34] `03/10/2023 - 11/01/2024` — No extracted record found with this treatment_date

**Extra extracted records (5):**
- `06/07/2023 - 12/12/2024` — Extracted record has no GT counterpart
- `03/02/2023 - 12/06/2024` — Extracted record has no GT counterpart
- `01/05/2024 - 09/03/2023` — Extracted record has no GT counterpart
- `07/14/2023 - 09/13/2024` — Extracted record has no GT counterpart
- `05/04/2023 - 11/01/2024` — Extracted record has no GT counterpart

**Field mismatches (68):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `payments` | 02/01/2023 - 12/07/2024 | extracted=83.45  expected=None |
| 0 | `balance` | 02/01/2023 - 12/07/2024 | extracted=0.0  expected=83.45  diff=83.45 |
| 1 | `payments` | 06/26/2023 - 12/11/2024 | extracted=154.09  expected=None |
| 1 | `balance` | 06/26/2023 - 12/11/2024 | extracted=0.0  expected=154.09  diff=154.09 |
| 2 | `payments` | 03/30/2023 - 07/18/2024 | extracted=35.14  expected=None |
| 2 | `balance` | 03/30/2023 - 07/18/2024 | extracted=0.0  expected=35.14  diff=35.14 |
| 3 | `payments` | 02/16/2023 - 10/01/2024 | extracted=65.76  expected=None |
| 3 | `balance` | 02/16/2023 - 10/01/2024 | extracted=0.0  expected=65.76  diff=65.76 |
| 4 | `payments` | 11/17/2023 - 12/02/2024 | extracted=43.37  expected=None |
| 4 | `balance` | 11/17/2023 - 12/02/2024 | extracted=0.0  expected=43.37  diff=43.37 |
| 5 | `payments` | 03/17/2023 - 09/30/2024 | extracted=24.36  expected=None |
| 5 | `balance` | 03/17/2023 - 09/30/2024 | extracted=0.0  expected=24.36  diff=24.36 |
| 6 | `payments` | 03/05/2023 - 12/18/2024 | extracted=109.17  expected=None |
| 6 | `balance` | 03/05/2023 - 12/18/2024 | extracted=0.0  expected=109.17  diff=109.17 |
| 7 | `payments` | 05/21/2023 - 11/23/2024 | extracted=31.29  expected=None |
| 7 | `balance` | 05/21/2023 - 11/23/2024 | extracted=0.0  expected=31.29  diff=31.29 |
| 8 | `payments` | 02/07/2023 - 10/23/2024 | extracted=95.72  expected=None |
| 8 | `balance` | 02/07/2023 - 10/23/2024 | extracted=0.0  expected=95.72  diff=95.72 |
| 9 | `payments` | 03/25/2023 - 12/21/2024 | extracted=88.51  expected=None |
| 9 | `balance` | 03/25/2023 - 12/21/2024 | extracted=0.0  expected=88.51  diff=88.51 |
| 10 | `payments` | 03/05/2023 - 08/20/2024 | extracted=16.46  expected=None |
| 10 | `balance` | 03/05/2023 - 08/20/2024 | extracted=0.0  expected=16.46  diff=16.46 |
| 11 | `payments` | 08/17/2023 - 10/18/2024 | extracted=10.39  expected=None |
| 11 | `balance` | 08/17/2023 - 10/18/2024 | extracted=0.0  expected=10.39  diff=10.39 |
| 12 | `payments` | 02/19/2023 - 11/07/2024 | extracted=85.28  expected=None |
| 12 | `balance` | 02/19/2023 - 11/07/2024 | extracted=0.0  expected=85.28  diff=85.28 |
| 14 | `payments` | 01/16/2023 - 11/20/2024 | extracted=131.29  expected=None |
| 14 | `balance` | 01/16/2023 - 11/20/2024 | extracted=0.0  expected=131.29  diff=131.29 |
| 15 | `payments` | 06/23/2023 - 12/25/2024 | extracted=139.96  expected=None |
| 15 | `balance` | 06/23/2023 - 12/25/2024 | extracted=0.0  expected=139.96  diff=139.96 |
| 16 | `payments` | 02/27/2023 - 12/09/2024 | extracted=120.67  expected=None |
| 16 | `balance` | 02/27/2023 - 12/09/2024 | extracted=0.0  expected=120.67  diff=120.67 |
| 17 | `payments` | 03/22/2023 - 08/22/2024 | extracted=138.98  expected=None |
| 17 | `balance` | 03/22/2023 - 08/22/2024 | extracted=0.0  expected=138.98  diff=138.98 |
| 18 | `payments` | 03/20/2023 - 09/03/2024 | extracted=72.69  expected=None |
| 18 | `balance` | 03/20/2023 - 09/03/2024 | extracted=0.0  expected=72.69  diff=72.69 |
| 20 | `payments` | 05/26/2023 - 05/09/2024 | extracted=47.74  expected=None |
| 20 | `balance` | 05/26/2023 - 05/09/2024 | extracted=0.0  expected=47.74  diff=47.74 |
| 21 | `payments` | 05/25/2023 - 11/20/2024 | extracted=168.39  expected=None |
| 21 | `balance` | 05/25/2023 - 11/20/2024 | extracted=0.0  expected=168.39  diff=168.39 |
| 22 | `payments` | 02/03/2023 - 12/28/2024 | extracted=64.73  expected=None |
| 22 | `balance` | 02/03/2023 - 12/28/2024 | extracted=0.0  expected=64.73  diff=64.73 |
| 25 | `payments` | 01/13/2023 - 10/20/2024 | extracted=372.14  expected=None |
| 25 | `balance` | 01/13/2023 - 10/20/2024 | extracted=0.0  expected=372.14  diff=372.14 |
| 26 | `payments` | 01/13/2023 - 10/04/2024 | extracted=108.64  expected=None |
| 26 | `balance` | 01/13/2023 - 10/04/2024 | extracted=0.0  expected=108.64  diff=108.64 |
| 27 | `payments` | 03/05/2023 - 12/18/2024 | extracted=148.37  expected=None |
| 27 | `balance` | 03/05/2023 - 12/18/2024 | extracted=0.0  expected=148.37  diff=148.37 |
| 28 | `payments` | 03/18/2023 - 12/03/2024 | extracted=75.54  expected=None |
| 28 | `balance` | 03/18/2023 - 12/03/2024 | extracted=0.0  expected=75.54  diff=75.54 |
| 29 | `payments` | 03/08/2023 - 12/31/2024 | extracted=119.56  expected=None |
| 29 | `balance` | 03/08/2023 - 12/31/2024 | extracted=0.0  expected=119.56  diff=119.56 |
| 30 | `payments` | 01/31/2023 - 12/18/2024 | extracted=65.28  expected=None |
| 30 | `balance` | 01/31/2023 - 12/18/2024 | extracted=0.0  expected=65.28  diff=65.28 |
| 31 | `payments` | 03/02/2023 - 12/26/2024 | extracted=245.92  expected=None |
| 31 | `balance` | 03/02/2023 - 12/26/2024 | extracted=0.0  expected=245.92  diff=245.92 |
| 33 | `payments` | 09/27/2023 - 12/14/2024 | extracted=49.89  expected=None |
| 33 | `balance` | 09/27/2023 - 12/14/2024 | extracted=0.0  expected=49.89  diff=49.89 |
| 35 | `payments` | 03/01/2023 - 12/06/2024 | extracted=107.8  expected=None |
| 35 | `balance` | 03/01/2023 - 12/06/2024 | extracted=0.0  expected=107.8  diff=107.80 |
| 36 | `payments` | 04/15/2023 - 10/29/2024 | extracted=86.96  expected=None |
| 36 | `balance` | 04/15/2023 - 10/29/2024 | extracted=0.0  expected=86.96  diff=86.96 |
| 37 | `payments` | 06/22/2023 - 11/28/2024 | extracted=130.55  expected=None |
| 37 | `balance` | 06/22/2023 - 11/28/2024 | extracted=0.0  expected=130.55  diff=130.55 |
| 38 | `payments` | 02/08/2023 - 12/04/2024 | extracted=45.56  expected=None |
| 38 | `balance` | 02/08/2023 - 12/04/2024 | extracted=0.0  expected=45.56  diff=45.56 |
| 39 | `payments` | 01/10/2023 - 11/24/2024 | extracted=199.96  expected=None |
| 39 | `balance` | 01/10/2023 - 11/24/2024 | extracted=0.0  expected=199.96  diff=199.96 |

### doc_003

**Count mismatch** — GT: 1, extracted: 2.

**Missing records (1):**
- GT[0] `01/04/2023 - 12/31/2024` — No extracted record found with this treatment_date

**Extra extracted records (2):**
- `01/04/2023 - 05/12/2024` — Extracted record has no GT counterpart
- `05/12/2024 - 12/31/2024` — Extracted record has no GT counterpart

### doc_004

**Count mismatch** — GT: 1, extracted: 2.

**Missing records (1):**
- GT[0] `01/04/2023 - 12/31/2024` — No extracted record found with this treatment_date

**Extra extracted records (2):**
- `01/04/2023 - 07/07/2024` — Extracted record has no GT counterpart
- `07/08/2024 - 12/31/2024` — Extracted record has no GT counterpart

### doc_005

**Count mismatch** — GT: 80, extracted: 77.

**Missing records (3):**
- GT[2] `07/02/2024 - 07/03/2024` — No extracted record found with this treatment_date
- GT[3] `11/30/2022 - 12/07/2022` — No extracted record found with this treatment_date
- GT[58] `07/18/2022 - 07/23/2022` — No extracted record found with this treatment_date

**Extra extracted records (1):**
- `07/19/2022 - 07/23/2022` — Extracted record has no GT counterpart

**Field mismatches (113):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 1 | `total_charges` | 05/16/2021 - 05/19/2021 | extracted=152524.06  expected=154571.29  diff=2047.23 |
| 1 | `ins_paid` | 05/16/2021 - 05/19/2021 | extracted=94007.19  expected=95268.99  diff=1261.80 |
| 1 | `adjustment` | 05/16/2021 - 05/19/2021 | extracted=58516.87  expected=59302.3  diff=785.43 |
| 4 | `description` | 03/23/2022 - 03/27/2022 | extracted='Chronic obstructive pulmonary disease with acute exacerbation'  expected='Acute kidney injury' |
| 5 | `total_charges` | 05/18/2021 - 05/21/2021 | extracted=256792.69  expected=152524.06  diff=104268.63 |
| 5 | `ins_paid` | 05/18/2021 - 05/21/2021 | extracted=158272.47  expected=94007.19  diff=64265.28 |
| 5 | `adjustment` | 05/18/2021 - 05/21/2021 | extracted=98520.22  expected=58516.87  diff=40003.35 |
| 11 | `total_charges` | 05/18/2021 - 05/21/2021 | extracted=256792.69  expected=104268.63  diff=152524.06 |
| 11 | `ins_paid` | 05/18/2021 - 05/21/2021 | extracted=158272.47  expected=64265.28  diff=94007.19 |
| 11 | `adjustment` | 05/18/2021 - 05/21/2021 | extracted=98520.22  expected=40003.35  diff=58516.87 |
| 11 | `description` | 05/18/2021 - 05/21/2021 | extracted='Major depressive disorder, recurrent'  expected='Type 2 diabetes mellitus with ketoacidosis' |
| 29 | `total_charges` | 05/09/2021 - 05/14/2021 | extracted=None  expected=108547.85 |
| 29 | `ins_paid` | 05/09/2021 - 05/14/2021 | extracted=None  expected=66902.75 |
| 29 | `adjustment` | 05/09/2021 - 05/14/2021 | extracted=None  expected=41645.1 |
| 29 | `balance` | 05/09/2021 - 05/14/2021 | extracted=None  expected=0.0 |
| 30 | `provider` | 01/24/2021 - 01/29/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 30 | `insurers` | 01/24/2021 - 01/29/2021 | missing=['amerihealth'] |
| 31 | `provider` | 07/10/2023 - 07/12/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 31 | `insurers` | 07/10/2023 - 07/12/2023 | missing=['amerihealth'] |
| 32 | `provider` | 11/23/2024 - 11/25/2024 | extracted='Unknown'  expected='Dyer Healthcare' |
| 32 | `insurers` | 11/23/2024 - 11/25/2024 | missing=['amerihealth'] |
| 33 | `provider` | 10/03/2022 - 10/07/2022 | extracted='Unknown'  expected='Dyer Healthcare' |
| 33 | `insurers` | 10/03/2022 - 10/07/2022 | missing=['amerihealth'] |
| 34 | `provider` | 01/11/2021 - 01/14/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 34 | `insurers` | 01/11/2021 - 01/14/2021 | missing=['amerihealth'] |
| 35 | `provider` | 04/08/2022 - 04/14/2022 | extracted='Unknown'  expected='Dyer Healthcare' |
| 35 | `insurers` | 04/08/2022 - 04/14/2022 | missing=['amerihealth'] |
| 36 | `provider` | 08/26/2023 - 09/01/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 36 | `insurers` | 08/26/2023 - 09/01/2023 | missing=['amerihealth'] |
| 37 | `provider` | 04/24/2021 - 04/29/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 37 | `insurers` | 04/24/2021 - 04/29/2021 | missing=['amerihealth'] |
| 38 | `provider` | 08/29/2022 - 08/31/2022 | extracted='Unknown'  expected='Dyer Healthcare' |
| 38 | `insurers` | 08/29/2022 - 08/31/2022 | missing=['amerihealth'] |
| 39 | `provider` | 10/08/2024 - 10/15/2024 | extracted='Unknown'  expected='Dyer Healthcare' |
| 39 | `insurers` | 10/08/2024 - 10/15/2024 | missing=['amerihealth'] |
| 40 | `provider` | 06/22/2023 - 06/26/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 40 | `insurers` | 06/22/2023 - 06/26/2023 | missing=['amerihealth'] |
| 41 | `provider` | 12/12/2021 - 12/19/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 41 | `insurers` | 12/12/2021 - 12/19/2021 | missing=['amerihealth'] |
| 42 | `provider` | 10/12/2024 - 10/14/2024 | extracted='Unknown'  expected='Dyer Healthcare' |
| 42 | `insurers` | 10/12/2024 - 10/14/2024 | missing=['amerihealth'] |
| 43 | `provider` | 06/13/2023 - 06/18/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 43 | `insurers` | 06/13/2023 - 06/18/2023 | missing=['amerihealth'] |
| 44 | `provider` | 06/18/2022 - 06/19/2022 | extracted='Unknown'  expected='Dyer Healthcare' |
| 44 | `insurers` | 06/18/2022 - 06/19/2022 | missing=['amerihealth'] |
| 45 | `provider` | 12/22/2021 - 12/25/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 45 | `insurers` | 12/22/2021 - 12/25/2021 | missing=['amerihealth'] |
| 46 | `provider` | 06/19/2021 - 06/26/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 46 | `insurers` | 06/19/2021 - 06/26/2021 | missing=['amerihealth'] |
| 47 | `provider` | 08/24/2023 - 08/28/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 47 | `insurers` | 08/24/2023 - 08/28/2023 | missing=['amerihealth'] |
| 48 | `provider` | 07/26/2021 - 08/01/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 48 | `insurers` | 07/26/2021 - 08/01/2021 | missing=['amerihealth'] |
| 49 | `provider` | 11/20/2024 - 11/26/2024 | extracted='Unknown'  expected='Dyer Healthcare' |
| 49 | `insurers` | 11/20/2024 - 11/26/2024 | missing=['amerihealth'] |
| 50 | `provider` | 01/30/2022 - 02/03/2022 | extracted='Unknown'  expected='Dyer Healthcare' |
| 50 | `insurers` | 01/30/2022 - 02/03/2022 | missing=['amerihealth'] |
| 51 | `provider` | 06/03/2023 - 06/07/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 51 | `insurers` | 06/03/2023 - 06/07/2023 | missing=['amerihealth'] |
| 52 | `provider` | 08/15/2021 - 08/16/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 52 | `insurers` | 08/15/2021 - 08/16/2021 | missing=['amerihealth'] |
| 53 | `provider` | 12/25/2021 - 12/26/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 53 | `insurers` | 12/25/2021 - 12/26/2021 | missing=['amerihealth'] |
| 54 | `provider` | 11/08/2022 - 11/14/2022 | extracted='Unknown'  expected='Dyer Healthcare' |
| 54 | `insurers` | 11/08/2022 - 11/14/2022 | missing=['amerihealth'] |
| 55 | `provider` | 08/07/2023 - 08/12/2023 | extracted='Unknown'  expected='Dyer Healthcare' |
| 55 | `insurers` | 08/07/2023 - 08/12/2023 | missing=['amerihealth'] |
| 56 | `provider` | 07/09/2024 - 07/12/2024 | extracted='Unknown'  expected='Dyer Healthcare' |
| 56 | `insurers` | 07/09/2024 - 07/12/2024 | missing=['amerihealth'] |
| 57 | `provider` | 11/20/2021 - 11/25/2021 | extracted='Unknown'  expected='Dyer Healthcare' |
| 57 | `insurers` | 11/20/2021 - 11/25/2021 | missing=['amerihealth'] |
| 59 | `provider` | 06/16/2024 - 06/17/2024 | extracted=''  expected='Dyer Healthcare' |
| 59 | `insurers` | 06/16/2024 - 06/17/2024 | missing=['amerihealth'] |
| 60 | `provider` | 02/16/2023 - 02/20/2023 | extracted=''  expected='Dyer Healthcare' |
| 60 | `insurers` | 02/16/2023 - 02/20/2023 | missing=['amerihealth'] |
| 61 | `provider` | 01/27/2023 - 01/30/2023 | extracted=''  expected='Dyer Healthcare' |
| 61 | `insurers` | 01/27/2023 - 01/30/2023 | missing=['amerihealth'] |
| 62 | `provider` | 01/25/2023 - 01/28/2023 | extracted=''  expected='Dyer Healthcare' |
| 62 | `insurers` | 01/25/2023 - 01/28/2023 | missing=['amerihealth'] |
| 63 | `provider` | 10/28/2022 - 11/03/2022 | extracted=''  expected='Dyer Healthcare' |
| 63 | `insurers` | 10/28/2022 - 11/03/2022 | missing=['amerihealth'] |
| 64 | `provider` | 11/20/2023 - 11/27/2023 | extracted=''  expected='Dyer Healthcare' |
| 64 | `insurers` | 11/20/2023 - 11/27/2023 | missing=['amerihealth'] |
| 65 | `provider` | 12/26/2021 - 12/27/2021 | extracted=''  expected='Dyer Healthcare' |
| 65 | `insurers` | 12/26/2021 - 12/27/2021 | missing=['amerihealth'] |
| 66 | `provider` | 06/16/2023 - 06/23/2023 | extracted=''  expected='Dyer Healthcare' |
| 66 | `insurers` | 06/16/2023 - 06/23/2023 | missing=['amerihealth'] |
| 67 | `provider` | 08/02/2023 - 08/06/2023 | extracted=''  expected='Dyer Healthcare' |
| 67 | `insurers` | 08/02/2023 - 08/06/2023 | missing=['amerihealth'] |
| 68 | `provider` | 08/28/2024 - 09/04/2024 | extracted=''  expected='Dyer Healthcare' |
| 68 | `insurers` | 08/28/2024 - 09/04/2024 | missing=['amerihealth'] |
| 69 | `provider` | 07/26/2022 - 07/30/2022 | extracted=''  expected='Dyer Healthcare' |
| 69 | `insurers` | 07/26/2022 - 07/30/2022 | missing=['amerihealth'] |
| 70 | `provider` | 10/28/2024 - 11/01/2024 | extracted=''  expected='Dyer Healthcare' |
| 70 | `insurers` | 10/28/2024 - 11/01/2024 | missing=['amerihealth'] |
| 71 | `provider` | 02/21/2022 - 02/27/2022 | extracted=''  expected='Dyer Healthcare' |
| 71 | `insurers` | 02/21/2022 - 02/27/2022 | missing=['amerihealth'] |
| 72 | `provider` | 10/25/2024 - 10/27/2024 | extracted=''  expected='Dyer Healthcare' |
| 72 | `insurers` | 10/25/2024 - 10/27/2024 | missing=['amerihealth'] |
| 73 | `provider` | 11/17/2022 - 11/21/2022 | extracted=''  expected='Dyer Healthcare' |
| 73 | `insurers` | 11/17/2022 - 11/21/2022 | missing=['amerihealth'] |
| 74 | `provider` | 11/29/2021 - 11/30/2021 | extracted=''  expected='Dyer Healthcare' |
| 74 | `insurers` | 11/29/2021 - 11/30/2021 | missing=['amerihealth'] |
| 75 | `provider` | 07/25/2023 - 07/29/2023 | extracted=''  expected='Dyer Healthcare' |
| 75 | `insurers` | 07/25/2023 - 07/29/2023 | missing=['amerihealth'] |
| 76 | `provider` | 03/20/2022 - 03/27/2022 | extracted=''  expected='Dyer Healthcare' |
| 76 | `insurers` | 03/20/2022 - 03/27/2022 | missing=['amerihealth'] |
| 77 | `provider` | 02/13/2022 - 02/16/2022 | extracted=''  expected='Dyer Healthcare' |
| 77 | `insurers` | 02/13/2022 - 02/16/2022 | missing=['amerihealth'] |
| 78 | `provider` | 06/16/2022 - 06/19/2022 | extracted=''  expected='Dyer Healthcare' |
| 78 | `insurers` | 06/16/2022 - 06/19/2022 | missing=['amerihealth'] |
| 79 | `provider` | 09/03/2021 - 09/07/2021 | extracted=''  expected='Dyer Healthcare' |
| 79 | `insurers` | 09/03/2021 - 09/07/2021 | missing=['amerihealth'] |

### doc_006

Record count matches GT.

**Field mismatches (3):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 18 | `ins_paid` | 11/01/2022 - 12/01/2022 | extracted=None  expected=8655.28 |
| 18 | `adjustment` | 11/01/2022 - 12/01/2022 | extracted=None  expected=2882.9 |
| 18 | `balance` | 11/01/2022 - 12/01/2022 | extracted=None  expected=0.0 |

### doc_007

**Count mismatch** — GT: 400, extracted: 402.

**Missing records (2):**
- GT[347] `03/04/2024` — No extracted record found with this treatment_date
- GT[385] `07/11/2023` — No extracted record found with this treatment_date

**Extra extracted records (4):**
- `10/06/2024` — Extracted record has no GT counterpart
- `01/18/2023` — Extracted record has no GT counterpart
- `10/08/2023` — Extracted record has no GT counterpart
- `12/28/2022` — Extracted record has no GT counterpart

**Field mismatches (908):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 1 | `payments` | 10/08/2021 | extracted=20.9  expected=None |
| 4 | `payments` | 04/22/2021 | extracted=59.03  expected=None |
| 5 | `payments` | 09/29/2023 | extracted=45.57  expected=None |
| 6 | `insurers` | 05/04/2022 | missing=['insurance payment'] |
| 7 | `payments` | 06/22/2021 | extracted=9.59  expected=None |
| 8 | `payments` | 07/10/2023 | extracted=19.82  expected=None |
| 9 | `insurers` | 10/13/2023 | missing=['insurance payment'] |
| 10 | `payments` | 06/22/2022 | extracted=26.88  expected=None |
| 11 | `payments` | 10/20/2021 | extracted=12.86  expected=None |
| 11 | `insurers` | 10/20/2021 | missing=['insurance payment'] |
| 12 | `payments` | 12/04/2024 | extracted=93.36  expected=None |
| 13 | `insurers` | 05/12/2021 | missing=['insurance payment'] |
| 15 | `payments` | 07/24/2021 | extracted=17.92  expected=None |
| 18 | `payments` | 10/22/2022 | extracted=2.78  expected=None |
| 18 | `insurers` | 10/22/2022 | missing=['molina healthcare of ny'] |
| 19 | `payments` | 12/27/2023 | extracted=57.63  expected=None |
| 19 | `insurers` | 12/27/2023 | missing=['insurance payment'] |
| 21 | `payments` | 11/28/2022 | extracted=29.25  expected=None |
| 21 | `insurers` | 11/28/2022 | missing=['molina healthcare of ny'] |
| 22 | `payments` | 10/06/2024 | extracted=41.27  expected=None |
| 23 | `payments` | 05/16/2021 | extracted=11.41  expected=None |
| 24 | `payments` | 07/24/2021 | extracted=27.01  expected=None |
| 25 | `payments` | 04/28/2023 | extracted=15.64  expected=None |
| 25 | `insurers` | 04/28/2023 | missing=['molina healthcare of ny'] |
| 27 | `payments` | 05/17/2024 | extracted=23.56  expected=None |
| 28 | `payments` | 04/07/2024 | extracted=9.38  expected=None |
| 30 | `insurers` | 12/06/2021 | missing=['molina healthcare of ny'] |
| 31 | `payments` | 01/03/2024 | extracted=23.73  expected=None |
| 32 | `payments` | 06/11/2023 | extracted=32.61  expected=None |
| 33 | `payments` | 06/17/2024 | extracted=2.53  expected=None |
| 34 | `payments` | 04/12/2024 | extracted=45.58  expected=None |
| 35 | `payments` | 03/18/2024 | extracted=9.91  expected=None |
| 36 | `cpt_codes` | 08/16/2022 | missing=['45378'] |
| 36 | `payments` | 08/16/2022 | extracted=7.92  expected=None |
| 36 | `balance` | 08/16/2022 | extracted=0.0  expected=7.92  diff=7.92 |
| 36 | `provider` | 08/16/2022 | extracted='HORN STACY'  expected='Smith Medical, PC' |
| 37 | `provider` | 06/22/2021 | extracted='GONZALEZ ELIZABETH'  expected='Smith Medical, PC' |
| 38 | `payments` | 12/18/2024 | extracted=1.52  expected=None |
| 38 | `balance` | 12/18/2024 | extracted=0.0  expected=1.52  diff=1.52 |
| 38 | `provider` | 12/18/2024 | extracted='LITTLE DANIELLE'  expected='Smith Medical, PC' |
| 39 | `payments` | 09/11/2023 | extracted=16.07  expected=None |
| 39 | `balance` | 09/11/2023 | extracted=0.0  expected=16.07  diff=16.07 |
| 39 | `provider` | 09/11/2023 | extracted='DAVIS DANIEL'  expected='Smith Medical, PC' |
| 40 | `provider` | 08/22/2021 | extracted='HENDRIX RAYMOND'  expected='Smith Medical, PC' |
| 41 | `provider` | 10/23/2024 | extracted='HANSEN ZACHARY'  expected='Smith Medical, PC' |
| 42 | `payments` | 06/27/2024 | extracted=6.41  expected=None |
| 42 | `balance` | 06/27/2024 | extracted=0.0  expected=6.41  diff=6.41 |
| 42 | `provider` | 06/27/2024 | extracted='HUMPHREY EMMA'  expected='Smith Medical, PC' |
| 43 | `provider` | 06/30/2022 | extracted='SPENCER KEVIN'  expected='Smith Medical, PC' |
| 44 | `payments` | 09/18/2021 | extracted=6.92  expected=None |
| 44 | `balance` | 09/18/2021 | extracted=0.0  expected=6.92  diff=6.92 |
| 44 | `provider` | 09/18/2021 | extracted='HENRY PATRICIA'  expected='Smith Medical, PC' |
| 45 | `payments` | 10/29/2021 | extracted=16.48  expected=None |
| 45 | `balance` | 10/29/2021 | extracted=0.0  expected=16.48  diff=16.48 |
| 45 | `provider` | 10/29/2021 | extracted='HERNANDEZ EMILY'  expected='Smith Medical, PC' |
| 46 | `payments` | 03/02/2022 | extracted=30.82  expected=None |
| 46 | `balance` | 03/02/2022 | extracted=0.0  expected=30.82  diff=30.82 |
| 46 | `provider` | 03/02/2022 | extracted='VELAZQUEZ YOLANDA'  expected='Smith Medical, PC' |
| 46 | `insurers` | 03/02/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 47 | `provider` | 09/29/2024 | extracted='BROWN ADAM'  expected='Smith Medical, PC' |
| 48 | `payments` | 12/14/2021 | extracted=31.58  expected=None |
| 48 | `balance` | 12/14/2021 | extracted=0.0  expected=31.58  diff=31.58 |
| 48 | `provider` | 12/14/2021 | extracted='MOORE JENNIFER'  expected='Smith Medical, PC' |
| 49 | `payments` | 07/25/2021 | extracted=39.04  expected=None |
| 49 | `balance` | 07/25/2021 | extracted=0.0  expected=39.04  diff=39.04 |
| 49 | `provider` | 07/25/2021 | extracted='VELAZQUEZ MATTHEW'  expected='Smith Medical, PC' |
| 50 | `payments` | 05/18/2024 | extracted=94.29  expected=None |
| 50 | `balance` | 05/18/2024 | extracted=0.0  expected=94.29  diff=94.29 |
| 50 | `provider` | 05/18/2024 | extracted='LEWIS BRIAN'  expected='Smith Medical, PC' |
| 50 | `insurers` | 05/18/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 51 | `payments` | 10/28/2024 | extracted=74.65  expected=None |
| 51 | `balance` | 10/28/2024 | extracted=0.0  expected=74.65  diff=74.65 |
| 51 | `provider` | 10/28/2024 | extracted='MITCHELL ROGER'  expected='Smith Medical, PC' |
| 52 | `payments` | 09/08/2024 | extracted=2.26  expected=None |
| 52 | `balance` | 09/08/2024 | extracted=0.0  expected=2.26  diff=2.26 |
| 52 | `provider` | 09/08/2024 | extracted='MARTIN ALEJANDRA'  expected='Smith Medical, PC' |
| 53 | `payments` | 04/13/2023 | extracted=27.7  expected=None |
| 53 | `balance` | 04/13/2023 | extracted=0.0  expected=27.7  diff=27.70 |
| 53 | `provider` | 04/13/2023 | extracted='PEREZ JAMES'  expected='Smith Medical, PC' |
| 54 | `payments` | 01/06/2023 | extracted=21.69  expected=None |
| 54 | `balance` | 01/06/2023 | extracted=0.0  expected=21.69  diff=21.69 |
| 54 | `provider` | 01/06/2023 | extracted='CORDOVA ROBERT'  expected='Smith Medical, PC' |
| 55 | `provider` | 06/19/2021 | extracted='GREENE TRACEY'  expected='Smith Medical, PC' |
| 56 | `provider` | 04/18/2023 | extracted='PETERS BARRY'  expected='Smith Medical, PC' |
| 57 | `provider` | 02/10/2024 | extracted='REED LYNN'  expected='Smith Medical, PC' |
| 58 | `payments` | 01/16/2021 | extracted=14.71  expected=None |
| 58 | `balance` | 01/16/2021 | extracted=0.0  expected=14.71  diff=14.71 |
| 58 | `provider` | 01/16/2021 | extracted='KIDD BRADLEY'  expected='Smith Medical, PC' |
| 59 | `provider` | 07/15/2021 | extracted='CONNER JOHN'  expected='Smith Medical, PC' |
| 60 | `provider` | 02/06/2024 | extracted='PETTY MICHAEL'  expected='Smith Medical, PC' |
| 61 | `payments` | 11/11/2022 | extracted=5.48  expected=None |
| 61 | `balance` | 11/11/2022 | extracted=0.0  expected=5.48  diff=5.48 |
| 61 | `provider` | 11/11/2022 | extracted='FREDERICK MICHELLE'  expected='Smith Medical, PC' |
| 62 | `payments` | 01/05/2022 | extracted=14.77  expected=None |
| 62 | `balance` | 01/05/2022 | extracted=0.0  expected=14.77  diff=14.77 |
| 62 | `provider` | 01/05/2022 | extracted='JOHNSON MARK'  expected='Smith Medical, PC' |
| 63 | `provider` | 11/29/2021 | extracted='SPENCER JAMES'  expected='Smith Medical, PC' |
| 64 | `payments` | 12/12/2023 | extracted=18.98  expected=None |
| 64 | `balance` | 12/12/2023 | extracted=0.0  expected=18.98  diff=18.98 |
| 64 | `provider` | 12/12/2023 | extracted='DAVIS DIANE'  expected='Smith Medical, PC' |
| 64 | `insurers` | 12/12/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 65 | `payments` | 11/02/2024 | extracted=2.31  expected=None |
| 65 | `balance` | 11/02/2024 | extracted=0.0  expected=2.31  diff=2.31 |
| 65 | `provider` | 11/02/2024 | extracted='CHARLES JOSHUA'  expected='Smith Medical, PC' |
| 65 | `insurers` | 11/02/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 66 | `payments` | 05/06/2022 | extracted=25.57  expected=None |
| 66 | `balance` | 05/06/2022 | extracted=0.0  expected=25.57  diff=25.57 |
| 66 | `provider` | 05/06/2022 | extracted='MOORE COURTNEY'  expected='Smith Medical, PC' |
| 66 | `insurers` | 05/06/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 67 | `payments` | 06/19/2021 | extracted=56.79  expected=None |
| 67 | `balance` | 06/19/2021 | extracted=0.0  expected=56.79  diff=56.79 |
| 67 | `provider` | 06/19/2021 | extracted='LUCERO BRIANNA'  expected='Smith Medical, PC' |
| 68 | `provider` | 12/29/2021 | extracted='NELSON SHARON'  expected='Smith Medical, PC' |
| 69 | `payments` | 11/18/2022 | extracted=10.83  expected=None |
| 69 | `balance` | 11/18/2022 | extracted=0.0  expected=10.83  diff=10.83 |
| 69 | `provider` | 11/18/2022 | extracted='SMITH JENNA'  expected='Smith Medical, PC' |
| 70 | `payments` | 07/18/2023 | extracted=20.18  expected=None |
| 70 | `balance` | 07/18/2023 | extracted=0.0  expected=20.18  diff=20.18 |
| 70 | `provider` | 07/18/2023 | extracted='KNAPP DEBRA'  expected='Smith Medical, PC' |
| 71 | `payments` | 03/07/2022 | extracted=13.06  expected=None |
| 71 | `balance` | 03/07/2022 | extracted=0.0  expected=13.06  diff=13.06 |
| 71 | `provider` | 03/07/2022 | extracted='SCHNEIDER FREDERICK'  expected='Smith Medical, PC' |
| 72 | `payments` | 10/09/2024 | extracted=53.35  expected=None |
| 72 | `balance` | 10/09/2024 | extracted=0.0  expected=53.35  diff=53.35 |
| 72 | `provider` | 10/09/2024 | extracted='RILEY KRISTIN'  expected='Smith Medical, PC' |
| 72 | `insurers` | 10/09/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 73 | `provider` | 05/06/2023 | extracted='DIAZ RANDALL'  expected='Smith Medical, PC' |
| 74 | `payments` | 10/08/2021 | extracted=29.51  expected=None |
| 74 | `balance` | 10/08/2021 | extracted=0.0  expected=29.51  diff=29.51 |
| 74 | `provider` | 10/08/2021 | extracted='WHEELER FRANK'  expected='Smith Medical, PC' |
| 75 | `cpt_codes` | 10/06/2024 | missing=['99239'] |
| 75 | `payments` | 10/06/2024 | extracted=44.17  expected=None |
| 75 | `balance` | 10/06/2024 | extracted=0.0  expected=44.17  diff=44.17 |
| 75 | `provider` | 10/06/2024 | extracted='ALEXANDER BRUCE'  expected='Smith Medical, PC' |
| 76 | `provider` | 10/15/2024 | extracted='MCBRIDE THERESA'  expected='Smith Medical, PC' |
| 77 | `payments` | 03/17/2022 | extracted=6.45  expected=None |
| 77 | `balance` | 03/17/2022 | extracted=0.0  expected=6.45  diff=6.45 |
| 77 | `provider` | 03/17/2022 | extracted='DODSON ALISON'  expected='Smith Medical, PC' |
| 78 | `payments` | 07/17/2022 | extracted=4.73  expected=None |
| 78 | `balance` | 07/17/2022 | extracted=0.0  expected=4.73  diff=4.73 |
| 78 | `provider` | 07/17/2022 | extracted='RUSSELL JOSEPH'  expected='Smith Medical, PC' |
| 79 | `provider` | 07/06/2021 | extracted='COLLINS DUSTIN'  expected='Smith Medical, PC' |
| 80 | `provider` | 06/24/2021 | extracted='MILLER MICHAEL'  expected='Smith Medical, PC' |
| 81 | `payments` | 04/19/2024 | extracted=11.54  expected=None |
| 81 | `balance` | 04/19/2024 | extracted=0.0  expected=11.54  diff=11.54 |
| 81 | `provider` | 04/19/2024 | extracted='JORDAN CYNTHIA'  expected='Smith Medical, PC' |
| 82 | `payments` | 11/18/2022 | extracted=10.81  expected=None |
| 82 | `balance` | 11/18/2022 | extracted=0.0  expected=10.81  diff=10.81 |
| 82 | `provider` | 11/18/2022 | extracted='SPENCER SAMANTHA'  expected='Smith Medical, PC' |
| 83 | `payments` | 08/07/2021 | extracted=86.96  expected=None |
| 83 | `balance` | 08/07/2021 | extracted=0.0  expected=86.96  diff=86.96 |
| 83 | `provider` | 08/07/2021 | extracted='MARTIN HOLLY'  expected='Smith Medical, PC' |
| 84 | `provider` | 10/27/2021 | extracted='WASHINGTON KRISTA'  expected='Smith Medical, PC' |
| 85 | `payments` | 09/04/2021 | extracted=50.52  expected=None |
| 85 | `balance` | 09/04/2021 | extracted=0.0  expected=50.52  diff=50.52 |
| 85 | `provider` | 09/04/2021 | extracted='CAMPOS CHAD'  expected='Smith Medical, PC' |
| 85 | `insurers` | 09/04/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 86 | `provider` | 04/01/2024 | extracted='GREENE BRANDON'  expected='Smith Medical, PC' |
| 87 | `payments` | 03/31/2021 | extracted=49.86  expected=None |
| 87 | `balance` | 03/31/2021 | extracted=0.0  expected=49.86  diff=49.86 |
| 87 | `provider` | 03/31/2021 | extracted='WILLIS AARON'  expected='Smith Medical, PC' |
| 88 | `provider` | 10/22/2023 | extracted='WEISS JONATHON'  expected='Smith Medical, PC' |
| 89 | `payments` | 10/03/2024 | extracted=9.13  expected=None |
| 89 | `balance` | 10/03/2024 | extracted=0.0  expected=9.13  diff=9.13 |
| 89 | `provider` | 10/03/2024 | extracted='MARTIN NICOLE'  expected='Smith Medical, PC' |
| 90 | `payments` | 05/10/2024 | extracted=6.67  expected=None |
| 90 | `balance` | 05/10/2024 | extracted=0.0  expected=6.67  diff=6.67 |
| 90 | `provider` | 05/10/2024 | extracted='HERNANDEZ JESSE'  expected='Smith Medical, PC' |
| 91 | `payments` | 07/21/2024 | extracted=25.14  expected=None |
| 91 | `balance` | 07/21/2024 | extracted=0.0  expected=25.14  diff=25.14 |
| 91 | `provider` | 07/21/2024 | extracted='SELLERS CHRISTOPHER'  expected='Smith Medical, PC' |
| 92 | `provider` | 01/08/2021 | extracted='ROBINSON SOPHIA'  expected='Smith Medical, PC' |
| 93 | `payments` | 04/11/2023 | extracted=24.24  expected=None |
| 93 | `balance` | 04/11/2023 | extracted=0.0  expected=24.24  diff=24.24 |
| 93 | `provider` | 04/11/2023 | extracted='RAY ANTHONY'  expected='Smith Medical, PC' |
| 94 | `payments` | 08/03/2024 | extracted=12.81  expected=None |
| 94 | `balance` | 08/03/2024 | extracted=0.0  expected=12.81  diff=12.81 |
| 94 | `provider` | 08/03/2024 | extracted='SMITH TIFFANY'  expected='Smith Medical, PC' |
| 95 | `payments` | 10/25/2022 | extracted=41.3  expected=None |
| 95 | `balance` | 10/25/2022 | extracted=0.0  expected=41.3  diff=41.30 |
| 95 | `provider` | 10/25/2022 | extracted='BRADLEY LAURA'  expected='Smith Medical, PC' |
| 95 | `insurers` | 10/25/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 96 | `provider` | 02/04/2024 | extracted='BLAIR MICHAEL'  expected='Smith Medical, PC' |
| 97 | `provider` | 10/17/2021 | extracted='FERGUSON MELISSA'  expected='Smith Medical, PC' |
| 98 | `provider` | 04/11/2022 | extracted='LAWRENCE MICHAEL'  expected='Smith Medical, PC' |
| 99 | `provider` | 08/20/2023 | extracted='LEONARD STEPHANIE'  expected='Smith Medical, PC' |
| 100 | `payments` | 05/15/2021 | extracted=81.52  expected=None |
| 100 | `balance` | 05/15/2021 | extracted=0.0  expected=81.52  diff=81.52 |
| 100 | `provider` | 05/15/2021 | extracted='HILL KARL'  expected='Smith Medical, PC' |
| 101 | `provider` | 11/12/2021 | extracted='LOPEZ CRAIG'  expected='Smith Medical, PC' |
| 102 | `provider` | 01/02/2024 | extracted='RICHARDSON MADELINE'  expected='Smith Medical, PC' |
| 103 | `provider` | 07/07/2022 | extracted='RIGGS SARA'  expected='Smith Medical, PC' |
| 104 | `provider` | 04/04/2022 | extracted='BELL EARL'  expected='Smith Medical, PC' |
| 105 | `payments` | 10/13/2023 | extracted=20.41  expected=None |
| 105 | `balance` | 10/13/2023 | extracted=0.0  expected=20.41  diff=20.41 |
| 105 | `provider` | 10/13/2023 | extracted='DOMINGUEZ TAMMIE'  expected='Smith Medical, PC' |
| 105 | `insurers` | 10/13/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 106 | `provider` | 01/19/2024 | extracted='TAYLOR CANDICE'  expected='Smith Medical, PC' |
| 107 | `payments` | 11/19/2023 | extracted=27.43  expected=None |
| 107 | `balance` | 11/19/2023 | extracted=0.0  expected=27.43  diff=27.43 |
| 107 | `provider` | 11/19/2023 | extracted='BARRON ISAIAH'  expected='Smith Medical, PC' |
| 108 | `payments` | 09/29/2022 | extracted=9.73  expected=None |
| 108 | `balance` | 09/29/2022 | extracted=0.0  expected=9.73  diff=9.73 |
| 108 | `provider` | 09/29/2022 | extracted='FIELDS JENNIFER'  expected='Smith Medical, PC' |
| 109 | `payments` | 03/20/2021 | extracted=4.44  expected=None |
| 109 | `balance` | 03/20/2021 | extracted=0.0  expected=4.44  diff=4.44 |
| 109 | `provider` | 03/20/2021 | extracted='BARRETT JASON'  expected='Smith Medical, PC' |
| 110 | `payments` | 06/12/2023 | extracted=16.88  expected=None |
| 110 | `balance` | 06/12/2023 | extracted=0.0  expected=16.88  diff=16.88 |
| 110 | `provider` | 06/12/2023 | extracted='HANSON SCOTT'  expected='Smith Medical, PC' |
| 111 | `payments` | 08/17/2021 | extracted=37.44  expected=None |
| 111 | `balance` | 08/17/2021 | extracted=0.0  expected=37.44  diff=37.44 |
| 111 | `provider` | 08/17/2021 | extracted='STONE STEPHANIE'  expected='Smith Medical, PC' |
| 112 | `payments` | 01/13/2021 | extracted=4.64  expected=None |
| 112 | `balance` | 01/13/2021 | extracted=0.0  expected=4.64  diff=4.64 |
| 112 | `provider` | 01/13/2021 | extracted='MILLS KENNETH'  expected='Smith Medical, PC' |
| 113 | `provider` | 11/03/2024 | extracted='WILEY GARRETT'  expected='Smith Medical, PC' |
| 114 | `provider` | 02/08/2022 | extracted='BROWN NICOLE'  expected='Smith Medical, PC' |
| 115 | `cpt_codes` | 01/18/2023 | missing=['99201'] |
| 115 | `provider` | 01/18/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 116 | `payments` | 05/22/2023 | extracted=5.52  expected=None |
| 116 | `balance` | 05/22/2023 | extracted=0.0  expected=5.52  diff=5.52 |
| 116 | `provider` | 05/22/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 117 | `payments` | 09/28/2024 | extracted=27.17  expected=None |
| 117 | `balance` | 09/28/2024 | extracted=0.0  expected=27.17  diff=27.17 |
| 117 | `provider` | 09/28/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 118 | `provider` | 09/09/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 119 | `provider` | 12/18/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 120 | `provider` | 07/04/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 120 | `insurers` | 07/04/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 121 | `payments` | 10/02/2023 | extracted=19.8  expected=None |
| 121 | `balance` | 10/02/2023 | extracted=0.0  expected=19.8  diff=19.80 |
| 121 | `provider` | 10/02/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 122 | `payments` | 05/14/2022 | extracted=30.1  expected=None |
| 122 | `balance` | 05/14/2022 | extracted=0.0  expected=30.1  diff=30.10 |
| 122 | `provider` | 05/14/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 123 | `payments` | 12/14/2022 | extracted=20.96  expected=None |
| 123 | `balance` | 12/14/2022 | extracted=0.0  expected=20.96  diff=20.96 |
| 123 | `provider` | 12/14/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 124 | `payments` | 04/15/2024 | extracted=46.4  expected=None |
| 124 | `balance` | 04/15/2024 | extracted=0.0  expected=46.4  diff=46.40 |
| 124 | `provider` | 04/15/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 125 | `provider` | 02/11/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 126 | `payments` | 01/08/2024 | extracted=7.93  expected=None |
| 126 | `balance` | 01/08/2024 | extracted=0.0  expected=7.93  diff=7.93 |
| 126 | `provider` | 01/08/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 127 | `payments` | 08/16/2024 | extracted=7.33  expected=None |
| 127 | `balance` | 08/16/2024 | extracted=0.0  expected=7.33  diff=7.33 |
| 127 | `provider` | 08/16/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 128 | `payments` | 11/19/2021 | extracted=5.31  expected=None |
| 128 | `balance` | 11/19/2021 | extracted=0.0  expected=5.31  diff=5.31 |
| 128 | `provider` | 11/19/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 129 | `payments` | 07/31/2021 | extracted=45.35  expected=None |
| 129 | `balance` | 07/31/2021 | extracted=0.0  expected=45.35  diff=45.35 |
| 129 | `provider` | 07/31/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 130 | `payments` | 07/22/2024 | extracted=6.72  expected=None |
| 130 | `balance` | 07/22/2024 | extracted=0.0  expected=6.72  diff=6.72 |
| 130 | `provider` | 07/22/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 131 | `provider` | 05/31/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 132 | `payments` | 02/20/2023 | extracted=147.62  expected=None |
| 132 | `balance` | 02/20/2023 | extracted=0.0  expected=147.62  diff=147.62 |
| 132 | `provider` | 02/20/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 133 | `payments` | 11/01/2022 | extracted=4.26  expected=None |
| 133 | `balance` | 11/01/2022 | extracted=0.0  expected=4.26  diff=4.26 |
| 133 | `provider` | 11/01/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 134 | `payments` | 01/09/2024 | extracted=66.88  expected=None |
| 134 | `balance` | 01/09/2024 | extracted=0.0  expected=66.88  diff=66.88 |
| 134 | `provider` | 01/09/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 135 | `payments` | 09/18/2024 | extracted=36.0  expected=None |
| 135 | `balance` | 09/18/2024 | extracted=0.0  expected=36.0  diff=36.00 |
| 135 | `provider` | 09/18/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 136 | `payments` | 04/18/2024 | extracted=53.53  expected=None |
| 136 | `balance` | 04/18/2024 | extracted=0.0  expected=53.53  diff=53.53 |
| 136 | `provider` | 04/18/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 137 | `payments` | 02/14/2021 | extracted=38.53  expected=None |
| 137 | `balance` | 02/14/2021 | extracted=0.0  expected=38.53  diff=38.53 |
| 137 | `provider` | 02/14/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 138 | `payments` | 11/02/2022 | extracted=15.74  expected=None |
| 138 | `balance` | 11/02/2022 | extracted=0.0  expected=15.74  diff=15.74 |
| 138 | `provider` | 11/02/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 139 | `provider` | 08/04/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 140 | `payments` | 06/04/2022 | extracted=3.74  expected=None |
| 140 | `balance` | 06/04/2022 | extracted=0.0  expected=3.74  diff=3.74 |
| 140 | `provider` | 06/04/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 141 | `payments` | 02/03/2023 | extracted=12.7  expected=None |
| 141 | `balance` | 02/03/2023 | extracted=0.0  expected=12.7  diff=12.70 |
| 141 | `provider` | 02/03/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 142 | `payments` | 04/12/2024 | extracted=8.09  expected=None |
| 142 | `balance` | 04/12/2024 | extracted=0.0  expected=8.09  diff=8.09 |
| 142 | `provider` | 04/12/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 143 | `payments` | 07/29/2022 | extracted=7.74  expected=None |
| 143 | `balance` | 07/29/2022 | extracted=0.0  expected=7.74  diff=7.74 |
| 143 | `provider` | 07/29/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 144 | `provider` | 12/13/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 145 | `payments` | 10/08/2024 | extracted=2.74  expected=None |
| 145 | `balance` | 10/08/2024 | extracted=0.0  expected=2.74  diff=2.74 |
| 145 | `provider` | 10/08/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 146 | `payments` | 05/07/2023 | extracted=26.11  expected=None |
| 146 | `balance` | 05/07/2023 | extracted=0.0  expected=26.11  diff=26.11 |
| 146 | `provider` | 05/07/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 147 | `payments` | 08/02/2023 | extracted=45.4  expected=None |
| 147 | `balance` | 08/02/2023 | extracted=0.0  expected=45.4  diff=45.40 |
| 147 | `provider` | 08/02/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 147 | `insurers` | 08/02/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 148 | `provider` | 07/28/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 149 | `provider` | 10/17/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 150 | `payments` | 08/05/2024 | extracted=5.61  expected=None |
| 150 | `balance` | 08/05/2024 | extracted=0.0  expected=5.61  diff=5.61 |
| 150 | `provider` | 08/05/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 151 | `provider` | 01/08/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 152 | `cpt_codes` | 10/08/2023 | missing=['99281', 'J9000'] |
| 152 | `payments` | 10/08/2023 | extracted=74.57  expected=None |
| 152 | `balance` | 10/08/2023 | extracted=0.0  expected=74.57  diff=74.57 |
| 152 | `provider` | 10/08/2023 | extracted='REEVES'  expected='Smith Medical, PC' |
| 153 | `provider` | 06/11/2022 | extracted='CARROLL'  expected='Smith Medical, PC' |
| 154 | `payments` | 05/22/2023 | extracted=37.21  expected=None |
| 154 | `balance` | 05/22/2023 | extracted=0.0  expected=37.21  diff=37.21 |
| 154 | `provider` | 05/22/2023 | extracted='GONZALEZ'  expected='Smith Medical, PC' |
| 155 | `provider` | 06/10/2022 | extracted='LUTZ'  expected='Smith Medical, PC' |
| 156 | `payments` | 07/10/2021 | extracted=14.9  expected=None |
| 156 | `balance` | 07/10/2021 | extracted=0.0  expected=14.9  diff=14.90 |
| 156 | `provider` | 07/10/2021 | extracted='KELLY'  expected='Smith Medical, PC' |
| 157 | `provider` | 12/04/2021 | extracted='PEARSON'  expected='Smith Medical, PC' |
| 158 | `payments` | 12/07/2022 | extracted=74.85  expected=None |
| 158 | `balance` | 12/07/2022 | extracted=0.0  expected=74.85  diff=74.85 |
| 158 | `provider` | 12/07/2022 | extracted='SULLIVAN'  expected='Smith Medical, PC' |
| 159 | `provider` | 08/06/2024 | extracted='SUAREZ'  expected='Smith Medical, PC' |
| 160 | `payments` | 07/30/2022 | extracted=62.01  expected=None |
| 160 | `balance` | 07/30/2022 | extracted=0.0  expected=62.01  diff=62.01 |
| 160 | `provider` | 07/30/2022 | extracted='ROSE'  expected='Smith Medical, PC' |
| 161 | `payments` | 03/16/2023 | extracted=6.54  expected=None |
| 161 | `balance` | 03/16/2023 | extracted=0.0  expected=6.54  diff=6.54 |
| 161 | `provider` | 03/16/2023 | extracted='RODRIGUEZ'  expected='Smith Medical, PC' |
| 162 | `provider` | 03/29/2021 | extracted='JOHNSON'  expected='Smith Medical, PC' |
| 163 | `provider` | 09/12/2023 | extracted='CARTER'  expected='Smith Medical, PC' |
| 164 | `payments` | 06/23/2024 | extracted=53.4  expected=None |
| 164 | `balance` | 06/23/2024 | extracted=0.0  expected=53.4  diff=53.40 |
| 164 | `provider` | 06/23/2024 | extracted='TURNER'  expected='Smith Medical, PC' |
| 165 | `payments` | 01/06/2021 | extracted=31.91  expected=None |
| 165 | `balance` | 01/06/2021 | extracted=0.0  expected=31.91  diff=31.91 |
| 165 | `provider` | 01/06/2021 | extracted='GARCIA'  expected='Smith Medical, PC' |
| 166 | `provider` | 11/22/2024 | extracted='VALDEZ'  expected='Smith Medical, PC' |
| 167 | `provider` | 12/06/2022 | extracted='COLLINS'  expected='Smith Medical, PC' |
| 167 | `insurers` | 12/06/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 168 | `provider` | 08/19/2022 | extracted='DAVIS'  expected='Smith Medical, PC' |
| 169 | `provider` | 06/17/2023 | extracted='BENSON'  expected='Smith Medical, PC' |
| 170 | `payments` | 04/13/2024 | extracted=4.28  expected=None |
| 170 | `balance` | 04/13/2024 | extracted=0.0  expected=4.28  diff=4.28 |
| 170 | `provider` | 04/13/2024 | extracted='JOHNSON'  expected='Smith Medical, PC' |
| 171 | `payments` | 10/05/2022 | extracted=4.81  expected=None |
| 171 | `balance` | 10/05/2022 | extracted=0.0  expected=4.81  diff=4.81 |
| 171 | `provider` | 10/05/2022 | extracted='SHAW'  expected='Smith Medical, PC' |
| 172 | `payments` | 01/07/2022 | extracted=11.24  expected=None |
| 172 | `balance` | 01/07/2022 | extracted=0.0  expected=11.24  diff=11.24 |
| 172 | `provider` | 01/07/2022 | extracted='SANCHEZ'  expected='Smith Medical, PC' |
| 173 | `payments` | 09/19/2022 | extracted=5.92  expected=None |
| 173 | `balance` | 09/19/2022 | extracted=0.0  expected=5.92  diff=5.92 |
| 173 | `provider` | 09/19/2022 | extracted='VANG'  expected='Smith Medical, PC' |
| 173 | `insurers` | 09/19/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 174 | `provider` | 01/05/2024 | extracted='LOPEZ'  expected='Smith Medical, PC' |
| 174 | `insurers` | 01/05/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 175 | `provider` | 03/09/2023 | extracted='JOHNSON'  expected='Smith Medical, PC' |
| 176 | `payments` | 11/12/2024 | extracted=4.24  expected=None |
| 176 | `balance` | 11/12/2024 | extracted=0.0  expected=4.24  diff=4.24 |
| 176 | `provider` | 11/12/2024 | extracted='HERRERA'  expected='Smith Medical, PC' |
| 177 | `payments` | 10/28/2024 | extracted=28.3  expected=None |
| 177 | `balance` | 10/28/2024 | extracted=0.0  expected=28.3  diff=28.30 |
| 177 | `provider` | 10/28/2024 | extracted='ROMERO'  expected='Smith Medical, PC' |
| 178 | `provider` | 10/15/2021 | extracted='TURNER'  expected='Smith Medical, PC' |
| 179 | `payments` | 08/01/2024 | extracted=4.95  expected=None |
| 179 | `balance` | 08/01/2024 | extracted=0.0  expected=4.95  diff=4.95 |
| 179 | `provider` | 08/01/2024 | extracted='WARD'  expected='Smith Medical, PC' |
| 180 | `payments` | 10/07/2023 | extracted=25.71  expected=None |
| 180 | `balance` | 10/07/2023 | extracted=0.0  expected=25.71  diff=25.71 |
| 180 | `provider` | 10/07/2023 | extracted='MOORE'  expected='Smith Medical, PC' |
| 181 | `provider` | 04/24/2024 | extracted='DUNLAP'  expected='Smith Medical, PC' |
| 182 | `payments` | 11/14/2022 | extracted=63.05  expected=None |
| 182 | `balance` | 11/14/2022 | extracted=0.0  expected=63.05  diff=63.05 |
| 182 | `provider` | 11/14/2022 | extracted='MILLER'  expected='Smith Medical, PC' |
| 183 | `provider` | 08/09/2021 | extracted='DELACRUZ'  expected='Smith Medical, PC' |
| 184 | `payments` | 07/04/2022 | extracted=7.01  expected=None |
| 184 | `balance` | 07/04/2022 | extracted=0.0  expected=7.01  diff=7.01 |
| 184 | `provider` | 07/04/2022 | extracted='COLEMAN'  expected='Smith Medical, PC' |
| 185 | `provider` | 06/19/2023 | extracted='THOMPSON'  expected='Smith Medical, PC' |
| 186 | `provider` | 04/17/2021 | extracted='ALLEN'  expected='Smith Medical, PC' |
| 187 | `payments` | 10/24/2022 | extracted=14.35  expected=None |
| 187 | `balance` | 10/24/2022 | extracted=0.0  expected=14.35  diff=14.35 |
| 187 | `provider` | 10/24/2022 | extracted='FIELDS'  expected='Smith Medical, PC' |
| 188 | `provider` | 05/23/2022 | extracted='MOORE'  expected='Smith Medical, PC' |
| 189 | `provider` | 02/22/2024 | extracted='EDWARDS'  expected='Smith Medical, PC' |
| 190 | `provider` | 02/03/2022 | extracted='WARE'  expected='Smith Medical, PC' |
| 190 | `insurers` | 02/03/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 191 | `total_charges` | 03/27/2023 | extracted=1447.81  expected=1154.55  diff=293.26 |
| 191 | `ins_paid` | 03/27/2023 | extracted=739.31  expected=683.98  diff=55.33 |
| 191 | `adjustment` | 03/27/2023 | extracted=708.5  expected=470.57  diff=237.93 |
| 191 | `provider` | 03/27/2023 | extracted='WALKER JOHN'  expected='Smith Medical, PC' |
| 192 | `provider` | 04/16/2022 | extracted='LANG GLEN'  expected='Smith Medical, PC' |
| 193 | `provider` | 06/16/2022 | extracted='FOX LAURA'  expected='Smith Medical, PC' |
| 194 | `payments` | 09/17/2023 | extracted=51.96  expected=None |
| 194 | `balance` | 09/17/2023 | extracted=0.0  expected=51.96  diff=51.96 |
| 194 | `provider` | 09/17/2023 | extracted='HENSLEY NICOLE'  expected='Smith Medical, PC' |
| 194 | `insurers` | 09/17/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 195 | `payments` | 06/20/2021 | extracted=77.66  expected=None |
| 195 | `balance` | 06/20/2021 | extracted=0.0  expected=77.66  diff=77.66 |
| 195 | `provider` | 06/20/2021 | extracted='VEGA ERIC'  expected='Smith Medical, PC' |
| 196 | `payments` | 12/18/2021 | extracted=19.35  expected=None |
| 196 | `balance` | 12/18/2021 | extracted=0.0  expected=19.35  diff=19.35 |
| 196 | `provider` | 12/18/2021 | extracted='JONES RUTH'  expected='Smith Medical, PC' |
| 197 | `provider` | 07/07/2024 | extracted='JOHNSON WILLIAM'  expected='Smith Medical, PC' |
| 198 | `provider` | 05/01/2024 | extracted='WILLIAMS MARK'  expected='Smith Medical, PC' |
| 199 | `provider` | 01/24/2021 | extracted='FLORES ROBERT'  expected='Smith Medical, PC' |
| 200 | `provider` | 09/04/2023 | extracted='HILL PHILIP'  expected='Smith Medical, PC' |
| 201 | `payments` | 10/14/2022 | extracted=6.94  expected=None |
| 201 | `balance` | 10/14/2022 | extracted=0.0  expected=6.94  diff=6.94 |
| 201 | `provider` | 10/14/2022 | extracted='LYNCH WILLIAM'  expected='Smith Medical, PC' |
| 202 | `payments` | 12/24/2021 | extracted=1.59  expected=None |
| 202 | `balance` | 12/24/2021 | extracted=0.0  expected=1.59  diff=1.59 |
| 202 | `provider` | 12/24/2021 | extracted='WILLIAMS TAYLOR'  expected='Smith Medical, PC' |
| 203 | `payments` | 02/06/2023 | extracted=57.17  expected=None |
| 203 | `balance` | 02/06/2023 | extracted=0.0  expected=57.17  diff=57.17 |
| 203 | `provider` | 02/06/2023 | extracted='HILL KATHRYN'  expected='Smith Medical, PC' |
| 204 | `payments` | 04/22/2022 | extracted=21.43  expected=None |
| 204 | `balance` | 04/22/2022 | extracted=0.0  expected=21.43  diff=21.43 |
| 204 | `provider` | 04/22/2022 | extracted='WOOD ANGELA'  expected='Smith Medical, PC' |
| 205 | `provider` | 06/05/2023 | extracted='SCHNEIDER HOLLY'  expected='Smith Medical, PC' |
| 206 | `payments` | 07/02/2023 | extracted=24.27  expected=None |
| 206 | `balance` | 07/02/2023 | extracted=0.0  expected=24.27  diff=24.27 |
| 206 | `provider` | 07/02/2023 | extracted='SMITH JENNIFER'  expected='Smith Medical, PC' |
| 207 | `provider` | 07/01/2021 | extracted='WEISS KATHERINE'  expected='Smith Medical, PC' |
| 208 | `provider` | 11/13/2021 | extracted='ROGERS ALLISON'  expected='Smith Medical, PC' |
| 209 | `payments` | 03/01/2024 | extracted=4.72  expected=None |
| 209 | `balance` | 03/01/2024 | extracted=0.0  expected=4.72  diff=4.72 |
| 209 | `provider` | 03/01/2024 | extracted='THOMPSON KYLE'  expected='Smith Medical, PC' |
| 210 | `provider` | 12/17/2022 | extracted='SOLOMON DAWN'  expected='Smith Medical, PC' |
| 211 | `provider` | 07/31/2021 | extracted='MURPHY HANNAH'  expected='Smith Medical, PC' |
| 212 | `provider` | 03/09/2024 | extracted='ROGERS JACOB'  expected='Smith Medical, PC' |
| 212 | `insurers` | 03/09/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 213 | `payments` | 06/20/2024 | extracted=27.33  expected=None |
| 213 | `balance` | 06/20/2024 | extracted=0.0  expected=27.33  diff=27.33 |
| 213 | `provider` | 06/20/2024 | extracted='CURTIS CRYSTAL'  expected='Smith Medical, PC' |
| 214 | `payments` | 08/11/2022 | extracted=1.57  expected=None |
| 214 | `balance` | 08/11/2022 | extracted=0.0  expected=1.57  diff=1.57 |
| 214 | `provider` | 08/11/2022 | extracted='MURPHY KENDRA'  expected='Smith Medical, PC' |
| 215 | `payments` | 01/04/2022 | extracted=19.85  expected=None |
| 215 | `balance` | 01/04/2022 | extracted=0.0  expected=19.85  diff=19.85 |
| 215 | `provider` | 01/04/2022 | extracted='ADAMS TROY'  expected='Smith Medical, PC' |
| 216 | `payments` | 11/15/2021 | extracted=6.44  expected=None |
| 216 | `balance` | 11/15/2021 | extracted=0.0  expected=6.44  diff=6.44 |
| 216 | `provider` | 11/15/2021 | extracted='MOODY YVONNE'  expected='Smith Medical, PC' |
| 217 | `payments` | 05/25/2022 | extracted=51.47  expected=None |
| 217 | `balance` | 05/25/2022 | extracted=0.0  expected=51.47  diff=51.47 |
| 217 | `provider` | 05/25/2022 | extracted='WEBB ASHLEY'  expected='Smith Medical, PC' |
| 218 | `payments` | 07/21/2024 | extracted=31.02  expected=None |
| 218 | `balance` | 07/21/2024 | extracted=0.0  expected=31.02  diff=31.02 |
| 218 | `provider` | 07/21/2024 | extracted='PETERS ANDREA'  expected='Smith Medical, PC' |
| 219 | `payments` | 07/05/2022 | extracted=22.45  expected=None |
| 219 | `balance` | 07/05/2022 | extracted=0.0  expected=22.45  diff=22.45 |
| 219 | `provider` | 07/05/2022 | extracted='MARTIN JAMES'  expected='Smith Medical, PC' |
| 220 | `provider` | 12/14/2022 | extracted='HUFF LESLIE'  expected='Smith Medical, PC' |
| 221 | `payments` | 08/19/2022 | extracted=32.58  expected=None |
| 221 | `balance` | 08/19/2022 | extracted=0.0  expected=32.58  diff=32.58 |
| 221 | `provider` | 08/19/2022 | extracted='EDWARDS SUSAN'  expected='Smith Medical, PC' |
| 222 | `payments` | 06/01/2021 | extracted=8.48  expected=None |
| 222 | `balance` | 06/01/2021 | extracted=0.0  expected=8.48  diff=8.48 |
| 222 | `provider` | 06/01/2021 | extracted='NELSON NANCY'  expected='Smith Medical, PC' |
| 223 | `payments` | 09/13/2022 | extracted=2.76  expected=None |
| 223 | `balance` | 09/13/2022 | extracted=0.0  expected=2.76  diff=2.76 |
| 223 | `provider` | 09/13/2022 | extracted='SMITH LARRY'  expected='Smith Medical, PC' |
| 224 | `payments` | 11/04/2023 | extracted=37.32  expected=None |
| 224 | `balance` | 11/04/2023 | extracted=0.0  expected=37.32  diff=37.32 |
| 224 | `provider` | 11/04/2023 | extracted='WARREN DIANA'  expected='Smith Medical, PC' |
| 225 | `provider` | 08/06/2023 | extracted='PERKINS JAMES'  expected='Smith Medical, PC' |
| 226 | `provider` | 05/02/2022 | extracted='BLANKENSHIP KAREN'  expected='Smith Medical, PC' |
| 227 | `payments` | 01/03/2021 | extracted=37.89  expected=None |
| 227 | `balance` | 01/03/2021 | extracted=0.0  expected=37.89  diff=37.89 |
| 227 | `provider` | 01/03/2021 | extracted='FERNANDEZ ROBERT'  expected='Smith Medical, PC' |
| 228 | `payments` | 01/14/2023 | extracted=2.55  expected=None |
| 228 | `balance` | 01/14/2023 | extracted=0.0  expected=2.55  diff=2.55 |
| 228 | `provider` | 01/14/2023 | extracted='BARNES STACY'  expected='Smith Medical, PC' |
| 229 | `payments` | 07/05/2024 | extracted=26.41  expected=None |
| 229 | `balance` | 07/05/2024 | extracted=0.0  expected=26.41  diff=26.41 |
| 229 | `provider` | 07/05/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 230 | `provider` | 10/20/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 231 | `provider` | 08/04/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 232 | `provider` | 03/21/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 232 | `insurers` | 03/21/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 233 | `payments` | 10/29/2024 | extracted=5.16  expected=None |
| 233 | `balance` | 10/29/2024 | extracted=0.0  expected=5.16  diff=5.16 |
| 233 | `provider` | 10/29/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 234 | `payments` | 03/29/2024 | extracted=16.8  expected=None |
| 234 | `balance` | 03/29/2024 | extracted=0.0  expected=16.8  diff=16.80 |
| 234 | `provider` | 03/29/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 235 | `provider` | 01/06/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 236 | `payments` | 11/11/2022 | extracted=1.26  expected=None |
| 236 | `balance` | 11/11/2022 | extracted=0.0  expected=1.26  diff=1.26 |
| 236 | `provider` | 11/11/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 237 | `payments` | 08/03/2024 | extracted=4.92  expected=None |
| 237 | `balance` | 08/03/2024 | extracted=0.0  expected=4.92  diff=4.92 |
| 237 | `provider` | 08/03/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 238 | `provider` | 05/25/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 239 | `provider` | 09/05/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 240 | `payments` | 11/24/2021 | extracted=51.21  expected=None |
| 240 | `balance` | 11/24/2021 | extracted=0.0  expected=51.21  diff=51.21 |
| 240 | `provider` | 11/24/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 241 | `payments` | 10/17/2022 | extracted=24.67  expected=None |
| 241 | `balance` | 10/17/2022 | extracted=0.0  expected=24.67  diff=24.67 |
| 241 | `provider` | 10/17/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 241 | `insurers` | 10/17/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 242 | `provider` | 09/26/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
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
| 256 | `payments` | 10/14/2022 | extracted=34.29  expected=None |
| 256 | `balance` | 10/14/2022 | extracted=0.0  expected=34.29  diff=34.29 |
| 256 | `provider` | 10/14/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 257 | `payments` | 03/26/2023 | extracted=30.37  expected=None |
| 257 | `balance` | 03/26/2023 | extracted=0.0  expected=30.37  diff=30.37 |
| 257 | `provider` | 03/26/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 258 | `payments` | 02/10/2021 | extracted=42.8  expected=None |
| 258 | `balance` | 02/10/2021 | extracted=0.0  expected=42.8  diff=42.80 |
| 258 | `provider` | 02/10/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 259 | `provider` | 10/17/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 260 | `payments` | 12/26/2021 | extracted=29.14  expected=None |
| 260 | `balance` | 12/26/2021 | extracted=0.0  expected=29.14  diff=29.14 |
| 260 | `provider` | 12/26/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 261 | `provider` | 06/22/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 262 | `provider` | 12/22/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 263 | `payments` | 10/28/2023 | extracted=48.22  expected=None |
| 263 | `balance` | 10/28/2023 | extracted=0.0  expected=48.22  diff=48.22 |
| 263 | `provider` | 10/28/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 264 | `payments` | 04/21/2023 | extracted=19.9  expected=None |
| 264 | `balance` | 04/21/2023 | extracted=0.0  expected=19.9  diff=19.90 |
| 264 | `provider` | 04/21/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 265 | `payments` | 11/17/2022 | extracted=31.75  expected=None |
| 265 | `balance` | 11/17/2022 | extracted=0.0  expected=31.75  diff=31.75 |
| 265 | `provider` | 11/17/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 266 | `provider` | 07/23/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 267 | `cpt_codes` | 01/15/2024 | missing=['72110', '80061'] |
| 267 | `total_charges` | 01/15/2024 | extracted=1650.9  expected=2833.37  diff=1182.47 |
| 267 | `ins_paid` | 01/15/2024 | extracted=842.75  expected=1472.22  diff=629.47 |
| 267 | `adjustment` | 01/15/2024 | extracted=672.29  expected=1305.66  diff=633.37 |
| 267 | `payments` | 01/15/2024 | extracted=135.86  expected=None |
| 267 | `balance` | 01/15/2024 | extracted=0.0  expected=55.49  diff=55.49 |
| 267 | `provider` | 01/15/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 268 | `provider` | 11/10/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 269 | `payments` | 08/12/2023 | extracted=13.9  expected=None |
| 269 | `provider` | 08/12/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 270 | `payments` | 08/06/2022 | extracted=42.61  expected=None |
| 270 | `provider` | 08/06/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 271 | `payments` | 11/18/2023 | extracted=12.66  expected=None |
| 271 | `provider` | 11/18/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 272 | `payments` | 12/26/2021 | extracted=2.89  expected=None |
| 272 | `provider` | 12/26/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 273 | `payments` | 01/22/2024 | extracted=21.96  expected=None |
| 273 | `provider` | 01/22/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 274 | `payments` | 01/31/2022 | extracted=5.98  expected=None |
| 274 | `provider` | 01/31/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 275 | `payments` | 06/06/2022 | extracted=58.08  expected=None |
| 275 | `provider` | 06/06/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 276 | `payments` | 07/29/2024 | extracted=14.82  expected=None |
| 276 | `provider` | 07/29/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 277 | `provider` | 11/28/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 278 | `payments` | 01/28/2024 | extracted=30.91  expected=None |
| 278 | `provider` | 01/28/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 279 | `payments` | 03/09/2024 | extracted=37.69  expected=None |
| 279 | `provider` | 03/09/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 280 | `payments` | 07/18/2023 | extracted=10.92  expected=None |
| 280 | `provider` | 07/18/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 281 | `payments` | 06/29/2024 | extracted=30.67  expected=None |
| 281 | `provider` | 06/29/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 281 | `insurers` | 06/29/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 282 | `provider` | 01/11/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 283 | `provider` | 02/22/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 283 | `insurers` | 02/22/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 284 | `provider` | 11/05/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 285 | `provider` | 02/17/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 286 | `provider` | 11/15/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 287 | `payments` | 04/29/2021 | extracted=61.19  expected=None |
| 287 | `provider` | 04/29/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 288 | `payments` | 06/07/2024 | extracted=5.98  expected=None |
| 288 | `provider` | 06/07/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 289 | `provider` | 03/04/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 290 | `payments` | 11/23/2022 | extracted=57.62  expected=None |
| 290 | `provider` | 11/23/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 291 | `payments` | 07/21/2021 | extracted=6.68  expected=None |
| 291 | `provider` | 07/21/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 292 | `provider` | 05/29/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 293 | `provider` | 06/13/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 294 | `payments` | 05/15/2024 | extracted=23.68  expected=None |
| 294 | `provider` | 05/15/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 295 | `payments` | 04/04/2024 | extracted=17.72  expected=None |
| 295 | `provider` | 04/04/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 295 | `insurers` | 04/04/2024 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 296 | `payments` | 07/10/2024 | extracted=4.79  expected=None |
| 296 | `provider` | 07/10/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 297 | `payments` | 08/20/2024 | extracted=13.23  expected=None |
| 297 | `provider` | 08/20/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 298 | `provider` | 05/26/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 299 | `payments` | 02/18/2022 | extracted=80.67  expected=None |
| 299 | `provider` | 02/18/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 300 | `payments` | 10/31/2023 | extracted=43.37  expected=None |
| 300 | `provider` | 10/31/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 301 | `payments` | 03/05/2021 | extracted=62.03  expected=None |
| 301 | `provider` | 03/05/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 302 | `provider` | 12/17/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 303 | `payments` | 09/16/2022 | extracted=16.08  expected=None |
| 303 | `provider` | 09/16/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 304 | `payments` | 03/25/2023 | extracted=4.34  expected=None |
| 304 | `provider` | 03/25/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 305 | `payments` | 10/28/2021 | extracted=22.45  expected=None |
| 305 | `provider` | 10/28/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 306 | `cpt_codes` | 12/28/2022 | missing=['90960'] |
| 306 | `total_charges` | 12/28/2022 | extracted=1543.55  expected=1701.71  diff=158.16 |
| 306 | `ins_paid` | 12/28/2022 | extracted=731.48  expected=947.26  diff=215.78 |
| 306 | `adjustment` | 12/28/2022 | extracted=516.9  expected=754.45  diff=237.55 |
| 306 | `payments` | 12/28/2022 | extracted=295.17  expected=None |
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
| 348 | `payments` | 03/13/2021 | extracted=54.98  expected=None |
| 348 | `balance` | 03/13/2021 | extracted=0.0  expected=54.98  diff=54.98 |
| 348 | `provider` | 03/13/2021 | extracted='VALENTINE'  expected='Smith Medical, PC' |
| 348 | `description` | 03/13/2021 | extracted='Strep A test, direct'  expected=None |
| 349 | `payments` | 12/11/2021 | extracted=35.61  expected=None |
| 349 | `balance` | 12/11/2021 | extracted=0.0  expected=35.61  diff=35.61 |
| 349 | `provider` | 12/11/2021 | extracted='THOMAS'  expected='Smith Medical, PC' |
| 349 | `description` | 12/11/2021 | extracted='Colonoscopy with biopsy'  expected=None |
| 350 | `payments` | 12/16/2022 | extracted=22.94  expected=None |
| 350 | `balance` | 12/16/2022 | extracted=0.0  expected=22.94  diff=22.94 |
| 350 | `provider` | 12/16/2022 | extracted='SLOAN'  expected='Smith Medical, PC' |
| 350 | `description` | 12/16/2022 | extracted='Office/outpatient visit, new patient, level 4'  expected=None |
| 351 | `provider` | 02/25/2021 | extracted='HALL'  expected='Smith Medical, PC' |
| 351 | `description` | 02/25/2021 | extracted='Physical therapy — paraffin bath'  expected=None |
| 352 | `payments` | 07/17/2022 | extracted=18.99  expected=None |
| 352 | `balance` | 07/17/2022 | extracted=0.0  expected=18.99  diff=18.99 |
| 352 | `provider` | 07/17/2022 | extracted='SHAFFER'  expected='Smith Medical, PC' |
| 352 | `description` | 07/17/2022 | extracted='Emergency dept visit, level 5'  expected=None |
| 353 | `payments` | 02/18/2022 | extracted=53.39  expected=None |
| 353 | `balance` | 02/18/2022 | extracted=0.0  expected=53.39  diff=53.39 |
| 353 | `provider` | 02/18/2022 | extracted='MCKEE'  expected='Smith Medical, PC' |
| 353 | `description` | 02/18/2022 | extracted='Psychotherapy, 45 min'  expected=None |
| 354 | `payments` | 08/04/2022 | extracted=29.34  expected=None |
| 354 | `balance` | 08/04/2022 | extracted=0.0  expected=29.34  diff=29.34 |
| 354 | `provider` | 08/04/2022 | extracted='HOOPER'  expected='Smith Medical, PC' |
| 354 | `description` | 08/04/2022 | extracted='Total hip arthroplasty'  expected=None |
| 355 | `provider` | 04/20/2023 | extracted='RICHMOND'  expected='Smith Medical, PC' |
| 355 | `description` | 04/20/2023 | extracted='Physical therapy — paraffin bath'  expected=None |
| 356 | `payments` | 08/13/2021 | extracted=38.45  expected=None |
| 356 | `balance` | 08/13/2021 | extracted=0.0  expected=38.45  diff=38.45 |
| 356 | `provider` | 08/13/2021 | extracted='BARRETT'  expected='Smith Medical, PC' |
| 356 | `description` | 08/13/2021 | extracted='Therapeutic activities'  expected=None |
| 357 | `payments` | 06/23/2023 | extracted=9.63  expected=None |
| 357 | `balance` | 06/23/2023 | extracted=0.0  expected=9.63  diff=9.63 |
| 357 | `provider` | 06/23/2023 | extracted='DOMINGUEZ'  expected='Smith Medical, PC' |
| 357 | `description` | 06/23/2023 | extracted='ESRD home dialysis, per month, age 20+'  expected=None |
| 358 | `payments` | 06/19/2021 | extracted=35.19  expected=None |
| 358 | `balance` | 06/19/2021 | extracted=0.0  expected=35.19  diff=35.19 |
| 358 | `provider` | 06/19/2021 | extracted='NORTON'  expected='Smith Medical, PC' |
| 358 | `description` | 06/19/2021 | extracted='Office/outpatient visit, established patient, level 1'  expected=None |
| 359 | `payments` | 04/21/2021 | extracted=15.89  expected=None |
| 359 | `balance` | 04/21/2021 | extracted=0.0  expected=15.89  diff=15.89 |
| 359 | `provider` | 04/21/2021 | extracted='JOHNSON'  expected='Smith Medical, PC' |
| 359 | `description` | 04/21/2021 | extracted='Self-care/home management training'  expected=None |
| 360 | `provider` | 10/31/2022 | extracted='PARKER'  expected='Smith Medical, PC' |
| 360 | `description` | 10/31/2022 | extracted='Cataract surgery with IOL'  expected=None |
| 361 | `payments` | 07/09/2022 | extracted=28.9  expected=None |
| 361 | `balance` | 07/09/2022 | extracted=0.0  expected=28.9  diff=28.90 |
| 361 | `provider` | 07/09/2022 | extracted='MAY'  expected='Smith Medical, PC' |
| 361 | `description` | 07/09/2022 | extracted='Physical therapy — whirlpool'  expected=None |
| 362 | `payments` | 12/14/2023 | extracted=17.43  expected=None |
| 362 | `balance` | 12/14/2023 | extracted=0.0  expected=17.43  diff=17.43 |
| 362 | `provider` | 12/14/2023 | extracted='ADAMS'  expected='Smith Medical, PC' |
| 362 | `insurers` | 12/14/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 362 | `description` | 12/14/2023 | extracted='Office/outpatient visit, established patient, level 2'  expected=None |
| 363 | `provider` | 06/28/2023 | extracted='GARRETT'  expected='Smith Medical, PC' |
| 363 | `description` | 06/28/2023 | extracted='Physical therapy — electrical stimulation'  expected=None |
| 364 | `payments` | 02/02/2023 | extracted=47.26  expected=None |
| 364 | `balance` | 02/02/2023 | extracted=0.0  expected=47.26  diff=47.26 |
| 364 | `provider` | 02/02/2023 | extracted='WHITE'  expected='Smith Medical, PC' |
| 364 | `insurers` | 02/02/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 364 | `description` | 02/02/2023 | extracted='Physical therapy — electrical stimulation'  expected=None |
| 365 | `payments` | 05/24/2023 | extracted=44.17  expected=None |
| 365 | `balance` | 05/24/2023 | extracted=0.0  expected=44.17  diff=44.17 |
| 365 | `provider` | 05/24/2023 | extracted='WILLIAMS'  expected='Smith Medical, PC' |
| 365 | `description` | 05/24/2023 | extracted='Lipid panel'  expected=None |
| 366 | `provider` | 04/25/2021 | extracted='GOMEZ'  expected='Smith Medical, PC' |
| 366 | `insurers` | 04/25/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 366 | `description` | 04/25/2021 | extracted='X-ray humerus, minimum 2 views'  expected=None |
| 367 | `provider` | 02/21/2022 | extracted='BURNS'  expected='Smith Medical, PC' |
| 367 | `insurers` | 02/21/2022 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 367 | `description` | 02/21/2022 | extracted='Physical therapy — ultrasound'  expected=None |
| 368 | `payments` | 10/20/2022 | extracted=25.16  expected=None |
| 368 | `balance` | 10/20/2022 | extracted=0.0  expected=25.16  diff=25.16 |
| 368 | `provider` | 10/20/2022 | extracted='BROWN'  expected='Smith Medical, PC' |
| 368 | `description` | 10/20/2022 | extracted='Immunization administration, first injection'  expected=None |
| 369 | `payments` | 12/21/2024 | extracted=32.42  expected=None |
| 369 | `balance` | 12/21/2024 | extracted=0.0  expected=32.42  diff=32.42 |
| 369 | `provider` | 12/21/2024 | extracted='RICHARDSON'  expected='Smith Medical, PC' |
| 369 | `description` | 12/21/2024 | extracted='Physical therapy — hot or cold packs'  expected=None |
| 370 | `provider` | 08/26/2022 | extracted='BOYD'  expected='Smith Medical, PC' |
| 370 | `description` | 08/26/2022 | extracted='Emergency dept visit, level 2'  expected=None |
| 371 | `payments` | 07/10/2021 | extracted=38.17  expected=None |
| 371 | `balance` | 07/10/2021 | extracted=0.0  expected=38.17  diff=38.17 |
| 371 | `provider` | 07/10/2021 | extracted='WILSON'  expected='Smith Medical, PC' |
| 371 | `description` | 07/10/2021 | extracted='Cisplatin, per 10 mg'  expected=None |
| 372 | `payments` | 05/11/2021 | extracted=21.47  expected=None |
| 372 | `balance` | 05/11/2021 | extracted=0.0  expected=21.47  diff=21.47 |
| 372 | `provider` | 05/11/2021 | extracted='GONZALEZ'  expected='Smith Medical, PC' |
| 372 | `description` | 05/11/2021 | extracted='Cataract surgery with IOL'  expected=None |
| 373 | `payments` | 10/15/2024 | extracted=15.45  expected=None |
| 373 | `balance` | 10/15/2024 | extracted=0.0  expected=15.45  diff=15.45 |
| 373 | `provider` | 10/15/2024 | extracted='HOFFMAN'  expected='Smith Medical, PC' |
| 373 | `description` | 10/15/2024 | extracted='Physical therapy — ultrasound'  expected=None |
| 374 | `payments` | 12/30/2021 | extracted=6.96  expected=None |
| 374 | `balance` | 12/30/2021 | extracted=0.0  expected=6.96  diff=6.96 |
| 374 | `provider` | 12/30/2021 | extracted='YORK'  expected='Smith Medical, PC' |
| 374 | `description` | 12/30/2021 | extracted='Cardiovascular stress test'  expected=None |
| 375 | `provider` | 07/05/2024 | extracted='STEWART'  expected='Smith Medical, PC' |
| 375 | `description` | 07/05/2024 | extracted='Betadine wipes, per box'  expected=None |
| 376 | `provider` | 01/28/2024 | extracted='BOOKER'  expected='Smith Medical, PC' |
| 376 | `description` | 01/28/2024 | extracted='Hemodialysis access flow study'  expected=None |
| 377 | `payments` | 08/27/2023 | extracted=17.57  expected=None |
| 377 | `balance` | 08/27/2023 | extracted=0.0  expected=17.57  diff=17.57 |
| 377 | `provider` | 08/27/2023 | extracted='BROWN'  expected='Smith Medical, PC' |
| 377 | `description` | 08/27/2023 | extracted='E&M level 4 with modifier 25'  expected=None |
| 378 | `payments` | 08/11/2021 | extracted=4.91  expected=None |
| 378 | `balance` | 08/11/2021 | extracted=0.0  expected=4.91  diff=4.91 |
| 378 | `provider` | 08/11/2021 | extracted='SANCHEZ'  expected='Smith Medical, PC' |
| 378 | `description` | 08/11/2021 | extracted='Subsequent hospital care, level 2'  expected=None |
| 379 | `provider` | 04/28/2023 | extracted='DAVIS'  expected='Smith Medical, PC' |
| 379 | `description` | 04/28/2023 | extracted='X-ray wrist, minimum 3 views'  expected=None |
| 380 | `payments` | 08/19/2021 | extracted=21.11  expected=None |
| 380 | `balance` | 08/19/2021 | extracted=0.0  expected=21.11  diff=21.11 |
| 380 | `provider` | 08/19/2021 | extracted='HARRIS'  expected='Smith Medical, PC' |
| 380 | `description` | 08/19/2021 | extracted='Office/outpatient visit, new patient, level 1'  expected=None |
| 381 | `payments` | 12/06/2024 | extracted=27.23  expected=None |
| 381 | `balance` | 12/06/2024 | extracted=0.0  expected=27.23  diff=27.23 |
| 381 | `provider` | 12/06/2024 | extracted='DAVIS'  expected='Smith Medical, PC' |
| 381 | `description` | 12/06/2024 | extracted='Echocardiography, transthoracic, complete'  expected=None |
| 382 | `payments` | 01/18/2023 | extracted=15.8  expected=None |
| 382 | `balance` | 01/18/2023 | extracted=0.0  expected=15.8  diff=15.80 |
| 382 | `provider` | 01/18/2023 | extracted='STEPHENS'  expected='Smith Medical, PC' |
| 382 | `description` | 01/18/2023 | extracted='Office/outpatient visit, new patient, level 1'  expected=None |
| 383 | `provider` | 12/14/2021 | extracted='FISHER'  expected='Smith Medical, PC' |
| 383 | `description` | 12/14/2021 | extracted='Urine culture'  expected=None |
| 384 | `payments` | 08/11/2024 | extracted=69.66  expected=None |
| 384 | `balance` | 08/11/2024 | extracted=0.0  expected=69.66  diff=69.66 |
| 384 | `provider` | 08/11/2024 | extracted='JACOBS'  expected='Smith Medical, PC' |
| 384 | `description` | 08/11/2024 | extracted='Family psychotherapy with patient'  expected=None |
| 386 | `cpt_codes` | 01/08/2021 | missing=['85027', '97010', '97018', '99221'] |
| 386 | `payments` | 01/08/2021 | extracted=24.5  expected=None |
| 386 | `balance` | 01/08/2021 | extracted=0.0  expected=24.5  diff=24.50 |
| 386 | `provider` | 01/08/2021 | extracted='GREGORY JAMES'  expected='Smith Medical, PC' |
| 387 | `payments` | 02/19/2022 | extracted=23.84  expected=None |
| 387 | `balance` | 02/19/2022 | extracted=0.0  expected=23.84  diff=23.84 |
| 387 | `provider` | 02/19/2022 | extracted='DELACRUZ SHERRY'  expected='Smith Medical, PC' |
| 388 | `payments` | 01/23/2022 | extracted=47.38  expected=None |
| 388 | `balance` | 01/23/2022 | extracted=0.0  expected=47.38  diff=47.38 |
| 388 | `provider` | 01/23/2022 | extracted='RICHARDSON KEITH'  expected='Smith Medical, PC' |
| 389 | `provider` | 06/05/2022 | extracted='DOYLE JENNIFER'  expected='Smith Medical, PC' |
| 390 | `payments` | 04/20/2021 | extracted=9.62  expected=None |
| 390 | `balance` | 04/20/2021 | extracted=0.0  expected=9.62  diff=9.62 |
| 390 | `provider` | 04/20/2021 | extracted='FARMER VANESSA'  expected='Smith Medical, PC' |
| 391 | `provider` | 11/19/2022 | extracted='RIVAS PAIGE'  expected='Smith Medical, PC' |
| 392 | `payments` | 04/13/2021 | extracted=8.07  expected=None |
| 392 | `balance` | 04/13/2021 | extracted=0.0  expected=8.07  diff=8.07 |
| 392 | `provider` | 04/13/2021 | extracted='GOLDEN DARREN'  expected='Smith Medical, PC' |
| 393 | `payments` | 08/10/2024 | extracted=31.99  expected=None |
| 393 | `balance` | 08/10/2024 | extracted=0.0  expected=31.99  diff=31.99 |
| 393 | `provider` | 08/10/2024 | extracted='DAVIS NATASHA'  expected='Smith Medical, PC' |
| 394 | `payments` | 07/22/2024 | extracted=5.56  expected=None |
| 394 | `balance` | 07/22/2024 | extracted=0.0  expected=5.56  diff=5.56 |
| 394 | `provider` | 07/22/2024 | extracted='DEAN ERIK'  expected='Smith Medical, PC' |
| 395 | `payments` | 06/30/2023 | extracted=51.64  expected=None |
| 395 | `balance` | 06/30/2023 | extracted=0.0  expected=51.64  diff=51.64 |
| 395 | `provider` | 06/30/2023 | extracted='BREWER ANDREW'  expected='Smith Medical, PC' |
| 396 | `provider` | 06/24/2023 | extracted='BERRY SANDRA'  expected='Smith Medical, PC' |
| 396 | `insurers` | 06/24/2023 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 397 | `payments` | 11/23/2022 | extracted=63.3  expected=None |
| 397 | `balance` | 11/23/2022 | extracted=0.0  expected=63.3  diff=63.30 |
| 397 | `provider` | 11/23/2022 | extracted='BROWN MICHAEL'  expected='Smith Medical, PC' |
| 398 | `provider` | 08/25/2024 | extracted='RIOS STEPHANIE'  expected='Smith Medical, PC' |
| 399 | `payments` | 01/12/2021 | extracted=24.5  expected=None |
| 399 | `balance` | 01/12/2021 | extracted=0.0  expected=24.5  diff=24.50 |
| 399 | `provider` | 01/12/2021 | extracted='SNYDER DAVID'  expected='Smith Medical, PC' |

### doc_008

**Count mismatch** — GT: 100, extracted: 1474.

**Extra extracted records (1392):**
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
- `02/23/2022` — Extracted record has no GT counterpart
- `03/02/2021` — Extracted record has no GT counterpart
- `08/10/2022` — Extracted record has no GT counterpart
- `08/20/2021` — Extracted record has no GT counterpart
- `10/10/2023` — Extracted record has no GT counterpart
- `04/04/2022` — Extracted record has no GT counterpart
- `09/16/2022` — Extracted record has no GT counterpart
- `04/25/2024` — Extracted record has no GT counterpart
- `06/20/2022` — Extracted record has no GT counterpart
- `12/13/2023` — Extracted record has no GT counterpart
- `11/19/2024` — Extracted record has no GT counterpart
- `06/21/2024` — Extracted record has no GT counterpart
- `11/06/2024` — Extracted record has no GT counterpart
- `07/07/2023` — Extracted record has no GT counterpart
- `10/07/2022` — Extracted record has no GT counterpart
- `10/13/2022` — Extracted record has no GT counterpart
- `07/18/2023` — Extracted record has no GT counterpart
- `03/23/2024` — Extracted record has no GT counterpart
- `03/24/2023` — Extracted record has no GT counterpart
- `03/17/2022` — Extracted record has no GT counterpart
- `02/21/2024` — Extracted record has no GT counterpart
- `07/22/2022` — Extracted record has no GT counterpart
- `04/06/2023` — Extracted record has no GT counterpart
- `07/19/2024` — Extracted record has no GT counterpart
- `02/04/2024` — Extracted record has no GT counterpart
- `11/04/2024` — Extracted record has no GT counterpart
- `10/02/2022` — Extracted record has no GT counterpart
- `01/14/2023` — Extracted record has no GT counterpart
- `04/16/2024` — Extracted record has no GT counterpart
- `07/30/2024` — Extracted record has no GT counterpart
- `11/23/2022` — Extracted record has no GT counterpart
- `11/26/2023` — Extracted record has no GT counterpart
- `04/19/2024` — Extracted record has no GT counterpart
- `02/06/2024` — Extracted record has no GT counterpart
- `01/09/2023` — Extracted record has no GT counterpart
- `07/03/2022` — Extracted record has no GT counterpart
- `06/08/2022` — Extracted record has no GT counterpart
- `08/18/2022` — Extracted record has no GT counterpart
- `07/20/2021` — Extracted record has no GT counterpart
- `12/06/2023` — Extracted record has no GT counterpart
- `05/01/2024` — Extracted record has no GT counterpart
- `12/05/2022` — Extracted record has no GT counterpart
- `08/04/2023` — Extracted record has no GT counterpart
- `11/22/2023` — Extracted record has no GT counterpart
- `01/07/2024` — Extracted record has no GT counterpart
- `10/19/2021` — Extracted record has no GT counterpart
- `09/23/2023` — Extracted record has no GT counterpart
- `10/11/2024` — Extracted record has no GT counterpart
- `08/20/2022` — Extracted record has no GT counterpart
- `08/24/2021` — Extracted record has no GT counterpart
- `08/31/2022` — Extracted record has no GT counterpart
- `12/18/2022` — Extracted record has no GT counterpart
- `06/05/2022` — Extracted record has no GT counterpart
- `02/21/2022` — Extracted record has no GT counterpart
- `12/03/2023` — Extracted record has no GT counterpart
- `06/25/2022` — Extracted record has no GT counterpart
- `02/10/2022` — Extracted record has no GT counterpart
- `05/27/2023` — Extracted record has no GT counterpart
- `02/19/2022` — Extracted record has no GT counterpart
- `01/24/2024` — Extracted record has no GT counterpart
- `06/29/2022` — Extracted record has no GT counterpart
- `12/20/2022` — Extracted record has no GT counterpart
- `01/20/2022` — Extracted record has no GT counterpart
- `06/20/2024` — Extracted record has no GT counterpart
- `12/02/2021` — Extracted record has no GT counterpart
- `08/12/2021` — Extracted record has no GT counterpart
- `07/23/2022` — Extracted record has no GT counterpart
- `08/08/2023` — Extracted record has no GT counterpart
- `11/14/2021` — Extracted record has no GT counterpart
- `06/04/2023` — Extracted record has no GT counterpart
- `08/08/2021` — Extracted record has no GT counterpart
- `10/31/2024` — Extracted record has no GT counterpart
- `01/15/2024` — Extracted record has no GT counterpart
- `09/08/2021` — Extracted record has no GT counterpart
- `02/25/2022` — Extracted record has no GT counterpart
- `06/06/2023` — Extracted record has no GT counterpart
- `04/06/2022` — Extracted record has no GT counterpart
- `08/03/2021` — Extracted record has no GT counterpart
- `10/19/2021` — Extracted record has no GT counterpart
- `11/04/2022` — Extracted record has no GT counterpart
- `12/18/2024` — Extracted record has no GT counterpart
- `09/26/2022` — Extracted record has no GT counterpart
- `02/03/2023` — Extracted record has no GT counterpart
- `08/04/2023` — Extracted record has no GT counterpart
- `12/03/2021` — Extracted record has no GT counterpart
- `10/17/2024` — Extracted record has no GT counterpart
- `04/11/2023` — Extracted record has no GT counterpart
- `11/04/2024` — Extracted record has no GT counterpart
- `11/28/2023` — Extracted record has no GT counterpart
- `02/27/2023` — Extracted record has no GT counterpart
- `12/27/2022` — Extracted record has no GT counterpart
- `10/26/2024` — Extracted record has no GT counterpart
- `06/24/2023` — Extracted record has no GT counterpart
- `06/03/2021` — Extracted record has no GT counterpart
- `06/15/2023` — Extracted record has no GT counterpart
- `08/11/2022` — Extracted record has no GT counterpart
- `02/24/2022` — Extracted record has no GT counterpart
- `09/05/2021` — Extracted record has no GT counterpart
- `05/06/2023` — Extracted record has no GT counterpart
- `08/28/2024` — Extracted record has no GT counterpart
- `12/27/2021` — Extracted record has no GT counterpart
- `04/03/2022` — Extracted record has no GT counterpart
- `01/20/2023` — Extracted record has no GT counterpart
- `02/04/2023` — Extracted record has no GT counterpart
- `10/20/2024` — Extracted record has no GT counterpart
- `10/06/2024` — Extracted record has no GT counterpart
- `12/16/2023` — Extracted record has no GT counterpart
- `02/13/2023` — Extracted record has no GT counterpart
- `06/08/2023` — Extracted record has no GT counterpart
- `11/24/2023` — Extracted record has no GT counterpart
- `08/08/2024` — Extracted record has no GT counterpart
- `09/02/2024` — Extracted record has no GT counterpart
- `01/14/2022` — Extracted record has no GT counterpart
- `07/16/2021` — Extracted record has no GT counterpart
- `09/27/2021` — Extracted record has no GT counterpart
- `06/03/2021` — Extracted record has no GT counterpart
- `01/18/2023` — Extracted record has no GT counterpart
- `02/14/2022` — Extracted record has no GT counterpart
- `05/16/2022` — Extracted record has no GT counterpart
- `12/04/2023` — Extracted record has no GT counterpart
- `05/09/2024` — Extracted record has no GT counterpart
- `05/29/2022` — Extracted record has no GT counterpart
- `05/24/2022` — Extracted record has no GT counterpart
- `11/12/2023` — Extracted record has no GT counterpart
- `01/12/2024` — Extracted record has no GT counterpart
- `02/14/2024` — Extracted record has no GT counterpart
- `11/25/2023` — Extracted record has no GT counterpart
- `05/14/2023` — Extracted record has no GT counterpart
- `06/18/2023` — Extracted record has no GT counterpart
- `10/22/2024` — Extracted record has no GT counterpart
- `11/23/2021` — Extracted record has no GT counterpart
- `02/06/2024` — Extracted record has no GT counterpart
- `03/18/2021` — Extracted record has no GT counterpart
- `03/18/2021` — Extracted record has no GT counterpart
- `07/04/2023` — Extracted record has no GT counterpart
- `07/08/2023` — Extracted record has no GT counterpart
- `09/10/2023` — Extracted record has no GT counterpart
- `04/15/2023` — Extracted record has no GT counterpart
- `08/24/2024` — Extracted record has no GT counterpart
- `04/26/2023` — Extracted record has no GT counterpart
- `12/21/2024` — Extracted record has no GT counterpart
- `06/25/2021` — Extracted record has no GT counterpart
- `09/14/2023` — Extracted record has no GT counterpart
- `06/02/2024` — Extracted record has no GT counterpart
- `01/03/2024` — Extracted record has no GT counterpart
- `01/14/2024` — Extracted record has no GT counterpart
- `09/25/2021` — Extracted record has no GT counterpart
- `03/10/2023` — Extracted record has no GT counterpart
- `12/21/2021` — Extracted record has no GT counterpart
- `05/27/2021` — Extracted record has no GT counterpart
- `04/22/2023` — Extracted record has no GT counterpart
- `11/07/2023` — Extracted record has no GT counterpart
- `11/18/2021` — Extracted record has no GT counterpart
- `02/08/2023` — Extracted record has no GT counterpart
- `07/28/2021` — Extracted record has no GT counterpart
- `10/26/2023` — Extracted record has no GT counterpart
- `09/19/2021` — Extracted record has no GT counterpart
- `03/29/2021` — Extracted record has no GT counterpart
- `01/18/2023` — Extracted record has no GT counterpart
- `11/01/2021` — Extracted record has no GT counterpart
- `10/07/2022` — Extracted record has no GT counterpart
- `06/03/2023` — Extracted record has no GT counterpart
- `05/17/2021` — Extracted record has no GT counterpart
- `08/07/2023` — Extracted record has no GT counterpart
- `11/15/2024` — Extracted record has no GT counterpart
- `11/12/2022` — Extracted record has no GT counterpart
- `01/26/2022` — Extracted record has no GT counterpart
- `02/03/2022` — Extracted record has no GT counterpart
- `12/13/2024` — Extracted record has no GT counterpart
- `08/25/2021` — Extracted record has no GT counterpart
- `08/14/2022` — Extracted record has no GT counterpart
- `04/02/2022` — Extracted record has no GT counterpart
- `03/11/2023` — Extracted record has no GT counterpart
- `12/04/2021` — Extracted record has no GT counterpart
- `12/01/2021` — Extracted record has no GT counterpart
- `06/20/2023` — Extracted record has no GT counterpart
- `03/05/2023` — Extracted record has no GT counterpart
- `08/05/2024` — Extracted record has no GT counterpart
- `06/25/2023` — Extracted record has no GT counterpart
- `07/22/2021` — Extracted record has no GT counterpart
- `05/26/2024` — Extracted record has no GT counterpart
- `08/17/2023` — Extracted record has no GT counterpart
- `07/14/2023` — Extracted record has no GT counterpart
- `11/17/2022` — Extracted record has no GT counterpart
- `07/03/2024` — Extracted record has no GT counterpart
- `02/12/2023` — Extracted record has no GT counterpart
- `10/14/2024` — Extracted record has no GT counterpart
- `05/22/2024` — Extracted record has no GT counterpart
- `04/21/2022` — Extracted record has no GT counterpart
- `05/06/2022` — Extracted record has no GT counterpart
- `07/28/2023` — Extracted record has no GT counterpart
- `11/05/2021` — Extracted record has no GT counterpart
- `06/02/2022` — Extracted record has no GT counterpart
- `06/05/2024` — Extracted record has no GT counterpart
- `07/09/2023` — Extracted record has no GT counterpart
- `04/28/2023` — Extracted record has no GT counterpart
- `07/30/2023` — Extracted record has no GT counterpart
- `01/27/2022` — Extracted record has no GT counterpart
- `10/23/2022` — Extracted record has no GT counterpart
- `09/07/2023` — Extracted record has no GT counterpart
- `09/09/2023` — Extracted record has no GT counterpart
- `06/20/2023` — Extracted record has no GT counterpart
- `03/15/2023` — Extracted record has no GT counterpart
- `02/10/2022` — Extracted record has no GT counterpart
- `06/13/2024` — Extracted record has no GT counterpart
- `03/24/2023` — Extracted record has no GT counterpart
- `06/10/2022` — Extracted record has no GT counterpart
- `02/18/2023` — Extracted record has no GT counterpart
- `12/01/2021` — Extracted record has no GT counterpart
- `11/30/2021` — Extracted record has no GT counterpart
- `08/15/2022` — Extracted record has no GT counterpart
- `03/22/2021` — Extracted record has no GT counterpart
- `10/10/2022` — Extracted record has no GT counterpart
- `09/09/2021` — Extracted record has no GT counterpart
- `11/24/2024` — Extracted record has no GT counterpart
- `12/24/2021` — Extracted record has no GT counterpart
- `02/09/2022` — Extracted record has no GT counterpart
- `06/14/2024` — Extracted record has no GT counterpart
- `07/06/2023` — Extracted record has no GT counterpart
- `12/25/2021` — Extracted record has no GT counterpart
- `03/14/2022` — Extracted record has no GT counterpart
- `09/25/2023` — Extracted record has no GT counterpart
- `01/12/2023` — Extracted record has no GT counterpart
- `03/28/2022` — Extracted record has no GT counterpart
- `12/22/2021` — Extracted record has no GT counterpart
- `05/17/2024` — Extracted record has no GT counterpart
- `05/17/2024` — Extracted record has no GT counterpart
- `11/27/2022` — Extracted record has no GT counterpart
- `05/31/2023` — Extracted record has no GT counterpart
- `08/17/2024` — Extracted record has no GT counterpart
- `05/24/2022` — Extracted record has no GT counterpart
- `05/17/2022` — Extracted record has no GT counterpart
- `10/12/2022` — Extracted record has no GT counterpart
- `06/18/2022` — Extracted record has no GT counterpart
- `07/06/2022` — Extracted record has no GT counterpart
- `06/17/2024` — Extracted record has no GT counterpart
- `07/02/2024` — Extracted record has no GT counterpart
- `11/15/2021` — Extracted record has no GT counterpart
- `01/01/2024` — Extracted record has no GT counterpart
- `07/10/2022` — Extracted record has no GT counterpart
- `08/09/2021` — Extracted record has no GT counterpart
- `10/14/2023` — Extracted record has no GT counterpart
- `04/06/2024` — Extracted record has no GT counterpart
- `07/19/2024` — Extracted record has no GT counterpart
- `03/07/2023` — Extracted record has no GT counterpart
- `12/23/2024` — Extracted record has no GT counterpart
- `02/23/2023` — Extracted record has no GT counterpart
- `02/27/2023` — Extracted record has no GT counterpart
- `04/15/2022` — Extracted record has no GT counterpart
- `10/28/2024` — Extracted record has no GT counterpart
- `07/01/2023` — Extracted record has no GT counterpart
- `07/02/2023` — Extracted record has no GT counterpart
- `05/18/2024` — Extracted record has no GT counterpart
- `10/25/2024` — Extracted record has no GT counterpart
- `02/06/2021` — Extracted record has no GT counterpart
- `10/02/2024` — Extracted record has no GT counterpart
- `03/05/2022` — Extracted record has no GT counterpart
- `01/01/2023` — Extracted record has no GT counterpart
- `03/07/2021` — Extracted record has no GT counterpart
- `04/04/2021` — Extracted record has no GT counterpart
- `08/12/2022` — Extracted record has no GT counterpart
- `05/30/2022` — Extracted record has no GT counterpart
- `11/02/2021` — Extracted record has no GT counterpart
- `10/28/2024` — Extracted record has no GT counterpart
- `01/14/2024` — Extracted record has no GT counterpart
- `09/28/2023` — Extracted record has no GT counterpart
- `03/20/2023` — Extracted record has no GT counterpart
- `05/01/2023` — Extracted record has no GT counterpart
- `11/23/2024` — Extracted record has no GT counterpart
- `01/30/2022` — Extracted record has no GT counterpart
- `07/25/2024` — Extracted record has no GT counterpart
- `03/10/2024` — Extracted record has no GT counterpart
- `02/24/2023` — Extracted record has no GT counterpart
- `03/26/2023` — Extracted record has no GT counterpart
- `06/01/2022` — Extracted record has no GT counterpart
- `03/17/2023` — Extracted record has no GT counterpart
- `07/18/2023` — Extracted record has no GT counterpart
- `09/08/2021` — Extracted record has no GT counterpart
- `05/30/2024` — Extracted record has no GT counterpart
- `12/28/2023` — Extracted record has no GT counterpart
- `12/08/2022` — Extracted record has no GT counterpart
- `01/10/2024` — Extracted record has no GT counterpart
- `04/07/2022` — Extracted record has no GT counterpart
- `07/20/2024` — Extracted record has no GT counterpart
- `02/12/2021` — Extracted record has no GT counterpart
- `01/11/2024` — Extracted record has no GT counterpart
- `03/11/2022` — Extracted record has no GT counterpart
- `08/07/2023` — Extracted record has no GT counterpart
- `11/23/2022` — Extracted record has no GT counterpart
- `06/15/2024` — Extracted record has no GT counterpart
- `05/20/2023` — Extracted record has no GT counterpart
- `10/16/2021` — Extracted record has no GT counterpart
- `12/02/2021` — Extracted record has no GT counterpart
- `06/13/2022` — Extracted record has no GT counterpart
- `01/02/2024` — Extracted record has no GT counterpart
- `12/07/2021` — Extracted record has no GT counterpart
- `04/20/2022` — Extracted record has no GT counterpart
- `09/18/2023` — Extracted record has no GT counterpart
- `04/09/2023` — Extracted record has no GT counterpart
- `09/12/2024` — Extracted record has no GT counterpart
- `09/21/2021` — Extracted record has no GT counterpart
- `08/31/2024` — Extracted record has no GT counterpart
- `12/30/2023` — Extracted record has no GT counterpart
- `09/22/2022` — Extracted record has no GT counterpart
- `05/26/2023` — Extracted record has no GT counterpart
- `01/16/2022` — Extracted record has no GT counterpart
- `03/12/2024` — Extracted record has no GT counterpart
- `03/18/2024` — Extracted record has no GT counterpart
- `04/05/2022` — Extracted record has no GT counterpart
- `08/16/2024` — Extracted record has no GT counterpart
- `07/19/2021` — Extracted record has no GT counterpart
- `04/03/2022` — Extracted record has no GT counterpart
- `11/21/2022` — Extracted record has no GT counterpart
- `08/08/2024` — Extracted record has no GT counterpart
- `11/01/2023` — Extracted record has no GT counterpart
- `04/02/2024` — Extracted record has no GT counterpart
- `11/25/2024` — Extracted record has no GT counterpart
- `02/14/2022` — Extracted record has no GT counterpart
- `06/11/2023` — Extracted record has no GT counterpart
- `06/27/2023` — Extracted record has no GT counterpart
- `12/12/2024` — Extracted record has no GT counterpart
- `08/18/2022` — Extracted record has no GT counterpart
- `09/25/2021` — Extracted record has no GT counterpart
- `12/07/2023` — Extracted record has no GT counterpart
- `04/10/2024` — Extracted record has no GT counterpart
- `04/21/2024` — Extracted record has no GT counterpart
- `07/29/2021` — Extracted record has no GT counterpart
- `02/22/2024` — Extracted record has no GT counterpart
- `06/09/2022` — Extracted record has no GT counterpart
- `06/20/2022` — Extracted record has no GT counterpart
- `04/02/2023` — Extracted record has no GT counterpart
- `12/31/2021` — Extracted record has no GT counterpart
- `01/31/2023` — Extracted record has no GT counterpart
- `12/28/2024` — Extracted record has no GT counterpart
- `10/30/2024` — Extracted record has no GT counterpart
- `05/10/2023` — Extracted record has no GT counterpart
- `01/23/2024` — Extracted record has no GT counterpart
- `01/03/2024` — Extracted record has no GT counterpart
- `07/28/2024` — Extracted record has no GT counterpart
- `01/14/2024` — Extracted record has no GT counterpart
- `01/17/2023` — Extracted record has no GT counterpart
- `08/13/2024` — Extracted record has no GT counterpart
- `03/09/2024` — Extracted record has no GT counterpart
- `08/28/2024` — Extracted record has no GT counterpart
- `02/21/2024` — Extracted record has no GT counterpart
- `10/05/2021` — Extracted record has no GT counterpart
- `10/25/2023` — Extracted record has no GT counterpart
- `04/24/2024` — Extracted record has no GT counterpart
- `06/01/2022` — Extracted record has no GT counterpart
- `01/07/2024` — Extracted record has no GT counterpart
- `11/23/2024` — Extracted record has no GT counterpart
- `05/02/2023` — Extracted record has no GT counterpart
- `12/12/2021` — Extracted record has no GT counterpart
- `04/28/2023` — Extracted record has no GT counterpart
- `10/02/2024` — Extracted record has no GT counterpart
- `01/15/2021` — Extracted record has no GT counterpart
- `01/07/2024` — Extracted record has no GT counterpart
- `09/09/2023` — Extracted record has no GT counterpart
- `05/19/2023` — Extracted record has no GT counterpart
- `08/16/2023` — Extracted record has no GT counterpart
- `07/06/2022` — Extracted record has no GT counterpart
- `03/30/2024` — Extracted record has no GT counterpart
- `07/20/2023` — Extracted record has no GT counterpart
- `09/18/2024` — Extracted record has no GT counterpart
- `04/10/2024` — Extracted record has no GT counterpart
- `07/28/2024` — Extracted record has no GT counterpart
- `12/21/2022` — Extracted record has no GT counterpart
- `05/07/2022` — Extracted record has no GT counterpart
- `11/01/2021` — Extracted record has no GT counterpart
- `08/19/2024` — Extracted record has no GT counterpart
- `09/19/2024` — Extracted record has no GT counterpart
- `01/19/2023` — Extracted record has no GT counterpart
- `10/17/2024` — Extracted record has no GT counterpart
- `09/10/2024` — Extracted record has no GT counterpart
- `10/29/2024` — Extracted record has no GT counterpart
- `11/28/2021` — Extracted record has no GT counterpart
- `09/18/2023` — Extracted record has no GT counterpart
- `12/23/2021` — Extracted record has no GT counterpart
- `03/26/2023` — Extracted record has no GT counterpart
- `01/15/2022` — Extracted record has no GT counterpart
- `12/30/2022` — Extracted record has no GT counterpart
- `03/07/2022` — Extracted record has no GT counterpart
- `06/17/2024` — Extracted record has no GT counterpart
- `07/27/2024` — Extracted record has no GT counterpart
- `05/20/2023` — Extracted record has no GT counterpart
- `08/16/2021` — Extracted record has no GT counterpart
- `12/12/2024` — Extracted record has no GT counterpart
- `09/18/2023` — Extracted record has no GT counterpart
- `03/17/2024` — Extracted record has no GT counterpart
- `07/06/2022` — Extracted record has no GT counterpart
- `09/20/2023` — Extracted record has no GT counterpart
- `07/28/2023` — Extracted record has no GT counterpart
- `03/12/2022` — Extracted record has no GT counterpart
- `06/19/2024` — Extracted record has no GT counterpart
- `11/15/2024` — Extracted record has no GT counterpart
- `10/14/2024` — Extracted record has no GT counterpart
- `10/20/2024` — Extracted record has no GT counterpart
- `12/07/2022` — Extracted record has no GT counterpart
- `08/29/2024` — Extracted record has no GT counterpart
- `07/10/2023` — Extracted record has no GT counterpart
- `04/28/2023` — Extracted record has no GT counterpart
- `12/10/2021` — Extracted record has no GT counterpart
- `04/05/2022` — Extracted record has no GT counterpart
- `04/10/2023` — Extracted record has no GT counterpart
- `06/27/2024` — Extracted record has no GT counterpart
- `11/08/2023` — Extracted record has no GT counterpart
- `09/30/2022` — Extracted record has no GT counterpart
- `02/06/2022` — Extracted record has no GT counterpart
- `08/05/2021` — Extracted record has no GT counterpart
- `08/13/2024` — Extracted record has no GT counterpart
- `10/30/2022` — Extracted record has no GT counterpart
- `05/20/2022` — Extracted record has no GT counterpart
- `08/05/2023` — Extracted record has no GT counterpart
- `11/21/2024` — Extracted record has no GT counterpart
- `02/01/2022` — Extracted record has no GT counterpart
- `06/13/2022` — Extracted record has no GT counterpart
- `06/02/2022` — Extracted record has no GT counterpart
- `11/28/2024` — Extracted record has no GT counterpart
- `06/16/2021` — Extracted record has no GT counterpart
- `07/30/2023` — Extracted record has no GT counterpart
- `04/25/2021` — Extracted record has no GT counterpart
- `07/23/2024` — Extracted record has no GT counterpart
- `03/01/2024` — Extracted record has no GT counterpart
- `09/20/2024` — Extracted record has no GT counterpart
- `11/28/2024` — Extracted record has no GT counterpart
- `12/25/2023` — Extracted record has no GT counterpart
- `03/19/2024` — Extracted record has no GT counterpart
- `12/16/2021` — Extracted record has no GT counterpart
- `05/11/2022` — Extracted record has no GT counterpart
- `11/13/2024` — Extracted record has no GT counterpart
- `04/29/2022` — Extracted record has no GT counterpart
- `01/28/2023` — Extracted record has no GT counterpart
- `10/16/2022` — Extracted record has no GT counterpart
- `01/02/2022` — Extracted record has no GT counterpart
- `08/03/2022` — Extracted record has no GT counterpart
- `12/06/2024` — Extracted record has no GT counterpart
- `07/16/2024` — Extracted record has no GT counterpart
- `03/02/2022` — Extracted record has no GT counterpart
- `02/08/2023` — Extracted record has no GT counterpart
- `12/25/2024` — Extracted record has no GT counterpart
- `10/12/2023` — Extracted record has no GT counterpart
- `07/05/2022` — Extracted record has no GT counterpart
- `09/25/2021` — Extracted record has no GT counterpart
- `06/24/2022` — Extracted record has no GT counterpart
- `10/18/2021` — Extracted record has no GT counterpart
- `12/12/2021` — Extracted record has no GT counterpart
- `01/08/2023` — Extracted record has no GT counterpart
- `08/26/2021` — Extracted record has no GT counterpart
- `12/24/2023` — Extracted record has no GT counterpart
- `07/03/2022` — Extracted record has no GT counterpart
- `02/26/2024` — Extracted record has no GT counterpart
- `05/07/2022` — Extracted record has no GT counterpart
- `06/18/2022` — Extracted record has no GT counterpart
- `03/09/2023` — Extracted record has no GT counterpart
- `09/28/2023` — Extracted record has no GT counterpart
- `07/01/2024` — Extracted record has no GT counterpart
- `08/15/2022` — Extracted record has no GT counterpart
- `07/21/2023` — Extracted record has no GT counterpart
- `10/24/2022` — Extracted record has no GT counterpart
- `03/26/2023` — Extracted record has no GT counterpart
- `12/28/2024` — Extracted record has no GT counterpart
- `06/01/2022` — Extracted record has no GT counterpart
- `03/21/2024` — Extracted record has no GT counterpart
- `07/26/2021` — Extracted record has no GT counterpart
- `10/07/2024` — Extracted record has no GT counterpart
- `04/12/2021` — Extracted record has no GT counterpart
- `02/09/2024` — Extracted record has no GT counterpart
- `09/27/2021` — Extracted record has no GT counterpart
- `05/02/2024` — Extracted record has no GT counterpart
- `11/16/2024` — Extracted record has no GT counterpart
- `07/06/2023` — Extracted record has no GT counterpart
- `11/26/2021` — Extracted record has no GT counterpart
- `09/28/2023` — Extracted record has no GT counterpart
- `11/28/2021` — Extracted record has no GT counterpart
- `01/12/2022` — Extracted record has no GT counterpart
- `09/27/2023` — Extracted record has no GT counterpart
- `05/05/2024` — Extracted record has no GT counterpart
- `05/22/2021` — Extracted record has no GT counterpart
- `04/23/2021` — Extracted record has no GT counterpart
- `11/16/2022` — Extracted record has no GT counterpart
- `10/01/2023` — Extracted record has no GT counterpart
- `10/01/2024` — Extracted record has no GT counterpart
- `01/09/2022` — Extracted record has no GT counterpart
- `06/05/2023` — Extracted record has no GT counterpart
- `04/02/2022` — Extracted record has no GT counterpart
- `10/29/2022` — Extracted record has no GT counterpart
- `08/20/2022` — Extracted record has no GT counterpart
- `12/18/2021` — Extracted record has no GT counterpart
- `11/14/2021` — Extracted record has no GT counterpart
- `12/06/2023` — Extracted record has no GT counterpart
- `03/12/2021` — Extracted record has no GT counterpart
- `02/07/2022` — Extracted record has no GT counterpart
- `12/02/2022` — Extracted record has no GT counterpart
- `12/06/2023` — Extracted record has no GT counterpart
- `07/02/2024` — Extracted record has no GT counterpart
- `11/29/2022` — Extracted record has no GT counterpart
- `11/28/2022` — Extracted record has no GT counterpart
- `12/03/2024` — Extracted record has no GT counterpart
- `01/08/2022` — Extracted record has no GT counterpart
- `06/12/2023` — Extracted record has no GT counterpart
- `08/07/2022` — Extracted record has no GT counterpart
- `06/23/2024` — Extracted record has no GT counterpart
- `08/16/2024` — Extracted record has no GT counterpart
- `02/20/2023` — Extracted record has no GT counterpart
- `09/14/2024` — Extracted record has no GT counterpart
- `10/31/2024` — Extracted record has no GT counterpart
- `07/05/2024` — Extracted record has no GT counterpart
- `01/24/2023` — Extracted record has no GT counterpart
- `05/27/2021` — Extracted record has no GT counterpart
- `08/13/2024` — Extracted record has no GT counterpart
- `06/28/2022` — Extracted record has no GT counterpart
- `08/15/2022` — Extracted record has no GT counterpart
- `05/31/2023` — Extracted record has no GT counterpart
- `04/16/2023` — Extracted record has no GT counterpart
- `03/02/2022` — Extracted record has no GT counterpart
- `09/03/2021` — Extracted record has no GT counterpart
- `03/03/2021` — Extracted record has no GT counterpart
- `01/17/2022` — Extracted record has no GT counterpart
- `04/16/2024` — Extracted record has no GT counterpart
- `06/17/2023` — Extracted record has no GT counterpart
- `04/22/2022` — Extracted record has no GT counterpart
- `12/10/2023` — Extracted record has no GT counterpart
- `08/12/2021` — Extracted record has no GT counterpart
- `11/09/2023` — Extracted record has no GT counterpart
- `07/27/2022` — Extracted record has no GT counterpart
- `05/07/2021` — Extracted record has no GT counterpart
- `08/24/2022` — Extracted record has no GT counterpart
- `05/31/2021` — Extracted record has no GT counterpart
- `02/28/2022` — Extracted record has no GT counterpart
- `01/17/2023` — Extracted record has no GT counterpart
- `05/01/2023` — Extracted record has no GT counterpart
- `07/02/2022` — Extracted record has no GT counterpart
- `02/13/2021` — Extracted record has no GT counterpart
- `11/04/2024` — Extracted record has no GT counterpart
- `11/17/2022` — Extracted record has no GT counterpart
- `08/23/2023` — Extracted record has no GT counterpart
- `06/24/2022` — Extracted record has no GT counterpart
- `10/13/2022` — Extracted record has no GT counterpart
- `02/14/2022` — Extracted record has no GT counterpart
- `10/25/2021` — Extracted record has no GT counterpart
- `12/29/2021` — Extracted record has no GT counterpart
- `03/12/2021` — Extracted record has no GT counterpart
- `04/26/2022` — Extracted record has no GT counterpart
- `09/03/2024` — Extracted record has no GT counterpart
- `12/04/2021` — Extracted record has no GT counterpart
- `12/06/2024` — Extracted record has no GT counterpart
- `11/18/2022` — Extracted record has no GT counterpart
- `01/28/2022` — Extracted record has no GT counterpart
- `05/24/2023` — Extracted record has no GT counterpart
- `12/24/2024` — Extracted record has no GT counterpart
- `01/29/2024` — Extracted record has no GT counterpart
- `12/17/2021` — Extracted record has no GT counterpart
- `05/23/2023` — Extracted record has no GT counterpart
- `03/01/2023` — Extracted record has no GT counterpart
- `11/12/2023` — Extracted record has no GT counterpart
- `04/02/2022` — Extracted record has no GT counterpart
- `07/18/2021` — Extracted record has no GT counterpart
- `06/05/2023` — Extracted record has no GT counterpart
- `02/03/2021` — Extracted record has no GT counterpart
- `10/29/2022` — Extracted record has no GT counterpart
- `10/28/2024` — Extracted record has no GT counterpart
- `08/15/2021` — Extracted record has no GT counterpart
- `10/11/2024` — Extracted record has no GT counterpart
- `09/03/2024` — Extracted record has no GT counterpart
- `12/19/2023` — Extracted record has no GT counterpart
- `04/09/2024` — Extracted record has no GT counterpart
- `10/08/2023` — Extracted record has no GT counterpart
- `12/14/2023` — Extracted record has no GT counterpart
- `04/20/2021` — Extracted record has no GT counterpart
- `01/09/2023` — Extracted record has no GT counterpart
- `01/30/2023` — Extracted record has no GT counterpart
- `03/21/2024` — Extracted record has no GT counterpart
- `05/06/2023` — Extracted record has no GT counterpart
- `05/06/2024` — Extracted record has no GT counterpart
- `07/14/2024` — Extracted record has no GT counterpart
- `01/04/2024` — Extracted record has no GT counterpart
- `05/01/2022` — Extracted record has no GT counterpart
- `02/29/2024` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `02/12/2022` — Extracted record has no GT counterpart
- `09/23/2024` — Extracted record has no GT counterpart
- `01/08/2024` — Extracted record has no GT counterpart
- `05/01/2021` — Extracted record has no GT counterpart
- `01/08/2023` — Extracted record has no GT counterpart
- `06/03/2021` — Extracted record has no GT counterpart
- `02/18/2022` — Extracted record has no GT counterpart
- `07/28/2023` — Extracted record has no GT counterpart
- `10/06/2023` — Extracted record has no GT counterpart
- `07/22/2024` — Extracted record has no GT counterpart
- `05/06/2022` — Extracted record has no GT counterpart
- `05/08/2024` — Extracted record has no GT counterpart
- `01/01/2024` — Extracted record has no GT counterpart
- `05/12/2024` — Extracted record has no GT counterpart
- `10/07/2024` — Extracted record has no GT counterpart
- `09/14/2021` — Extracted record has no GT counterpart
- `08/03/2021` — Extracted record has no GT counterpart
- `12/13/2021` — Extracted record has no GT counterpart
- `09/12/2022` — Extracted record has no GT counterpart
- `04/18/2024` — Extracted record has no GT counterpart
- `05/28/2022` — Extracted record has no GT counterpart
- `07/17/2022` — Extracted record has no GT counterpart
- `03/29/2021` — Extracted record has no GT counterpart
- `06/22/2021` — Extracted record has no GT counterpart
- `04/05/2022` — Extracted record has no GT counterpart
- `03/17/2021` — Extracted record has no GT counterpart
- `08/17/2023` — Extracted record has no GT counterpart
- `03/23/2022` — Extracted record has no GT counterpart
- `08/08/2022` — Extracted record has no GT counterpart
- `02/20/2022` — Extracted record has no GT counterpart
- `05/23/2021` — Extracted record has no GT counterpart
- `01/10/2021` — Extracted record has no GT counterpart
- `02/14/2023` — Extracted record has no GT counterpart
- `10/26/2023` — Extracted record has no GT counterpart
- `05/14/2023` — Extracted record has no GT counterpart
- `11/07/2022` — Extracted record has no GT counterpart
- `09/08/2022` — Extracted record has no GT counterpart
- `03/29/2023` — Extracted record has no GT counterpart
- `02/12/2023` — Extracted record has no GT counterpart
- `06/12/2022` — Extracted record has no GT counterpart
- `05/24/2024` — Extracted record has no GT counterpart
- `02/13/2024` — Extracted record has no GT counterpart
- `02/04/2021` — Extracted record has no GT counterpart
- `03/28/2021` — Extracted record has no GT counterpart
- `02/16/2021` — Extracted record has no GT counterpart
- `05/04/2022` — Extracted record has no GT counterpart
- `11/02/2021` — Extracted record has no GT counterpart
- `02/13/2022` — Extracted record has no GT counterpart
- `12/21/2024` — Extracted record has no GT counterpart
- `09/24/2022` — Extracted record has no GT counterpart
- `10/10/2024` — Extracted record has no GT counterpart
- `05/27/2023` — Extracted record has no GT counterpart
- `10/20/2022` — Extracted record has no GT counterpart
- `07/18/2024` — Extracted record has no GT counterpart
- `07/16/2023` — Extracted record has no GT counterpart
- `07/30/2022` — Extracted record has no GT counterpart
- `06/09/2023` — Extracted record has no GT counterpart
- `12/03/2024` — Extracted record has no GT counterpart
- `06/03/2021` — Extracted record has no GT counterpart
- `10/12/2023` — Extracted record has no GT counterpart
- `03/12/2023` — Extracted record has no GT counterpart
- `09/20/2022` — Extracted record has no GT counterpart
- `11/02/2022` — Extracted record has no GT counterpart
- `05/14/2024` — Extracted record has no GT counterpart
- `02/15/2024` — Extracted record has no GT counterpart
- `10/02/2021` — Extracted record has no GT counterpart
- `08/23/2021` — Extracted record has no GT counterpart
- `09/19/2021` — Extracted record has no GT counterpart
- `08/13/2024` — Extracted record has no GT counterpart
- `09/29/2024` — Extracted record has no GT counterpart
- `05/31/2022` — Extracted record has no GT counterpart
- `07/22/2024` — Extracted record has no GT counterpart
- `07/09/2023` — Extracted record has no GT counterpart
- `09/04/2022` — Extracted record has no GT counterpart
- `06/17/2023` — Extracted record has no GT counterpart
- `03/26/2023` — Extracted record has no GT counterpart
- `09/16/2024` — Extracted record has no GT counterpart
- `02/28/2023` — Extracted record has no GT counterpart
- `11/10/2022` — Extracted record has no GT counterpart
- `12/25/2022` — Extracted record has no GT counterpart
- `06/30/2022` — Extracted record has no GT counterpart
- `09/18/2024` — Extracted record has no GT counterpart
- `07/08/2022` — Extracted record has no GT counterpart
- `06/16/2022` — Extracted record has no GT counterpart
- `12/12/2023` — Extracted record has no GT counterpart
- `02/17/2024` — Extracted record has no GT counterpart
- `12/20/2022` — Extracted record has no GT counterpart
- `12/01/2022` — Extracted record has no GT counterpart
- `09/29/2023` — Extracted record has no GT counterpart
- `10/12/2023` — Extracted record has no GT counterpart
- `03/18/2022` — Extracted record has no GT counterpart
- `05/01/2023` — Extracted record has no GT counterpart
- `03/25/2023` — Extracted record has no GT counterpart
- `09/10/2023` — Extracted record has no GT counterpart
- `01/04/2022` — Extracted record has no GT counterpart
- `09/15/2021` — Extracted record has no GT counterpart
- `06/21/2023` — Extracted record has no GT counterpart
- `06/27/2023` — Extracted record has no GT counterpart
- `08/01/2023` — Extracted record has no GT counterpart
- `01/29/2022` — Extracted record has no GT counterpart
- `11/30/2022` — Extracted record has no GT counterpart
- `07/16/2021` — Extracted record has no GT counterpart
- `05/16/2021` — Extracted record has no GT counterpart
- `07/08/2021` — Extracted record has no GT counterpart
- `08/30/2024` — Extracted record has no GT counterpart
- `07/19/2021` — Extracted record has no GT counterpart
- `03/31/2023` — Extracted record has no GT counterpart
- `04/02/2022` — Extracted record has no GT counterpart
- `12/25/2021` — Extracted record has no GT counterpart
- `07/13/2023` — Extracted record has no GT counterpart
- `04/20/2024` — Extracted record has no GT counterpart
- `04/22/2022` — Extracted record has no GT counterpart
- `12/28/2023` — Extracted record has no GT counterpart
- `06/29/2022` — Extracted record has no GT counterpart
- `03/23/2023` — Extracted record has no GT counterpart
- `06/14/2023` — Extracted record has no GT counterpart
- `10/02/2024` — Extracted record has no GT counterpart
- `09/28/2021` — Extracted record has no GT counterpart
- `02/12/2023` — Extracted record has no GT counterpart
- `10/28/2021` — Extracted record has no GT counterpart
- `06/22/2022` — Extracted record has no GT counterpart
- `06/02/2023` — Extracted record has no GT counterpart
- `03/01/2022` — Extracted record has no GT counterpart
- `02/07/2021` — Extracted record has no GT counterpart
- `01/29/2022` — Extracted record has no GT counterpart
- `10/19/2024` — Extracted record has no GT counterpart
- `05/23/2023` — Extracted record has no GT counterpart
- `07/10/2024` — Extracted record has no GT counterpart
- `06/12/2021` — Extracted record has no GT counterpart
- `05/08/2022` — Extracted record has no GT counterpart
- `01/16/2022` — Extracted record has no GT counterpart
- `03/22/2024` — Extracted record has no GT counterpart
- `09/24/2021` — Extracted record has no GT counterpart
- `08/09/2021` — Extracted record has no GT counterpart
- `09/09/2024` — Extracted record has no GT counterpart
- `05/15/2021` — Extracted record has no GT counterpart
- `09/21/2021` — Extracted record has no GT counterpart
- `03/26/2023` — Extracted record has no GT counterpart
- `05/12/2023` — Extracted record has no GT counterpart
- `09/17/2024` — Extracted record has no GT counterpart
- `08/21/2022` — Extracted record has no GT counterpart
- `07/01/2022` — Extracted record has no GT counterpart
- `08/27/2021` — Extracted record has no GT counterpart
- `06/04/2023` — Extracted record has no GT counterpart
- `02/25/2024` — Extracted record has no GT counterpart
- `06/27/2022` — Extracted record has no GT counterpart
- `12/31/2022` — Extracted record has no GT counterpart
- `08/03/2022` — Extracted record has no GT counterpart
- `07/12/2023` — Extracted record has no GT counterpart
- `03/06/2024` — Extracted record has no GT counterpart
- `04/01/2024` — Extracted record has no GT counterpart
- `06/22/2023` — Extracted record has no GT counterpart
- `02/15/2023` — Extracted record has no GT counterpart
- `01/23/2022` — Extracted record has no GT counterpart
- `09/14/2024` — Extracted record has no GT counterpart
- `07/23/2024` — Extracted record has no GT counterpart
- `01/20/2024` — Extracted record has no GT counterpart
- `02/27/2022` — Extracted record has no GT counterpart
- `02/11/2024` — Extracted record has no GT counterpart
- `02/25/2022` — Extracted record has no GT counterpart
- `01/22/2022` — Extracted record has no GT counterpart
- `07/15/2022` — Extracted record has no GT counterpart
- `05/13/2022` — Extracted record has no GT counterpart
- `07/20/2022` — Extracted record has no GT counterpart
- `10/04/2021` — Extracted record has no GT counterpart
- `04/08/2024` — Extracted record has no GT counterpart
- `05/25/2022` — Extracted record has no GT counterpart
- `07/11/2022` — Extracted record has no GT counterpart
- `03/01/2024` — Extracted record has no GT counterpart
- `09/16/2024` — Extracted record has no GT counterpart
- `10/14/2023` — Extracted record has no GT counterpart
- `04/25/2022` — Extracted record has no GT counterpart
- `10/05/2021` — Extracted record has no GT counterpart
- `04/26/2023` — Extracted record has no GT counterpart
- `06/07/2021` — Extracted record has no GT counterpart
- `05/10/2023` — Extracted record has no GT counterpart
- `03/11/2023` — Extracted record has no GT counterpart
- `08/18/2024` — Extracted record has no GT counterpart
- `09/22/2022` — Extracted record has no GT counterpart
- `09/24/2023` — Extracted record has no GT counterpart
- `02/14/2022` — Extracted record has no GT counterpart
- `08/05/2024` — Extracted record has no GT counterpart
- `07/08/2022` — Extracted record has no GT counterpart
- `03/25/2023` — Extracted record has no GT counterpart
- `02/23/2021` — Extracted record has no GT counterpart
- `03/18/2024` — Extracted record has no GT counterpart
- `07/06/2021` — Extracted record has no GT counterpart
- `06/29/2024` — Extracted record has no GT counterpart
- `07/16/2021` — Extracted record has no GT counterpart
- `12/11/2023` — Extracted record has no GT counterpart
- `07/29/2023` — Extracted record has no GT counterpart
- `05/15/2022` — Extracted record has no GT counterpart
- `10/02/2023` — Extracted record has no GT counterpart
- `08/19/2022` — Extracted record has no GT counterpart
- `02/03/2023` — Extracted record has no GT counterpart
- `07/31/2022` — Extracted record has no GT counterpart
- `05/24/2022` — Extracted record has no GT counterpart
- `01/31/2023` — Extracted record has no GT counterpart
- `09/07/2023` — Extracted record has no GT counterpart
- `02/28/2024` — Extracted record has no GT counterpart
- `04/10/2024` — Extracted record has no GT counterpart
- `10/07/2024` — Extracted record has no GT counterpart
- `12/14/2022` — Extracted record has no GT counterpart
- `02/18/2023` — Extracted record has no GT counterpart
- `03/22/2022` — Extracted record has no GT counterpart
- `08/06/2021` — Extracted record has no GT counterpart
- `01/12/2022` — Extracted record has no GT counterpart
- `09/18/2023` — Extracted record has no GT counterpart
- `03/13/2024` — Extracted record has no GT counterpart
- `02/05/2024` — Extracted record has no GT counterpart
- `06/02/2021` — Extracted record has no GT counterpart
- `09/22/2024` — Extracted record has no GT counterpart
- `03/23/2021` — Extracted record has no GT counterpart
- `11/08/2022` — Extracted record has no GT counterpart
- `07/19/2023` — Extracted record has no GT counterpart
- `08/29/2021` — Extracted record has no GT counterpart
- `01/22/2021` — Extracted record has no GT counterpart
- `12/31/2021` — Extracted record has no GT counterpart
- `08/08/2022` — Extracted record has no GT counterpart
- `07/30/2022` — Extracted record has no GT counterpart
- `02/17/2021` — Extracted record has no GT counterpart
- `10/17/2023` — Extracted record has no GT counterpart
- `11/16/2021` — Extracted record has no GT counterpart
- `12/15/2021` — Extracted record has no GT counterpart
- `02/24/2022` — Extracted record has no GT counterpart
- `01/09/2024` — Extracted record has no GT counterpart
- `01/08/2024` — Extracted record has no GT counterpart
- `10/01/2023` — Extracted record has no GT counterpart
- `08/14/2022` — Extracted record has no GT counterpart
- `12/05/2024` — Extracted record has no GT counterpart
- `08/03/2024` — Extracted record has no GT counterpart
- `05/01/2023` — Extracted record has no GT counterpart
- `07/20/2024` — Extracted record has no GT counterpart
- `03/03/2021` — Extracted record has no GT counterpart
- `06/25/2023` — Extracted record has no GT counterpart
- `03/08/2022` — Extracted record has no GT counterpart
- `06/21/2022` — Extracted record has no GT counterpart
- `12/26/2021` — Extracted record has no GT counterpart
- `02/22/2023` — Extracted record has no GT counterpart
- `12/02/2022` — Extracted record has no GT counterpart
- `08/15/2022` — Extracted record has no GT counterpart
- `11/15/2021` — Extracted record has no GT counterpart
- `10/04/2021` — Extracted record has no GT counterpart
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
- `03/10/2021` — Extracted record has no GT counterpart
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
- `06/26/2021` — Extracted record has no GT counterpart
- `03/16/2023` — Extracted record has no GT counterpart
- `05/24/2024` — Extracted record has no GT counterpart
- `11/21/2022` — Extracted record has no GT counterpart
- `04/06/2024` — Extracted record has no GT counterpart
- `10/26/2021` — Extracted record has no GT counterpart
- `06/11/2022` — Extracted record has no GT counterpart
- `03/11/2023` — Extracted record has no GT counterpart
- `11/24/2021` — Extracted record has no GT counterpart
- `12/02/2023` — Extracted record has no GT counterpart
- `03/19/2022` — Extracted record has no GT counterpart
- `02/03/2022` — Extracted record has no GT counterpart
- `12/22/2022` — Extracted record has no GT counterpart
- `08/12/2024` — Extracted record has no GT counterpart
- `01/27/2023` — Extracted record has no GT counterpart
- `03/15/2021` — Extracted record has no GT counterpart
- `10/18/2021` — Extracted record has no GT counterpart
- `12/28/2021` — Extracted record has no GT counterpart
- `10/22/2021` — Extracted record has no GT counterpart
- `03/14/2024` — Extracted record has no GT counterpart
- `09/15/2021` — Extracted record has no GT counterpart
- `11/13/2023` — Extracted record has no GT counterpart
- `12/23/2021` — Extracted record has no GT counterpart
- `08/03/2021` — Extracted record has no GT counterpart
- `11/03/2023` — Extracted record has no GT counterpart
- `02/09/2021` — Extracted record has no GT counterpart
- `07/05/2022` — Extracted record has no GT counterpart
- `05/18/2024` — Extracted record has no GT counterpart
- `12/26/2024` — Extracted record has no GT counterpart
- `10/08/2022` — Extracted record has no GT counterpart
- `03/30/2024` — Extracted record has no GT counterpart
- `01/11/2023` — Extracted record has no GT counterpart
- `12/09/2024` — Extracted record has no GT counterpart
- `08/30/2022` — Extracted record has no GT counterpart
- `11/30/2022` — Extracted record has no GT counterpart
- `03/21/2023` — Extracted record has no GT counterpart
- `06/25/2021` — Extracted record has no GT counterpart
- `11/14/2021` — Extracted record has no GT counterpart
- `01/06/2024` — Extracted record has no GT counterpart
- `11/08/2023` — Extracted record has no GT counterpart
- `05/12/2023` — Extracted record has no GT counterpart
- `05/07/2024` — Extracted record has no GT counterpart
- `05/06/2021` — Extracted record has no GT counterpart
- `11/06/2024` — Extracted record has no GT counterpart
- `07/05/2022` — Extracted record has no GT counterpart
- `05/28/2024` — Extracted record has no GT counterpart
- `10/16/2023` — Extracted record has no GT counterpart
- `10/25/2021` — Extracted record has no GT counterpart
- `08/15/2024` — Extracted record has no GT counterpart
- `11/18/2023` — Extracted record has no GT counterpart
- `02/27/2021` — Extracted record has no GT counterpart
- `07/26/2021` — Extracted record has no GT counterpart
- `04/30/2022` — Extracted record has no GT counterpart
- `12/11/2021` — Extracted record has no GT counterpart
- `10/23/2022` — Extracted record has no GT counterpart
- `02/18/2022` — Extracted record has no GT counterpart
- `06/09/2021` — Extracted record has no GT counterpart
- `12/15/2022` — Extracted record has no GT counterpart
- `05/13/2022` — Extracted record has no GT counterpart
- `09/20/2023` — Extracted record has no GT counterpart
- `10/29/2021` — Extracted record has no GT counterpart
- `08/13/2024` — Extracted record has no GT counterpart
- `11/16/2023` — Extracted record has no GT counterpart
- `03/19/2024` — Extracted record has no GT counterpart
- `05/24/2024` — Extracted record has no GT counterpart
- `05/07/2023` — Extracted record has no GT counterpart
- `06/08/2023` — Extracted record has no GT counterpart
- `03/02/2023` — Extracted record has no GT counterpart
- `07/13/2022` — Extracted record has no GT counterpart
- `09/30/2024` — Extracted record has no GT counterpart
- `05/06/2022` — Extracted record has no GT counterpart
- `05/03/2024` — Extracted record has no GT counterpart
- `07/13/2023` — Extracted record has no GT counterpart
- `07/13/2022` — Extracted record has no GT counterpart
- `06/15/2024` — Extracted record has no GT counterpart
- `07/19/2024` — Extracted record has no GT counterpart
- `11/14/2024` — Extracted record has no GT counterpart
- `05/29/2024` — Extracted record has no GT counterpart
- `11/17/2022` — Extracted record has no GT counterpart
- `08/28/2022` — Extracted record has no GT counterpart
- `05/19/2024` — Extracted record has no GT counterpart
- `12/09/2022` — Extracted record has no GT counterpart
- `08/26/2022` — Extracted record has no GT counterpart
- `05/07/2021` — Extracted record has no GT counterpart
- `03/23/2022` — Extracted record has no GT counterpart
- `12/07/2023` — Extracted record has no GT counterpart
- `09/23/2023` — Extracted record has no GT counterpart
- `01/06/2023` — Extracted record has no GT counterpart
- `08/10/2021` — Extracted record has no GT counterpart
- `01/12/2023` — Extracted record has no GT counterpart
- `10/31/2021` — Extracted record has no GT counterpart
- `11/18/2024` — Extracted record has no GT counterpart
- `07/18/2021` — Extracted record has no GT counterpart
- `03/11/2022` — Extracted record has no GT counterpart
- `01/27/2023` — Extracted record has no GT counterpart
- `10/27/2023` — Extracted record has no GT counterpart
- `05/06/2021` — Extracted record has no GT counterpart
- `07/09/2024` — Extracted record has no GT counterpart
- `06/16/2024` — Extracted record has no GT counterpart
- `06/24/2022` — Extracted record has no GT counterpart
- `10/20/2021` — Extracted record has no GT counterpart
- `01/28/2023` — Extracted record has no GT counterpart
- `08/11/2023` — Extracted record has no GT counterpart
- `02/18/2023` — Extracted record has no GT counterpart
- `03/14/2024` — Extracted record has no GT counterpart
- `02/27/2021` — Extracted record has no GT counterpart
- `06/26/2024` — Extracted record has no GT counterpart
- `04/16/2023` — Extracted record has no GT counterpart
- `05/09/2021` — Extracted record has no GT counterpart
- `04/18/2021` — Extracted record has no GT counterpart
- `06/20/2024` — Extracted record has no GT counterpart
- `09/15/2022` — Extracted record has no GT counterpart
- `03/17/2024` — Extracted record has no GT counterpart
- `05/08/2022` — Extracted record has no GT counterpart
- `06/09/2024` — Extracted record has no GT counterpart
- `02/11/2023` — Extracted record has no GT counterpart
- `02/05/2022` — Extracted record has no GT counterpart
- `01/20/2024` — Extracted record has no GT counterpart
- `03/14/2024` — Extracted record has no GT counterpart
- `04/19/2021` — Extracted record has no GT counterpart
- `05/15/2023` — Extracted record has no GT counterpart
- `06/23/2022` — Extracted record has no GT counterpart
- `09/21/2023` — Extracted record has no GT counterpart
- `08/07/2022` — Extracted record has no GT counterpart
- `12/11/2024` — Extracted record has no GT counterpart
- `07/24/2021` — Extracted record has no GT counterpart
- `06/08/2023` — Extracted record has no GT counterpart
- `02/10/2023` — Extracted record has no GT counterpart
- `06/23/2021` — Extracted record has no GT counterpart
- `04/28/2022` — Extracted record has no GT counterpart
- `01/13/2021` — Extracted record has no GT counterpart
- `05/30/2024` — Extracted record has no GT counterpart
- `09/12/2024` — Extracted record has no GT counterpart
- `07/14/2023` — Extracted record has no GT counterpart
- `11/29/2021` — Extracted record has no GT counterpart
- `12/09/2024` — Extracted record has no GT counterpart
- `08/31/2023` — Extracted record has no GT counterpart
- `04/01/2021` — Extracted record has no GT counterpart
- `09/09/2023` — Extracted record has no GT counterpart
- `11/28/2022` — Extracted record has no GT counterpart
- `02/20/2021` — Extracted record has no GT counterpart
- `12/01/2023` — Extracted record has no GT counterpart
- `03/20/2022` — Extracted record has no GT counterpart
- `09/07/2022` — Extracted record has no GT counterpart
- `04/28/2022` — Extracted record has no GT counterpart
- `01/09/2022` — Extracted record has no GT counterpart
- `07/23/2024` — Extracted record has no GT counterpart
- `10/04/2023` — Extracted record has no GT counterpart
- `11/16/2024` — Extracted record has no GT counterpart
- `12/15/2021` — Extracted record has no GT counterpart
- `06/07/2024` — Extracted record has no GT counterpart
- `07/08/2024` — Extracted record has no GT counterpart
- `01/13/2021` — Extracted record has no GT counterpart
- `09/26/2021` — Extracted record has no GT counterpart
- `05/08/2024` — Extracted record has no GT counterpart
- `01/02/2023` — Extracted record has no GT counterpart
- `04/25/2021` — Extracted record has no GT counterpart
- `03/10/2022` — Extracted record has no GT counterpart
- `07/31/2021` — Extracted record has no GT counterpart
- `06/05/2024` — Extracted record has no GT counterpart
- `11/25/2021` — Extracted record has no GT counterpart
- `02/25/2024` — Extracted record has no GT counterpart
- `03/26/2023` — Extracted record has no GT counterpart
- `10/30/2022` — Extracted record has no GT counterpart
- `09/01/2022` — Extracted record has no GT counterpart
- `05/26/2023` — Extracted record has no GT counterpart
- `12/26/2021` — Extracted record has no GT counterpart
- `05/28/2023` — Extracted record has no GT counterpart
- `09/21/2024` — Extracted record has no GT counterpart
- `08/29/2021` — Extracted record has no GT counterpart
- `05/11/2024` — Extracted record has no GT counterpart
- `02/06/2023` — Extracted record has no GT counterpart
- `10/28/2023` — Extracted record has no GT counterpart
- `02/13/2023` — Extracted record has no GT counterpart
- `07/10/2024` — Extracted record has no GT counterpart
- `08/29/2022` — Extracted record has no GT counterpart
- `07/13/2024` — Extracted record has no GT counterpart
- `12/24/2021` — Extracted record has no GT counterpart
- `12/04/2024` — Extracted record has no GT counterpart
- `10/06/2023` — Extracted record has no GT counterpart
- `08/25/2022` — Extracted record has no GT counterpart
- `07/07/2021` — Extracted record has no GT counterpart
- `11/05/2022` — Extracted record has no GT counterpart
- `01/24/2024` — Extracted record has no GT counterpart
- `03/14/2024` — Extracted record has no GT counterpart
- `08/14/2024` — Extracted record has no GT counterpart
- `10/23/2024` — Extracted record has no GT counterpart
- `04/01/2021` — Extracted record has no GT counterpart
- `03/23/2024` — Extracted record has no GT counterpart
- `05/28/2024` — Extracted record has no GT counterpart
- `01/17/2024` — Extracted record has no GT counterpart
- `08/01/2022` — Extracted record has no GT counterpart
- `07/16/2023` — Extracted record has no GT counterpart
- `10/03/2023` — Extracted record has no GT counterpart
- `01/03/2023` — Extracted record has no GT counterpart
- `02/04/2021` — Extracted record has no GT counterpart
- `07/08/2024` — Extracted record has no GT counterpart
- `12/23/2021` — Extracted record has no GT counterpart
- `05/26/2024` — Extracted record has no GT counterpart
- `03/02/2021` — Extracted record has no GT counterpart
- `08/19/2021` — Extracted record has no GT counterpart
- `01/15/2024` — Extracted record has no GT counterpart
- `05/15/2024` — Extracted record has no GT counterpart
- `01/17/2023` — Extracted record has no GT counterpart
- `11/20/2024` — Extracted record has no GT counterpart
- `09/06/2024` — Extracted record has no GT counterpart
- `05/31/2022` — Extracted record has no GT counterpart
- `12/31/2021` — Extracted record has no GT counterpart
- `06/07/2021` — Extracted record has no GT counterpart
- `04/15/2024` — Extracted record has no GT counterpart
- `06/19/2022` — Extracted record has no GT counterpart
- `02/15/2022` — Extracted record has no GT counterpart
- `07/05/2022` — Extracted record has no GT counterpart
- `12/18/2024` — Extracted record has no GT counterpart
- `07/01/2021` — Extracted record has no GT counterpart
- `10/01/2024` — Extracted record has no GT counterpart
- `07/19/2022` — Extracted record has no GT counterpart
- `07/21/2021` — Extracted record has no GT counterpart
- `05/07/2022` — Extracted record has no GT counterpart
- `11/16/2023` — Extracted record has no GT counterpart
- `04/14/2021` — Extracted record has no GT counterpart
- `08/01/2022` — Extracted record has no GT counterpart
- `10/14/2022` — Extracted record has no GT counterpart
- `04/15/2024` — Extracted record has no GT counterpart
- `08/19/2022` — Extracted record has no GT counterpart
- `02/04/2021` — Extracted record has no GT counterpart
- `08/27/2022` — Extracted record has no GT counterpart
- `12/17/2024` — Extracted record has no GT counterpart
- `07/07/2024` — Extracted record has no GT counterpart
- `06/12/2022` — Extracted record has no GT counterpart
- `12/01/2022` — Extracted record has no GT counterpart
- `04/03/2022` — Extracted record has no GT counterpart
- `04/17/2023` — Extracted record has no GT counterpart
- `11/17/2022` — Extracted record has no GT counterpart
- `05/07/2023` — Extracted record has no GT counterpart
- `07/09/2021` — Extracted record has no GT counterpart
- `12/03/2021` — Extracted record has no GT counterpart
- `02/13/2023` — Extracted record has no GT counterpart
- `03/13/2022` — Extracted record has no GT counterpart
- `11/26/2024` — Extracted record has no GT counterpart
- `07/25/2021` — Extracted record has no GT counterpart
- `01/15/2024` — Extracted record has no GT counterpart
- `12/15/2023` — Extracted record has no GT counterpart
- `12/31/2022` — Extracted record has no GT counterpart
- `05/01/2024` — Extracted record has no GT counterpart
- `04/23/2021` — Extracted record has no GT counterpart
- `09/15/2021` — Extracted record has no GT counterpart
- `06/11/2022` — Extracted record has no GT counterpart
- `08/04/2022` — Extracted record has no GT counterpart
- `11/25/2023` — Extracted record has no GT counterpart
- `10/03/2021` — Extracted record has no GT counterpart
- `10/14/2022` — Extracted record has no GT counterpart
- `06/18/2021` — Extracted record has no GT counterpart
- `05/05/2024` — Extracted record has no GT counterpart
- `10/20/2023` — Extracted record has no GT counterpart
- `09/21/2023` — Extracted record has no GT counterpart
- `09/07/2021` — Extracted record has no GT counterpart
- `07/20/2021` — Extracted record has no GT counterpart
- `07/22/2023` — Extracted record has no GT counterpart
- `09/17/2023` — Extracted record has no GT counterpart
- `05/30/2023` — Extracted record has no GT counterpart
- `07/08/2024` — Extracted record has no GT counterpart
- `02/03/2023` — Extracted record has no GT counterpart
- `12/21/2023` — Extracted record has no GT counterpart
- `01/24/2024` — Extracted record has no GT counterpart
- `06/29/2021` — Extracted record has no GT counterpart
- `07/24/2021` — Extracted record has no GT counterpart
- `12/16/2024` — Extracted record has no GT counterpart
- `07/24/2021` — Extracted record has no GT counterpart
- `04/27/2022` — Extracted record has no GT counterpart
- `01/24/2022` — Extracted record has no GT counterpart
- `01/21/2022` — Extracted record has no GT counterpart
- `12/29/2024` — Extracted record has no GT counterpart
- `07/08/2022` — Extracted record has no GT counterpart
- `03/18/2022` — Extracted record has no GT counterpart
- `07/07/2024` — Extracted record has no GT counterpart
- `07/31/2023` — Extracted record has no GT counterpart
- `08/19/2024` — Extracted record has no GT counterpart
- `12/16/2021` — Extracted record has no GT counterpart
- `09/23/2023` — Extracted record has no GT counterpart
- `06/22/2024` — Extracted record has no GT counterpart
- `06/09/2021` — Extracted record has no GT counterpart
- `10/28/2023` — Extracted record has no GT counterpart
- `08/27/2024` — Extracted record has no GT counterpart
- `04/08/2024` — Extracted record has no GT counterpart
- `06/24/2021` — Extracted record has no GT counterpart
- `08/07/2021` — Extracted record has no GT counterpart
- `08/07/2021` — Extracted record has no GT counterpart
- `02/12/2021` — Extracted record has no GT counterpart
- `09/16/2021` — Extracted record has no GT counterpart
- `02/20/2021` — Extracted record has no GT counterpart
- `01/06/2024` — Extracted record has no GT counterpart
- `08/31/2023` — Extracted record has no GT counterpart
- `08/01/2024` — Extracted record has no GT counterpart
- `06/02/2021` — Extracted record has no GT counterpart
- `12/23/2021` — Extracted record has no GT counterpart
- `08/30/2023` — Extracted record has no GT counterpart
- `09/21/2024` — Extracted record has no GT counterpart
- `06/27/2021` — Extracted record has no GT counterpart
- `01/14/2023` — Extracted record has no GT counterpart
- `12/24/2021` — Extracted record has no GT counterpart
- `03/17/2023` — Extracted record has no GT counterpart
- `10/10/2023` — Extracted record has no GT counterpart
- `09/01/2022` — Extracted record has no GT counterpart
- `11/24/2022` — Extracted record has no GT counterpart
- `02/22/2022` — Extracted record has no GT counterpart
- `07/15/2023` — Extracted record has no GT counterpart
- `11/30/2024` — Extracted record has no GT counterpart
- `04/19/2024` — Extracted record has no GT counterpart
- `10/20/2021` — Extracted record has no GT counterpart
- `05/08/2024` — Extracted record has no GT counterpart
- `05/22/2024` — Extracted record has no GT counterpart
- `06/20/2021` — Extracted record has no GT counterpart
- `11/14/2023` — Extracted record has no GT counterpart
- `04/06/2021` — Extracted record has no GT counterpart
- `01/29/2023` — Extracted record has no GT counterpart
- `10/28/2024` — Extracted record has no GT counterpart
- `12/13/2022` — Extracted record has no GT counterpart
- `11/15/2023` — Extracted record has no GT counterpart
- `12/23/2022` — Extracted record has no GT counterpart
- `10/19/2022` — Extracted record has no GT counterpart
- `03/03/2024` — Extracted record has no GT counterpart
- `11/28/2021` — Extracted record has no GT counterpart
- `12/22/2023` — Extracted record has no GT counterpart
- `04/13/2024` — Extracted record has no GT counterpart
- `11/19/2024` — Extracted record has no GT counterpart
- `09/13/2023` — Extracted record has no GT counterpart
- `12/22/2023` — Extracted record has no GT counterpart
- `10/13/2024` — Extracted record has no GT counterpart
- `04/01/2022` — Extracted record has no GT counterpart
- `08/08/2024` — Extracted record has no GT counterpart
- `08/05/2021` — Extracted record has no GT counterpart
- `06/29/2024` — Extracted record has no GT counterpart
- `09/23/2023` — Extracted record has no GT counterpart
- `05/19/2022` — Extracted record has no GT counterpart
- `08/14/2022` — Extracted record has no GT counterpart
- `09/15/2023` — Extracted record has no GT counterpart
- `05/26/2021` — Extracted record has no GT counterpart
- `12/10/2023` — Extracted record has no GT counterpart
- `01/24/2022` — Extracted record has no GT counterpart
- `06/21/2024` — Extracted record has no GT counterpart
- `02/05/2024` — Extracted record has no GT counterpart
- `07/28/2024` — Extracted record has no GT counterpart
- `06/02/2024` — Extracted record has no GT counterpart
- `03/30/2021` — Extracted record has no GT counterpart
- `08/22/2023` — Extracted record has no GT counterpart
- `05/10/2021` — Extracted record has no GT counterpart
- `03/27/2023` — Extracted record has no GT counterpart
- `07/12/2021` — Extracted record has no GT counterpart
- `07/19/2023` — Extracted record has no GT counterpart
- `10/15/2021` — Extracted record has no GT counterpart
- `03/23/2022` — Extracted record has no GT counterpart
- `06/06/2021` — Extracted record has no GT counterpart
- `07/05/2022` — Extracted record has no GT counterpart
- `06/15/2024` — Extracted record has no GT counterpart
- `08/14/2021` — Extracted record has no GT counterpart
- `05/22/2023` — Extracted record has no GT counterpart
- `01/14/2023` — Extracted record has no GT counterpart
- `04/23/2024` — Extracted record has no GT counterpart
- `10/26/2021` — Extracted record has no GT counterpart
- `11/16/2021` — Extracted record has no GT counterpart
- `11/01/2022` — Extracted record has no GT counterpart
- `11/28/2023` — Extracted record has no GT counterpart
- `12/11/2023` — Extracted record has no GT counterpart
- `11/05/2022` — Extracted record has no GT counterpart
- `05/31/2022` — Extracted record has no GT counterpart
- `04/11/2022` — Extracted record has no GT counterpart
- `06/26/2023` — Extracted record has no GT counterpart
- `11/13/2021` — Extracted record has no GT counterpart
- `07/29/2024` — Extracted record has no GT counterpart
- `07/10/2023` — Extracted record has no GT counterpart
- `09/22/2022` — Extracted record has no GT counterpart
- `02/10/2024` — Extracted record has no GT counterpart
- `06/07/2024` — Extracted record has no GT counterpart
- `07/09/2023` — Extracted record has no GT counterpart
- `12/23/2024` — Extracted record has no GT counterpart
- `04/30/2023` — Extracted record has no GT counterpart
- `10/19/2022` — Extracted record has no GT counterpart
- `08/04/2023` — Extracted record has no GT counterpart
- `08/16/2021` — Extracted record has no GT counterpart
- `04/06/2024` — Extracted record has no GT counterpart
- `03/17/2022` — Extracted record has no GT counterpart
- `05/23/2023` — Extracted record has no GT counterpart
- `09/20/2021` — Extracted record has no GT counterpart
- `05/28/2023` — Extracted record has no GT counterpart
- `03/03/2021` — Extracted record has no GT counterpart
- `10/31/2022` — Extracted record has no GT counterpart
- `02/07/2024` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `11/28/2021` — Extracted record has no GT counterpart
- `01/18/2023` — Extracted record has no GT counterpart
- `02/18/2022` — Extracted record has no GT counterpart
- `06/06/2024` — Extracted record has no GT counterpart
- `06/11/2021` — Extracted record has no GT counterpart
- `11/11/2021` — Extracted record has no GT counterpart
- `01/29/2024` — Extracted record has no GT counterpart
- `11/23/2022` — Extracted record has no GT counterpart
- `05/14/2024` — Extracted record has no GT counterpart
- `06/19/2023` — Extracted record has no GT counterpart
- `09/04/2024` — Extracted record has no GT counterpart
- `08/27/2022` — Extracted record has no GT counterpart
- `10/11/2021` — Extracted record has no GT counterpart
- `10/27/2021` — Extracted record has no GT counterpart
- `07/20/2024` — Extracted record has no GT counterpart
- `07/01/2023` — Extracted record has no GT counterpart
- `09/26/2022` — Extracted record has no GT counterpart
- `05/07/2024` — Extracted record has no GT counterpart
- `06/10/2021` — Extracted record has no GT counterpart
- `08/21/2022` — Extracted record has no GT counterpart
- `06/11/2022` — Extracted record has no GT counterpart
- `02/18/2022` — Extracted record has no GT counterpart
- `12/22/2024` — Extracted record has no GT counterpart
- `04/15/2021` — Extracted record has no GT counterpart
- `02/17/2024` — Extracted record has no GT counterpart
- `08/27/2024` — Extracted record has no GT counterpart
- `04/22/2024` — Extracted record has no GT counterpart
- `12/08/2022` — Extracted record has no GT counterpart
- `09/08/2021` — Extracted record has no GT counterpart
- `03/30/2023` — Extracted record has no GT counterpart
- `12/15/2023` — Extracted record has no GT counterpart
- `08/21/2024` — Extracted record has no GT counterpart
- `02/18/2023` — Extracted record has no GT counterpart
- `12/28/2021` — Extracted record has no GT counterpart
- `12/11/2022` — Extracted record has no GT counterpart
- `08/02/2024` — Extracted record has no GT counterpart
- `08/05/2021` — Extracted record has no GT counterpart
- `09/30/2023` — Extracted record has no GT counterpart
- `08/28/2021` — Extracted record has no GT counterpart
- `02/27/2022` — Extracted record has no GT counterpart
- `07/18/2024` — Extracted record has no GT counterpart
- `09/25/2022` — Extracted record has no GT counterpart
- `05/24/2021` — Extracted record has no GT counterpart
- `03/18/2022` — Extracted record has no GT counterpart
- `06/21/2021` — Extracted record has no GT counterpart
- `12/23/2021` — Extracted record has no GT counterpart
- `06/05/2024` — Extracted record has no GT counterpart
- `06/01/2023` — Extracted record has no GT counterpart
- `10/17/2021` — Extracted record has no GT counterpart
- `08/24/2022` — Extracted record has no GT counterpart
- `10/07/2022` — Extracted record has no GT counterpart
- `11/20/2024` — Extracted record has no GT counterpart
- `02/26/2023` — Extracted record has no GT counterpart
- `01/25/2024` — Extracted record has no GT counterpart
- `03/03/2024` — Extracted record has no GT counterpart
- `07/23/2021` — Extracted record has no GT counterpart
- `01/15/2024` — Extracted record has no GT counterpart
- `09/14/2021` — Extracted record has no GT counterpart
- `11/03/2024` — Extracted record has no GT counterpart
- `09/11/2024` — Extracted record has no GT counterpart
- `11/24/2024` — Extracted record has no GT counterpart
- `06/24/2024` — Extracted record has no GT counterpart
- `11/13/2023` — Extracted record has no GT counterpart
- `02/12/2022` — Extracted record has no GT counterpart
- `07/13/2023` — Extracted record has no GT counterpart
- `08/25/2022` — Extracted record has no GT counterpart
- `07/18/2021` — Extracted record has no GT counterpart
- `05/12/2022` — Extracted record has no GT counterpart
- `08/07/2023` — Extracted record has no GT counterpart
- `02/21/2023` — Extracted record has no GT counterpart
- `10/11/2024` — Extracted record has no GT counterpart
- `05/24/2023` — Extracted record has no GT counterpart
- `02/02/2023` — Extracted record has no GT counterpart
- `06/06/2022` — Extracted record has no GT counterpart
- `05/12/2021` — Extracted record has no GT counterpart
- `03/10/2024` — Extracted record has no GT counterpart
- `04/09/2024` — Extracted record has no GT counterpart
- `09/13/2024` — Extracted record has no GT counterpart
- `12/24/2023` — Extracted record has no GT counterpart
- `07/17/2024` — Extracted record has no GT counterpart
- `03/25/2024` — Extracted record has no GT counterpart
- `05/21/2024` — Extracted record has no GT counterpart
- `12/11/2023` — Extracted record has no GT counterpart
- `01/17/2021` — Extracted record has no GT counterpart
- `06/20/2023` — Extracted record has no GT counterpart
- `05/07/2024` — Extracted record has no GT counterpart
- `12/11/2021` — Extracted record has no GT counterpart
- `11/22/2022` — Extracted record has no GT counterpart
- `06/20/2021` — Extracted record has no GT counterpart
- `10/30/2022` — Extracted record has no GT counterpart
- `05/24/2023` — Extracted record has no GT counterpart
- `09/12/2024` — Extracted record has no GT counterpart
- `05/19/2023` — Extracted record has no GT counterpart
- `12/14/2021` — Extracted record has no GT counterpart
- `02/02/2022` — Extracted record has no GT counterpart
- `02/04/2022` — Extracted record has no GT counterpart
- `02/18/2022` — Extracted record has no GT counterpart
- `04/28/2024` — Extracted record has no GT counterpart
- `07/03/2023` — Extracted record has no GT counterpart
- `09/16/2022` — Extracted record has no GT counterpart
- `09/28/2023` — Extracted record has no GT counterpart
- `09/18/2021` — Extracted record has no GT counterpart
- `07/27/2022` — Extracted record has no GT counterpart
- `05/14/2021` — Extracted record has no GT counterpart
- `02/04/2023` — Extracted record has no GT counterpart
- `05/07/2023` — Extracted record has no GT counterpart
- `06/30/2022` — Extracted record has no GT counterpart
- `11/27/2022` — Extracted record has no GT counterpart
- `08/03/2024` — Extracted record has no GT counterpart
- `01/25/2023` — Extracted record has no GT counterpart
- `06/25/2024` — Extracted record has no GT counterpart
- `11/18/2021` — Extracted record has no GT counterpart
- `04/29/2022` — Extracted record has no GT counterpart
- `06/09/2022` — Extracted record has no GT counterpart
- `11/01/2024` — Extracted record has no GT counterpart
- `08/18/2021` — Extracted record has no GT counterpart
- `07/18/2022` — Extracted record has no GT counterpart
- `11/13/2023` — Extracted record has no GT counterpart
- `11/08/2024` — Extracted record has no GT counterpart

**Field mismatches (730):**

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
| 2 | `cpt_codes` | 01/08/2021 - 11/19/2024 | missing=['71046', '72100', '72158', '73030', '73060', '74177', '76705', '76830', 'J0205', 'J2720', 'J3480', 'J9060'] |
| 2 | `total_charges` | 01/08/2021 - 11/19/2024 | extracted=179.57  expected=7351.46  diff=7171.89 |
| 2 | `ins_paid` | 01/08/2021 - 11/19/2024 | extracted=116.53  expected=4342.54  diff=4226.01 |
| 2 | `adjustment` | 01/08/2021 - 11/19/2024 | extracted=63.04  expected=2799.07  diff=2736.03 |
| 2 | `balance` | 01/08/2021 - 11/19/2024 | extracted=0.0  expected=209.85  diff=209.85 |
| 2 | `description` | 01/08/2021 - 11/19/2024 | extracted='Ultrasound abdomen, complete'  expected=None |
| 3 | `cpt_codes` | 05/23/2021 - 11/04/2024 | missing=['71048', '73110', '73564', '74177', 'A4209', 'A4637', 'J9035'] |
| 3 | `total_charges` | 05/23/2021 - 11/04/2024 | extracted=581.57  expected=6749.4  diff=6167.83 |
| 3 | `ins_paid` | 05/23/2021 - 11/04/2024 | extracted=412.76  expected=4126.34  diff=3713.58 |
| 3 | `adjustment` | 05/23/2021 - 11/04/2024 | extracted=136.01  expected=2386.56  diff=2250.55 |
| 3 | `payments` | 05/23/2021 - 11/04/2024 | extracted=32.8  expected=None |
| 3 | `balance` | 05/23/2021 - 11/04/2024 | extracted=0.0  expected=236.5  diff=236.50 |
| 3 | `description` | 05/23/2021 - 11/04/2024 | extracted='Ultrasound abdomen, complete'  expected=None |
| 4 | `cpt_codes` | 03/30/2022 - 07/30/2024 | missing=['72100', '73030', '73060', '73100', '73110', '73562', 'A4244', 'J2720'] |
| 4 | `total_charges` | 03/30/2022 - 07/30/2024 | extracted=123.45  expected=3907.03  diff=3783.58 |
| 4 | `ins_paid` | 03/30/2022 - 07/30/2024 | extracted=73.94  expected=2265.2  diff=2191.26 |
| 4 | `adjustment` | 03/30/2022 - 07/30/2024 | extracted=49.51  expected=1620.86  diff=1571.35 |
| 4 | `balance` | 03/30/2022 - 07/30/2024 | extracted=0.0  expected=20.97  diff=20.97 |
| 4 | `description` | 03/30/2022 - 07/30/2024 | extracted='MRI lumbar spine without contrast'  expected=None |
| 5 | `cpt_codes` | 07/12/2021 - 05/01/2024 | missing=['72110', '73030', '73110', '73564', '76705', '76830', 'A4246'] |
| 5 | `total_charges` | 07/12/2021 - 05/01/2024 | extracted=618.0  expected=6972.2  diff=6354.20 |
| 5 | `ins_paid` | 07/12/2021 - 05/01/2024 | extracted=411.26  expected=4437.88  diff=4026.62 |
| 5 | `adjustment` | 07/12/2021 - 05/01/2024 | extracted=206.74  expected=2417.45  diff=2210.71 |
| 5 | `balance` | 07/12/2021 - 05/01/2024 | extracted=0.0  expected=116.87  diff=116.87 |
| 5 | `description` | 07/12/2021 - 05/01/2024 | extracted='CT abdomen & pelvis with contrast'  expected=None |
| 6 | `cpt_codes` | 04/12/2021 - 10/11/2024 | missing=['71046', '72100', '72158', '73110', '73562', '73564', '74178', '76700', '77067', 'J0171', 'Q9920'] |
| 6 | `total_charges` | 04/12/2021 - 10/11/2024 | extracted=602.5  expected=8218.92  diff=7616.42 |
| 6 | `ins_paid` | 04/12/2021 - 10/11/2024 | extracted=436.47  expected=5286.07  diff=4849.60 |
| 6 | `adjustment` | 04/12/2021 - 10/11/2024 | extracted=92.59  expected=2677.81  diff=2585.22 |
| 6 | `payments` | 04/12/2021 - 10/11/2024 | extracted=73.44  expected=None |
| 6 | `balance` | 04/12/2021 - 10/11/2024 | extracted=0.0  expected=255.04  diff=255.04 |
| 6 | `description` | 04/12/2021 - 10/11/2024 | extracted='MRI lumbar spine without contrast'  expected=None |
| 7 | `cpt_codes` | 04/08/2021 - 06/20/2024 | missing=['71048', '72110', '72148', '73030', '73110', '73564', '74178', 'A4244', 'J0205'] |
| 7 | `total_charges` | 04/08/2021 - 06/20/2024 | extracted=309.19  expected=5683.58  diff=5374.39 |
| 7 | `ins_paid` | 04/08/2021 - 06/20/2024 | extracted=181.88  expected=3686.91  diff=3505.03 |
| 7 | `adjustment` | 04/08/2021 - 06/20/2024 | extracted=127.31  expected=1786.37  diff=1659.06 |
| 7 | `balance` | 04/08/2021 - 06/20/2024 | extracted=0.0  expected=210.3  diff=210.30 |
| 7 | `description` | 04/08/2021 - 06/20/2024 | extracted='Screening mammography, bilateral'  expected=None |
| 8 | `cpt_codes` | 03/13/2021 - 12/18/2024 | missing=['71048', '72100', '72110', '72158', '73100', '73110', '73562', '74178', '76705', '76830', 'A4604', 'J3010'] |
| 8 | `total_charges` | 03/13/2021 - 12/18/2024 | extracted=882.62  expected=7524.59  diff=6641.97 |
| 8 | `ins_paid` | 03/13/2021 - 12/18/2024 | extracted=506.01  expected=4768.13  diff=4262.12 |
| 8 | `adjustment` | 03/13/2021 - 12/18/2024 | extracted=305.38  expected=2591.0  diff=2285.62 |
| 8 | `payments` | 03/13/2021 - 12/18/2024 | extracted=71.23  expected=None |
| 8 | `balance` | 03/13/2021 - 12/18/2024 | extracted=0.0  expected=165.46  diff=165.46 |
| 8 | `description` | 03/13/2021 - 12/18/2024 | extracted='Abciximab, 10 mg'  expected=None |
| 9 | `cpt_codes` | 04/03/2021 - 11/04/2024 | missing=['73030', '73060', '73100', '73562', '76700', '77067', 'A4244'] |
| 9 | `total_charges` | 04/03/2021 - 11/04/2024 | extracted=274.28  expected=5175.81  diff=4901.53 |
| 9 | `ins_paid` | 04/03/2021 - 11/04/2024 | extracted=142.3  expected=3284.13  diff=3141.83 |
| 9 | `adjustment` | 04/03/2021 - 11/04/2024 | extracted=112.97  expected=1788.95  diff=1675.98 |
| 9 | `payments` | 04/03/2021 - 11/04/2024 | extracted=19.01  expected=None |
| 9 | `balance` | 04/03/2021 - 11/04/2024 | extracted=0.0  expected=102.73  diff=102.73 |
| 9 | `description` | 04/03/2021 - 11/04/2024 | extracted='X-ray spine, lumbosacral, 2-3 views'  expected=None |
| 10 | `cpt_codes` | 01/29/2021 - 10/20/2024 | missing=['71048', '72100', '72110', '72148', '72158', '73030', '73100', '74177', '74178', '76705', 'A4244', 'Q0163'] |
| 10 | `total_charges` | 01/29/2021 - 10/20/2024 | extracted=794.54  expected=6874.72  diff=6080.18 |
| 10 | `ins_paid` | 01/29/2021 - 10/20/2024 | extracted=501.09  expected=4485.45  diff=3984.36 |
| 10 | `adjustment` | 01/29/2021 - 10/20/2024 | extracted=293.45  expected=2339.56  diff=2046.11 |
| 10 | `balance` | 01/29/2021 - 10/20/2024 | extracted=0.0  expected=49.71  diff=49.71 |
| 10 | `description` | 01/29/2021 - 10/20/2024 | extracted='Screening mammography, bilateral'  expected=None |
| 11 | `cpt_codes` | 01/15/2021 - 09/02/2024 | missing=['72100', '72110', '72148', '72158', '73030', '73564', '74177', '76700', '76705', '76830', 'A4649', 'J0205', 'J1040', 'J2001'] |
| 11 | `total_charges` | 01/15/2021 - 09/02/2024 | extracted=371.49  expected=9246.87  diff=8875.38 |
| 11 | `ins_paid` | 01/15/2021 - 09/02/2024 | extracted=246.11  expected=5816.55  diff=5570.44 |
| 11 | `adjustment` | 01/15/2021 - 09/02/2024 | extracted=125.38  expected=3170.29  diff=3044.91 |
| 11 | `balance` | 01/15/2021 - 09/02/2024 | extracted=0.0  expected=260.03  diff=260.03 |
| 11 | `description` | 01/15/2021 - 09/02/2024 | extracted='X-ray wrist, minimum 3 views'  expected=None |
| 12 | `cpt_codes` | 01/02/2021 - 10/22/2024 | missing=['72100', '72158', '73060', '73110', '76830', '77067', 'A4244', 'A4245', 'J2730', 'J2796'] |
| 12 | `total_charges` | 01/02/2021 - 10/22/2024 | extracted=335.88  expected=6764.66  diff=6428.78 |
| 12 | `ins_paid` | 01/02/2021 - 10/22/2024 | extracted=176.77  expected=4371.78  diff=4195.01 |
| 12 | `adjustment` | 01/02/2021 - 10/22/2024 | extracted=113.3  expected=2266.9  diff=2153.60 |
| 12 | `payments` | 01/02/2021 - 10/22/2024 | extracted=45.81  expected=None |
| 12 | `balance` | 01/02/2021 - 10/22/2024 | extracted=0.0  expected=125.98  diff=125.98 |
| 12 | `description` | 01/02/2021 - 10/22/2024 | extracted='X-ray wrist, 2 views'  expected=None |
| 13 | `cpt_codes` | 04/11/2021 - 12/21/2024 | missing=['73030', '73060', '73100', '73110', '73562', '74177', '76700', '76705', '76830', '77067', 'A4263', 'A4616', 'A4627', 'J1055', 'J1642', 'J3480'] |
| 13 | `total_charges` | 04/11/2021 - 12/21/2024 | extracted=387.79  expected=10334.6  diff=9946.81 |
| 13 | `ins_paid` | 04/11/2021 - 12/21/2024 | extracted=239.9  expected=6176.83  diff=5936.93 |
| 13 | `adjustment` | 04/11/2021 - 12/21/2024 | extracted=147.89  expected=3841.14  diff=3693.25 |
| 13 | `balance` | 04/11/2021 - 12/21/2024 | extracted=0.0  expected=316.63  diff=316.63 |
| 13 | `description` | 04/11/2021 - 12/21/2024 | extracted='CT abdomen & pelvis without and with contrast'  expected=None |
| 14 | `cpt_codes` | 01/07/2021 - 12/13/2024 | missing=['72100', '72158', '73060', '73100', '74177', '74178', '76705', '77067', 'A4640', 'J0270', 'J2405'] |
| 14 | `total_charges` | 01/07/2021 - 12/13/2024 | extracted=415.44  expected=7739.46  diff=7324.02 |
| 14 | `ins_paid` | 01/07/2021 - 12/13/2024 | extracted=298.23  expected=4781.57  diff=4483.34 |
| 14 | `adjustment` | 01/07/2021 - 12/13/2024 | extracted=117.21  expected=2752.33  diff=2635.12 |
| 14 | `balance` | 01/07/2021 - 12/13/2024 | extracted=0.0  expected=205.56  diff=205.56 |
| 14 | `description` | 01/07/2021 - 12/13/2024 | extracted='X-ray knee, 3 views'  expected=None |
| 15 | `cpt_codes` | 02/15/2021 - 10/14/2024 | missing=['72100', '72110', '73030', '73100', '76700', '76830', '77067', 'A4209', 'A4263', 'A4656', 'J9060', 'Q4100'] |
| 15 | `total_charges` | 02/15/2021 - 10/14/2024 | extracted=335.44  expected=11727.38  diff=11391.94 |
| 15 | `ins_paid` | 02/15/2021 - 10/14/2024 | extracted=246.86  expected=7269.09  diff=7022.23 |
| 15 | `adjustment` | 02/15/2021 - 10/14/2024 | extracted=88.58  expected=3998.82  diff=3910.24 |
| 15 | `balance` | 02/15/2021 - 10/14/2024 | extracted=0.0  expected=459.47  diff=459.47 |
| 15 | `description` | 02/15/2021 - 10/14/2024 | extracted='X-ray wrist, minimum 3 views'  expected=None |
| 16 | `cpt_codes` | 02/08/2021 - 06/05/2024 | missing=['71046', '72100', '72110', '73110', '73562', '74177', '76700', '76705', '76830', '77067', 'A4570', 'A4649', 'A4656', 'J0153', 'J9045'] |
| 16 | `total_charges` | 02/08/2021 - 06/05/2024 | extracted=621.74  expected=11217.58  diff=10595.84 |
| 16 | `ins_paid` | 02/08/2021 - 06/05/2024 | extracted=368.7  expected=6735.57  diff=6366.87 |
| 16 | `adjustment` | 02/08/2021 - 06/05/2024 | extracted=253.04  expected=4318.61  diff=4065.57 |
| 16 | `balance` | 02/08/2021 - 06/05/2024 | extracted=0.0  expected=163.4  diff=163.40 |
| 16 | `description` | 02/08/2021 - 06/05/2024 | extracted='Spacer, bag, or reservoir with or without mask'  expected=None |
| 17 | `cpt_codes` | 03/04/2021 - 11/24/2024 | missing=['71046', '71048', '72148', '72158', '73030', '73060', '73110', '73564', '76830', '77067', 'A4253', 'A4630', 'J0130', 'Q0169'] |
| 17 | `total_charges` | 03/04/2021 - 11/24/2024 | extracted=280.0  expected=9293.78  diff=9013.78 |
| 17 | `ins_paid` | 03/04/2021 - 11/24/2024 | extracted=160.79  expected=5502.3  diff=5341.51 |
| 17 | `adjustment` | 03/04/2021 - 11/24/2024 | extracted=82.73  expected=3507.83  diff=3425.10 |
| 17 | `payments` | 03/04/2021 - 11/24/2024 | extracted=36.48  expected=None |
| 17 | `balance` | 03/04/2021 - 11/24/2024 | extracted=0.0  expected=283.65  diff=283.65 |
| 17 | `description` | 03/04/2021 - 11/24/2024 | extracted='X-ray knee, 3 views'  expected=None |
| 18 | `cpt_codes` | 10/15/2021 - 08/17/2024 | missing=['71046', '72100', '72110', '72148', '73060', '73100', '73564', '74177', '76830', '77067', 'A4246', 'A4656', 'J0171'] |
| 18 | `total_charges` | 10/15/2021 - 08/17/2024 | extracted=539.86  expected=8032.11  diff=7492.25 |
| 18 | `ins_paid` | 10/15/2021 - 08/17/2024 | extracted=351.58  expected=5047.73  diff=4696.15 |
| 18 | `adjustment` | 10/15/2021 - 08/17/2024 | extracted=174.04  expected=2556.36  diff=2382.32 |
| 18 | `payments` | 10/15/2021 - 08/17/2024 | extracted=14.24  expected=None |
| 18 | `balance` | 10/15/2021 - 08/17/2024 | extracted=0.0  expected=428.02  diff=428.02 |
| 18 | `description` | 10/15/2021 - 08/17/2024 | extracted='X-ray shoulder, minimum 2 views'  expected=None |
| 19 | `cpt_codes` | 02/04/2021 - 12/23/2024 | missing=['71046', '72148', '73030', '73060', '73100', '73562', '73564', '74178', 'A4206', 'J0153', 'J0290', 'J9060', 'Q2043'] |
| 19 | `total_charges` | 02/04/2021 - 12/23/2024 | extracted=567.57  expected=10380.95  diff=9813.38 |
| 19 | `ins_paid` | 02/04/2021 - 12/23/2024 | extracted=307.18  expected=6387.75  diff=6080.57 |
| 19 | `adjustment` | 02/04/2021 - 12/23/2024 | extracted=189.22  expected=3844.82  diff=3655.60 |
| 19 | `payments` | 02/04/2021 - 12/23/2024 | extracted=71.17  expected=None |
| 19 | `balance` | 02/04/2021 - 12/23/2024 | extracted=0.0  expected=148.38  diff=148.38 |
| 19 | `description` | 02/04/2021 - 12/23/2024 | extracted='Chest X-ray, 4+ views'  expected=None |
| 20 | `cpt_codes` | 01/31/2021 - 10/28/2024 | missing=['71046', '72148', '73100', '73110', '73564', '76700', '76705', '76830', '77067', 'A4246', 'A4247', 'A4600', 'J2730', 'J3370'] |
| 20 | `total_charges` | 01/31/2021 - 10/28/2024 | extracted=485.84  expected=8933.72  diff=8447.88 |
| 20 | `ins_paid` | 01/31/2021 - 10/28/2024 | extracted=331.11  expected=5717.12  diff=5386.01 |
| 20 | `adjustment` | 01/31/2021 - 10/28/2024 | extracted=118.68  expected=2811.76  diff=2693.08 |
| 20 | `payments` | 01/31/2021 - 10/28/2024 | extracted=36.05  expected=None |
| 20 | `balance` | 01/31/2021 - 10/28/2024 | extracted=0.0  expected=404.84  diff=404.84 |
| 20 | `description` | 01/31/2021 - 10/28/2024 | extracted='X-ray knee, 3 views'  expected=None |
| 21 | `cpt_codes` | 02/19/2021 - 11/23/2024 | missing=['71046', '71048', '73060', '73100', '74177', '74178', '76705', '76830', '77067'] |
| 21 | `total_charges` | 02/19/2021 - 11/23/2024 | extracted=218.69  expected=6521.85  diff=6303.16 |
| 21 | `ins_paid` | 02/19/2021 - 11/23/2024 | extracted=156.22  expected=3863.71  diff=3707.49 |
| 21 | `adjustment` | 02/19/2021 - 11/23/2024 | extracted=62.47  expected=2569.17  diff=2506.70 |
| 21 | `balance` | 02/19/2021 - 11/23/2024 | extracted=0.0  expected=88.97  diff=88.97 |
| 21 | `description` | 02/19/2021 - 11/23/2024 | extracted='Ampicillin sodium, 500 mg'  expected=None |
| 22 | `cpt_codes` | 01/10/2021 - 11/04/2024 | missing=['71046', '71048', '72100', '73030', '73060', '73100', '73564', '74177', '74178', '77067', 'A4209'] |
| 22 | `total_charges` | 01/10/2021 - 11/04/2024 | extracted=352.65  expected=7393.21  diff=7040.56 |
| 22 | `ins_paid` | 01/10/2021 - 11/04/2024 | extracted=195.19  expected=4868.11  diff=4672.92 |
| 22 | `adjustment` | 01/10/2021 - 11/04/2024 | extracted=157.46  expected=2248.42  diff=2090.96 |
| 22 | `balance` | 01/10/2021 - 11/04/2024 | extracted=0.0  expected=276.68  diff=276.68 |
| 22 | `description` | 01/10/2021 - 11/04/2024 | extracted='X-ray wrist, minimum 3 views'  expected=None |
| 23 | `cpt_codes` | 09/21/2021 - 09/12/2024 | missing=['72100', '72148', '73564', '74178', '76700', '76830', 'A4245', 'A4636', 'J0153', 'J2796']  extra=['Q4100'] |
| 23 | `total_charges` | 09/21/2021 - 09/12/2024 | extracted=317.05  expected=4261.01  diff=3943.96 |
| 23 | `ins_paid` | 09/21/2021 - 09/12/2024 | extracted=206.2  expected=2799.98  diff=2593.78 |
| 23 | `adjustment` | 09/21/2021 - 09/12/2024 | extracted=110.85  expected=1239.07  diff=1128.22 |
| 23 | `balance` | 09/21/2021 - 09/12/2024 | extracted=0.0  expected=221.96  diff=221.96 |
| 23 | `description` | 09/21/2021 - 09/12/2024 | extracted='Skin substitute, not otherwise specified, per sq cm'  expected=None |
| 24 | `cpt_codes` | 03/03/2021 - 11/25/2024 | missing=['71046', '71048', '72158', '73110', '73562', '73564', '74177', '74178', '76705', '77067'] |
| 24 | `total_charges` | 03/03/2021 - 11/25/2024 | extracted=312.03  expected=6624.15  diff=6312.12 |
| 24 | `ins_paid` | 03/03/2021 - 11/25/2024 | extracted=212.53  expected=4281.97  diff=4069.44 |
| 24 | `adjustment` | 03/03/2021 - 11/25/2024 | extracted=72.88  expected=2160.39  diff=2087.51 |
| 24 | `payments` | 03/03/2021 - 11/25/2024 | extracted=26.62  expected=None |
| 24 | `balance` | 03/03/2021 - 11/25/2024 | extracted=0.0  expected=181.79  diff=181.79 |
| 24 | `description` | 03/03/2021 - 11/25/2024 | extracted='X-ray spine, lumbosacral, 4+ views'  expected=None |
| 25 | `cpt_codes` | 04/29/2021 - 12/12/2024 | missing=['72100', '72110', '72148', '73030', '73060', '73100', '73562', '74177', '74178', '76700', '76830', 'A4600', 'A4637', 'J0205', 'J0360'] |
| 25 | `total_charges` | 04/29/2021 - 12/12/2024 | extracted=853.32  expected=7362.39  diff=6509.07 |
| 25 | `ins_paid` | 04/29/2021 - 12/12/2024 | extracted=562.96  expected=4457.92  diff=3894.96 |
| 25 | `adjustment` | 04/29/2021 - 12/12/2024 | extracted=290.36  expected=2758.41  diff=2468.05 |
| 25 | `balance` | 04/29/2021 - 12/12/2024 | extracted=0.0  expected=146.06  diff=146.06 |
| 25 | `description` | 04/29/2021 - 12/12/2024 | extracted='X-ray knee, 4+ views'  expected=None |
| 26 | `cpt_codes` | 12/24/2022 - 12/28/2024 | missing=['72110', '72148', '73060', '73562', '77067'] |
| 26 | `total_charges` | 12/24/2022 - 12/28/2024 | extracted=425.91  expected=3683.62  diff=3257.71 |
| 26 | `ins_paid` | 12/24/2022 - 12/28/2024 | extracted=298.93  expected=2381.01  diff=2082.08 |
| 26 | `adjustment` | 12/24/2022 - 12/28/2024 | extracted=126.98  expected=1292.68  diff=1165.70 |
| 26 | `balance` | 12/24/2022 - 12/28/2024 | extracted=0.0  expected=9.93  diff=9.93 |
| 26 | `description` | 12/24/2022 - 12/28/2024 | extracted='X-ray wrist, minimum 3 views'  expected=None |
| 27 | `cpt_codes` | 07/18/2021 - 11/23/2024 | missing=['71046', '71048', '72100', '72110', '72158', '73060', '73562', '76700', 'A4246', 'J0180', 'J0360'] |
| 27 | `total_charges` | 07/18/2021 - 11/23/2024 | extracted=360.63  expected=7749.22  diff=7388.59 |
| 27 | `ins_paid` | 07/18/2021 - 11/23/2024 | extracted=247.83  expected=4782.1  diff=4534.27 |
| 27 | `adjustment` | 07/18/2021 - 11/23/2024 | extracted=112.8  expected=2871.16  diff=2758.36 |
| 27 | `balance` | 07/18/2021 - 11/23/2024 | extracted=0.0  expected=95.96  diff=95.96 |
| 27 | `description` | 07/18/2021 - 11/23/2024 | extracted='CT abdomen & pelvis with contrast'  expected=None |
| 28 | `cpt_codes` | 01/15/2021 - 10/02/2024 | missing=['72100', '72158', '73030', '73060', '74177', '77067', 'A4637', 'J0285', 'Q0169', 'Q2043']  extra=['73110'] |
| 28 | `total_charges` | 01/15/2021 - 10/02/2024 | extracted=371.49  expected=5093.7  diff=4722.21 |
| 28 | `ins_paid` | 01/15/2021 - 10/02/2024 | extracted=246.11  expected=3126.65  diff=2880.54 |
| 28 | `adjustment` | 01/15/2021 - 10/02/2024 | extracted=125.38  expected=1870.03  diff=1744.65 |
| 28 | `balance` | 01/15/2021 - 10/02/2024 | extracted=0.0  expected=97.02  diff=97.02 |
| 28 | `description` | 01/15/2021 - 10/02/2024 | extracted='X-ray wrist, minimum 3 views'  expected=None |
| 29 | `cpt_codes` | 06/26/2021 - 10/17/2024 | missing=['72100', '72158', '73030', '73110', '73564', '76830', '77067', 'J2001'] |
| 29 | `total_charges` | 06/26/2021 - 10/17/2024 | extracted=675.66  expected=5429.05  diff=4753.39 |
| 29 | `ins_paid` | 06/26/2021 - 10/17/2024 | extracted=439.42  expected=3268.05  diff=2828.63 |
| 29 | `adjustment` | 06/26/2021 - 10/17/2024 | extracted=136.17  expected=2019.01  diff=1882.84 |
| 29 | `payments` | 06/26/2021 - 10/17/2024 | extracted=100.07  expected=None |
| 29 | `balance` | 06/26/2021 - 10/17/2024 | extracted=0.0  expected=141.99  diff=141.99 |
| 29 | `provider` | 06/26/2021 - 10/17/2024 | extracted='Account 990119'  expected='Hudson Medical, PC' |
| 29 | `insurers` | 06/26/2021 - 10/17/2024 | missing=['tricare'] |
| 29 | `description` | 06/26/2021 - 10/17/2024 | extracted='X-ray wrist, 2 views'  expected=None |
| 30 | `cpt_codes` | 05/26/2021 - 12/12/2024 | missing=['71046', '71048', '72148', '73100', '73562', '73564', '74177', '74178', '76700', 'A4656', 'J0290', 'J2405', 'Q9920'] |
| 30 | `total_charges` | 05/26/2021 - 12/12/2024 | extracted=861.9  expected=8719.06  diff=7857.16 |
| 30 | `ins_paid` | 05/26/2021 - 12/12/2024 | extracted=637.46  expected=5707.95  diff=5070.49 |
| 30 | `adjustment` | 05/26/2021 - 12/12/2024 | extracted=224.44  expected=2772.97  diff=2548.53 |
| 30 | `balance` | 05/26/2021 - 12/12/2024 | extracted=0.0  expected=238.14  diff=238.14 |
| 30 | `provider` | 05/26/2021 - 12/12/2024 | extracted='Account 632701'  expected='Hudson Medical, PC' |
| 30 | `insurers` | 05/26/2021 - 12/12/2024 | missing=['tricare'] |
| 30 | `description` | 05/26/2021 - 12/12/2024 | extracted='Screening mammography, bilateral'  expected=None |
| 31 | `cpt_codes` | 02/20/2021 - 11/15/2024 | missing=['71048', '72100', '72110', '72148', '72158', '73100', '73110', '73564', '74177', '76700', '76705', '76830', 'A4209', 'J0270', 'J2796', 'J9045'] |
| 31 | `total_charges` | 02/20/2021 - 11/15/2024 | extracted=709.76  expected=7512.15  diff=6802.39 |
| 31 | `ins_paid` | 02/20/2021 - 11/15/2024 | extracted=402.32  expected=4798.36  diff=4396.04 |
| 31 | `adjustment` | 02/20/2021 - 11/15/2024 | extracted=238.1  expected=2504.5  diff=2266.40 |
| 31 | `payments` | 02/20/2021 - 11/15/2024 | extracted=69.34  expected=None |
| 31 | `balance` | 02/20/2021 - 11/15/2024 | extracted=0.0  expected=209.29  diff=209.29 |
| 31 | `provider` | 02/20/2021 - 11/15/2024 | extracted='Account 819529'  expected='Hudson Medical, PC' |
| 31 | `insurers` | 02/20/2021 - 11/15/2024 | missing=['tricare'] |
| 31 | `description` | 02/20/2021 - 11/15/2024 | extracted='CT abdomen & pelvis without and with contrast'  expected=None |
| 32 | `cpt_codes` | 01/06/2021 - 11/28/2024 | missing=['71048', '72100', '72148', '73030', '73060', '73100', '73110', '74177', '76700', '76705', '76830', '77067', 'A4253', 'J1040', 'J2730', 'Q4100'] |
| 32 | `total_charges` | 01/06/2021 - 11/28/2024 | extracted=365.47  expected=8036.1  diff=7670.63 |
| 32 | `ins_paid` | 01/06/2021 - 11/28/2024 | extracted=196.92  expected=4729.55  diff=4532.63 |
| 32 | `adjustment` | 01/06/2021 - 11/28/2024 | extracted=168.55  expected=3209.12  diff=3040.57 |
| 32 | `balance` | 01/06/2021 - 11/28/2024 | extracted=0.0  expected=97.43  diff=97.43 |
| 32 | `provider` | 01/06/2021 - 11/28/2024 | extracted='Account 307433'  expected='Hudson Medical, PC' |
| 32 | `insurers` | 01/06/2021 - 11/28/2024 | missing=['tricare'] |
| 32 | `description` | 01/06/2021 - 11/28/2024 | extracted='Alcohol or peroxide, per pint'  expected=None |
| 33 | `cpt_codes` | 03/10/2021 - 12/25/2024 | missing=['71048', '73030', '73100', '73562', '74177', '74178', '76700', '76705', 'A4244', 'A4630'] |
| 33 | `total_charges` | 03/10/2021 - 12/25/2024 | extracted=519.73  expected=7034.09  diff=6514.36 |
| 33 | `ins_paid` | 03/10/2021 - 12/25/2024 | extracted=269.51  expected=4187.26  diff=3917.75 |
| 33 | `adjustment` | 03/10/2021 - 12/25/2024 | extracted=224.08  expected=2820.69  diff=2596.61 |
| 33 | `payments` | 03/10/2021 - 12/25/2024 | extracted=26.14  expected=None |
| 33 | `balance` | 03/10/2021 - 12/25/2024 | extracted=0.0  expected=26.14  diff=26.14 |
| 33 | `provider` | 03/10/2021 - 12/25/2024 | extracted='Account 563287'  expected='Hudson Medical, PC' |
| 33 | `insurers` | 03/10/2021 - 12/25/2024 | missing=['tricare'] |
| 33 | `description` | 03/10/2021 - 12/25/2024 | extracted='MRI lumbar spine without contrast'  expected=None |
| 34 | `cpt_codes` | 08/26/2021 - 02/26/2024 | missing=['71048', '72148', '73030', '73060', '73110', '76830', 'A4636']  extra=['J2405'] |
| 34 | `total_charges` | 08/26/2021 - 02/26/2024 | extracted=557.8  expected=4898.95  diff=4341.15 |
| 34 | `ins_paid` | 08/26/2021 - 02/26/2024 | extracted=279.82  expected=3072.3  diff=2792.48 |
| 34 | `adjustment` | 08/26/2021 - 02/26/2024 | extracted=277.98  expected=1826.65  diff=1548.67 |
| 34 | `description` | 08/26/2021 - 02/26/2024 | extracted='Ondansetron HCl, per 1 mg'  expected=None |
| 35 | `cpt_codes` | 04/12/2021 - 12/28/2024 | missing=['71046', '72100', '72110', '73030', '73060', '73562', '74178', '76830', '77067', 'A4208', 'A4570', 'Q0163'] |
| 35 | `total_charges` | 04/12/2021 - 12/28/2024 | extracted=602.5  expected=8771.27  diff=8168.77 |
| 35 | `ins_paid` | 04/12/2021 - 12/28/2024 | extracted=436.47  expected=5571.47  diff=5135.00 |
| 35 | `adjustment` | 04/12/2021 - 12/28/2024 | extracted=92.59  expected=2937.91  diff=2845.32 |
| 35 | `payments` | 04/12/2021 - 12/28/2024 | extracted=73.44  expected=None |
| 35 | `balance` | 04/12/2021 - 12/28/2024 | extracted=0.0  expected=261.89  diff=261.89 |
| 35 | `description` | 04/12/2021 - 12/28/2024 | extracted='MRI lumbar spine without contrast'  expected=None |
| 36 | `cpt_codes` | 03/23/2021 - 05/05/2024 | missing=['73030', '73100', '73562', '74177', '74178', '76830', 'A4550', 'A4627', 'J1642', 'Q9920'] |
| 36 | `total_charges` | 03/23/2021 - 05/05/2024 | extracted=413.69  expected=6565.07  diff=6151.38 |
| 36 | `ins_paid` | 03/23/2021 - 05/05/2024 | extracted=299.52  expected=4032.73  diff=3733.21 |
| 36 | `adjustment` | 03/23/2021 - 05/05/2024 | extracted=114.17  expected=2400.82  diff=2286.65 |
| 36 | `balance` | 03/23/2021 - 05/05/2024 | extracted=0.0  expected=131.52  diff=131.52 |
| 36 | `provider` | 03/23/2021 - 05/05/2024 | extracted='Account 299943'  expected='Hudson Medical, PC' |
| 36 | `insurers` | 03/23/2021 - 05/05/2024 | missing=['tricare'] |
| 36 | `description` | 03/23/2021 - 05/05/2024 | extracted='Chest X-ray, 4+ views'  expected=None |
| 37 | `cpt_codes` | 02/27/2021 - 12/03/2024 | missing=['72158', '73030', '73060', '73100', '73110', '76700', '77067', 'A4570', 'J0270', 'J1055', 'J1642', 'J2405', 'Q4100'] |
| 37 | `total_charges` | 02/27/2021 - 12/03/2024 | extracted=215.64  expected=9665.78  diff=9450.14 |
| 37 | `ins_paid` | 02/27/2021 - 12/03/2024 | extracted=144.57  expected=6131.18  diff=5986.61 |
| 37 | `adjustment` | 02/27/2021 - 12/03/2024 | extracted=41.7  expected=3148.2  diff=3106.50 |
| 37 | `payments` | 02/27/2021 - 12/03/2024 | extracted=29.37  expected=None |
| 37 | `balance` | 02/27/2021 - 12/03/2024 | extracted=0.0  expected=386.4  diff=386.40 |
| 37 | `provider` | 02/27/2021 - 12/03/2024 | extracted='Account 951078'  expected='Hudson Medical, PC' |
| 37 | `insurers` | 02/27/2021 - 12/03/2024 | missing=['tricare'] |
| 37 | `description` | 02/27/2021 - 12/03/2024 | extracted='CT abdomen & pelvis with contrast'  expected=None |
| 38 | `cpt_codes` | 03/14/2021 - 10/31/2024 | missing=['71046', '71048', '72110', '72148', '73110', '73562', '73564', '74177', '76700', '76830', 'A4616', 'A4636', 'J3370'] |
| 38 | `total_charges` | 03/14/2021 - 10/31/2024 | extracted=260.3  expected=9401.97  diff=9141.67 |
| 38 | `ins_paid` | 03/14/2021 - 10/31/2024 | extracted=183.61  expected=5779.66  diff=5596.05 |
| 38 | `adjustment` | 03/14/2021 - 10/31/2024 | extracted=76.69  expected=3430.45  diff=3353.76 |
| 38 | `balance` | 03/14/2021 - 10/31/2024 | extracted=0.0  expected=191.86  diff=191.86 |
| 38 | `provider` | 03/14/2021 - 10/31/2024 | extracted='Account 173440'  expected='Hudson Medical, PC' |
| 38 | `insurers` | 03/14/2021 - 10/31/2024 | missing=['tricare'] |
| 38 | `description` | 03/14/2021 - 10/31/2024 | extracted='X-ray humerus, minimum 2 views'  expected=None |
| 39 | `cpt_codes` | 01/19/2021 - 11/04/2024 | missing=['71046', '71048', '72110', '72148', '72158', '73100', '74177', '76700', '76705', '76830', 'A4550', 'J0360', 'J2796', 'J3370', 'Q4100'] |
| 39 | `total_charges` | 01/19/2021 - 11/04/2024 | extracted=413.38  expected=8610.74  diff=8197.36 |
| 39 | `ins_paid` | 01/19/2021 - 11/04/2024 | extracted=272.85  expected=5449.39  diff=5176.54 |
| 39 | `adjustment` | 01/19/2021 - 11/04/2024 | extracted=115.52  expected=2919.66  diff=2804.14 |
| 39 | `payments` | 01/19/2021 - 11/04/2024 | extracted=25.01  expected=None |
| 39 | `balance` | 01/19/2021 - 11/04/2024 | extracted=0.0  expected=241.69  diff=241.69 |
| 39 | `provider` | 01/19/2021 - 11/04/2024 | extracted='Account 359478'  expected='Hudson Medical, PC' |
| 39 | `insurers` | 01/19/2021 - 11/04/2024 | missing=['tricare'] |
| 39 | `description` | 01/19/2021 - 11/04/2024 | extracted='X-ray knee, 4+ views'  expected=None |
| 40 | `cpt_codes` | 01/22/2021 - 09/03/2024 | missing=['72110', '73110', '73562', '73564', '74178', '76705', 'J1644', 'J3480'] |
| 40 | `total_charges` | 01/22/2021 - 09/03/2024 | extracted=863.02  expected=5604.51  diff=4741.49 |
| 40 | `ins_paid` | 01/22/2021 - 09/03/2024 | extracted=619.92  expected=3594.14  diff=2974.22 |
| 40 | `adjustment` | 01/22/2021 - 09/03/2024 | extracted=243.1  expected=1874.28  diff=1631.18 |
| 40 | `balance` | 01/22/2021 - 09/03/2024 | extracted=0.0  expected=136.09  diff=136.09 |
| 40 | `provider` | 01/22/2021 - 09/03/2024 | extracted='Account 220437'  expected='Hudson Medical, PC' |
| 40 | `insurers` | 01/22/2021 - 09/03/2024 | missing=['tricare'] |
| 40 | `description` | 01/22/2021 - 09/03/2024 | extracted='X-ray wrist, 2 views'  expected=None |
| 41 | `cpt_codes` | 05/01/2021 - 12/24/2024 | missing=['72148', '72158', '73100', '73564', '74178', '76700', '76705', 'A4245', 'A4570', 'A4630', 'J9190'] |
| 41 | `total_charges` | 05/01/2021 - 12/24/2024 | extracted=749.07  expected=7932.64  diff=7183.57 |
| 41 | `ins_paid` | 05/01/2021 - 12/24/2024 | extracted=488.98  expected=4839.82  diff=4350.84 |
| 41 | `adjustment` | 05/01/2021 - 12/24/2024 | extracted=260.09  expected=2834.7  diff=2574.61 |
| 41 | `balance` | 05/01/2021 - 12/24/2024 | extracted=0.0  expected=258.12  diff=258.12 |
| 41 | `provider` | 05/01/2021 - 12/24/2024 | extracted='Account 203166'  expected='Hudson Medical, PC' |
| 41 | `insurers` | 05/01/2021 - 12/24/2024 | missing=['tricare'] |
| 41 | `description` | 05/01/2021 - 12/24/2024 | extracted='Chest X-ray, 2 views'  expected=None |
| 42 | `cpt_codes` | 02/03/2021 - 10/28/2024 | missing=['71046', '71048', '72100', '72110', '73060', '73564', '74177', '74178', '77067', 'A4207', 'A4636']  extra=['J2796'] |
| 42 | `total_charges` | 02/03/2021 - 10/28/2024 | extracted=331.33  expected=5965.57  diff=5634.24 |
| 42 | `ins_paid` | 02/03/2021 - 10/28/2024 | extracted=239.23  expected=3704.2  diff=3464.97 |
| 42 | `adjustment` | 02/03/2021 - 10/28/2024 | extracted=92.1  expected=2108.92  diff=2016.82 |
| 42 | `balance` | 02/03/2021 - 10/28/2024 | extracted=0.0  expected=152.45  diff=152.45 |
| 42 | `provider` | 02/03/2021 - 10/28/2024 | extracted='Account 359478'  expected='Hudson Medical, PC' |
| 42 | `insurers` | 02/03/2021 - 10/28/2024 | missing=['tricare'] |
| 42 | `description` | 02/03/2021 - 10/28/2024 | extracted='Romiplostim, 10 mcg'  expected=None |
| 43 | `cpt_codes` | 03/25/2021 - 09/23/2024 | missing=['72100', '72110', '72148', '73030', '73060', '73110', '74177', '74178', '76830', 'A4637', 'J1644', 'J2250'] |
| 43 | `total_charges` | 03/25/2021 - 09/23/2024 | extracted=250.62  expected=7921.39  diff=7670.77 |
| 43 | `ins_paid` | 03/25/2021 - 09/23/2024 | extracted=156.24  expected=4881.25  diff=4725.01 |
| 43 | `adjustment` | 03/25/2021 - 09/23/2024 | extracted=94.38  expected=2930.37  diff=2835.99 |
| 43 | `balance` | 03/25/2021 - 09/23/2024 | extracted=0.0  expected=109.77  diff=109.77 |
| 43 | `provider` | 03/25/2021 - 09/23/2024 | extracted='Account 137383'  expected='Hudson Medical, PC' |
| 43 | `insurers` | 03/25/2021 - 09/23/2024 | missing=['tricare'] |
| 43 | `description` | 03/25/2021 - 09/23/2024 | extracted='X-ray wrist, 2 views'  expected=None |
| 44 | `cpt_codes` | 02/07/2021 - 10/07/2024 | missing=['71046', '72148', '72158', '73100', '73562', '74178', '77067', 'A4253', 'A4600', 'A4616', 'J0130'] |
| 44 | `total_charges` | 02/07/2021 - 10/07/2024 | extracted=804.04  expected=6985.55  diff=6181.51 |
| 44 | `ins_paid` | 02/07/2021 - 10/07/2024 | extracted=454.43  expected=4342.69  diff=3888.26 |
| 44 | `adjustment` | 02/07/2021 - 10/07/2024 | extracted=349.61  expected=2503.16  diff=2153.55 |
| 44 | `balance` | 02/07/2021 - 10/07/2024 | extracted=0.0  expected=139.7  diff=139.70 |
| 44 | `provider` | 02/07/2021 - 10/07/2024 | extracted='Account 933311'  expected='Hudson Medical, PC' |
| 44 | `insurers` | 02/07/2021 - 10/07/2024 | missing=['tricare'] |
| 44 | `description` | 02/07/2021 - 10/07/2024 | extracted='Ultrasound abdomen, limited'  expected=None |
| 45 | `cpt_codes` | 01/10/2021 - 04/18/2024 | missing=['71048', '72158', '73030', '73100', '73562', '73564', '74178', 'A4637', 'J0153', 'Q2043'] |
| 45 | `total_charges` | 01/10/2021 - 04/18/2024 | extracted=352.65  expected=9434.65  diff=9082.00 |
| 45 | `ins_paid` | 01/10/2021 - 04/18/2024 | extracted=195.19  expected=5918.03  diff=5722.84 |
| 45 | `adjustment` | 01/10/2021 - 04/18/2024 | extracted=157.46  expected=3476.29  diff=3318.83 |
| 45 | `balance` | 01/10/2021 - 04/18/2024 | extracted=0.0  expected=40.33  diff=40.33 |
| 45 | `description` | 01/10/2021 - 04/18/2024 | extracted='X-ray wrist, minimum 3 views'  expected=None |
| 46 | `cpt_codes` | 02/04/2021 - 12/21/2024 | missing=['72100', '73030', '73060', '73110', '74177', '76700', 'A4637', 'J0180', 'J0290', 'J2796', 'J3010', 'J3370', 'J3480']  extra=['71048'] |
| 46 | `total_charges` | 02/04/2021 - 12/21/2024 | extracted=567.57  expected=10391.29  diff=9823.72 |
| 46 | `ins_paid` | 02/04/2021 - 12/21/2024 | extracted=307.18  expected=6455.59  diff=6148.41 |
| 46 | `adjustment` | 02/04/2021 - 12/21/2024 | extracted=189.22  expected=3668.41  diff=3479.19 |
| 46 | `payments` | 02/04/2021 - 12/21/2024 | extracted=71.17  expected=None |
| 46 | `balance` | 02/04/2021 - 12/21/2024 | extracted=0.0  expected=267.29  diff=267.29 |
| 46 | `description` | 02/04/2021 - 12/21/2024 | extracted='Chest X-ray, 4+ views'  expected=None |
| 47 | `cpt_codes` | 05/12/2021 - 12/03/2024 | missing=['71046', '72100', '73030', '73060', '74177', '74178', '76700', '76705', '77067', 'J2250', 'J9190', 'Q9920'] |
| 47 | `total_charges` | 05/12/2021 - 12/03/2024 | extracted=506.64  expected=9309.16  diff=8802.52 |
| 47 | `ins_paid` | 05/12/2021 - 12/03/2024 | extracted=350.77  expected=5756.99  diff=5406.22 |
| 47 | `adjustment` | 05/12/2021 - 12/03/2024 | extracted=122.63  expected=3229.74  diff=3107.11 |
| 47 | `payments` | 05/12/2021 - 12/03/2024 | extracted=33.24  expected=None |
| 47 | `balance` | 05/12/2021 - 12/03/2024 | extracted=0.0  expected=322.43  diff=322.43 |
| 47 | `provider` | 05/12/2021 - 12/03/2024 | extracted='Account 365503'  expected='Hudson Medical, PC' |
| 47 | `insurers` | 05/12/2021 - 12/03/2024 | missing=['tricare'] |
| 47 | `description` | 05/12/2021 - 12/03/2024 | extracted='X-ray wrist, 2 views'  expected=None |
| 48 | `cpt_codes` | 06/07/2022 - 09/18/2024 | missing=['71046', '71048', '72148', '73030', '73060', '73564', '74177', '74178', '76700', '76830', '77067', 'A4550', 'J0171'] |
| 48 | `total_charges` | 06/07/2022 - 09/18/2024 | extracted=490.11  expected=9633.47  diff=9143.36 |
| 48 | `ins_paid` | 06/07/2022 - 09/18/2024 | extracted=282.71  expected=5894.35  diff=5611.64 |
| 48 | `adjustment` | 06/07/2022 - 09/18/2024 | extracted=177.8  expected=3575.9  diff=3398.10 |
| 48 | `payments` | 06/07/2022 - 09/18/2024 | extracted=29.6  expected=None |
| 48 | `balance` | 06/07/2022 - 09/18/2024 | extracted=0.0  expected=163.22  diff=163.22 |
| 48 | `provider` | 06/07/2022 - 09/18/2024 | extracted='Account 419764'  expected='Hudson Medical, PC' |
| 48 | `insurers` | 06/07/2022 - 09/18/2024 | missing=['tricare'] |
| 48 | `description` | 06/07/2022 - 09/18/2024 | extracted='MRI lumbar spine without and with contrast'  expected=None |
| 49 | `cpt_codes` | 02/23/2021 - 08/30/2024 | missing=['71046', '72100', '72110', '72148', '73100', '73562', '74177', '74178', '77067', 'A4206', 'J0285', 'J1642', 'J9000', 'Q0169'] |
| 49 | `total_charges` | 02/23/2021 - 08/30/2024 | extracted=333.85  expected=8898.48  diff=8564.63 |
| 49 | `ins_paid` | 02/23/2021 - 08/30/2024 | extracted=172.78  expected=5553.56  diff=5380.78 |
| 49 | `adjustment` | 02/23/2021 - 08/30/2024 | extracted=136.4  expected=3135.99  diff=2999.59 |
| 49 | `payments` | 02/23/2021 - 08/30/2024 | extracted=24.67  expected=None |
| 49 | `balance` | 02/23/2021 - 08/30/2024 | extracted=0.0  expected=208.93  diff=208.93 |
| 49 | `provider` | 02/23/2021 - 08/30/2024 | extracted='Account 878098'  expected='Hudson Medical, PC' |
| 49 | `insurers` | 02/23/2021 - 08/30/2024 | missing=['tricare'] |
| 49 | `description` | 02/23/2021 - 08/30/2024 | extracted='X-ray shoulder, minimum 2 views'  expected=None |
| 50 | `cpt_codes` | 08/28/2021 - 10/02/2024 | missing=['72110', '72148', '73030', '73110', '73564', '74178', '76705', '76830', 'A4263', 'A4604'] |
| 50 | `total_charges` | 08/28/2021 - 10/02/2024 | extracted=629.36  expected=6700.03  diff=6070.67 |
| 50 | `ins_paid` | 08/28/2021 - 10/02/2024 | extracted=461.14  expected=4383.97  diff=3922.83 |
| 50 | `adjustment` | 08/28/2021 - 10/02/2024 | extracted=168.22  expected=2052.54  diff=1884.32 |
| 50 | `balance` | 08/28/2021 - 10/02/2024 | extracted=0.0  expected=263.52  diff=263.52 |
| 50 | `provider` | 08/28/2021 - 10/02/2024 | extracted='Account 305985'  expected='Hudson Medical, PC' |
| 50 | `insurers` | 08/28/2021 - 10/02/2024 | missing=['tricare'] |
| 50 | `description` | 08/28/2021 - 10/02/2024 | extracted='Chest X-ray, 2 views'  expected=None |
| 51 | `cpt_codes` | 02/07/2021 - 10/19/2024 | missing=['71046', '71048', '72100', '72148', '73030', '73564', '74177', '76830'] |
| 51 | `total_charges` | 02/07/2021 - 10/19/2024 | extracted=804.04  expected=4904.47  diff=4100.43 |
| 51 | `ins_paid` | 02/07/2021 - 10/19/2024 | extracted=454.43  expected=3292.42  diff=2837.99 |
| 51 | `adjustment` | 02/07/2021 - 10/19/2024 | extracted=349.61  expected=1531.36  diff=1181.75 |
| 51 | `balance` | 02/07/2021 - 10/19/2024 | extracted=0.0  expected=80.69  diff=80.69 |
| 51 | `provider` | 02/07/2021 - 10/19/2024 | extracted='Account 933311'  expected='Hudson Medical, PC' |
| 51 | `insurers` | 02/07/2021 - 10/19/2024 | missing=['tricare'] |
| 51 | `description` | 02/07/2021 - 10/19/2024 | extracted='Ultrasound abdomen, limited'  expected=None |
| 52 | `cpt_codes` | 01/13/2021 - 09/09/2024 | missing=['71046', '71048', '72110', '74177', '74178', '76705', 'A4570', 'J0360', 'J3010'] |
| 52 | `total_charges` | 01/13/2021 - 09/09/2024 | extracted=645.72  expected=5729.54  diff=5083.82 |
| 52 | `ins_paid` | 01/13/2021 - 09/09/2024 | extracted=435.37  expected=3662.37  diff=3227.00 |
| 52 | `adjustment` | 01/13/2021 - 09/09/2024 | extracted=144.42  expected=1876.74  diff=1732.32 |
| 52 | `payments` | 01/13/2021 - 09/09/2024 | extracted=65.93  expected=None |
| 52 | `balance` | 01/13/2021 - 09/09/2024 | extracted=0.0  expected=190.43  diff=190.43 |
| 52 | `provider` | 01/13/2021 - 09/09/2024 | extracted='Account 862727'  expected='Hudson Medical, PC' |
| 52 | `insurers` | 01/13/2021 - 09/09/2024 | missing=['tricare'] |
| 52 | `description` | 01/13/2021 - 09/09/2024 | extracted='Syringe with needle, sterile, 2cc'  expected=None |
| 53 | `cpt_codes` | 03/01/2021 - 09/17/2024 | missing=['71046', '71048', '72110', '73030', '73110', '76830', '77067', 'A4636', 'A4649', 'J2720', 'Q2043'] |
| 53 | `total_charges` | 03/01/2021 - 09/17/2024 | extracted=276.35  expected=6087.7  diff=5811.35 |
| 53 | `ins_paid` | 03/01/2021 - 09/17/2024 | extracted=193.06  expected=4028.08  diff=3835.02 |
| 53 | `adjustment` | 03/01/2021 - 09/17/2024 | extracted=83.29  expected=1772.94  diff=1689.65 |
| 53 | `balance` | 03/01/2021 - 09/17/2024 | extracted=0.0  expected=286.68  diff=286.68 |
| 53 | `provider` | 03/01/2021 - 09/17/2024 | extracted='Account 765299'  expected='Hudson Medical, PC' |
| 53 | `insurers` | 03/01/2021 - 09/17/2024 | missing=['tricare'] |
| 53 | `description` | 03/01/2021 - 09/17/2024 | extracted='X-ray knee, 4+ views'  expected=None |
| 54 | `cpt_codes` | 05/29/2021 - 09/14/2024 | missing=['71046', '71048', '72100', '72110', '73562', 'J0285', 'J9035', 'J9190'] |
| 54 | `total_charges` | 05/29/2021 - 09/14/2024 | extracted=831.1  expected=7134.76  diff=6303.66 |
| 54 | `ins_paid` | 05/29/2021 - 09/14/2024 | extracted=484.59  expected=4369.39  diff=3884.80 |
| 54 | `adjustment` | 05/29/2021 - 09/14/2024 | extracted=346.51  expected=2643.22  diff=2296.71 |
| 54 | `balance` | 05/29/2021 - 09/14/2024 | extracted=0.0  expected=122.15  diff=122.15 |
| 54 | `provider` | 05/29/2021 - 09/14/2024 | extracted='Account 487559'  expected='Hudson Medical, PC' |
| 54 | `insurers` | 05/29/2021 - 09/14/2024 | missing=['tricare'] |
| 54 | `description` | 05/29/2021 - 09/14/2024 | extracted='Ultrasound pelvis, transvaginal'  expected=None |
| 55 | `cpt_codes` | 10/04/2021 - 09/16/2024 | missing=['72148', '72158', '73030', '73100', '73110', '74177', '74178', '76830', '77067', 'J0171']  extra=['71046'] |
| 55 | `total_charges` | 10/04/2021 - 09/16/2024 | extracted=534.97  expected=4085.52  diff=3550.55 |
| 55 | `ins_paid` | 10/04/2021 - 09/16/2024 | extracted=281.71  expected=2432.48  diff=2150.77 |
| 55 | `adjustment` | 10/04/2021 - 09/16/2024 | extracted=253.26  expected=1560.39  diff=1307.13 |
| 55 | `balance` | 10/04/2021 - 09/16/2024 | extracted=0.0  expected=92.65  diff=92.65 |
| 55 | `description` | 10/04/2021 - 09/16/2024 | extracted='Chest X-ray, 2 views'  expected=None |
| 56 | `cpt_codes` | 02/23/2021 - 08/18/2024 | missing=['71046', '72100', '72148', '72158', '73100', '73110', '76700', '76830', 'J2001', 'J2405'] |
| 56 | `total_charges` | 02/23/2021 - 08/18/2024 | extracted=333.85  expected=7993.93  diff=7660.08 |
| 56 | `ins_paid` | 02/23/2021 - 08/18/2024 | extracted=172.78  expected=4956.43  diff=4783.65 |
| 56 | `adjustment` | 02/23/2021 - 08/18/2024 | extracted=136.4  expected=2810.57  diff=2674.17 |
| 56 | `payments` | 02/23/2021 - 08/18/2024 | extracted=24.67  expected=None |
| 56 | `balance` | 02/23/2021 - 08/18/2024 | extracted=0.0  expected=226.93  diff=226.93 |
| 56 | `provider` | 02/23/2021 - 08/18/2024 | extracted='Account 878098'  expected='Hudson Medical, PC' |
| 56 | `insurers` | 02/23/2021 - 08/18/2024 | missing=['tricare'] |
| 56 | `description` | 02/23/2021 - 08/18/2024 | extracted='X-ray shoulder, minimum 2 views'  expected=None |
| 57 | `cpt_codes` | 05/03/2021 - 06/29/2024 | missing=['72158', '73060', '73100', '73564', '74178', '76700', '76705', '76830', '77067', 'J0290', 'J1055', 'J2730'] |
| 57 | `total_charges` | 05/03/2021 - 06/29/2024 | extracted=118.0  expected=6031.92  diff=5913.92 |
| 57 | `ins_paid` | 05/03/2021 - 06/29/2024 | extracted=63.57  expected=3958.31  diff=3894.74 |
| 57 | `adjustment` | 05/03/2021 - 06/29/2024 | extracted=54.43  expected=2010.86  diff=1956.43 |
| 57 | `balance` | 05/03/2021 - 06/29/2024 | extracted=0.0  expected=62.75  diff=62.75 |
| 57 | `provider` | 05/03/2021 - 06/29/2024 | extracted='Account 456066'  expected='Hudson Medical, PC' |
| 57 | `insurers` | 05/03/2021 - 06/29/2024 | missing=['tricare'] |
| 57 | `description` | 05/03/2021 - 06/29/2024 | extracted='Heparin sodium, 10 units'  expected=None |
| 58 | `cpt_codes` | 03/23/2021 - 10/07/2024 | missing=['71046', '72100', '72148', '73060', '73110', '74178', '76700', '76705', 'A4207', 'A4247', 'J1040', 'J2720', 'J9035']  extra=['71048'] |
| 58 | `total_charges` | 03/23/2021 - 10/07/2024 | extracted=413.69  expected=7191.32  diff=6777.63 |
| 58 | `ins_paid` | 03/23/2021 - 10/07/2024 | extracted=299.52  expected=4516.75  diff=4217.23 |
| 58 | `adjustment` | 03/23/2021 - 10/07/2024 | extracted=114.17  expected=2429.67  diff=2315.50 |
| 58 | `balance` | 03/23/2021 - 10/07/2024 | extracted=0.0  expected=244.9  diff=244.90 |
| 58 | `provider` | 03/23/2021 - 10/07/2024 | extracted='Account 299943'  expected='Hudson Medical, PC' |
| 58 | `insurers` | 03/23/2021 - 10/07/2024 | missing=['tricare'] |
| 58 | `description` | 03/23/2021 - 10/07/2024 | extracted='Chest X-ray, 4+ views'  expected=None |
| 59 | `cpt_codes` | 01/22/2021 - 12/05/2024 | missing=['72100', '72110', '72148', '73564', '74177', '74178', '76700', '76705', '76830', 'A4207', 'A4245', 'A4246'] |
| 59 | `total_charges` | 01/22/2021 - 12/05/2024 | extracted=863.02  expected=9587.28  diff=8724.26 |
| 59 | `ins_paid` | 01/22/2021 - 12/05/2024 | extracted=619.92  expected=6029.89  diff=5409.97 |
| 59 | `adjustment` | 01/22/2021 - 12/05/2024 | extracted=243.1  expected=3357.02  diff=3113.92 |
| 59 | `balance` | 01/22/2021 - 12/05/2024 | extracted=0.0  expected=200.37  diff=200.37 |
| 59 | `provider` | 01/22/2021 - 12/05/2024 | extracted='Account 220437'  expected='Hudson Medical, PC' |
| 59 | `insurers` | 01/22/2021 - 12/05/2024 | missing=['tricare'] |
| 59 | `description` | 01/22/2021 - 12/05/2024 | extracted='X-ray wrist, 2 views'  expected=None |
| 60 | `cpt_codes` | 01/08/2021 - 07/20/2024 | missing=['71046', '71048', '72110', '72148', '72158', '73030', '73060', '73100', '73564', '74178', '76830', '77067', 'A4209', 'A4657'] |
| 60 | `total_charges` | 01/08/2021 - 07/20/2024 | extracted=179.57  expected=9589.68  diff=9410.11 |
| 60 | `ins_paid` | 01/08/2021 - 07/20/2024 | extracted=116.53  expected=5933.0  diff=5816.47 |
| 60 | `adjustment` | 01/08/2021 - 07/20/2024 | extracted=63.04  expected=3570.71  diff=3507.67 |
| 60 | `balance` | 01/08/2021 - 07/20/2024 | extracted=0.0  expected=85.97  diff=85.97 |
| 60 | `description` | 01/08/2021 - 07/20/2024 | extracted='Ultrasound abdomen, complete'  expected=None |
| 61 | `cpt_codes` | 03/10/2021 - 06/19/2024 | missing=['72110', '72158', '73100', '73110', '73562', '74177', '76700', '76830', 'J0290', 'Q0163']  extra=['72148'] |
| 61 | `total_charges` | 03/10/2021 - 06/19/2024 | extracted=519.73  expected=6414.64  diff=5894.91 |
| 61 | `ins_paid` | 03/10/2021 - 06/19/2024 | extracted=269.51  expected=4049.51  diff=3780.00 |
| 61 | `adjustment` | 03/10/2021 - 06/19/2024 | extracted=224.08  expected=2107.19  diff=1883.11 |
| 61 | `payments` | 03/10/2021 - 06/19/2024 | extracted=26.14  expected=None |
| 61 | `balance` | 03/10/2021 - 06/19/2024 | extracted=0.0  expected=257.94  diff=257.94 |
| 61 | `provider` | 03/10/2021 - 06/19/2024 | extracted='Account 563287'  expected='Hudson Medical, PC' |
| 61 | `insurers` | 03/10/2021 - 06/19/2024 | missing=['tricare'] |
| 61 | `description` | 03/10/2021 - 06/19/2024 | extracted='MRI lumbar spine without contrast'  expected=None |
| 62 | `cpt_codes` | 06/08/2021 - 09/14/2024 | missing=['72100', '72110', '72148', '73030', '73060', '73562', '74178', '76705', '76830', 'A4627', 'J0270', 'J1040', 'J9000', 'Q9920'] |
| 62 | `total_charges` | 06/08/2021 - 09/14/2024 | extracted=590.13  expected=8552.72  diff=7962.59 |
| 62 | `ins_paid` | 06/08/2021 - 09/14/2024 | extracted=404.87  expected=5250.97  diff=4846.10 |
| 62 | `adjustment` | 06/08/2021 - 09/14/2024 | extracted=185.26  expected=3260.12  diff=3074.86 |
| 62 | `balance` | 06/08/2021 - 09/14/2024 | extracted=0.0  expected=41.63  diff=41.63 |
| 62 | `provider` | 06/08/2021 - 09/14/2024 | extracted='Account 576163'  expected='Hudson Medical, PC' |
| 62 | `insurers` | 06/08/2021 - 09/14/2024 | missing=['tricare'] |
| 63 | `cpt_codes` | 10/21/2021 - 08/12/2024 | missing=['72100', '72148', '72158', '73060', '73100', '76830', 'A4656', 'J0290'] |
| 63 | `total_charges` | 10/21/2021 - 08/12/2024 | extracted=899.01  expected=7076.0  diff=6176.99 |
| 63 | `ins_paid` | 10/21/2021 - 08/12/2024 | extracted=452.54  expected=4197.0  diff=3744.46 |
| 63 | `adjustment` | 10/21/2021 - 08/12/2024 | extracted=446.47  expected=2628.99  diff=2182.52 |
| 63 | `balance` | 10/21/2021 - 08/12/2024 | extracted=0.0  expected=250.01  diff=250.01 |
| 63 | `provider` | 10/21/2021 - 08/12/2024 | extracted='Account 529041'  expected='Hudson Medical, PC' |
| 63 | `insurers` | 10/21/2021 - 08/12/2024 | missing=['tricare'] |
| 64 | `cpt_codes` | 02/02/2021 - 12/26/2024 | missing=['71046', '72100', '72110', '73030', '73060', '73110', '73562', '73564', '76705', '76830', 'A4253', 'J0270', 'J1040', 'J2250'] |
| 64 | `total_charges` | 02/02/2021 - 12/26/2024 | extracted=476.27  expected=9529.24  diff=9052.97 |
| 64 | `ins_paid` | 02/02/2021 - 12/26/2024 | extracted=238.82  expected=5869.7  diff=5630.88 |
| 64 | `adjustment` | 02/02/2021 - 12/26/2024 | extracted=237.45  expected=3437.88  diff=3200.43 |
| 64 | `balance` | 02/02/2021 - 12/26/2024 | extracted=0.0  expected=221.66  diff=221.66 |
| 64 | `provider` | 02/02/2021 - 12/26/2024 | extracted='Account 546793'  expected='Hudson Medical, PC' |
| 64 | `insurers` | 02/02/2021 - 12/26/2024 | missing=['tricare'] |
| 65 | `cpt_codes` | 04/22/2021 - 05/07/2024 | missing=['72158', '73030', '73100', '73110', '73562', '73564', '76700', 'A4253', 'A4636'] |
| 65 | `total_charges` | 04/22/2021 - 05/07/2024 | extracted=849.81  expected=6822.95  diff=5973.14 |
| 65 | `ins_paid` | 04/22/2021 - 05/07/2024 | extracted=516.82  expected=4085.1  diff=3568.28 |
| 65 | `adjustment` | 04/22/2021 - 05/07/2024 | extracted=332.99  expected=2558.2  diff=2225.21 |
| 65 | `balance` | 04/22/2021 - 05/07/2024 | extracted=0.0  expected=179.65  diff=179.65 |
| 65 | `provider` | 04/22/2021 - 05/07/2024 | extracted='Account 701202'  expected='Hudson Medical, PC' |
| 65 | `insurers` | 04/22/2021 - 05/07/2024 | missing=['tricare'] |
| 66 | `cpt_codes` | 02/27/2021 - 11/06/2024 | missing=['71048', '72100', '72110', '73030', '73060', '73100', '73110', '76700', '77067', 'A4614', 'A4630', 'J1644']  extra=['74177'] |
| 66 | `total_charges` | 02/27/2021 - 11/06/2024 | extracted=215.64  expected=9532.44  diff=9316.80 |
| 66 | `ins_paid` | 02/27/2021 - 11/06/2024 | extracted=144.57  expected=5685.27  diff=5540.70 |
| 66 | `adjustment` | 02/27/2021 - 11/06/2024 | extracted=41.7  expected=3707.86  diff=3666.16 |
| 66 | `payments` | 02/27/2021 - 11/06/2024 | extracted=29.37  expected=None |
| 66 | `balance` | 02/27/2021 - 11/06/2024 | extracted=0.0  expected=139.31  diff=139.31 |
| 66 | `provider` | 02/27/2021 - 11/06/2024 | extracted='Account 951078'  expected='Hudson Medical, PC' |
| 66 | `insurers` | 02/27/2021 - 11/06/2024 | missing=['tricare'] |
| 66 | `description` | 02/27/2021 - 11/06/2024 | extracted='CT abdomen & pelvis with contrast'  expected=None |
| 67 | `cpt_codes` | 06/24/2021 - 09/30/2024 | missing=['71048', '72100', '72110', '73030', '73060', '73100', '73110', '73562', 'A4637', 'J0285'] |
| 67 | `total_charges` | 06/24/2021 - 09/30/2024 | extracted=694.84  expected=6186.91  diff=5492.07 |
| 67 | `ins_paid` | 06/24/2021 - 09/30/2024 | extracted=411.54  expected=3761.19  diff=3349.65 |
| 67 | `adjustment` | 06/24/2021 - 09/30/2024 | extracted=283.3  expected=2425.72  diff=2142.42 |
| 67 | `provider` | 06/24/2021 - 09/30/2024 | extracted='Account 372274'  expected='Hudson Medical, PC' |
| 67 | `insurers` | 06/24/2021 - 09/30/2024 | missing=['tricare'] |
| 68 | `cpt_codes` | 01/09/2021 - 11/14/2024 | missing=['72100', '72110', '72148', '73060', '73100', '73110', '73562', '73564', '76700', '76830', 'A4209', 'J9190'] |
| 68 | `total_charges` | 01/09/2021 - 11/14/2024 | extracted=584.38  expected=8356.42  diff=7772.04 |
| 68 | `ins_paid` | 01/09/2021 - 11/14/2024 | extracted=425.78  expected=5255.62  diff=4829.84 |
| 68 | `adjustment` | 01/09/2021 - 11/14/2024 | extracted=158.6  expected=2755.55  diff=2596.95 |
| 68 | `balance` | 01/09/2021 - 11/14/2024 | extracted=0.0  expected=345.25  diff=345.25 |
| 68 | `provider` | 01/09/2021 - 11/14/2024 | extracted='Account 749764'  expected='Hudson Medical, PC' |
| 68 | `insurers` | 01/09/2021 - 11/14/2024 | missing=['tricare'] |
| 69 | `cpt_codes` | 03/09/2021 - 11/18/2024 | missing=['71048', '72100', '72148', '72158', '73100', '73562', '74178', '76700', '76830', '77067', 'A4207', 'A4247', 'Q0163'] |
| 69 | `total_charges` | 03/09/2021 - 11/18/2024 | extracted=470.09  expected=9131.34  diff=8661.25 |
| 69 | `ins_paid` | 03/09/2021 - 11/18/2024 | extracted=280.81  expected=5593.31  diff=5312.50 |
| 69 | `adjustment` | 03/09/2021 - 11/18/2024 | extracted=189.28  expected=3306.65  diff=3117.37 |
| 69 | `balance` | 03/09/2021 - 11/18/2024 | extracted=0.0  expected=231.38  diff=231.38 |
| 69 | `provider` | 03/09/2021 - 11/18/2024 | extracted='Account 424259'  expected='Hudson Medical, PC' |
| 69 | `insurers` | 03/09/2021 - 11/18/2024 | missing=['tricare'] |
| 70 | `cpt_codes` | 02/27/2021 - 06/26/2024 | missing=['71046', '72110', '72148', '72158', '73060', '76705', 'J2796', 'J9000']  extra=['74177'] |
| 70 | `total_charges` | 02/27/2021 - 06/26/2024 | extracted=215.64  expected=3626.36  diff=3410.72 |
| 70 | `ins_paid` | 02/27/2021 - 06/26/2024 | extracted=144.57  expected=2130.09  diff=1985.52 |
| 70 | `adjustment` | 02/27/2021 - 06/26/2024 | extracted=41.7  expected=1374.78  diff=1333.08 |
| 70 | `payments` | 02/27/2021 - 06/26/2024 | extracted=29.37  expected=None |
| 70 | `balance` | 02/27/2021 - 06/26/2024 | extracted=0.0  expected=121.49  diff=121.49 |
| 70 | `provider` | 02/27/2021 - 06/26/2024 | extracted='Account 951078'  expected='Hudson Medical, PC' |
| 70 | `insurers` | 02/27/2021 - 06/26/2024 | missing=['tricare'] |
| 70 | `description` | 02/27/2021 - 06/26/2024 | extracted='CT abdomen & pelvis with contrast'  expected=None |
| 71 | `cpt_codes` | 04/19/2021 - 06/09/2024 | missing=['71048', '73030', '73110', '76700', '76705', '77067', 'A4247']  extra=['J9045'] |
| 71 | `total_charges` | 04/19/2021 - 06/09/2024 | extracted=731.96  expected=4905.43  diff=4173.47 |
| 71 | `ins_paid` | 04/19/2021 - 06/09/2024 | extracted=413.63  expected=3204.24  diff=2790.61 |
| 71 | `adjustment` | 04/19/2021 - 06/09/2024 | extracted=318.33  expected=1594.44  diff=1276.11 |
| 71 | `balance` | 04/19/2021 - 06/09/2024 | extracted=0.0  expected=106.75  diff=106.75 |
| 71 | `description` | 04/19/2021 - 06/09/2024 | extracted='Carboplatin, 50 mg'  expected=None |
| 72 | `cpt_codes` | 01/13/2021 - 12/11/2024 | missing=['71046', '72100', '72148', '73030', '73060', '73562', '76700', '76705', '77067']  extra=['A4207'] |
| 72 | `total_charges` | 01/13/2021 - 12/11/2024 | extracted=645.72  expected=6338.2  diff=5692.48 |
| 72 | `ins_paid` | 01/13/2021 - 12/11/2024 | extracted=435.37  expected=4311.42  diff=3876.05 |
| 72 | `adjustment` | 01/13/2021 - 12/11/2024 | extracted=144.42  expected=1962.39  diff=1817.97 |
| 72 | `payments` | 01/13/2021 - 12/11/2024 | extracted=65.93  expected=None |
| 72 | `balance` | 01/13/2021 - 12/11/2024 | extracted=0.0  expected=64.39  diff=64.39 |
| 72 | `provider` | 01/13/2021 - 12/11/2024 | extracted='Account 862727'  expected='Hudson Medical, PC' |
| 72 | `insurers` | 01/13/2021 - 12/11/2024 | missing=['tricare'] |
| 72 | `description` | 01/13/2021 - 12/11/2024 | extracted='Syringe with needle, sterile, 2cc'  expected=None |
| 73 | `cpt_codes` | 02/20/2021 - 12/09/2024 | missing=['71046', '72148', '72158', '73060', '73100', '73110', '73564', '74177', '77067', 'A4207', 'J0270']  extra=['74178'] |
| 73 | `total_charges` | 02/20/2021 - 12/09/2024 | extracted=709.76  expected=7811.45  diff=7101.69 |
| 73 | `ins_paid` | 02/20/2021 - 12/09/2024 | extracted=402.32  expected=4751.73  diff=4349.41 |
| 73 | `adjustment` | 02/20/2021 - 12/09/2024 | extracted=238.1  expected=2922.69  diff=2684.59 |
| 73 | `payments` | 02/20/2021 - 12/09/2024 | extracted=69.34  expected=None |
| 73 | `balance` | 02/20/2021 - 12/09/2024 | extracted=0.0  expected=137.03  diff=137.03 |
| 73 | `provider` | 02/20/2021 - 12/09/2024 | extracted='Account 819529'  expected='Hudson Medical, PC' |
| 73 | `insurers` | 02/20/2021 - 12/09/2024 | missing=['tricare'] |
| 73 | `description` | 02/20/2021 - 12/09/2024 | extracted='CT abdomen & pelvis without and with contrast'  expected=None |
| 74 | `cpt_codes` | 01/13/2021 - 11/16/2024 | missing=['72110', '72148', '72158', '73030', '73100', '76700', '76705', '76830', '77067', 'A4604', 'J3010']  extra=['A4207'] |
| 74 | `total_charges` | 01/13/2021 - 11/16/2024 | extracted=645.72  expected=6180.74  diff=5535.02 |
| 74 | `ins_paid` | 01/13/2021 - 11/16/2024 | extracted=435.37  expected=3657.7  diff=3222.33 |
| 74 | `adjustment` | 01/13/2021 - 11/16/2024 | extracted=144.42  expected=2308.1  diff=2163.68 |
| 74 | `payments` | 01/13/2021 - 11/16/2024 | extracted=65.93  expected=None |
| 74 | `balance` | 01/13/2021 - 11/16/2024 | extracted=0.0  expected=214.94  diff=214.94 |
| 74 | `provider` | 01/13/2021 - 11/16/2024 | extracted='Account 862727'  expected='Hudson Medical, PC' |
| 74 | `insurers` | 01/13/2021 - 11/16/2024 | missing=['tricare'] |
| 74 | `description` | 01/13/2021 - 11/16/2024 | extracted='Syringe with needle, sterile, 2cc'  expected=None |
| 75 | `cpt_codes` | 04/07/2021 - 09/21/2024 | missing=['71048', '72100', '72158', '73030', '73562', '74177', '74178', '76700', '76705', 'A4206', 'A4637', 'Q0169'] |
| 75 | `total_charges` | 04/07/2021 - 09/21/2024 | extracted=650.91  expected=8378.53  diff=7727.62 |
| 75 | `ins_paid` | 04/07/2021 - 09/21/2024 | extracted=391.72  expected=5450.53  diff=5058.81 |
| 75 | `adjustment` | 04/07/2021 - 09/21/2024 | extracted=259.19  expected=2487.31  diff=2228.12 |
| 75 | `balance` | 04/07/2021 - 09/21/2024 | extracted=0.0  expected=440.69  diff=440.69 |
| 75 | `provider` | 04/07/2021 - 09/21/2024 | extracted='Account 489315'  expected='Hudson Medical, PC' |
| 75 | `insurers` | 04/07/2021 - 09/21/2024 | missing=['tricare'] |
| 76 | `cpt_codes` | 01/26/2021 - 12/04/2024 | missing=['72110', '73100', '73562', 'A4245', 'J0270', 'J2730'] |
| 76 | `total_charges` | 01/26/2021 - 12/04/2024 | extracted=564.68  expected=4328.53  diff=3763.85 |
| 76 | `ins_paid` | 01/26/2021 - 12/04/2024 | extracted=377.2  expected=2887.41  diff=2510.21 |
| 76 | `adjustment` | 01/26/2021 - 12/04/2024 | extracted=187.48  expected=1417.95  diff=1230.47 |
| 76 | `balance` | 01/26/2021 - 12/04/2024 | extracted=0.0  expected=23.17  diff=23.17 |
| 76 | `provider` | 01/26/2021 - 12/04/2024 | extracted='Account 792854'  expected='Hudson Medical, PC' |
| 76 | `insurers` | 01/26/2021 - 12/04/2024 | missing=['tricare'] |
| 77 | `cpt_codes` | 02/04/2021 - 10/23/2024 | missing=['72100', '72110', '73100', '73562', '73564', '74178', '76700', '76830', 'A4570', 'J9190']  extra=['71048'] |
| 77 | `total_charges` | 02/04/2021 - 10/23/2024 | extracted=567.57  expected=6029.6  diff=5462.03 |
| 77 | `ins_paid` | 02/04/2021 - 10/23/2024 | extracted=307.18  expected=3646.81  diff=3339.63 |
| 77 | `adjustment` | 02/04/2021 - 10/23/2024 | extracted=189.22  expected=2052.44  diff=1863.22 |
| 77 | `payments` | 02/04/2021 - 10/23/2024 | extracted=71.17  expected=None |
| 77 | `balance` | 02/04/2021 - 10/23/2024 | extracted=0.0  expected=330.35  diff=330.35 |
| 77 | `description` | 02/04/2021 - 10/23/2024 | extracted='Chest X-ray, 4+ views'  expected=None |
| 78 | `cpt_codes` | 01/05/2021 - 11/20/2024 | missing=['71046', '71048', '72110', '73100', '73562', '74177', '77067', 'A4209', 'A4263', 'J0171'] |
| 78 | `total_charges` | 01/05/2021 - 11/20/2024 | extracted=762.72  expected=6903.55  diff=6140.83 |
| 78 | `ins_paid` | 01/05/2021 - 11/20/2024 | extracted=491.81  expected=4378.68  diff=3886.87 |
| 78 | `adjustment` | 01/05/2021 - 11/20/2024 | extracted=270.91  expected=2402.61  diff=2131.70 |
| 78 | `balance` | 01/05/2021 - 11/20/2024 | extracted=0.0  expected=122.26  diff=122.26 |
| 78 | `provider` | 01/05/2021 - 11/20/2024 | extracted='Account 336260'  expected='Hudson Medical, PC' |
| 78 | `insurers` | 01/05/2021 - 11/20/2024 | missing=['tricare'] |
| 79 | `cpt_codes` | 04/14/2021 - 12/18/2024 | missing=['72100', '72110', '72148', '72158', '73030', '73060', '73100', '74177', '76830', 'A4245', 'A4570', 'J9045']  extra=['J2001'] |
| 79 | `total_charges` | 04/14/2021 - 12/18/2024 | extracted=566.41  expected=7043.89  diff=6477.48 |
| 79 | `ins_paid` | 04/14/2021 - 12/18/2024 | extracted=412.96  expected=4280.0  diff=3867.04 |
| 79 | `adjustment` | 04/14/2021 - 12/18/2024 | extracted=83.16  expected=2456.58  diff=2373.42 |
| 79 | `payments` | 04/14/2021 - 12/18/2024 | extracted=70.29  expected=None |
| 79 | `balance` | 04/14/2021 - 12/18/2024 | extracted=0.0  expected=307.31  diff=307.31 |
| 79 | `provider` | 04/14/2021 - 12/18/2024 | extracted='Account 885862'  expected='Hudson Medical, PC' |
| 79 | `insurers` | 04/14/2021 - 12/18/2024 | missing=['tricare'] |
| 79 | `description` | 04/14/2021 - 12/18/2024 | extracted='Lidocaine HCl for intravenous infusion, 10 mg'  expected=None |
| 80 | `cpt_codes` | 02/04/2021 - 12/17/2024 | missing=['71046', '72110', '72148', '72158', '73060', '73564', '74177', '76705', '76830', '77067', 'A4209', 'J0270'] |
| 80 | `total_charges` | 02/04/2021 - 12/17/2024 | extracted=567.57  expected=6531.49  diff=5963.92 |
| 80 | `ins_paid` | 02/04/2021 - 12/17/2024 | extracted=307.18  expected=4170.43  diff=3863.25 |
| 80 | `adjustment` | 02/04/2021 - 12/17/2024 | extracted=189.22  expected=2209.84  diff=2020.62 |
| 80 | `payments` | 02/04/2021 - 12/17/2024 | extracted=71.17  expected=None |
| 80 | `balance` | 02/04/2021 - 12/17/2024 | extracted=0.0  expected=151.22  diff=151.22 |
| 80 | `description` | 02/04/2021 - 12/17/2024 | extracted='Chest X-ray, 4+ views'  expected=None |
| 81 | `cpt_codes` | 04/23/2021 - 11/26/2024 | missing=['71046', '72100', '72110', '73060', '73100', '73110', '73562', '74177', '74178', '76705', '76830', 'A4247', 'A4630', 'J0171', 'J0180', 'J2405']  extra=['A4656'] |
| 81 | `total_charges` | 04/23/2021 - 11/26/2024 | extracted=354.08  expected=10037.28  diff=9683.20 |
| 81 | `ins_paid` | 04/23/2021 - 11/26/2024 | extracted=185.04  expected=6242.59  diff=6057.55 |
| 81 | `adjustment` | 04/23/2021 - 11/26/2024 | extracted=169.04  expected=3546.15  diff=3377.11 |
| 81 | `balance` | 04/23/2021 - 11/26/2024 | extracted=0.0  expected=248.54  diff=248.54 |
| 81 | `description` | 04/23/2021 - 11/26/2024 | extracted='Needle, any type, each'  expected=None |
| 82 | `cpt_codes` | 01/04/2021 - 12/16/2024 | missing=['71048', '72148', '72158', '73030', '73060', '73110', '76830', '77067', 'A4550', 'Q2043'] |
| 82 | `total_charges` | 01/04/2021 - 12/16/2024 | extracted=781.45  expected=7584.5  diff=6803.05 |
| 82 | `ins_paid` | 01/04/2021 - 12/16/2024 | extracted=523.06  expected=4956.17  diff=4433.11 |
| 82 | `adjustment` | 01/04/2021 - 12/16/2024 | extracted=258.39  expected=2508.66  diff=2250.27 |
| 82 | `balance` | 01/04/2021 - 12/16/2024 | extracted=0.0  expected=119.67  diff=119.67 |
| 82 | `provider` | 01/04/2021 - 12/16/2024 | extracted='Account 434662'  expected='Hudson Medical, PC' |
| 82 | `insurers` | 01/04/2021 - 12/16/2024 | missing=['tricare'] |
| 83 | `cpt_codes` | 06/09/2021 - 12/29/2024 | missing=['71048', '72100', '72110', '72158', '73060', '73564', '77067', 'Q4100'] |
| 83 | `total_charges` | 06/09/2021 - 12/29/2024 | extracted=298.25  expected=7292.81  diff=6994.56 |
| 83 | `ins_paid` | 06/09/2021 - 12/29/2024 | extracted=222.51  expected=4490.75  diff=4268.24 |
| 83 | `adjustment` | 06/09/2021 - 12/29/2024 | extracted=43.53  expected=2683.52  diff=2639.99 |
| 83 | `payments` | 06/09/2021 - 12/29/2024 | extracted=32.21  expected=None |
| 83 | `balance` | 06/09/2021 - 12/29/2024 | extracted=0.0  expected=118.54  diff=118.54 |
| 83 | `description` | 06/09/2021 - 12/29/2024 | extracted='X-ray wrist, minimum 3 views'  expected=None |
| 84 | `cpt_codes` | 02/12/2021 - 09/21/2024 | missing=['71048', '72100', '72148', '73060', '73564', '74177', '74178', '77067', 'A4244', 'A4649']  extra=['72158'] |
| 84 | `total_charges` | 02/12/2021 - 09/21/2024 | extracted=334.63  expected=5922.26  diff=5587.63 |
| 84 | `ins_paid` | 02/12/2021 - 09/21/2024 | extracted=225.34  expected=3684.26  diff=3458.92 |
| 84 | `adjustment` | 02/12/2021 - 09/21/2024 | extracted=109.29  expected=2162.28  diff=2052.99 |
| 84 | `balance` | 02/12/2021 - 09/21/2024 | extracted=0.0  expected=75.72  diff=75.72 |
| 84 | `description` | 02/12/2021 - 09/21/2024 | extracted='MRI lumbar spine without and with contrast'  expected=None |
| 85 | `cpt_codes` | 04/06/2021 - 11/30/2024 | missing=['71046', '73060', '73564', '74177', '74178', '76700', '76705', 'A4209', 'A4550', 'J0153', 'Q0163']  extra=['73110'] |
| 85 | `total_charges` | 04/06/2021 - 11/30/2024 | extracted=273.59  expected=6419.81  diff=6146.22 |
| 85 | `ins_paid` | 04/06/2021 - 11/30/2024 | extracted=190.83  expected=3965.87  diff=3775.04 |
| 85 | `adjustment` | 04/06/2021 - 11/30/2024 | extracted=82.76  expected=2350.49  diff=2267.73 |
| 85 | `balance` | 04/06/2021 - 11/30/2024 | extracted=0.0  expected=103.45  diff=103.45 |
| 85 | `provider` | 04/06/2021 - 11/30/2024 | extracted='Account 280485'  expected='Hudson Medical, PC' |
| 85 | `insurers` | 04/06/2021 - 11/30/2024 | missing=['tricare'] |
| 86 | `cpt_codes` | 05/05/2021 - 11/19/2024 | missing=['71046', '71048', '72148', '72158', '73100', '73562', '76700', '76705', '76830', 'J0270', 'J0360', 'J3370'] |
| 86 | `total_charges` | 05/05/2021 - 11/19/2024 | extracted=432.71  expected=11344.81  diff=10912.10 |
| 86 | `ins_paid` | 05/05/2021 - 11/19/2024 | extracted=275.64  expected=6986.74  diff=6711.10 |
| 86 | `adjustment` | 05/05/2021 - 11/19/2024 | extracted=157.07  expected=4151.55  diff=3994.48 |
| 86 | `balance` | 05/05/2021 - 11/19/2024 | extracted=0.0  expected=206.52  diff=206.52 |
| 86 | `provider` | 05/05/2021 - 11/19/2024 | extracted='Account 177320'  expected='Hudson Medical, PC' |
| 86 | `insurers` | 05/05/2021 - 11/19/2024 | missing=['tricare'] |
| 87 | `cpt_codes` | 01/30/2021 - 07/28/2024 | missing=['71046', '71048', '72110', '72158', '73100', '73110', '76700', '76830', 'J9045', 'Q2043'] |
| 87 | `total_charges` | 01/30/2021 - 07/28/2024 | extracted=554.63  expected=8337.03  diff=7782.40 |
| 87 | `ins_paid` | 01/30/2021 - 07/28/2024 | extracted=377.15  expected=5326.16  diff=4949.01 |
| 87 | `adjustment` | 01/30/2021 - 07/28/2024 | extracted=177.48  expected=2683.97  diff=2506.49 |
| 87 | `balance` | 01/30/2021 - 07/28/2024 | extracted=0.0  expected=326.9  diff=326.90 |
| 87 | `provider` | 01/30/2021 - 07/28/2024 | extracted='Account 106470'  expected='Hudson Medical, PC' |
| 87 | `insurers` | 01/30/2021 - 07/28/2024 | missing=['tricare'] |
| 87 | `description` | 01/30/2021 - 07/28/2024 | extracted='CT abdomen & pelvis with contrast'  expected=None |
| 88 | `cpt_codes` | 06/06/2021 - 06/15/2024 | missing=['71048', '72110', '73060', '73110', '73562', '76830', '77067', 'A4209', 'A4656']  extra=['72158'] |
| 88 | `total_charges` | 06/06/2021 - 06/15/2024 | extracted=791.23  expected=6536.53  diff=5745.30 |
| 88 | `ins_paid` | 06/06/2021 - 06/15/2024 | extracted=517.41  expected=4120.77  diff=3603.36 |
| 88 | `adjustment` | 06/06/2021 - 06/15/2024 | extracted=161.62  expected=2246.05  diff=2084.43 |
| 88 | `payments` | 06/06/2021 - 06/15/2024 | extracted=112.2  expected=None |
| 88 | `balance` | 06/06/2021 - 06/15/2024 | extracted=0.0  expected=169.71  diff=169.71 |
| 88 | `description` | 06/06/2021 - 06/15/2024 | extracted='MRI lumbar spine without and with contrast'  expected=None |
| 89 | `cpt_codes` | 11/13/2021 - 07/29/2024 | missing=['71046', '71048', '72148', '74178', '76705', '76830', 'A4209', 'J1055', 'J9045']  extra=['J0360'] |
| 89 | `total_charges` | 11/13/2021 - 07/29/2024 | extracted=211.88  expected=6605.32  diff=6393.44 |
| 89 | `ins_paid` | 11/13/2021 - 07/29/2024 | extracted=131.19  expected=4148.46  diff=4017.27 |
| 89 | `adjustment` | 11/13/2021 - 07/29/2024 | extracted=80.69  expected=2400.98  diff=2320.29 |
| 89 | `balance` | 11/13/2021 - 07/29/2024 | extracted=0.0  expected=55.88  diff=55.88 |
| 89 | `description` | 11/13/2021 - 07/29/2024 | extracted='Hydralazine HCl, up to 20 mg'  expected=None |
| 90 | `cpt_codes` | 03/03/2021 - 12/23/2024 | missing=['71046', '71048', '73030', '73110', '73562', '73564', '74178', '76830', 'A4636', 'J1644'] |
| 90 | `total_charges` | 03/03/2021 - 12/23/2024 | extracted=312.03  expected=6927.91  diff=6615.88 |
| 90 | `ins_paid` | 03/03/2021 - 12/23/2024 | extracted=212.53  expected=4414.78  diff=4202.25 |
| 90 | `adjustment` | 03/03/2021 - 12/23/2024 | extracted=72.88  expected=2079.95  diff=2007.07 |
| 90 | `payments` | 03/03/2021 - 12/23/2024 | extracted=26.62  expected=None |
| 90 | `balance` | 03/03/2021 - 12/23/2024 | extracted=0.0  expected=433.18  diff=433.18 |
| 90 | `description` | 03/03/2021 - 12/23/2024 | extracted='X-ray spine, lumbosacral, 4+ views'  expected=None |
| 91 | `cpt_codes` | 01/11/2021 - 09/04/2024 | missing=['71048', '72100', '72148', '72158', '73110', '76700', '76705', '77067', 'A4207', 'J1644', 'J9035'] |
| 91 | `total_charges` | 01/11/2021 - 09/04/2024 | extracted=773.02  expected=9447.57  diff=8674.55 |
| 91 | `ins_paid` | 01/11/2021 - 09/04/2024 | extracted=505.31  expected=5816.51  diff=5311.20 |
| 91 | `adjustment` | 01/11/2021 - 09/04/2024 | extracted=267.71  expected=3400.25  diff=3132.54 |
| 91 | `balance` | 01/11/2021 - 09/04/2024 | extracted=0.0  expected=230.81  diff=230.81 |
| 91 | `provider` | 01/11/2021 - 09/04/2024 | extracted='Account 996489'  expected='Hudson Medical, PC' |
| 91 | `insurers` | 01/11/2021 - 09/04/2024 | missing=['tricare'] |
| 91 | `description` | 01/11/2021 - 09/04/2024 | extracted='X-ray humerus, minimum 2 views'  expected=None |
| 92 | `cpt_codes` | 04/15/2021 - 12/22/2024 | missing=['71046', '72148', '73060', '73100', '73110', '73564', '74177', '74178', '76700', '76830', 'J0171']  extra=['73030'] |
| 92 | `total_charges` | 04/15/2021 - 12/22/2024 | extracted=108.06  expected=7289.57  diff=7181.51 |
| 92 | `ins_paid` | 04/15/2021 - 12/22/2024 | extracted=55.94  expected=4506.88  diff=4450.94 |
| 92 | `adjustment` | 04/15/2021 - 12/22/2024 | extracted=40.86  expected=2569.57  diff=2528.71 |
| 92 | `payments` | 04/15/2021 - 12/22/2024 | extracted=11.26  expected=None |
| 92 | `balance` | 04/15/2021 - 12/22/2024 | extracted=0.0  expected=213.12  diff=213.12 |
| 92 | `description` | 04/15/2021 - 12/22/2024 | extracted='X-ray shoulder, minimum 2 views'  expected=None |
| 93 | `cpt_codes` | 01/18/2021 - 08/27/2024 | missing=['71046', '71048', '72110', '73030', '73110', '73562', '73564', '74177', '77067'] |
| 93 | `total_charges` | 01/18/2021 - 08/27/2024 | extracted=696.85  expected=5550.55  diff=4853.70 |
| 93 | `ins_paid` | 01/18/2021 - 08/27/2024 | extracted=457.98  expected=3586.59  diff=3128.61 |
| 93 | `adjustment` | 01/18/2021 - 08/27/2024 | extracted=238.87  expected=1825.41  diff=1586.54 |
| 93 | `balance` | 01/18/2021 - 08/27/2024 | extracted=0.0  expected=138.55  diff=138.55 |
| 93 | `provider` | 01/18/2021 - 08/27/2024 | extracted='Account 882598'  expected='Hudson Medical, PC' |
| 93 | `insurers` | 01/18/2021 - 08/27/2024 | missing=['tricare'] |
| 93 | `description` | 01/18/2021 - 08/27/2024 | extracted='Midazolam HCl, per 1 mg'  expected=None |
| 94 | `cpt_codes` | 05/24/2021 - 07/18/2024 | missing=['72100', '72158', '73110', '73562', '73564', '74178', '76700', '77067', 'J0360'] |
| 94 | `total_charges` | 05/24/2021 - 07/18/2024 | extracted=305.61  expected=7248.75  diff=6943.14 |
| 94 | `ins_paid` | 05/24/2021 - 07/18/2024 | extracted=207.42  expected=4335.67  diff=4128.25 |
| 94 | `adjustment` | 05/24/2021 - 07/18/2024 | extracted=98.19  expected=2624.55  diff=2526.36 |
| 94 | `balance` | 05/24/2021 - 07/18/2024 | extracted=0.0  expected=288.53  diff=288.53 |
| 94 | `provider` | 05/24/2021 - 07/18/2024 | extracted='Account 503435'  expected='Hudson Medical, PC' |
| 94 | `insurers` | 05/24/2021 - 07/18/2024 | missing=['tricare'] |
| 94 | `description` | 05/24/2021 - 07/18/2024 | extracted='Chest X-ray, 4+ views'  expected=None |
| 95 | `cpt_codes` | 01/21/2021 - 11/24/2024 | missing=['71046', '71048', '72100', '72110', '72148', '73100', '73110', '73562', '73564', '76705', '76830', 'A4206', 'A4616', 'J3370', 'J9000'] |
| 95 | `total_charges` | 01/21/2021 - 11/24/2024 | extracted=700.16  expected=10120.24  diff=9420.08 |
| 95 | `ins_paid` | 01/21/2021 - 11/24/2024 | extracted=421.64  expected=6319.85  diff=5898.21 |
| 95 | `adjustment` | 01/21/2021 - 11/24/2024 | extracted=278.52  expected=3576.8  diff=3298.28 |
| 95 | `balance` | 01/21/2021 - 11/24/2024 | extracted=0.0  expected=223.59  diff=223.59 |
| 95 | `provider` | 01/21/2021 - 11/24/2024 | extracted='Account 625783'  expected='Hudson Medical, PC' |
| 95 | `insurers` | 01/21/2021 - 11/24/2024 | missing=['tricare'] |
| 95 | `description` | 01/21/2021 - 11/24/2024 | extracted='X-ray humerus, minimum 2 views'  expected=None |
| 96 | `cpt_codes` | 04/30/2021 - 10/11/2024 | missing=['72148', '73564', '74177', '74178', '76705', '76830', 'J0360', 'J3010', 'J9035'] |
| 96 | `total_charges` | 04/30/2021 - 10/11/2024 | extracted=761.83  expected=5986.57  diff=5224.74 |
| 96 | `ins_paid` | 04/30/2021 - 10/11/2024 | extracted=545.92  expected=3767.99  diff=3222.07 |
| 96 | `adjustment` | 04/30/2021 - 10/11/2024 | extracted=215.91  expected=2148.75  diff=1932.84 |
| 96 | `balance` | 04/30/2021 - 10/11/2024 | extracted=0.0  expected=69.83  diff=69.83 |
| 96 | `provider` | 04/30/2021 - 10/11/2024 | extracted='Account 762887'  expected='Hudson Medical, PC' |
| 96 | `insurers` | 04/30/2021 - 10/11/2024 | missing=['tricare'] |
| 96 | `description` | 04/30/2021 - 10/11/2024 | extracted='MRI lumbar spine without and with contrast'  expected=None |
| 97 | `cpt_codes` | 01/17/2021 - 07/17/2024 | missing=['72100', '72110', '72148', '72158', '73060', '73562', '76700', '76830', 'J0130']  extra=['J9035'] |
| 97 | `total_charges` | 01/17/2021 - 07/17/2024 | extracted=831.38  expected=6344.92  diff=5513.54 |
| 97 | `ins_paid` | 01/17/2021 - 07/17/2024 | extracted=597.9  expected=4043.01  diff=3445.11 |
| 97 | `adjustment` | 01/17/2021 - 07/17/2024 | extracted=233.48  expected=2219.83  diff=1986.35 |
| 97 | `balance` | 01/17/2021 - 07/17/2024 | extracted=0.0  expected=82.08  diff=82.08 |
| 97 | `provider` | 01/17/2021 - 07/17/2024 | extracted='Account 996489'  expected='Hudson Medical, PC' |
| 97 | `insurers` | 01/17/2021 - 07/17/2024 | missing=['tricare'] |
| 97 | `description` | 01/17/2021 - 07/17/2024 | extracted='Bevacizumab, 10 mg'  expected=None |
| 98 | `cpt_codes` | 05/14/2021 - 09/12/2024 | missing=['71048', '73030', '73100', '73110', '73562', '73564', '74178', '76705', 'A4616', 'J2796']  extra=['J1055'] |
| 98 | `total_charges` | 05/14/2021 - 09/12/2024 | extracted=112.53  expected=7356.38  diff=7243.85 |
| 98 | `ins_paid` | 05/14/2021 - 09/12/2024 | extracted=59.52  expected=4557.59  diff=4498.07 |
| 98 | `adjustment` | 05/14/2021 - 09/12/2024 | extracted=53.01  expected=2594.32  diff=2541.31 |
| 98 | `balance` | 05/14/2021 - 09/12/2024 | extracted=0.0  expected=204.47  diff=204.47 |
| 98 | `provider` | 05/14/2021 - 09/12/2024 | extracted='Account 456066'  expected='Hudson Medical, PC' |
| 98 | `insurers` | 05/14/2021 - 09/12/2024 | missing=['tricare'] |
| 98 | `description` | 05/14/2021 - 09/12/2024 | extracted='Medroxyprogesterone acetate, 150 mg'  expected=None |
| 99 | `cpt_codes` | 08/18/2021 - 11/08/2024 | missing=['71048', '72148', '72158', '73060', '73110', '76700', '76830', 'A4550', 'J0270']  extra=['74177'] |
| 99 | `total_charges` | 08/18/2021 - 11/08/2024 | extracted=668.21  expected=6355.31  diff=5687.10 |
| 99 | `ins_paid` | 08/18/2021 - 11/08/2024 | extracted=404.47  expected=3964.4  diff=3559.93 |
| 99 | `adjustment` | 08/18/2021 - 11/08/2024 | extracted=263.74  expected=2261.11  diff=1997.37 |
| 99 | `balance` | 08/18/2021 - 11/08/2024 | extracted=0.0  expected=129.8  diff=129.80 |
| 99 | `description` | 08/18/2021 - 11/08/2024 | extracted='CT abdomen & pelvis with contrast'  expected=None |

### doc_009

**Count mismatch** — GT: 1, extracted: 53.

**Missing records (1):**
- GT[0] `01/01/2017 - 12/31/2024` — No extracted record found with this treatment_date

**Extra extracted records (53):**
- `01/01/2017 - 07/21/2017` — Extracted record has no GT counterpart
- `07/22/2017 - 03/04/2018` — Extracted record has no GT counterpart
- `03/05/2018 - 10/03/2018` — Extracted record has no GT counterpart
- `03/06/2018 - 09/29/2018` — Extracted record has no GT counterpart
- `03/07/2018 - 10/03/2018` — Extracted record has no GT counterpart
- `03/07/2018 - 09/29/2018` — Extracted record has no GT counterpart
- `03/09/2018 - 10/03/2018` — Extracted record has no GT counterpart
- `10/03/2018 - 06/03/2019` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `06/05/2019 - 02/05/2020` — Extracted record has no GT counterpart
- `02/05/2020 - 09/26/2020` — Extracted record has no GT counterpart
- `09/26/2020 - 05/15/2021` — Extracted record has no GT counterpart
- `09/27/2020 - 05/15/2021` — Extracted record has no GT counterpart
- `09/28/2020 - 05/05/2021` — Extracted record has no GT counterpart
- `09/29/2020 - 05/13/2021` — Extracted record has no GT counterpart
- `10/02/2020 - 05/15/2021` — Extracted record has no GT counterpart
- `10/02/2020 - 04/06/2021` — Extracted record has no GT counterpart
- `10/03/2020 - 05/10/2021` — Extracted record has no GT counterpart
- `10/04/2020 - 05/03/2021` — Extracted record has no GT counterpart
- `10/06/2020 - 05/13/2021` — Extracted record has no GT counterpart
- `10/06/2020 - 05/03/2021` — Extracted record has no GT counterpart
- `10/06/2020 - 05/03/2021` — Extracted record has no GT counterpart
- `10/14/2020 - 04/24/2021` — Extracted record has no GT counterpart
- `10/14/2020 - 05/04/2021` — Extracted record has no GT counterpart
- `10/19/2020 - 03/16/2021` — Extracted record has no GT counterpart
- `10/21/2020 - 04/10/2021` — Extracted record has no GT counterpart
- `10/22/2020 - 05/05/2021` — Extracted record has no GT counterpart
- `11/19/2020 - 05/01/2021` — Extracted record has no GT counterpart
- `11/13/2020 - 03/22/2021` — Extracted record has no GT counterpart
- `10/05/2020 - 04/28/2021` — Extracted record has no GT counterpart
- `05/15/2021 - 12/08/2021` — Extracted record has no GT counterpart
- `12/10/2021 - 07/16/2022` — Extracted record has no GT counterpart
- `07/17/2022 - 02/16/2023` — Extracted record has no GT counterpart
- `02/16/2023 - 09/24/2023` — Extracted record has no GT counterpart
- `09/24/2023 - 04/20/2024` — Extracted record has no GT counterpart
- `04/21/2024 - 12/02/2024` — Extracted record has no GT counterpart
- `12/03/2024 - 12/31/2024` — Extracted record has no GT counterpart
- `03/10/2026 - 05/01/2026` — Extracted record has no GT counterpart
- `03/15/2026 - 04/29/2026` — Extracted record has no GT counterpart

### doc_010

**Count mismatch** — GT: 1, extracted: 28.

**Missing records (1):**
- GT[0] `01/01/2017 - 12/29/2024` — No extracted record found with this treatment_date

**Extra extracted records (28):**
- `01/01/2017 - 09/18/2017` — Extracted record has no GT counterpart
- `09/19/2017 - 06/08/2018` — Extracted record has no GT counterpart
- `06/08/2018 - 02/21/2019` — Extracted record has no GT counterpart
- `02/22/2019 - 10/16/2019` — Extracted record has no GT counterpart
- `10/16/2019 - 06/18/2020` — Extracted record has no GT counterpart
- `06/18/2020 - 02/16/2021` — Extracted record has no GT counterpart
- `02/18/2021 - 10/24/2021` — Extracted record has no GT counterpart
- `10/24/2021 - 06/28/2022` — Extracted record has no GT counterpart
- `06/29/2022 - 02/23/2023` — Extracted record has no GT counterpart
- `02/23/2023 - 11/09/2023` — Extracted record has no GT counterpart
- `02/27/2023 - 11/03/2023` — Extracted record has no GT counterpart
- `03/03/2023 - 10/22/2023` — Extracted record has no GT counterpart
- `03/05/2023 - 10/22/2023` — Extracted record has no GT counterpart
- `03/05/2023 - 10/25/2023` — Extracted record has no GT counterpart
- `03/07/2023 - 08/22/2023` — Extracted record has no GT counterpart
- `03/13/2023 - 11/02/2023` — Extracted record has no GT counterpart
- `03/15/2023 - 10/21/2023` — Extracted record has no GT counterpart
- `03/17/2023 - 11/02/2023` — Extracted record has no GT counterpart
- `03/18/2023 - 10/25/2023` — Extracted record has no GT counterpart
- `03/27/2023 - 11/07/2023` — Extracted record has no GT counterpart
- `03/29/2023 - 11/03/2023` — Extracted record has no GT counterpart
- `04/04/2023 - 11/09/2023` — Extracted record has no GT counterpart
- `04/08/2023 - 11/01/2023` — Extracted record has no GT counterpart
- `04/13/2023 - 11/03/2023` — Extracted record has no GT counterpart
- `02/27/2023 - 11/09/2023` — Extracted record has no GT counterpart
- `11/10/2023 - 07/25/2024` — Extracted record has no GT counterpart
- `07/25/2024 - 12/29/2024` — Extracted record has no GT counterpart
- `03/24/2026 - 04/29/2026` — Extracted record has no GT counterpart

### doc_011

**Count mismatch** — GT: 150, extracted: 149.

**Missing records (4):**
- GT[23] `12/16/2022 - 12/20/2022` — No extracted record found with this treatment_date
- GT[47] `05/04/2021 - 05/06/2021` — No extracted record found with this treatment_date
- GT[105] `07/30/2021 - 08/02/2021` — No extracted record found with this treatment_date
- GT[130] `09/08/2024 - 09/14/2024` — No extracted record found with this treatment_date

**Extra extracted records (3):**
- `03/13/2024 – 03/15/2024` — Extracted record has no GT counterpart
- `03/15/2026 - 04/30/2026` — Extracted record has no GT counterpart
- `03/09/2026 - 05/05/2026` — Extracted record has no GT counterpart

**Field mismatches (662):**

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
| 11 | `provider` | 05/09/2022 - 05/10/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 11 | `insurers` | 05/09/2022 - 05/10/2022 | missing=['medicaid'] |
| 11 | `description` | 05/09/2022 - 05/10/2022 | extracted='Septicemia due to gram-negative organism'  expected='Urinary tract infection' |
| 12 | `payments` | 01/17/2018 - 01/24/2018 | extracted=16177.43  expected=None |
| 12 | `balance` | 01/17/2018 - 01/24/2018 | extracted=0.0  expected=16177.43  diff=16177.43 |
| 12 | `provider` | 01/17/2018 - 01/24/2018 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 12 | `insurers` | 01/17/2018 - 01/24/2018 | missing=['medicaid'] |
| 12 | `description` | 01/17/2018 - 01/24/2018 | extracted='Bowel obstruction'  expected='Septicemia due to gram-negative organism' |
| 13 | `payments` | 12/29/2019 - 01/05/2020 | extracted=21530.69  expected=None |
| 13 | `balance` | 12/29/2019 - 01/05/2020 | extracted=0.0  expected=21530.69  diff=21530.69 |
| 13 | `provider` | 12/29/2019 - 01/05/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 13 | `insurers` | 12/29/2019 - 01/05/2020 | missing=['medicaid'] |
| 13 | `description` | 12/29/2019 - 01/05/2020 | extracted='Stroke, ischemic'  expected='Bowel obstruction' |
| 14 | `payments` | 05/28/2024 - 06/01/2024 | extracted=18143.4  expected=None |
| 14 | `balance` | 05/28/2024 - 06/01/2024 | extracted=0.0  expected=18143.4  diff=18143.40 |
| 14 | `provider` | 05/28/2024 - 06/01/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 14 | `insurers` | 05/28/2024 - 06/01/2024 | missing=['medicaid'] |
| 14 | `description` | 05/28/2024 - 06/01/2024 | extracted='Total knee arthroplasty'  expected='Stroke, ischemic' |
| 15 | `payments` | 06/16/2021 - 06/23/2021 | extracted=22926.63  expected=None |
| 15 | `balance` | 06/16/2021 - 06/23/2021 | extracted=0.0  expected=22926.63  diff=22926.63 |
| 15 | `provider` | 06/16/2021 - 06/23/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 15 | `insurers` | 06/16/2021 - 06/23/2021 | missing=['medicaid'] |
| 15 | `description` | 06/16/2021 - 06/23/2021 | extracted='Alcohol withdrawal syndrome'  expected='Total knee arthroplasty' |
| 16 | `payments` | 02/03/2023 - 02/09/2023 | extracted=14427.58  expected=None |
| 16 | `balance` | 02/03/2023 - 02/09/2023 | extracted=0.0  expected=14427.58  diff=14427.58 |
| 16 | `provider` | 02/03/2023 - 02/09/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 16 | `insurers` | 02/03/2023 - 02/09/2023 | missing=['medicaid'] |
| 16 | `description` | 02/03/2023 - 02/09/2023 | extracted='Hip fracture, right femur'  expected='Alcohol withdrawal syndrome' |
| 17 | `payments` | 05/04/2021 - 05/08/2021 | extracted=15878.74  expected=None |
| 17 | `balance` | 05/04/2021 - 05/08/2021 | extracted=0.0  expected=15878.74  diff=15878.74 |
| 17 | `provider` | 05/04/2021 - 05/08/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 17 | `insurers` | 05/04/2021 - 05/08/2021 | missing=['medicaid'] |
| 17 | `description` | 05/04/2021 - 05/08/2021 | extracted='Acute myocardial infarction'  expected='Hip fracture, right femur' |
| 18 | `payments` | 09/21/2019 - 09/26/2019 | extracted=25196.84  expected=None |
| 18 | `balance` | 09/21/2019 - 09/26/2019 | extracted=0.0  expected=25196.84  diff=25196.84 |
| 18 | `provider` | 09/21/2019 - 09/26/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 18 | `insurers` | 09/21/2019 - 09/26/2019 | missing=['medicaid'] |
| 18 | `description` | 09/21/2019 - 09/26/2019 | extracted='Alcohol withdrawal syndrome'  expected='Acute myocardial infarction' |
| 19 | `payments` | 07/06/2018 - 07/07/2018 | extracted=17904.72  expected=None |
| 19 | `balance` | 07/06/2018 - 07/07/2018 | extracted=0.0  expected=17904.72  diff=17904.72 |
| 19 | `provider` | 07/06/2018 - 07/07/2018 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 19 | `insurers` | 07/06/2018 - 07/07/2018 | missing=['medicaid'] |
| 19 | `description` | 07/06/2018 - 07/07/2018 | extracted='Urinary tract infection'  expected='Alcohol withdrawal syndrome' |
| 20 | `payments` | 09/15/2022 - 09/22/2022 | extracted=20237.77  expected=None |
| 20 | `balance` | 09/15/2022 - 09/22/2022 | extracted=0.0  expected=20237.77  diff=20237.77 |
| 20 | `provider` | 09/15/2022 - 09/22/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 20 | `insurers` | 09/15/2022 - 09/22/2022 | missing=['medicaid'] |
| 20 | `description` | 09/15/2022 - 09/22/2022 | extracted='Lumbar spine fusion'  expected='Urinary tract infection' |
| 21 | `payments` | 10/28/2021 - 11/03/2021 | extracted=16866.56  expected=None |
| 21 | `balance` | 10/28/2021 - 11/03/2021 | extracted=0.0  expected=16866.56  diff=16866.56 |
| 21 | `provider` | 10/28/2021 - 11/03/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 21 | `insurers` | 10/28/2021 - 11/03/2021 | missing=['medicaid'] |
| 21 | `description` | 10/28/2021 - 11/03/2021 | extracted='Gastrointestinal hemorrhage'  expected='Lumbar spine fusion' |
| 22 | `payments` | 07/14/2024 - 07/16/2024 | extracted=12561.64  expected=None |
| 22 | `balance` | 07/14/2024 - 07/16/2024 | extracted=0.0  expected=12561.64  diff=12561.64 |
| 22 | `provider` | 07/14/2024 - 07/16/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 22 | `insurers` | 07/14/2024 - 07/16/2024 | missing=['medicaid'] |
| 24 | `payments` | 04/16/2021 - 04/23/2021 | extracted=22427.28  expected=None |
| 24 | `balance` | 04/16/2021 - 04/23/2021 | extracted=0.0  expected=22427.28  diff=22427.28 |
| 24 | `provider` | 04/16/2021 - 04/23/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 24 | `insurers` | 04/16/2021 - 04/23/2021 | missing=['medicaid'] |
| 25 | `payments` | 08/21/2022 - 08/28/2022 | extracted=25723.55  expected=None |
| 25 | `balance` | 08/21/2022 - 08/28/2022 | extracted=0.0  expected=25723.55  diff=25723.55 |
| 25 | `provider` | 08/21/2022 - 08/28/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 25 | `insurers` | 08/21/2022 - 08/28/2022 | missing=['medicaid'] |
| 26 | `payments` | 01/26/2023 - 02/02/2023 | extracted=27219.37  expected=None |
| 26 | `balance` | 01/26/2023 - 02/02/2023 | extracted=0.0  expected=27219.37  diff=27219.37 |
| 26 | `provider` | 01/26/2023 - 02/02/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 26 | `insurers` | 01/26/2023 - 02/02/2023 | missing=['medicaid'] |
| 27 | `payments` | 03/12/2018 - 03/15/2018 | extracted=16389.43  expected=None |
| 27 | `balance` | 03/12/2018 - 03/15/2018 | extracted=0.0  expected=16389.43  diff=16389.43 |
| 27 | `provider` | 03/12/2018 - 03/15/2018 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 27 | `insurers` | 03/12/2018 - 03/15/2018 | missing=['medicaid'] |
| 28 | `payments` | 11/09/2020 - 11/15/2020 | extracted=16140.46  expected=None |
| 28 | `balance` | 11/09/2020 - 11/15/2020 | extracted=0.0  expected=16140.46  diff=16140.46 |
| 28 | `provider` | 11/09/2020 - 11/15/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 28 | `insurers` | 11/09/2020 - 11/15/2020 | missing=['medicaid'] |
| 29 | `payments` | 12/13/2022 - 12/16/2022 | extracted=20601.25  expected=None |
| 29 | `balance` | 12/13/2022 - 12/16/2022 | extracted=0.0  expected=20601.25  diff=20601.25 |
| 29 | `provider` | 12/13/2022 - 12/16/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 29 | `insurers` | 12/13/2022 - 12/16/2022 | missing=['medicaid'] |
| 30 | `payments` | 03/22/2023 - 03/23/2023 | extracted=22281.49  expected=None |
| 30 | `balance` | 03/22/2023 - 03/23/2023 | extracted=0.0  expected=22281.49  diff=22281.49 |
| 30 | `provider` | 03/22/2023 - 03/23/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 30 | `insurers` | 03/22/2023 - 03/23/2023 | missing=['medicaid'] |
| 31 | `payments` | 10/08/2021 - 10/14/2021 | extracted=15615.27  expected=None |
| 31 | `balance` | 10/08/2021 - 10/14/2021 | extracted=0.0  expected=15615.27  diff=15615.27 |
| 31 | `provider` | 10/08/2021 - 10/14/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 31 | `insurers` | 10/08/2021 - 10/14/2021 | missing=['medicaid'] |
| 32 | `payments` | 10/24/2024 - 10/28/2024 | extracted=25167.12  expected=None |
| 32 | `balance` | 10/24/2024 - 10/28/2024 | extracted=0.0  expected=25167.12  diff=25167.12 |
| 32 | `provider` | 10/24/2024 - 10/28/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 32 | `insurers` | 10/24/2024 - 10/28/2024 | missing=['medicaid'] |
| 33 | `payments` | 10/10/2024 - 10/11/2024 | extracted=23656.92  expected=None |
| 33 | `balance` | 10/10/2024 - 10/11/2024 | extracted=0.0  expected=23656.92  diff=23656.92 |
| 33 | `provider` | 10/10/2024 - 10/11/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 33 | `insurers` | 10/10/2024 - 10/11/2024 | missing=['medicaid'] |
| 34 | `payments` | 01/30/2019 - 02/03/2019 | extracted=18015.28  expected=None |
| 34 | `balance` | 01/30/2019 - 02/03/2019 | extracted=0.0  expected=18015.28  diff=18015.28 |
| 34 | `provider` | 01/30/2019 - 02/03/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 34 | `insurers` | 01/30/2019 - 02/03/2019 | missing=['medicaid'] |
| 35 | `payments` | 05/11/2017 - 05/14/2017 | extracted=19815.67  expected=None |
| 35 | `balance` | 05/11/2017 - 05/14/2017 | extracted=0.0  expected=19815.67  diff=19815.67 |
| 35 | `provider` | 05/11/2017 - 05/14/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 35 | `insurers` | 05/11/2017 - 05/14/2017 | missing=['medicaid'] |
| 35 | `description` | 05/11/2017 - 05/14/2017 | extracted='Schizophrenia, acute exacerbation'  expected='Bowel obstruction' |
| 36 | `payments` | 03/20/2021 - 03/24/2021 | extracted=17129.77  expected=None |
| 36 | `balance` | 03/20/2021 - 03/24/2021 | extracted=0.0  expected=17129.77  diff=17129.77 |
| 36 | `provider` | 03/20/2021 - 03/24/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 36 | `insurers` | 03/20/2021 - 03/24/2021 | missing=['medicaid'] |
| 36 | `description` | 03/20/2021 - 03/24/2021 | extracted='Heart failure, unspecified'  expected='Schizophrenia, acute exacerbation' |
| 37 | `payments` | 05/17/2020 - 05/20/2020 | extracted=25958.32  expected=None |
| 37 | `balance` | 05/17/2020 - 05/20/2020 | extracted=0.0  expected=25958.32  diff=25958.32 |
| 37 | `provider` | 05/17/2020 - 05/20/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 37 | `insurers` | 05/17/2020 - 05/20/2020 | missing=['medicaid'] |
| 37 | `description` | 05/17/2020 - 05/20/2020 | extracted='Bowel obstruction'  expected='Heart failure, unspecified' |
| 38 | `payments` | 12/19/2022 - 12/21/2022 | extracted=21455.21  expected=None |
| 38 | `balance` | 12/19/2022 - 12/21/2022 | extracted=0.0  expected=21455.21  diff=21455.21 |
| 38 | `provider` | 12/19/2022 - 12/21/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 38 | `insurers` | 12/19/2022 - 12/21/2022 | missing=['medicaid'] |
| 38 | `description` | 12/19/2022 - 12/21/2022 | extracted='Gastrointestinal hemorrhage'  expected='Bowel obstruction' |
| 39 | `payments` | 08/06/2020 - 08/07/2020 | extracted=19020.69  expected=None |
| 39 | `balance` | 08/06/2020 - 08/07/2020 | extracted=0.0  expected=19020.69  diff=19020.69 |
| 39 | `provider` | 08/06/2020 - 08/07/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 39 | `insurers` | 08/06/2020 - 08/07/2020 | missing=['medicaid'] |
| 39 | `description` | 08/06/2020 - 08/07/2020 | extracted='Pulmonary embolism'  expected='Gastrointestinal hemorrhage' |
| 40 | `payments` | 04/09/2017 - 04/13/2017 | extracted=19340.89  expected=None |
| 40 | `balance` | 04/09/2017 - 04/13/2017 | extracted=0.0  expected=19340.89  diff=19340.89 |
| 40 | `provider` | 04/09/2017 - 04/13/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 40 | `insurers` | 04/09/2017 - 04/13/2017 | missing=['medicaid'] |
| 40 | `description` | 04/09/2017 - 04/13/2017 | extracted='Total knee arthroplasty'  expected='Pulmonary embolism' |
| 41 | `payments` | 07/25/2023 - 07/30/2023 | extracted=23705.95  expected=None |
| 41 | `balance` | 07/25/2023 - 07/30/2023 | extracted=0.0  expected=23705.95  diff=23705.95 |
| 41 | `provider` | 07/25/2023 - 07/30/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 41 | `insurers` | 07/25/2023 - 07/30/2023 | missing=['medicaid'] |
| 41 | `description` | 07/25/2023 - 07/30/2023 | extracted='Lumbar spine fusion'  expected='Total knee arthroplasty' |
| 42 | `payments` | 07/15/2019 - 07/18/2019 | extracted=15259.96  expected=None |
| 42 | `balance` | 07/15/2019 - 07/18/2019 | extracted=0.0  expected=15259.96  diff=15259.96 |
| 42 | `provider` | 07/15/2019 - 07/18/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 42 | `insurers` | 07/15/2019 - 07/18/2019 | missing=['medicaid'] |
| 42 | `description` | 07/15/2019 - 07/18/2019 | extracted='Acute pancreatitis'  expected='Lumbar spine fusion' |
| 43 | `payments` | 07/28/2022 - 08/04/2022 | extracted=12127.85  expected=None |
| 43 | `balance` | 07/28/2022 - 08/04/2022 | extracted=0.0  expected=12127.85  diff=12127.85 |
| 43 | `provider` | 07/28/2022 - 08/04/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 43 | `insurers` | 07/28/2022 - 08/04/2022 | missing=['medicaid'] |
| 43 | `description` | 07/28/2022 - 08/04/2022 | extracted='Alcohol withdrawal syndrome'  expected='Acute pancreatitis' |
| 44 | `payments` | 12/25/2019 - 12/27/2019 | extracted=18799.08  expected=None |
| 44 | `balance` | 12/25/2019 - 12/27/2019 | extracted=0.0  expected=18799.08  diff=18799.08 |
| 44 | `provider` | 12/25/2019 - 12/27/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 44 | `insurers` | 12/25/2019 - 12/27/2019 | missing=['medicaid'] |
| 44 | `description` | 12/25/2019 - 12/27/2019 | extracted='Urinary tract infection'  expected='Alcohol withdrawal syndrome' |
| 45 | `payments` | 01/01/2019 - 01/08/2019 | extracted=13491.95  expected=None |
| 45 | `balance` | 01/01/2019 - 01/08/2019 | extracted=0.0  expected=13491.95  diff=13491.95 |
| 45 | `provider` | 01/01/2019 - 01/08/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 45 | `insurers` | 01/01/2019 - 01/08/2019 | missing=['medicaid'] |
| 45 | `description` | 01/01/2019 - 01/08/2019 | extracted='Gastrointestinal hemorrhage'  expected='Urinary tract infection' |
| 46 | `payments` | 10/11/2023 - 10/14/2023 | extracted=17934.49  expected=None |
| 46 | `balance` | 10/11/2023 - 10/14/2023 | extracted=0.0  expected=17934.49  diff=17934.49 |
| 46 | `provider` | 10/11/2023 - 10/14/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 46 | `insurers` | 10/11/2023 - 10/14/2023 | missing=['medicaid'] |
| 46 | `description` | 10/11/2023 - 10/14/2023 | extracted='Acute pancreatitis'  expected='Gastrointestinal hemorrhage' |
| 48 | `payments` | 09/10/2017 - 09/14/2017 | extracted=14044.89  expected=None |
| 48 | `balance` | 09/10/2017 - 09/14/2017 | extracted=0.0  expected=14044.89  diff=14044.89 |
| 48 | `provider` | 09/10/2017 - 09/14/2017 | extracted=''  expected='South Patrickmouth General Hospital' |
| 48 | `insurers` | 09/10/2017 - 09/14/2017 | missing=['medicaid'] |
| 49 | `payments` | 07/08/2022 - 07/10/2022 | extracted=19341.42  expected=None |
| 49 | `balance` | 07/08/2022 - 07/10/2022 | extracted=0.0  expected=19341.42  diff=19341.42 |
| 49 | `provider` | 07/08/2022 - 07/10/2022 | extracted=''  expected='South Patrickmouth General Hospital' |
| 49 | `insurers` | 07/08/2022 - 07/10/2022 | missing=['medicaid'] |
| 50 | `payments` | 08/08/2022 - 08/12/2022 | extracted=16045.24  expected=None |
| 50 | `balance` | 08/08/2022 - 08/12/2022 | extracted=0.0  expected=16045.24  diff=16045.24 |
| 50 | `provider` | 08/08/2022 - 08/12/2022 | extracted=''  expected='South Patrickmouth General Hospital' |
| 50 | `insurers` | 08/08/2022 - 08/12/2022 | missing=['medicaid'] |
| 51 | `payments` | 08/05/2023 - 08/11/2023 | extracted=24802.71  expected=None |
| 51 | `balance` | 08/05/2023 - 08/11/2023 | extracted=0.0  expected=24802.71  diff=24802.71 |
| 51 | `provider` | 08/05/2023 - 08/11/2023 | extracted=''  expected='South Patrickmouth General Hospital' |
| 51 | `insurers` | 08/05/2023 - 08/11/2023 | missing=['medicaid'] |
| 52 | `payments` | 02/23/2020 - 02/28/2020 | extracted=13278.62  expected=None |
| 52 | `balance` | 02/23/2020 - 02/28/2020 | extracted=0.0  expected=13278.62  diff=13278.62 |
| 52 | `provider` | 02/23/2020 - 02/28/2020 | extracted=''  expected='South Patrickmouth General Hospital' |
| 52 | `insurers` | 02/23/2020 - 02/28/2020 | missing=['medicaid'] |
| 53 | `payments` | 03/12/2019 - 03/14/2019 | extracted=26277.73  expected=None |
| 53 | `balance` | 03/12/2019 - 03/14/2019 | extracted=0.0  expected=26277.73  diff=26277.73 |
| 53 | `provider` | 03/12/2019 - 03/14/2019 | extracted=''  expected='South Patrickmouth General Hospital' |
| 53 | `insurers` | 03/12/2019 - 03/14/2019 | missing=['medicaid'] |
| 54 | `payments` | 12/20/2021 - 12/27/2021 | extracted=20528.7  expected=None |
| 54 | `balance` | 12/20/2021 - 12/27/2021 | extracted=0.0  expected=20528.7  diff=20528.70 |
| 54 | `provider` | 12/20/2021 - 12/27/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 54 | `insurers` | 12/20/2021 - 12/27/2021 | missing=['medicaid'] |
| 55 | `payments` | 10/15/2020 - 10/16/2020 | extracted=18000.91  expected=None |
| 55 | `balance` | 10/15/2020 - 10/16/2020 | extracted=0.0  expected=18000.91  diff=18000.91 |
| 55 | `provider` | 10/15/2020 - 10/16/2020 | extracted=''  expected='South Patrickmouth General Hospital' |
| 55 | `insurers` | 10/15/2020 - 10/16/2020 | missing=['medicaid'] |
| 56 | `payments` | 12/10/2021 - 12/12/2021 | extracted=21210.1  expected=None |
| 56 | `balance` | 12/10/2021 - 12/12/2021 | extracted=0.0  expected=21210.1  diff=21210.10 |
| 56 | `provider` | 12/10/2021 - 12/12/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 56 | `insurers` | 12/10/2021 - 12/12/2021 | missing=['medicaid'] |
| 57 | `payments` | 07/11/2019 - 07/12/2019 | extracted=25985.51  expected=None |
| 57 | `balance` | 07/11/2019 - 07/12/2019 | extracted=0.0  expected=25985.51  diff=25985.51 |
| 57 | `provider` | 07/11/2019 - 07/12/2019 | extracted=''  expected='South Patrickmouth General Hospital' |
| 57 | `insurers` | 07/11/2019 - 07/12/2019 | missing=['medicaid'] |
| 58 | `payments` | 01/27/2021 - 02/02/2021 | extracted=21168.67  expected=None |
| 58 | `balance` | 01/27/2021 - 02/02/2021 | extracted=0.0  expected=21168.67  diff=21168.67 |
| 58 | `provider` | 01/27/2021 - 02/02/2021 | extracted=''  expected='South Patrickmouth General Hospital' |
| 58 | `insurers` | 01/27/2021 - 02/02/2021 | missing=['medicaid'] |
| 59 | `payments` | 10/15/2022 - 10/16/2022 | extracted=19839.5  expected=None |
| 59 | `balance` | 10/15/2022 - 10/16/2022 | extracted=0.0  expected=19839.5  diff=19839.50 |
| 59 | `provider` | 10/15/2022 - 10/16/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 59 | `insurers` | 10/15/2022 - 10/16/2022 | missing=['medicaid'] |
| 59 | `description` | 10/15/2022 - 10/16/2022 | extracted='Cellulitis of lower leg'  expected='Lumbar spine fusion' |
| 60 | `payments` | 05/08/2017 - 05/10/2017 | extracted=25111.81  expected=None |
| 60 | `balance` | 05/08/2017 - 05/10/2017 | extracted=0.0  expected=25111.81  diff=25111.81 |
| 60 | `provider` | 05/08/2017 - 05/10/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 60 | `insurers` | 05/08/2017 - 05/10/2017 | missing=['medicaid'] |
| 61 | `payments` | 01/26/2022 - 01/31/2022 | extracted=21938.32  expected=None |
| 61 | `balance` | 01/26/2022 - 01/31/2022 | extracted=0.0  expected=21938.32  diff=21938.32 |
| 61 | `provider` | 01/26/2022 - 01/31/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 61 | `insurers` | 01/26/2022 - 01/31/2022 | missing=['medicaid'] |
| 62 | `payments` | 05/01/2024 - 05/02/2024 | extracted=22315.55  expected=None |
| 62 | `balance` | 05/01/2024 - 05/02/2024 | extracted=0.0  expected=22315.55  diff=22315.55 |
| 62 | `provider` | 05/01/2024 - 05/02/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 62 | `insurers` | 05/01/2024 - 05/02/2024 | missing=['medicaid'] |
| 63 | `payments` | 04/07/2017 - 04/11/2017 | extracted=16818.14  expected=None |
| 63 | `balance` | 04/07/2017 - 04/11/2017 | extracted=0.0  expected=16818.14  diff=16818.14 |
| 63 | `provider` | 04/07/2017 - 04/11/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 63 | `insurers` | 04/07/2017 - 04/11/2017 | missing=['medicaid'] |
| 64 | `payments` | 03/27/2024 - 04/03/2024 | extracted=20522.97  expected=None |
| 64 | `balance` | 03/27/2024 - 04/03/2024 | extracted=0.0  expected=20522.97  diff=20522.97 |
| 64 | `provider` | 03/27/2024 - 04/03/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 64 | `insurers` | 03/27/2024 - 04/03/2024 | missing=['medicaid'] |
| 65 | `payments` | 10/03/2019 - 10/08/2019 | extracted=13338.09  expected=None |
| 65 | `balance` | 10/03/2019 - 10/08/2019 | extracted=0.0  expected=13338.09  diff=13338.09 |
| 65 | `provider` | 10/03/2019 - 10/08/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 65 | `insurers` | 10/03/2019 - 10/08/2019 | missing=['medicaid'] |
| 66 | `payments` | 05/05/2024 - 05/12/2024 | extracted=24824.37  expected=None |
| 66 | `balance` | 05/05/2024 - 05/12/2024 | extracted=0.0  expected=24824.37  diff=24824.37 |
| 66 | `provider` | 05/05/2024 - 05/12/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 66 | `insurers` | 05/05/2024 - 05/12/2024 | missing=['medicaid'] |
| 67 | `payments` | 03/30/2021 - 04/01/2021 | extracted=23101.69  expected=None |
| 67 | `balance` | 03/30/2021 - 04/01/2021 | extracted=0.0  expected=23101.69  diff=23101.69 |
| 67 | `provider` | 03/30/2021 - 04/01/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 67 | `insurers` | 03/30/2021 - 04/01/2021 | missing=['medicaid'] |
| 68 | `payments` | 02/03/2024 - 02/04/2024 | extracted=21895.23  expected=None |
| 68 | `balance` | 02/03/2024 - 02/04/2024 | extracted=0.0  expected=21895.23  diff=21895.23 |
| 68 | `provider` | 02/03/2024 - 02/04/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 68 | `insurers` | 02/03/2024 - 02/04/2024 | missing=['medicaid'] |
| 69 | `payments` | 10/14/2017 - 10/20/2017 | extracted=11167.73  expected=None |
| 69 | `balance` | 10/14/2017 - 10/20/2017 | extracted=0.0  expected=11167.73  diff=11167.73 |
| 69 | `provider` | 10/14/2017 - 10/20/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 69 | `insurers` | 10/14/2017 - 10/20/2017 | missing=['medicaid'] |
| 70 | `payments` | 08/14/2023 - 08/21/2023 | extracted=21622.2  expected=None |
| 70 | `balance` | 08/14/2023 - 08/21/2023 | extracted=0.0  expected=21622.2  diff=21622.20 |
| 70 | `provider` | 08/14/2023 - 08/21/2023 | extracted=''  expected='South Patrickmouth General Hospital' |
| 70 | `insurers` | 08/14/2023 - 08/21/2023 | missing=['medicaid'] |
| 71 | `payments` | 09/29/2023 - 10/06/2023 | extracted=23423.97  expected=None |
| 71 | `balance` | 09/29/2023 - 10/06/2023 | extracted=0.0  expected=23423.97  diff=23423.97 |
| 71 | `provider` | 09/29/2023 - 10/06/2023 | extracted=''  expected='South Patrickmouth General Hospital' |
| 71 | `insurers` | 09/29/2023 - 10/06/2023 | missing=['medicaid'] |
| 72 | `payments` | 03/10/2019 - 03/15/2019 | extracted=24620.73  expected=None |
| 72 | `balance` | 03/10/2019 - 03/15/2019 | extracted=0.0  expected=24620.73  diff=24620.73 |
| 72 | `provider` | 03/10/2019 - 03/15/2019 | extracted=''  expected='South Patrickmouth General Hospital' |
| 72 | `insurers` | 03/10/2019 - 03/15/2019 | missing=['medicaid'] |
| 73 | `payments` | 11/01/2020 - 11/03/2020 | extracted=13061.14  expected=None |
| 73 | `balance` | 11/01/2020 - 11/03/2020 | extracted=0.0  expected=13061.14  diff=13061.14 |
| 73 | `provider` | 11/01/2020 - 11/03/2020 | extracted=''  expected='South Patrickmouth General Hospital' |
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
| 81 | `provider` | 03/13/2024 - 03/15/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 81 | `insurers` | 03/13/2024 - 03/15/2024 | missing=['medicaid'] |
| 81 | `description` | 03/13/2024 - 03/15/2024 | extracted='Total knee arthroplasty'  expected='Cellulitis of lower leg' |
| 82 | `payments` | 06/20/2020 - 06/27/2020 | extracted=20879.61  expected=None |
| 82 | `balance` | 06/20/2020 - 06/27/2020 | extracted=0.0  expected=20879.61  diff=20879.61 |
| 82 | `provider` | 06/20/2020 - 06/27/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 82 | `insurers` | 06/20/2020 - 06/27/2020 | missing=['medicaid'] |
| 83 | `payments` | 01/12/2017 - 01/13/2017 | extracted=21751.41  expected=None |
| 83 | `balance` | 01/12/2017 - 01/13/2017 | extracted=0.0  expected=21751.41  diff=21751.41 |
| 83 | `provider` | 01/12/2017 - 01/13/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 83 | `insurers` | 01/12/2017 - 01/13/2017 | missing=['medicaid'] |
| 84 | `payments` | 06/17/2020 - 06/21/2020 | extracted=31034.51  expected=None |
| 84 | `balance` | 06/17/2020 - 06/21/2020 | extracted=0.0  expected=31034.51  diff=31034.51 |
| 84 | `provider` | 06/17/2020 - 06/21/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 84 | `insurers` | 06/17/2020 - 06/21/2020 | missing=['medicaid'] |
| 85 | `payments` | 02/24/2019 - 02/28/2019 | extracted=14609.98  expected=None |
| 85 | `balance` | 02/24/2019 - 02/28/2019 | extracted=0.0  expected=14609.98  diff=14609.98 |
| 85 | `provider` | 02/24/2019 - 02/28/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 85 | `insurers` | 02/24/2019 - 02/28/2019 | missing=['medicaid'] |
| 86 | `payments` | 02/06/2017 - 02/11/2017 | extracted=18635.03  expected=None |
| 86 | `balance` | 02/06/2017 - 02/11/2017 | extracted=0.0  expected=18635.03  diff=18635.03 |
| 86 | `provider` | 02/06/2017 - 02/11/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 86 | `insurers` | 02/06/2017 - 02/11/2017 | missing=['medicaid'] |
| 87 | `payments` | 11/26/2021 - 11/28/2021 | extracted=26884.97  expected=None |
| 87 | `balance` | 11/26/2021 - 11/28/2021 | extracted=0.0  expected=26884.97  diff=26884.97 |
| 87 | `provider` | 11/26/2021 - 11/28/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 87 | `insurers` | 11/26/2021 - 11/28/2021 | missing=['medicaid'] |
| 88 | `payments` | 12/07/2021 - 12/14/2021 | extracted=21602.65  expected=None |
| 88 | `balance` | 12/07/2021 - 12/14/2021 | extracted=0.0  expected=21602.65  diff=21602.65 |
| 88 | `provider` | 12/07/2021 - 12/14/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 88 | `insurers` | 12/07/2021 - 12/14/2021 | missing=['medicaid'] |
| 89 | `payments` | 12/16/2024 - 12/17/2024 | extracted=14246.55  expected=None |
| 89 | `balance` | 12/16/2024 - 12/17/2024 | extracted=0.0  expected=14246.55  diff=14246.55 |
| 89 | `provider` | 12/16/2024 - 12/17/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 89 | `insurers` | 12/16/2024 - 12/17/2024 | missing=['medicaid'] |
| 90 | `payments` | 09/16/2022 - 09/20/2022 | extracted=11491.79  expected=None |
| 90 | `balance` | 09/16/2022 - 09/20/2022 | extracted=0.0  expected=11491.79  diff=11491.79 |
| 90 | `provider` | 09/16/2022 - 09/20/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 90 | `insurers` | 09/16/2022 - 09/20/2022 | missing=['medicaid'] |
| 91 | `payments` | 11/20/2022 - 11/21/2022 | extracted=24740.24  expected=None |
| 91 | `balance` | 11/20/2022 - 11/21/2022 | extracted=0.0  expected=24740.24  diff=24740.24 |
| 91 | `provider` | 11/20/2022 - 11/21/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 91 | `insurers` | 11/20/2022 - 11/21/2022 | missing=['medicaid'] |
| 92 | `payments` | 09/16/2020 - 09/22/2020 | extracted=13196.5  expected=None |
| 92 | `balance` | 09/16/2020 - 09/22/2020 | extracted=0.0  expected=13196.5  diff=13196.50 |
| 92 | `provider` | 09/16/2020 - 09/22/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 92 | `insurers` | 09/16/2020 - 09/22/2020 | missing=['medicaid'] |
| 93 | `payments` | 11/28/2023 - 11/30/2023 | extracted=16576.05  expected=None |
| 93 | `balance` | 11/28/2023 - 11/30/2023 | extracted=0.0  expected=16576.05  diff=16576.05 |
| 93 | `provider` | 11/28/2023 - 11/30/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 93 | `insurers` | 11/28/2023 - 11/30/2023 | missing=['medicaid'] |
| 94 | `payments` | 09/03/2023 - 09/06/2023 | extracted=12828.97  expected=None |
| 94 | `balance` | 09/03/2023 - 09/06/2023 | extracted=0.0  expected=12828.97  diff=12828.97 |
| 94 | `provider` | 09/03/2023 - 09/06/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 94 | `insurers` | 09/03/2023 - 09/06/2023 | missing=['medicaid'] |
| 95 | `payments` | 09/25/2024 - 10/01/2024 | extracted=14703.7  expected=None |
| 95 | `balance` | 09/25/2024 - 10/01/2024 | extracted=0.0  expected=14703.7  diff=14703.70 |
| 95 | `provider` | 09/25/2024 - 10/01/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 95 | `insurers` | 09/25/2024 - 10/01/2024 | missing=['medicaid'] |
| 96 | `payments` | 06/18/2019 - 06/20/2019 | extracted=24040.21  expected=None |
| 96 | `balance` | 06/18/2019 - 06/20/2019 | extracted=0.0  expected=24040.21  diff=24040.21 |
| 96 | `provider` | 06/18/2019 - 06/20/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 96 | `insurers` | 06/18/2019 - 06/20/2019 | missing=['medicaid'] |
| 97 | `payments` | 07/26/2019 - 08/01/2019 | extracted=13636.3  expected=None |
| 97 | `balance` | 07/26/2019 - 08/01/2019 | extracted=0.0  expected=13636.3  diff=13636.30 |
| 97 | `provider` | 07/26/2019 - 08/01/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 97 | `insurers` | 07/26/2019 - 08/01/2019 | missing=['medicaid'] |
| 98 | `payments` | 01/15/2019 - 01/17/2019 | extracted=14460.88  expected=None |
| 98 | `balance` | 01/15/2019 - 01/17/2019 | extracted=0.0  expected=14460.88  diff=14460.88 |
| 98 | `provider` | 01/15/2019 - 01/17/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 98 | `insurers` | 01/15/2019 - 01/17/2019 | missing=['medicaid'] |
| 99 | `payments` | 03/03/2023 - 03/06/2023 | extracted=12038.18  expected=None |
| 99 | `balance` | 03/03/2023 - 03/06/2023 | extracted=0.0  expected=12038.18  diff=12038.18 |
| 99 | `provider` | 03/03/2023 - 03/06/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 99 | `insurers` | 03/03/2023 - 03/06/2023 | missing=['medicaid'] |
| 100 | `payments` | 11/30/2021 - 12/02/2021 | extracted=17788.93  expected=None |
| 100 | `balance` | 11/30/2021 - 12/02/2021 | extracted=0.0  expected=17788.93  diff=17788.93 |
| 100 | `provider` | 11/30/2021 - 12/02/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 100 | `insurers` | 11/30/2021 - 12/02/2021 | missing=['medicaid'] |
| 101 | `payments` | 06/27/2021 - 07/02/2021 | extracted=16844.11  expected=None |
| 101 | `balance` | 06/27/2021 - 07/02/2021 | extracted=0.0  expected=16844.11  diff=16844.11 |
| 101 | `provider` | 06/27/2021 - 07/02/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 101 | `insurers` | 06/27/2021 - 07/02/2021 | missing=['medicaid'] |
| 102 | `payments` | 06/16/2019 - 06/22/2019 | extracted=16690.62  expected=None |
| 102 | `balance` | 06/16/2019 - 06/22/2019 | extracted=0.0  expected=16690.62  diff=16690.62 |
| 102 | `provider` | 06/16/2019 - 06/22/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 102 | `insurers` | 06/16/2019 - 06/22/2019 | missing=['medicaid'] |
| 103 | `payments` | 01/09/2024 - 01/12/2024 | extracted=23049.57  expected=None |
| 103 | `balance` | 01/09/2024 - 01/12/2024 | extracted=0.0  expected=23049.57  diff=23049.57 |
| 103 | `provider` | 01/09/2024 - 01/12/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 103 | `insurers` | 01/09/2024 - 01/12/2024 | missing=['medicaid'] |
| 104 | `payments` | 10/25/2020 - 10/29/2020 | extracted=24173.12  expected=None |
| 104 | `balance` | 10/25/2020 - 10/29/2020 | extracted=0.0  expected=24173.12  diff=24173.12 |
| 104 | `provider` | 10/25/2020 - 10/29/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 104 | `insurers` | 10/25/2020 - 10/29/2020 | missing=['medicaid'] |
| 106 | `total_charges` | 09/09/2021 - 09/15/2021 | extracted=279141.24  expected=285351.94  diff=6210.70 |
| 106 | `ins_paid` | 09/09/2021 - 09/15/2021 | extracted=134646.23  expected=137642.01  diff=2995.78 |
| 106 | `adjustment` | 09/09/2021 - 09/15/2021 | extracted=126685.8  expected=129504.48  diff=2818.68 |
| 106 | `payments` | 09/09/2021 - 09/15/2021 | extracted=17809.21  expected=None |
| 106 | `balance` | 09/09/2021 - 09/15/2021 | extracted=0.0  expected=18205.45  diff=18205.45 |
| 106 | `provider` | 09/09/2021 - 09/15/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 106 | `insurers` | 09/09/2021 - 09/15/2021 | missing=['medicaid'] |
| 107 | `total_charges` | 03/20/2020 - 03/27/2020 | extracted=285351.94  expected=261606.96  diff=23744.98 |
| 107 | `ins_paid` | 03/20/2020 - 03/27/2020 | extracted=137642.01  expected=126188.41  diff=11453.60 |
| 107 | `adjustment` | 03/20/2020 - 03/27/2020 | extracted=129504.48  expected=118728.03  diff=10776.45 |
| 107 | `payments` | 03/20/2020 - 03/27/2020 | extracted=18205.45  expected=None |
| 107 | `balance` | 03/20/2020 - 03/27/2020 | extracted=0.0  expected=16690.52  diff=16690.52 |
| 107 | `provider` | 03/20/2020 - 03/27/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 107 | `insurers` | 03/20/2020 - 03/27/2020 | missing=['medicaid'] |
| 108 | `total_charges` | 08/28/2017 - 09/04/2017 | extracted=261606.96  expected=265480.16  diff=3873.20 |
| 108 | `ins_paid` | 08/28/2017 - 09/04/2017 | extracted=126188.41  expected=128056.69  diff=1868.28 |
| 108 | `adjustment` | 08/28/2017 - 09/04/2017 | extracted=118728.03  expected=120485.84  diff=1757.81 |
| 108 | `payments` | 08/28/2017 - 09/04/2017 | extracted=16690.52  expected=None |
| 108 | `balance` | 08/28/2017 - 09/04/2017 | extracted=0.0  expected=16937.63  diff=16937.63 |
| 108 | `provider` | 08/28/2017 - 09/04/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 108 | `insurers` | 08/28/2017 - 09/04/2017 | missing=['medicaid'] |
| 109 | `total_charges` | 02/10/2023 - 02/16/2023 | extracted=265480.16  expected=224778.93  diff=40701.23 |
| 109 | `ins_paid` | 02/10/2023 - 02/16/2023 | extracted=128056.69  expected=108424.09  diff=19632.60 |
| 109 | `adjustment` | 02/10/2023 - 02/16/2023 | extracted=120485.84  expected=102013.94  diff=18471.90 |
| 109 | `payments` | 02/10/2023 - 02/16/2023 | extracted=16937.63  expected=None |
| 109 | `balance` | 02/10/2023 - 02/16/2023 | extracted=0.0  expected=14340.9  diff=14340.90 |
| 109 | `provider` | 02/10/2023 - 02/16/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 109 | `insurers` | 02/10/2023 - 02/16/2023 | missing=['medicaid'] |
| 110 | `total_charges` | 06/24/2018 - 06/26/2018 | extracted=224778.93  expected=434449.42  diff=209670.49 |
| 110 | `ins_paid` | 06/24/2018 - 06/26/2018 | extracted=108424.09  expected=209560.49  diff=101136.40 |
| 110 | `adjustment` | 06/24/2018 - 06/26/2018 | extracted=102013.94  expected=197171.06  diff=95157.12 |
| 110 | `payments` | 06/24/2018 - 06/26/2018 | extracted=14340.9  expected=None |
| 110 | `balance` | 06/24/2018 - 06/26/2018 | extracted=0.0  expected=27717.87  diff=27717.87 |
| 110 | `provider` | 06/24/2018 - 06/26/2018 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 110 | `insurers` | 06/24/2018 - 06/26/2018 | missing=['medicaid'] |
| 111 | `total_charges` | 04/12/2021 - 04/15/2021 | extracted=434449.42  expected=300732.48  diff=133716.94 |
| 111 | `ins_paid` | 04/12/2021 - 04/15/2021 | extracted=209560.49  expected=145060.95  diff=64499.54 |
| 111 | `adjustment` | 04/12/2021 - 04/15/2021 | extracted=197171.06  expected=136484.8  diff=60686.26 |
| 111 | `payments` | 04/12/2021 - 04/15/2021 | extracted=27717.87  expected=None |
| 111 | `balance` | 04/12/2021 - 04/15/2021 | extracted=0.0  expected=19186.73  diff=19186.73 |
| 111 | `provider` | 04/12/2021 - 04/15/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 111 | `insurers` | 04/12/2021 - 04/15/2021 | missing=['medicaid'] |
| 112 | `total_charges` | 02/22/2023 - 03/01/2023 | extracted=300732.48  expected=280920.35  diff=19812.13 |
| 112 | `ins_paid` | 02/22/2023 - 03/01/2023 | extracted=145060.95  expected=135504.4  diff=9556.55 |
| 112 | `adjustment` | 02/22/2023 - 03/01/2023 | extracted=136484.8  expected=127493.23  diff=8991.57 |
| 112 | `payments` | 02/22/2023 - 03/01/2023 | extracted=19186.73  expected=None |
| 112 | `balance` | 02/22/2023 - 03/01/2023 | extracted=0.0  expected=17922.72  diff=17922.72 |
| 112 | `provider` | 02/22/2023 - 03/01/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 112 | `insurers` | 02/22/2023 - 03/01/2023 | missing=['medicaid'] |
| 113 | `total_charges` | 07/28/2021 - 07/29/2021 | extracted=280920.35  expected=373542.81  diff=92622.46 |
| 113 | `ins_paid` | 07/28/2021 - 07/29/2021 | extracted=135504.4  expected=180181.65  diff=44677.25 |
| 113 | `adjustment` | 07/28/2021 - 07/29/2021 | extracted=127493.23  expected=169529.13  diff=42035.90 |
| 113 | `payments` | 07/28/2021 - 07/29/2021 | extracted=17922.72  expected=None |
| 113 | `balance` | 07/28/2021 - 07/29/2021 | extracted=0.0  expected=23832.03  diff=23832.03 |
| 113 | `provider` | 07/28/2021 - 07/29/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 113 | `insurers` | 07/28/2021 - 07/29/2021 | missing=['medicaid'] |
| 114 | `total_charges` | 11/22/2022 - 11/26/2022 | extracted=373542.81  expected=226594.8  diff=146948.01 |
| 114 | `ins_paid` | 11/22/2022 - 11/26/2022 | extracted=180181.65  expected=109299.99  diff=70881.66 |
| 114 | `adjustment` | 11/22/2022 - 11/26/2022 | extracted=169529.13  expected=102838.06  diff=66691.07 |
| 114 | `payments` | 11/22/2022 - 11/26/2022 | extracted=23832.03  expected=None |
| 114 | `balance` | 11/22/2022 - 11/26/2022 | extracted=0.0  expected=14456.75  diff=14456.75 |
| 114 | `provider` | 11/22/2022 - 11/26/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 114 | `insurers` | 11/22/2022 - 11/26/2022 | missing=['medicaid'] |
| 115 | `total_charges` | 01/11/2024 - 01/18/2024 | extracted=226594.8  expected=399311.33  diff=172716.53 |
| 115 | `ins_paid` | 01/11/2024 - 01/18/2024 | extracted=109299.99  expected=192611.32  diff=83311.33 |
| 115 | `adjustment` | 01/11/2024 - 01/18/2024 | extracted=102838.06  expected=181223.95  diff=78385.89 |
| 115 | `payments` | 01/11/2024 - 01/18/2024 | extracted=14456.75  expected=None |
| 115 | `balance` | 01/11/2024 - 01/18/2024 | extracted=0.0  expected=25476.06  diff=25476.06 |
| 115 | `provider` | 01/11/2024 - 01/18/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 115 | `insurers` | 01/11/2024 - 01/18/2024 | missing=['medicaid'] |
| 116 | `total_charges` | 02/07/2022 - 02/14/2022 | extracted=399311.33  expected=313143.24  diff=86168.09 |
| 116 | `ins_paid` | 02/07/2022 - 02/14/2022 | extracted=192611.32  expected=151047.39  diff=41563.93 |
| 116 | `adjustment` | 02/07/2022 - 02/14/2022 | extracted=181223.95  expected=142117.31  diff=39106.64 |
| 116 | `payments` | 02/07/2022 - 02/14/2022 | extracted=25476.06  expected=None |
| 116 | `balance` | 02/07/2022 - 02/14/2022 | extracted=0.0  expected=19978.54  diff=19978.54 |
| 116 | `provider` | 02/07/2022 - 02/14/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 116 | `insurers` | 02/07/2022 - 02/14/2022 | missing=['medicaid'] |
| 117 | `total_charges` | 04/27/2023 - 05/02/2023 | extracted=313143.24  expected=315790.6  diff=2647.36 |
| 117 | `ins_paid` | 04/27/2023 - 05/02/2023 | extracted=151047.39  expected=152324.37  diff=1276.98 |
| 117 | `adjustment` | 04/27/2023 - 05/02/2023 | extracted=142117.31  expected=143318.79  diff=1201.48 |
| 117 | `payments` | 04/27/2023 - 05/02/2023 | extracted=19978.54  expected=None |
| 117 | `balance` | 04/27/2023 - 05/02/2023 | extracted=0.0  expected=20147.44  diff=20147.44 |
| 117 | `provider` | 04/27/2023 - 05/02/2023 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 117 | `insurers` | 04/27/2023 - 05/02/2023 | missing=['medicaid'] |
| 118 | `payments` | 12/15/2018 - 12/17/2018 | extracted=20740.83  expected=None |
| 118 | `balance` | 12/15/2018 - 12/17/2018 | extracted=0.0  expected=20740.83  diff=20740.83 |
| 118 | `provider` | 12/15/2018 - 12/17/2018 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 118 | `insurers` | 12/15/2018 - 12/17/2018 | missing=['medicaid'] |
| 119 | `payments` | 09/06/2017 - 09/10/2017 | extracted=17070.82  expected=None |
| 119 | `balance` | 09/06/2017 - 09/10/2017 | extracted=0.0  expected=17070.82  diff=17070.82 |
| 119 | `provider` | 09/06/2017 - 09/10/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 119 | `insurers` | 09/06/2017 - 09/10/2017 | missing=['medicaid'] |
| 120 | `payments` | 01/16/2024 - 01/21/2024 | extracted=16253.14  expected=None |
| 120 | `balance` | 01/16/2024 - 01/21/2024 | extracted=0.0  expected=16253.14  diff=16253.14 |
| 120 | `provider` | 01/16/2024 - 01/21/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 120 | `insurers` | 01/16/2024 - 01/21/2024 | missing=['medicaid'] |
| 121 | `payments` | 07/17/2018 - 07/22/2018 | extracted=22418.15  expected=None |
| 121 | `balance` | 07/17/2018 - 07/22/2018 | extracted=0.0  expected=22418.15  diff=22418.15 |
| 121 | `provider` | 07/17/2018 - 07/22/2018 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 121 | `insurers` | 07/17/2018 - 07/22/2018 | missing=['medicaid'] |
| 122 | `payments` | 04/28/2024 - 05/02/2024 | extracted=16373.04  expected=None |
| 122 | `balance` | 04/28/2024 - 05/02/2024 | extracted=0.0  expected=16373.04  diff=16373.04 |
| 122 | `provider` | 04/28/2024 - 05/02/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 122 | `insurers` | 04/28/2024 - 05/02/2024 | missing=['medicaid'] |
| 123 | `payments` | 10/06/2017 - 10/09/2017 | extracted=18940.85  expected=None |
| 123 | `balance` | 10/06/2017 - 10/09/2017 | extracted=0.0  expected=18940.85  diff=18940.85 |
| 123 | `provider` | 10/06/2017 - 10/09/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 123 | `insurers` | 10/06/2017 - 10/09/2017 | missing=['medicaid'] |
| 124 | `payments` | 03/27/2020 - 03/30/2020 | extracted=13849.45  expected=None |
| 124 | `balance` | 03/27/2020 - 03/30/2020 | extracted=0.0  expected=13849.45  diff=13849.45 |
| 124 | `provider` | 03/27/2020 - 03/30/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 124 | `insurers` | 03/27/2020 - 03/30/2020 | missing=['medicaid'] |
| 125 | `payments` | 08/22/2024 - 08/27/2024 | extracted=16978.46  expected=None |
| 125 | `balance` | 08/22/2024 - 08/27/2024 | extracted=0.0  expected=16978.46  diff=16978.46 |
| 125 | `provider` | 08/22/2024 - 08/27/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 125 | `insurers` | 08/22/2024 - 08/27/2024 | missing=['medicaid'] |
| 126 | `payments` | 06/14/2021 - 06/17/2021 | extracted=17580.42  expected=None |
| 126 | `balance` | 06/14/2021 - 06/17/2021 | extracted=0.0  expected=17580.42  diff=17580.42 |
| 126 | `provider` | 06/14/2021 - 06/17/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 126 | `insurers` | 06/14/2021 - 06/17/2021 | missing=['medicaid'] |
| 127 | `payments` | 09/26/2021 - 10/03/2021 | extracted=23957.03  expected=None |
| 127 | `balance` | 09/26/2021 - 10/03/2021 | extracted=0.0  expected=23957.03  diff=23957.03 |
| 127 | `provider` | 09/26/2021 - 10/03/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 127 | `insurers` | 09/26/2021 - 10/03/2021 | missing=['medicaid'] |
| 128 | `payments` | 03/10/2019 - 03/13/2019 | extracted=27244.56  expected=None |
| 128 | `balance` | 03/10/2019 - 03/13/2019 | extracted=0.0  expected=27244.56  diff=27244.56 |
| 128 | `provider` | 03/10/2019 - 03/13/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 128 | `insurers` | 03/10/2019 - 03/13/2019 | missing=['medicaid'] |
| 129 | `payments` | 10/05/2021 - 10/11/2021 | extracted=20969.26  expected=None |
| 129 | `balance` | 10/05/2021 - 10/11/2021 | extracted=0.0  expected=20969.26  diff=20969.26 |
| 129 | `provider` | 10/05/2021 - 10/11/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 129 | `insurers` | 10/05/2021 - 10/11/2021 | missing=['medicaid'] |
| 131 | `total_charges` | 05/12/2021 - 05/13/2021 | extracted=275974.68  expected=423112.28  diff=147137.60 |
| 131 | `ins_paid` | 05/12/2021 - 05/13/2021 | extracted=133118.81  expected=204091.92  diff=70973.11 |
| 131 | `adjustment` | 05/12/2021 - 05/13/2021 | extracted=125248.69  expected=192025.8  diff=66777.11 |
| 131 | `payments` | 05/12/2021 - 05/13/2021 | extracted=17607.18  expected=None |
| 131 | `balance` | 05/12/2021 - 05/13/2021 | extracted=0.0  expected=26994.56  diff=26994.56 |
| 131 | `provider` | 05/12/2021 - 05/13/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 131 | `insurers` | 05/12/2021 - 05/13/2021 | missing=['medicaid'] |
| 132 | `total_charges` | 08/31/2024 - 09/07/2024 | extracted=423112.28  expected=193350.97  diff=229761.31 |
| 132 | `ins_paid` | 08/31/2024 - 09/07/2024 | extracted=204091.92  expected=93264.54  diff=110827.38 |
| 132 | `adjustment` | 08/31/2024 - 09/07/2024 | extracted=192025.8  expected=87750.64  diff=104275.16 |
| 132 | `payments` | 08/31/2024 - 09/07/2024 | extracted=26994.56  expected=None |
| 132 | `balance` | 08/31/2024 - 09/07/2024 | extracted=0.0  expected=12335.79  diff=12335.79 |
| 132 | `provider` | 08/31/2024 - 09/07/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 132 | `insurers` | 08/31/2024 - 09/07/2024 | missing=['medicaid'] |
| 133 | `total_charges` | 12/08/2019 - 12/12/2019 | extracted=193350.97  expected=247115.99  diff=53765.02 |
| 133 | `ins_paid` | 12/08/2019 - 12/12/2019 | extracted=93264.54  expected=119198.57  diff=25934.03 |
| 133 | `adjustment` | 12/08/2019 - 12/12/2019 | extracted=87750.64  expected=112151.42  diff=24400.78 |
| 133 | `payments` | 12/08/2019 - 12/12/2019 | extracted=12335.79  expected=None |
| 133 | `balance` | 12/08/2019 - 12/12/2019 | extracted=0.0  expected=15766.0  diff=15766.00 |
| 133 | `provider` | 12/08/2019 - 12/12/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 133 | `insurers` | 12/08/2019 - 12/12/2019 | missing=['medicaid'] |
| 134 | `total_charges` | 06/09/2020 - 06/10/2020 | extracted=247115.99  expected=254465.09  diff=7349.10 |
| 134 | `ins_paid` | 06/09/2020 - 06/10/2020 | extracted=119198.57  expected=122743.47  diff=3544.90 |
| 134 | `adjustment` | 06/09/2020 - 06/10/2020 | extracted=112151.42  expected=115486.75  diff=3335.33 |
| 134 | `payments` | 06/09/2020 - 06/10/2020 | extracted=15766.0  expected=None |
| 134 | `balance` | 06/09/2020 - 06/10/2020 | extracted=0.0  expected=16234.87  diff=16234.87 |
| 134 | `provider` | 06/09/2020 - 06/10/2020 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 134 | `insurers` | 06/09/2020 - 06/10/2020 | missing=['medicaid'] |
| 135 | `total_charges` | 07/11/2017 - 07/12/2017 | extracted=254465.09  expected=273995.04  diff=19529.95 |
| 135 | `ins_paid` | 07/11/2017 - 07/12/2017 | extracted=122743.47  expected=132163.91  diff=9420.44 |
| 135 | `adjustment` | 07/11/2017 - 07/12/2017 | extracted=115486.75  expected=124350.25  diff=8863.50 |
| 135 | `payments` | 07/11/2017 - 07/12/2017 | extracted=16234.87  expected=None |
| 135 | `balance` | 07/11/2017 - 07/12/2017 | extracted=0.0  expected=17480.88  diff=17480.88 |
| 135 | `provider` | 07/11/2017 - 07/12/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 135 | `insurers` | 07/11/2017 - 07/12/2017 | missing=['medicaid'] |
| 136 | `total_charges` | 11/06/2019 - 11/07/2019 | extracted=273995.04  expected=283061.58  diff=9066.54 |
| 136 | `ins_paid` | 11/06/2019 - 11/07/2019 | extracted=132163.91  expected=136537.24  diff=4373.33 |
| 136 | `adjustment` | 11/06/2019 - 11/07/2019 | extracted=124350.25  expected=128465.01  diff=4114.76 |
| 136 | `payments` | 11/06/2019 - 11/07/2019 | extracted=17480.88  expected=None |
| 136 | `balance` | 11/06/2019 - 11/07/2019 | extracted=0.0  expected=18059.33  diff=18059.33 |
| 136 | `provider` | 11/06/2019 - 11/07/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 136 | `insurers` | 11/06/2019 - 11/07/2019 | missing=['medicaid'] |
| 137 | `total_charges` | 09/16/2021 - 09/17/2021 | extracted=283061.58  expected=190936.99  diff=92124.59 |
| 137 | `ins_paid` | 09/16/2021 - 09/17/2021 | extracted=136537.24  expected=92100.13  diff=44437.11 |
| 137 | `adjustment` | 09/16/2021 - 09/17/2021 | extracted=128465.01  expected=86655.08  diff=41809.93 |
| 137 | `payments` | 09/16/2021 - 09/17/2021 | extracted=18059.33  expected=None |
| 137 | `balance` | 09/16/2021 - 09/17/2021 | extracted=0.0  expected=12181.78  diff=12181.78 |
| 137 | `provider` | 09/16/2021 - 09/17/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 137 | `insurers` | 09/16/2021 - 09/17/2021 | missing=['medicaid'] |
| 138 | `total_charges` | 12/02/2017 - 12/08/2017 | extracted=190936.99  expected=385889.87  diff=194952.88 |
| 138 | `ins_paid` | 12/02/2017 - 12/08/2017 | extracted=92100.13  expected=186137.37  diff=94037.24 |
| 138 | `adjustment` | 12/02/2017 - 12/08/2017 | extracted=86655.08  expected=175132.73  diff=88477.65 |
| 138 | `payments` | 12/02/2017 - 12/08/2017 | extracted=12181.78  expected=None |
| 138 | `balance` | 12/02/2017 - 12/08/2017 | extracted=0.0  expected=24619.77  diff=24619.77 |
| 138 | `provider` | 12/02/2017 - 12/08/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 138 | `insurers` | 12/02/2017 - 12/08/2017 | missing=['medicaid'] |
| 139 | `total_charges` | 05/29/2019 - 06/05/2019 | extracted=385889.87  expected=389960.22  diff=4070.35 |
| 139 | `ins_paid` | 05/29/2019 - 06/05/2019 | extracted=186137.37  expected=188100.73  diff=1963.36 |
| 139 | `adjustment` | 05/29/2019 - 06/05/2019 | extracted=175132.73  expected=176980.03  diff=1847.30 |
| 139 | `payments` | 05/29/2019 - 06/05/2019 | extracted=24619.77  expected=None |
| 139 | `balance` | 05/29/2019 - 06/05/2019 | extracted=0.0  expected=24879.46  diff=24879.46 |
| 139 | `provider` | 05/29/2019 - 06/05/2019 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 139 | `insurers` | 05/29/2019 - 06/05/2019 | missing=['medicaid'] |
| 140 | `total_charges` | 10/05/2018 - 10/08/2018 | extracted=389960.22  expected=343625.59  diff=46334.63 |
| 140 | `ins_paid` | 10/05/2018 - 10/08/2018 | extracted=188100.73  expected=165750.82  diff=22349.91 |
| 140 | `adjustment` | 10/05/2018 - 10/08/2018 | extracted=176980.03  expected=155951.46  diff=21028.57 |
| 140 | `payments` | 10/05/2018 - 10/08/2018 | extracted=24879.46  expected=None |
| 140 | `balance` | 10/05/2018 - 10/08/2018 | extracted=0.0  expected=21923.31  diff=21923.31 |
| 140 | `provider` | 10/05/2018 - 10/08/2018 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 140 | `insurers` | 10/05/2018 - 10/08/2018 | missing=['medicaid'] |
| 141 | `total_charges` | 05/25/2017 - 06/01/2017 | extracted=343625.59  expected=292278.13  diff=51347.46 |
| 141 | `ins_paid` | 05/25/2017 - 06/01/2017 | extracted=165750.82  expected=140982.92  diff=24767.90 |
| 141 | `adjustment` | 05/25/2017 - 06/01/2017 | extracted=155951.46  expected=132647.87  diff=23303.59 |
| 141 | `payments` | 05/25/2017 - 06/01/2017 | extracted=21923.31  expected=None |
| 141 | `balance` | 05/25/2017 - 06/01/2017 | extracted=0.0  expected=18647.34  diff=18647.34 |
| 141 | `provider` | 05/25/2017 - 06/01/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 141 | `insurers` | 05/25/2017 - 06/01/2017 | missing=['medicaid'] |
| 142 | `total_charges` | 07/15/2022 - 07/16/2022 | extracted=292278.13  expected=388750.46  diff=96472.33 |
| 142 | `ins_paid` | 07/15/2022 - 07/16/2022 | extracted=140982.92  expected=187517.2  diff=46534.28 |
| 142 | `adjustment` | 07/15/2022 - 07/16/2022 | extracted=132647.87  expected=176430.98  diff=43783.11 |
| 142 | `payments` | 07/15/2022 - 07/16/2022 | extracted=18647.34  expected=None |
| 142 | `balance` | 07/15/2022 - 07/16/2022 | extracted=0.0  expected=24802.28  diff=24802.28 |
| 142 | `provider` | 07/15/2022 - 07/16/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 142 | `insurers` | 07/15/2022 - 07/16/2022 | missing=['medicaid'] |
| 143 | `total_charges` | 07/11/2021 - 07/12/2021 | extracted=777945.8  expected=389195.34  diff=388750.46 |
| 143 | `ins_paid` | 07/11/2021 - 07/12/2021 | extracted=375248.99  expected=187731.79  diff=187517.20 |
| 143 | `adjustment` | 07/11/2021 - 07/12/2021 | extracted=353063.87  expected=176632.89  diff=176430.98 |
| 143 | `payments` | 07/11/2021 - 07/12/2021 | extracted=49632.94  expected=None |
| 143 | `balance` | 07/11/2021 - 07/12/2021 | extracted=0.0  expected=24830.66  diff=24830.66 |
| 143 | `provider` | 07/11/2021 - 07/12/2021 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 143 | `insurers` | 07/11/2021 - 07/12/2021 | missing=['medicaid'] |
| 144 | `payments` | 05/02/2017 - 05/07/2017 | extracted=17588.77  expected=None |
| 144 | `balance` | 05/02/2017 - 05/07/2017 | extracted=0.0  expected=17588.77  diff=17588.77 |
| 144 | `provider` | 05/02/2017 - 05/07/2017 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 144 | `insurers` | 05/02/2017 - 05/07/2017 | missing=['medicaid'] |
| 145 | `payments` | 11/13/2018 - 11/14/2018 | extracted=23379.92  expected=None |
| 145 | `balance` | 11/13/2018 - 11/14/2018 | extracted=0.0  expected=23379.92  diff=23379.92 |
| 145 | `provider` | 11/13/2018 - 11/14/2018 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 145 | `insurers` | 11/13/2018 - 11/14/2018 | missing=['medicaid'] |
| 146 | `payments` | 04/07/2022 - 04/13/2022 | extracted=20822.33  expected=None |
| 146 | `balance` | 04/07/2022 - 04/13/2022 | extracted=0.0  expected=20822.33  diff=20822.33 |
| 146 | `provider` | 04/07/2022 - 04/13/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 146 | `insurers` | 04/07/2022 - 04/13/2022 | missing=['medicaid'] |
| 147 | `payments` | 05/23/2024 - 05/30/2024 | extracted=19529.89  expected=None |
| 147 | `balance` | 05/23/2024 - 05/30/2024 | extracted=0.0  expected=19529.89  diff=19529.89 |
| 147 | `provider` | 05/23/2024 - 05/30/2024 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 147 | `insurers` | 05/23/2024 - 05/30/2024 | missing=['medicaid'] |
| 148 | `payments` | 12/01/2018 - 12/08/2018 | extracted=22588.91  expected=None |
| 148 | `balance` | 12/01/2018 - 12/08/2018 | extracted=0.0  expected=22588.91  diff=22588.91 |
| 148 | `provider` | 12/01/2018 - 12/08/2018 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 148 | `insurers` | 12/01/2018 - 12/08/2018 | missing=['medicaid'] |
| 149 | `payments` | 11/13/2022 - 11/15/2022 | extracted=22019.33  expected=None |
| 149 | `balance` | 11/13/2022 - 11/15/2022 | extracted=0.0  expected=22019.33  diff=22019.33 |
| 149 | `provider` | 11/13/2022 - 11/15/2022 | extracted='Inpatient Episode'  expected='South Patrickmouth General Hospital' |
| 149 | `insurers` | 11/13/2022 - 11/15/2022 | missing=['medicaid'] |

### doc_012

**Count mismatch** — GT: 120, extracted: 122.

**Extra extracted records (2):**
- `10/22/2020 - 11/18/2020` — Extracted record has no GT counterpart
- `03/15/2023 - 04/14/2023` — Extracted record has no GT counterpart

**Field mismatches (11):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 22 | `adjustment` | 07/02/2018 - 08/01/2018 | extracted=None  expected=1653.11 |
| 22 | `payments` | 07/02/2018 - 08/01/2018 | extracted=1653.11  expected=None |
| 57 | `ins_paid` | 10/18/2020 - 11/18/2020 | extracted=None  expected=9843.67 |
| 57 | `adjustment` | 10/18/2020 - 11/18/2020 | extracted=None  expected=2927.28 |
| 57 | `balance` | 10/18/2020 - 11/18/2020 | extracted=None  expected=0.0 |
| 74 | `ins_paid` | 12/13/2021 - 01/13/2022 | extracted=None  expected=9640.07 |
| 74 | `adjustment` | 12/13/2021 - 01/13/2022 | extracted=None  expected=2866.74 |
| 74 | `balance` | 12/13/2021 - 01/13/2022 | extracted=None  expected=0.0 |
| 93 | `ins_paid` | 03/13/2023 - 04/14/2023 | extracted=None  expected=8893.02 |
| 93 | `adjustment` | 03/13/2023 - 04/14/2023 | extracted=None  expected=2644.58 |
| 93 | `balance` | 03/13/2023 - 04/14/2023 | extracted=None  expected=0.0 |

---

_Generated by `scripts/eval_extraction.py`_
