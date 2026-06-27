# Extraction Evaluation Results

Evaluated **12 documents** against ground truth.

---

## Summary

| Doc | GT | Extracted | Count | Weighted Acc | Cost USD | Duration |
|---|---|---|---|---|---|---|
| doc_001 | 50 | 50 | ✓ | 96.4% | $0.1047 | 51.67s |
| doc_002 | 40 | 12 | ✗ | 0.0% | $0.0593 | 15.72s |
| doc_003 | 1 | 1 | ✓ | 67.9% | $0.0795 | 7.39s |
| doc_004 | 1 | 1 | ✓ | 75.0% | $0.0664 | 7.72s |
| doc_005 | 80 | 15 | ✗ | 18.1% | $0.1266 | 15.51s |
| doc_006 | 33 | 3 | ✗ | 7.8% | $0.0348 | 7.4s |
| doc_007 | 400 | 16 | ✗ | 3.8% | $0.4162 | 36.74s |
| doc_008 | 100 | 11 | ✗ | 0.0% | $0.1555 | 36.43s |
| doc_009 | 1 | 108 | ✗ | 0.0% | $0.6746 | 163.51s |
| doc_010 | 1 | 2 | ✗ | 0.0% | $0.5184 | 23.05s |
| doc_011 | 150 | 14 | ✗ | 7.7% | $0.5414 | 44.04s |
| doc_012 | 120 | 28 | ✗ | 17.6% | $0.2017 | 59.18s |

**Total cost:** $2.9791  
**Total tokens:** 1,367,007 (input 1,326,157 / output 40,850)  
**Total wall-clock:** 468.4s

---

## Field Accuracy by Document

| Doc | date | cpt | total$ | ins$ | adj | pmts | bal | prov | insrs | 3p | desc |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doc_001 | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% |
| doc_002 | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% |
| doc_003 | ✓100% | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% | ✗0% | ✓100% | ✓100% | ✗0% | ✗0% |
| doc_004 | ✓100% | ✓100% | ✓100% | ✓100% | ✗0% | ✓100% | ✗0% | ✓100% | ✓100% | ✓100% | ✗0% |
| doc_005 | ✗19% | ✗19% | ✗19% | ✗19% | ✗19% | ✗19% | ✗19% | ✗19% | ✗19% | ✗19% | ✗0% |
| doc_006 | ✗9% | ✗0% | ✗9% | ✗9% | ✗9% | ✗9% | ✗9% | ✗9% | ✗9% | ✗9% | ✗0% |
| doc_007 | ✗4% | ✗4% | ✗4% | ✗4% | ✗4% | ✗4% | ✗4% | ✗2% | ✗4% | ✗4% | ✗0% |
| doc_008 | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% |
| doc_009 | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% |
| doc_010 | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% | ✗0% |
| doc_011 | ✗9% | ✗9% | ✗9% | ✗9% | ✗9% | ✗9% | ✗9% | ✗4% | ✗4% | ✗9% | ✗0% |
| doc_012 | ✗21% | ✗0% | ✗21% | ✗21% | ✗20% | ✗20% | ✗20% | ✗21% | ✗21% | ✗21% | ✗0% |

---

## Error Details per Document

### doc_001

Record count matches GT.

**Field mismatches (50):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `description` | 07/28/2024 | extracted='ESRD related services, per month, 1 physician'  expected=None |
| 1 | `description` | 12/11/2023 | extracted='Self-care/home management training, Subsequent hospital care, level 3'  expected=None |
| 2 | `description` | 01/06/2024 | extracted='Initial hospital care, Autonomic nervous system function testing, X-ray spine lumbosacral 4+ views, Office/outpatient visit established patient level 5, Emergency dept visit level 3'  expected=None |
| 3 | `description` | 02/27/2023 | extracted='Office/outpatient visit established patient level 4, Colonoscopy diagnostic, Emergency dept visit level 1'  expected=None |
| 4 | `description` | 03/14/2024 | extracted='Initial hospital care level 2, Emergency dept visit level 3, Strep A test direct, Physical therapy electrical stimulation attended, Psychotherapy 30 min'  expected=None |
| 5 | `description` | 10/28/2023 | extracted='ESRD related services, per month, 1 physician'  expected=None |
| 6 | `description` | 09/15/2024 | extracted='Office/outpatient visit new patient level 3, X-ray humerus minimum 2 views, IV push infusion initial, Hospital discharge day management, X-ray knee 3 views'  expected=None |
| 7 | `description` | 12/31/2024 | extracted='Spacer, bag, or reservoir with/without mask; Therapeutic procedure group'  expected=None |
| 8 | `description` | 08/23/2023 | extracted='X-ray humerus, minimum 2 views'  expected=None |
| 9 | `description` | 08/13/2024 | extracted='Initial hospital care level 3, Autonomic nervous system testing sudomotor, Upper GI endoscopy with biopsy, Subsequent hospital care level 1, Electrocardiogram 12-lead'  expected=None |
| 10 | `description` | 04/11/2023 | extracted='Influenza vaccine 3+ years, Office/outpatient visit level 3, ESRD related per day, Hemodialysis procedure requiring repeat eval, Emergency dept visit level 2'  expected=None |
| 11 | `description` | 03/04/2023 | extracted='Physical therapy paraffin bath, Chest X-ray 2 views, Therapeutic exercise, Tetanus toxoid (Td) IM, X-ray knee 3 views'  expected=None |
| 12 | `description` | 11/18/2024 | extracted='Initial hospital care level 3, Blood count complete (CBC) automated differential'  expected=None |
| 13 | `description` | 07/10/2024 | extracted='X-ray knee 3 views, X-ray knee 4+ views, Psychotherapy 30 min, Office/outpatient visit level 2'  expected=None |
| 14 | `description` | 05/14/2023 | extracted='Office/outpatient visit new patient level 2, Emergency dept visit level 2, Emergency dept visit level 1'  expected=None |
| 15 | `description` | 01/02/2024 | extracted='Influenza vaccine 3+ years IM'  expected=None |
| 16 | `description` | 02/27/2024 | extracted='Emergency dept visit level 3, MRI lumbar spine without and with contrast'  expected=None |
| 17 | `description` | 08/17/2023 | extracted='ESRD home dialysis per month age 20+, Physical therapy whirlpool'  expected=None |
| 18 | `description` | 02/09/2023 | extracted='Physical therapy electrical stimulation, Office/outpatient visit established patient level 1, Hemodialysis procedure physician'  expected=None |
| 19 | `description` | 11/11/2024 | extracted='Cataract surgery with IOL'  expected=None |
| 20 | `description` | 03/06/2024 | extracted='Ultrasound abdomen limited, Colonoscopy diagnostic'  expected=None |
| 21 | `description` | 06/23/2023 | extracted='MRI lumbar spine without and with contrast, Autonomic testing with modifier, Total hip arthroplasty, Immunization administration each additional injection'  expected=None |
| 22 | `description` | 03/11/2024 | extracted='Autonomic nervous system function testing'  expected=None |
| 23 | `description` | 11/21/2023 | extracted='Romiplostim, ESRD home dialysis, Echocardiography transthoracic complete, Screening mammography bilateral, Cervical cytology (Pap) liquid-based'  expected=None |
| 24 | `description` | 07/09/2024 | extracted='ESRD home dialysis per month age 20+, Strep A test direct, Bevacizumab 10 mg'  expected=None |
| 25 | `description` | 09/09/2024 | extracted='Office/outpatient visit new patient level 4, Hemodialysis procedure physician, Total knee arthroplasty, Colonoscopy with biopsy, Autonomic nervous system testing sudomotor'  expected=None |
| 26 | `description` | 12/12/2023 | extracted='Autonomic testing with modifier, Colonoscopy diagnostic, Office/outpatient visit new patient level 4'  expected=None |
| 27 | `description` | 05/10/2023 | extracted='Emergency dept visit level 4, Dialysis training patient/caregiver per session'  expected=None |
| 28 | `description` | 08/12/2024 | extracted='Psychotherapy 60 min, Subsequent hospital care level 3, Physical therapy whirlpool'  expected=None |
| 29 | `description` | 03/06/2024 | extracted='Colonoscopy diagnostic'  expected=None |
| 30 | `description` | 03/22/2024 | extracted='Stress echocardiography, Strep A test direct, IV push infusion initial, Therapeutic activities'  expected=None |
| 31 | `description` | 09/05/2023 | extracted='Initial hospital care level 2'  expected=None |
| 32 | `description` | 01/13/2024 | extracted='Ultrasound pelvis transvaginal, Subsequent hospital care level 3, Chest X-ray 4+ views, ESRD related services per month, Chest X-ray 4+ views'  expected=None |
| 33 | `description` | 05/10/2023 | extracted='Arthroscopy knee surgical with meniscectomy, Autonomic testing with modifier, Therapeutic injection subcutaneous or IM, Gait training, Therapeutic exercise'  expected=None |
| 34 | `description` | 09/12/2024 | extracted='Therapeutic exercise, ESRD related services per month, Emergency dept visit level 3, Influenza vaccine 3+ years IM'  expected=None |
| 35 | `description` | 12/24/2024 | extracted='ESRD related services per day, Subsequent hospital care level 2, Office/outpatient visit established patient level 5'  expected=None |
| 36 | `description` | 10/23/2023 | extracted='Therapeutic activities, X-ray wrist minimum 3 views, Gait training, X-ray knee 4+ views, Physical therapy vasopneumatic device'  expected=None |
| 37 | `description` | 10/12/2024 | extracted='Comprehensive metabolic panel, Psychotherapy 45 min, ESRD related services per month, Comprehensive metabolic panel'  expected=None |
| 38 | `description` | 04/18/2024 | extracted='X-ray spine lumbosacral 4+ views, Psychotherapy 60 min, E&M level 4 with modifier 25, Physical therapy electrical stimulation attended, Subsequent hospital care level 3'  expected=None |
| 39 | `description` | 03/01/2024 | extracted='Chest X-ray 4+ views, CT abdomen & pelvis with contrast, ESRD related services per day'  expected=None |
| 40 | `description` | 08/16/2024 | extracted='ESRD related services per month, Chest X-ray 4+ views, Dialysis training patient/caregiver per session, Diphenhydramine HCl 50 mg oral, Physical therapy hot or cold packs'  expected=None |
| 41 | `description` | 04/13/2023 | extracted='Colonoscopy diagnostic, X-ray knee 3 views, Lipid panel, Screening mammography bilateral'  expected=None |
| 42 | `description` | 09/24/2024 | extracted='Cardiovascular stress test'  expected=None |
| 43 | `description` | 06/20/2023 | extracted='Prothrombin time, Therapeutic exercise, Physical performance testing, Manual therapy techniques'  expected=None |
| 44 | `description` | 04/21/2024 | extracted='Ultrasound abdomen limited'  expected=None |
| 45 | `description` | 07/23/2023 | extracted='Prothrombin time, Colonoscopy with biopsy, Office/outpatient visit established patient level 2'  expected=None |
| 46 | `description` | 09/13/2024 | extracted='Total hip arthroplasty, ESRD related services per day'  expected=None |
| 47 | `description` | 12/01/2023 | extracted='Physical therapy paraffin bath, Therapeutic injection subcutaneous or IM, Autonomic nervous system testing sudomotor'  expected=None |
| 48 | `description` | 07/24/2024 | extracted='Physical therapy whirlpool, X-ray knee 3 views, X-ray shoulder minimum 2 views, Physical performance testing'  expected=None |
| 49 | `description` | 04/30/2023 | extracted='Subsequent hospital care level 2, Replacement batteries alkaline 9 volt each, Physical therapy infrared, Tetanus toxoid (Td) IM'  expected=None |

### doc_002

**Count mismatch** — GT: 40, extracted: 12.

**Missing records (40):**
- GT[0] `02/01/2023 - 12/07/2024` — No extracted record found with this treatment_date
- GT[1] `06/26/2023 - 12/11/2024` — No extracted record found with this treatment_date
- GT[2] `03/30/2023 - 07/18/2024` — No extracted record found with this treatment_date
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
- GT[18] `03/20/2023 - 09/03/2024` — No extracted record found with this treatment_date
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

**Extra extracted records (12):**
- `01/31/2024` — Extracted record has no GT counterpart
- `06/15/2024` — Extracted record has no GT counterpart
- `09/08/2024` — Extracted record has no GT counterpart
- `11/07/2024` — Extracted record has no GT counterpart
- `12/07/2024` — Extracted record has no GT counterpart
- `03/21/2024` — Extracted record has no GT counterpart
- `11/18/2024` — Extracted record has no GT counterpart
- `02/01/2023` — Extracted record has no GT counterpart
- `05/10/2023` — Extracted record has no GT counterpart
- `08/03/2024` — Extracted record has no GT counterpart
- `03/20/2023` — Extracted record has no GT counterpart
- `09/13/2023` — Extracted record has no GT counterpart

### doc_003

Record count matches GT.

**Field mismatches (4):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `payments` | 01/04/2023 - 12/31/2024 | extracted=None  expected=31072.93 |
| 0 | `balance` | 01/04/2023 - 12/31/2024 | extracted=31072.93  expected=0.0  diff=31072.93 |
| 0 | `third_parties` | 01/04/2023 - 12/31/2024 | missing=['omnisys immunizations', 'paramount lonestar']  extra=['im health pbm', 'lonestar', 'omnisys', 'paramount'] |
| 0 | `description` | 01/04/2023 - 12/31/2024 | extracted='Pharmacy claim summary: all fills 01/04/2023 to 12/31/2024'  expected='Pharmacy Record' |

### doc_004

Record count matches GT.

**Field mismatches (3):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `adjustment` | 01/04/2023 - 12/31/2024 | extracted=None  expected=55776.23 |
| 0 | `balance` | 01/04/2023 - 12/31/2024 | extracted=None  expected=0.0 |
| 0 | `description` | 01/04/2023 - 12/31/2024 | extracted='Pharmacy prescription fills for Gregory Tate'  expected='Pharmacy Expense Report' |

### doc_005

**Count mismatch** — GT: 80, extracted: 15.

**Missing records (65):**
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

**Field mismatches (15):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `description` | 12/22/2023 - 12/24/2023 | extracted='Inpatient: Lumbar spine fusion'  expected='Lumbar spine fusion' |
| 1 | `description` | 05/16/2021 - 05/19/2021 | extracted='Inpatient: Bowel obstruction'  expected='Bowel obstruction' |
| 2 | `description` | 07/02/2024 - 07/03/2024 | extracted='Inpatient: Acute pancreatitis'  expected='Acute pancreatitis' |
| 3 | `description` | 11/30/2022 - 12/07/2022 | extracted='Inpatient: Bowel obstruction'  expected='Bowel obstruction' |
| 4 | `description` | 03/23/2022 - 03/27/2022 | extracted='Inpatient: Acute kidney injury'  expected='Acute kidney injury' |
| 5 | `description` | 05/18/2021 - 05/21/2021 | extracted='Inpatient: Major depressive disorder, recurrent'  expected='Major depressive disorder, recurrent' |
| 6 | `description` | 09/20/2023 - 09/23/2023 | extracted='Inpatient: Bowel obstruction'  expected='Bowel obstruction' |
| 7 | `description` | 11/07/2021 - 11/08/2021 | extracted='Inpatient: Schizophrenia, acute exacerbation'  expected='Schizophrenia, acute exacerbation' |
| 8 | `description` | 06/29/2022 - 07/04/2022 | extracted='Inpatient: Urinary tract infection'  expected='Urinary tract infection' |
| 9 | `description` | 09/11/2022 - 09/13/2022 | extracted='Inpatient: Acute kidney injury'  expected='Acute kidney injury' |
| 10 | `description` | 12/03/2021 - 12/04/2021 | extracted='Inpatient: Stroke, ischemic'  expected='Stroke, ischemic' |
| 11 | `description` | 05/18/2021 - 05/21/2021 | extracted='Inpatient: Type 2 diabetes mellitus with ketoacidosis'  expected='Type 2 diabetes mellitus with ketoacidosis' |
| 12 | `description` | 07/14/2021 - 07/15/2021 | extracted='Inpatient: Chronic obstructive pulmonary disease with acute exacerbation'  expected='Chronic obstructive pulmonary disease with acute exacerbation' |
| 13 | `description` | 07/27/2021 - 07/29/2021 | extracted='Inpatient: Chronic obstructive pulmonary disease with acute exacerbation'  expected='Chronic obstructive pulmonary disease with acute exacerbation' |
| 14 | `description` | 09/14/2022 - 09/21/2022 | extracted='Inpatient: Chronic obstructive pulmonary disease with acute exacerbation'  expected='Chronic obstructive pulmonary disease with acute exacerbation' |

### doc_006

**Count mismatch** — GT: 33, extracted: 3.

**Missing records (30):**
- GT[1] `01/28/2021 - 02/22/2021` — No extracted record found with this treatment_date
- GT[2] `02/23/2021 - 03/20/2021` — No extracted record found with this treatment_date
- GT[3] `03/21/2021 - 04/19/2021` — No extracted record found with this treatment_date
- GT[4] `04/20/2021 - 05/21/2021` — No extracted record found with this treatment_date
- GT[5] `05/22/2021 - 06/20/2021` — No extracted record found with this treatment_date
- GT[6] `06/21/2021 - 07/21/2021` — No extracted record found with this treatment_date
- GT[7] `07/22/2021 - 08/16/2021` — No extracted record found with this treatment_date
- GT[8] `08/17/2021 - 09/16/2021` — No extracted record found with this treatment_date
- GT[9] `09/17/2021 - 10/15/2021` — No extracted record found with this treatment_date
- GT[10] `10/16/2021 - 11/16/2021` — No extracted record found with this treatment_date
- GT[11] `11/17/2021 - 12/15/2021` — No extracted record found with this treatment_date
- GT[13] `05/29/2022 - 06/30/2022` — No extracted record found with this treatment_date
- GT[14] `07/01/2022 - 08/02/2022` — No extracted record found with this treatment_date
- GT[15] `08/03/2022 - 09/01/2022` — No extracted record found with this treatment_date
- GT[16] `09/02/2022 - 09/29/2022` — No extracted record found with this treatment_date
- GT[17] `09/30/2022 - 10/31/2022` — No extracted record found with this treatment_date
- GT[18] `11/01/2022 - 12/01/2022` — No extracted record found with this treatment_date
- GT[19] `12/02/2022 - 01/03/2023` — No extracted record found with this treatment_date
- GT[20] `01/04/2023 - 02/01/2023` — No extracted record found with this treatment_date
- GT[21] `02/02/2023 - 02/28/2023` — No extracted record found with this treatment_date
- GT[22] `03/01/2023 - 03/26/2023` — No extracted record found with this treatment_date
- GT[24] `10/01/2023 - 10/30/2023` — No extracted record found with this treatment_date
- GT[25] `10/31/2023 - 11/28/2023` — No extracted record found with this treatment_date
- GT[26] `11/29/2023 - 12/25/2023` — No extracted record found with this treatment_date
- GT[27] `12/26/2023 - 01/26/2024` — No extracted record found with this treatment_date
- GT[28] `01/27/2024 - 02/28/2024` — No extracted record found with this treatment_date
- GT[29] `02/29/2024 - 04/01/2024` — No extracted record found with this treatment_date
- GT[30] `04/02/2024 - 05/03/2024` — No extracted record found with this treatment_date
- GT[31] `05/04/2024 - 06/03/2024` — No extracted record found with this treatment_date
- GT[32] `06/04/2024 - 07/05/2024` — No extracted record found with this treatment_date

**Field mismatches (6):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `cpt_codes` | 01/01/2021 - 01/27/2021 | extra=['82565', '84100', '84132', '84295', '90937', '93975', '99213', 'A4690', 'A4706', 'G0491', 'J0885', 'J2916'] |
| 0 | `description` | 01/01/2021 - 01/27/2021 | extracted='Dialysis, labs & associated procedures (10 treatments)'  expected='Dialysis — 10 treatments' |
| 12 | `cpt_codes` | 05/02/2022 - 05/28/2022 | extra=['36831', '82310', '84295', '86000', '90935', '90937', '90940', '99213', 'A4750', 'A4860', 'A4920', 'J0885', 'J3370'] |
| 12 | `description` | 05/02/2022 - 05/28/2022 | extracted='Dialysis, labs & associated procedures (10 treatments)'  expected='Dialysis — 10 treatments' |
| 23 | `cpt_codes` | 08/31/2023 - 09/30/2023 | extra=['36831', '82728', '84132', '85025', '86000', '93975', '99213', 'A4706', 'A4802', 'G0491', 'J0885', 'J2916'] |
| 23 | `description` | 08/31/2023 - 09/30/2023 | extracted='Dialysis, labs & associated procedures (13 treatments)'  expected='Dialysis — 13 treatments' |

### doc_007

**Count mismatch** — GT: 400, extracted: 16.

**Missing records (382):**
- GT[5] `09/29/2023` — No extracted record found with this treatment_date
- GT[6] `05/04/2022` — No extracted record found with this treatment_date
- GT[7] `06/22/2021` — No extracted record found with this treatment_date
- GT[8] `07/10/2023` — No extracted record found with this treatment_date
- GT[9] `10/13/2023` — No extracted record found with this treatment_date
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
- GT[37] `06/22/2021` — No extracted record found with this treatment_date
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
- GT[105] `10/13/2023` — No extracted record found with this treatment_date
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
- GT[254] `04/23/2022` — No extracted record found with this treatment_date
- GT[255] `10/09/2021` — No extracted record found with this treatment_date
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

**Field mismatches (42):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `description` | 08/01/2023 | extracted='Colonoscopy, diagnostic / Romiplostim, 10 mcg / Autonomic nervous system testing, sudomotor / Ultrasound abdomen, complete'  expected=None |
| 1 | `description` | 10/08/2021 | extracted='Methylprednisolone acetate, 80 mg / Physical therapy — ultrasound / Betadine or phisohex, per pint / ESRD related services, per month, 1 physician / Emergency dept visit, level 4 / Physical therapy — hot or cold packs / Tubing, oxygen, per supplier'  expected=None |
| 2 | `description` | 10/13/2021 | extracted='Medroxyprogesterone acetate, 150 mg / Immunization administration, each additional injection / Office/outpatient visit, established patient, level 4 / X-ray spine, lumbosacral, 2-3 views / Hemodialysis procedure, physician / Cisplatin, per 10 mg'  expected=None |
| 3 | `description` | 02/04/2023 | extracted='X-ray wrist, 2 views / Office/outpatient visit, established patient, level 3 / Syphilis test, qualitative'  expected=None |
| 4 | `description` | 04/22/2021 | extracted='Manual therapy techniques / Chest X-ray, 4+ views / Total hip arthroplasty / Diphenhydramine HCl, 50 mg, oral / X-ray wrist, 2 views / Initial hospital care, level 2 / Upper GI endoscopy with biopsy'  expected=None |
| 74 | `cpt_codes` | 10/08/2021 | missing=['72110', '73564', '76700', '90472', '99281', '99282']  extra=['90960', '97010', '97035', '99284', 'A4246', 'A4616', 'J1040'] |
| 74 | `total_charges` | 10/08/2021 | extracted=1747.47  expected=2078.23  diff=330.76 |
| 74 | `ins_paid` | 10/08/2021 | extracted=950.39  expected=1242.08  diff=291.69 |
| 74 | `adjustment` | 10/08/2021 | extracted=776.18  expected=806.64  diff=30.46 |
| 74 | `balance` | 10/08/2021 | extracted=20.9  expected=29.51  diff=8.61 |
| 74 | `description` | 10/08/2021 | extracted='Methylprednisolone acetate, 80 mg / Physical therapy — ultrasound / Betadine or phisohex, per pint / ESRD related services, per month, 1 physician / Emergency dept visit, level 4 / Physical therapy — hot or cold packs / Tubing, oxygen, per supplier'  expected=None |
| 243 | `cpt_codes` | 06/25/2023 | missing=['97116', '99201'] |
| 243 | `provider` | 06/25/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 243 | `description` | 06/25/2023 | extracted='Subsequent hospital care, level 1; Dialysis training, patient/caregiver, per session'  expected=None |
| 244 | `provider` | 05/05/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 244 | `insurers` | 05/05/2021 | missing=['insurance payment']  extra=['molina healthcare of ny'] |
| 244 | `description` | 05/05/2021 | extracted='Ondansetron HCl, per 1 mg; Hemodialysis procedure, physician; Subsequent hospital care, level 1; Gait training; Therapeutic activities; Immunization administration, first injection'  expected=None |
| 245 | `provider` | 01/13/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 245 | `description` | 01/13/2024 | extracted='Alglucerase, per 10 units; Gait training; Therapeutic exercise; Therapeutic procedure group; ESRD related services, per day; CT abdomen & pelvis with contrast'  expected=None |
| 246 | `provider` | 07/22/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 246 | `description` | 07/22/2022 | extracted='Hospital discharge day management, more than 30 min; Colonoscopy, diagnostic; Methylprednisolone acetate, 80 mg; Blood count, complete (CBC), automated; Physical performance testing'  expected=None |
| 247 | `cpt_codes` | 08/05/2023 |  |
| 247 | `provider` | 08/05/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 247 | `description` | 08/05/2023 | extracted='Psychiatric diagnostic evaluation; Strep A test, direct'  expected=None |
| 248 | `provider` | 08/28/2024 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 248 | `description` | 08/28/2024 | extracted='Doxorubicin HCl, 10 mg; Physical therapy — whirlpool; X-ray spine, lumbosacral, 2-3 views; X-ray humerus, minimum 2 views; Tubing, oxygen, per supplier; Agalsidase beta, 1 mg'  expected=None |
| 249 | `provider` | 10/08/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 249 | `description` | 10/08/2022 | extracted='Subsequent hospital care, level 3; Psychotherapy, 45 min; X-ray knee, 4+ views; Physical performance testing; Prothrombin time; Office/outpatient visit, established patient, level 1'  expected=None |
| 250 | `provider` | 05/31/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 250 | `description` | 05/31/2022 | extracted='Medroxyprogesterone acetate, 150 mg; Emergency dept visit, level 3; Arthroscopy, knee, surgical with meniscectomy; Office/outpatient visit, new patient, level 2; Surgical supply, not otherwise classified; Physical therapy — infrared'  expected=None |
| 251 | `provider` | 08/30/2022 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 251 | `description` | 08/30/2022 | extracted='Romiplostim, 10 mcg; Cisplatin, per 10 mg; Lipid panel; Surgical supply, not otherwise classified; Upper GI endoscopy with biopsy; Therapeutic activities'  expected=None |
| 252 | `provider` | 12/31/2021 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 252 | `description` | 12/31/2021 | extracted='Therapeutic exercise; Office/outpatient visit, established patient, level 3; Pralidoxime chloride, per 1 g; Cardiovascular stress test; Hemodialysis procedure, physician; Office/outpatient visit, new patient, level 5; Ultrasound pelvis, transvaginal'  expected=None |
| 253 | `provider` | 02/23/2023 | extracted='Molina Healthcare of NY'  expected='Smith Medical, PC' |
| 253 | `description` | 02/23/2023 | extracted='Strep A test, direct; Carboplatin, 50 mg; Tetanus toxoid (Td), IM'  expected=None |
| 340 | `cpt_codes` | 10/13/2021 | missing=['86592', '93306', '97022', '97530', '99233', '99284']  extra=['72100', '90472', '90935', '99214', 'J1055', 'J9060'] |
| 340 | `total_charges` | 10/13/2021 | extracted=1882.58  expected=1615.5  diff=267.08 |
| 340 | `ins_paid` | 10/13/2021 | extracted=844.46  expected=1000.03  diff=155.57 |
| 340 | `adjustment` | 10/13/2021 | extracted=1038.12  expected=582.78  diff=455.34 |
| 340 | `balance` | 10/13/2021 | extracted=0.0  expected=32.69  diff=32.69 |
| 340 | `description` | 10/13/2021 | extracted='Medroxyprogesterone acetate, 150 mg / Immunization administration, each additional injection / Office/outpatient visit, established patient, level 4 / X-ray spine, lumbosacral, 2-3 views / Hemodialysis procedure, physician / Cisplatin, per 10 mg'  expected=None |

### doc_008

**Count mismatch** — GT: 100, extracted: 11.

**Missing records (100):**
- GT[0] `06/04/2021 - 11/30/2024` — No extracted record found with this treatment_date
- GT[1] `01/25/2021 - 10/20/2024` — No extracted record found with this treatment_date
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

**Extra extracted records (11):**
- `01/23/2023` — Extracted record has no GT counterpart
- `10/22/2021` — Extracted record has no GT counterpart
- `02/04/2023` — Extracted record has no GT counterpart
- `07/10/2023` — Extracted record has no GT counterpart
- `07/15/2021` — Extracted record has no GT counterpart
- `11/30/2024` — Extracted record has no GT counterpart
- `09/26/2023` — Extracted record has no GT counterpart
- `01/06/2024` — Extracted record has no GT counterpart
- `11/13/2022` — Extracted record has no GT counterpart
- `06/04/2021` — Extracted record has no GT counterpart
- `Account Total` — Extracted record has no GT counterpart

### doc_009

**Count mismatch** — GT: 1, extracted: 108.

**Missing records (1):**
- GT[0] `01/01/2017 - 12/31/2024` — No extracted record found with this treatment_date

**Extra extracted records (108):**
- `01/01/2017 - 12/07/2020` — Extracted record has no GT counterpart
- `12/24/2020` — Extracted record has no GT counterpart
- `12/24/2020` — Extracted record has no GT counterpart
- `12/25/2020` — Extracted record has no GT counterpart
- `12/28/2020` — Extracted record has no GT counterpart
- `12/29/2020` — Extracted record has no GT counterpart
- `01/03/2021` — Extracted record has no GT counterpart
- `02/04/2021` — Extracted record has no GT counterpart
- `02/05/2021` — Extracted record has no GT counterpart
- `02/06/2021` — Extracted record has no GT counterpart
- `02/07/2021` — Extracted record has no GT counterpart
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
- `12/10/2024` — Extracted record has no GT counterpart
- `12/11/2024` — Extracted record has no GT counterpart
- `12/11/2024` — Extracted record has no GT counterpart
- `12/12/2024` — Extracted record has no GT counterpart
- `12/12/2024` — Extracted record has no GT counterpart
- `12/12/2024` — Extracted record has no GT counterpart
- `12/12/2024` — Extracted record has no GT counterpart
- `12/13/2024` — Extracted record has no GT counterpart
- `12/13/2024` — Extracted record has no GT counterpart
- `12/13/2024` — Extracted record has no GT counterpart
- `12/14/2024` — Extracted record has no GT counterpart
- `12/14/2024` — Extracted record has no GT counterpart
- `12/16/2024` — Extracted record has no GT counterpart
- `12/17/2024` — Extracted record has no GT counterpart
- `12/18/2024` — Extracted record has no GT counterpart
- `12/19/2024` — Extracted record has no GT counterpart
- `12/19/2024` — Extracted record has no GT counterpart
- `12/20/2024` — Extracted record has no GT counterpart
- `12/20/2024` — Extracted record has no GT counterpart
- `12/21/2024` — Extracted record has no GT counterpart
- `12/21/2024` — Extracted record has no GT counterpart
- `12/21/2024` — Extracted record has no GT counterpart
- `12/22/2024` — Extracted record has no GT counterpart
- `12/23/2024` — Extracted record has no GT counterpart
- `12/23/2024` — Extracted record has no GT counterpart
- `12/23/2024` — Extracted record has no GT counterpart
- `12/25/2024` — Extracted record has no GT counterpart
- `12/30/2024` — Extracted record has no GT counterpart
- `12/30/2024` — Extracted record has no GT counterpart
- `12/30/2024` — Extracted record has no GT counterpart
- `12/30/2024` — Extracted record has no GT counterpart
- `12/31/2024` — Extracted record has no GT counterpart
- `12/31/2024` — Extracted record has no GT counterpart

### doc_010

**Count mismatch** — GT: 1, extracted: 2.

**Missing records (1):**
- GT[0] `01/01/2017 - 12/29/2024` — No extracted record found with this treatment_date

**Extra extracted records (2):**
- `01/01/2017 - 12/31/2017` — Extracted record has no GT counterpart
- `04/24/2021 - 08/24/2024` — Extracted record has no GT counterpart

### doc_011

**Count mismatch** — GT: 150, extracted: 14.

**Missing records (137):**
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
- GT[82] `06/20/2020 - 06/27/2020` — No extracted record found with this treatment_date
- GT[83] `01/12/2017 - 01/13/2017` — No extracted record found with this treatment_date
- GT[84] `06/17/2020 - 06/21/2020` — No extracted record found with this treatment_date
- GT[85] `02/24/2019 - 02/28/2019` — No extracted record found with this treatment_date
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

**Field mismatches (27):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `description` | 01/25/2023 - 01/26/2023 | extracted='Inpatient Episode: Total knee arthroplasty'  expected='Total knee arthroplasty' |
| 1 | `description` | 09/13/2023 - 09/19/2023 | extracted='Inpatient Episode: Pulmonary embolism'  expected='Pulmonary embolism' |
| 2 | `description` | 02/27/2023 - 03/05/2023 | extracted='Inpatient Episode: Cellulitis of lower leg'  expected='Cellulitis of lower leg' |
| 3 | `description` | 07/21/2017 - 07/28/2017 | extracted='Inpatient Episode: Total knee arthroplasty'  expected='Total knee arthroplasty' |
| 4 | `description` | 04/18/2023 - 04/22/2023 | extracted='Inpatient Episode: Heart failure, unspecified'  expected='Heart failure, unspecified' |
| 5 | `description` | 08/08/2022 - 08/11/2022 | extracted='Inpatient Episode: Urinary tract infection'  expected='Urinary tract infection' |
| 75 | `provider` | 02/26/2021 - 03/05/2021 | extracted='Unknown (Hospital name not provided)'  expected='South Patrickmouth General Hospital' |
| 75 | `insurers` | 02/26/2021 - 03/05/2021 | missing=['medicaid'] |
| 75 | `description` | 02/26/2021 - 03/05/2021 | extracted='Inpatient Episode: Alcohol withdrawal syndrome'  expected='Alcohol withdrawal syndrome' |
| 76 | `provider` | 06/11/2021 - 06/17/2021 | extracted='Unknown (Hospital name not provided)'  expected='South Patrickmouth General Hospital' |
| 76 | `insurers` | 06/11/2021 - 06/17/2021 | missing=['medicaid'] |
| 76 | `description` | 06/11/2021 - 06/17/2021 | extracted='Inpatient Episode: Pulmonary embolism'  expected='Pulmonary embolism' |
| 77 | `provider` | 04/05/2018 - 04/07/2018 | extracted='Unknown (Hospital name not provided)'  expected='South Patrickmouth General Hospital' |
| 77 | `insurers` | 04/05/2018 - 04/07/2018 | missing=['medicaid'] |
| 77 | `description` | 04/05/2018 - 04/07/2018 | extracted='Inpatient Episode: Schizophrenia, acute exacerbation'  expected='Schizophrenia, acute exacerbation' |
| 78 | `provider` | 12/17/2018 - 12/23/2018 | extracted='Unknown (Hospital name not provided)'  expected='South Patrickmouth General Hospital' |
| 78 | `insurers` | 12/17/2018 - 12/23/2018 | missing=['medicaid'] |
| 78 | `description` | 12/17/2018 - 12/23/2018 | extracted='Inpatient Episode: Stroke, ischemic'  expected='Stroke, ischemic' |
| 79 | `provider` | 03/12/2019 - 03/15/2019 | extracted='Unknown (Hospital name not provided)'  expected='South Patrickmouth General Hospital' |
| 79 | `insurers` | 03/12/2019 - 03/15/2019 | missing=['medicaid'] |
| 79 | `description` | 03/12/2019 - 03/15/2019 | extracted='Inpatient Episode: Pneumonia, unspecified organism'  expected='Pneumonia, unspecified organism' |
| 80 | `provider` | 06/18/2020 - 06/20/2020 | extracted='Unknown (Hospital name not provided)'  expected='South Patrickmouth General Hospital' |
| 80 | `insurers` | 06/18/2020 - 06/20/2020 | missing=['medicaid'] |
| 80 | `description` | 06/18/2020 - 06/20/2020 | extracted='Inpatient Episode: Acute pancreatitis'  expected='Acute pancreatitis' |
| 81 | `provider` | 03/13/2024 - 03/15/2024 | extracted='Unknown (Hospital name not provided)'  expected='South Patrickmouth General Hospital' |
| 81 | `insurers` | 03/13/2024 - 03/15/2024 | missing=['medicaid'] |
| 81 | `description` | 03/13/2024 - 03/15/2024 | extracted='Inpatient Episode: Cellulitis of lower leg'  expected='Cellulitis of lower leg' |

### doc_012

**Count mismatch** — GT: 120, extracted: 28.

**Missing records (95):**
- GT[1] `01/31/2017 - 03/02/2017` — No extracted record found with this treatment_date
- GT[2] `03/03/2017 - 04/04/2017` — No extracted record found with this treatment_date
- GT[3] `04/05/2017 - 04/07/2017` — No extracted record found with this treatment_date
- GT[5] `05/04/2017 - 06/05/2017` — No extracted record found with this treatment_date
- GT[6] `06/06/2017 - 07/04/2017` — No extracted record found with this treatment_date
- GT[7] `07/05/2017 - 07/13/2017` — No extracted record found with this treatment_date
- GT[9] `08/13/2017 - 09/08/2017` — No extracted record found with this treatment_date
- GT[10] `09/09/2017 - 10/09/2017` — No extracted record found with this treatment_date
- GT[11] `10/10/2017 - 10/18/2017` — No extracted record found with this treatment_date
- GT[13] `11/16/2017 - 12/11/2017` — No extracted record found with this treatment_date
- GT[14] `12/12/2017 - 01/12/2018` — No extracted record found with this treatment_date
- GT[15] `01/13/2018 - 01/23/2018` — No extracted record found with this treatment_date
- GT[17] `02/23/2018 - 03/23/2018` — No extracted record found with this treatment_date
- GT[18] `03/24/2018 - 04/25/2018` — No extracted record found with this treatment_date
- GT[19] `04/26/2018 - 04/30/2018` — No extracted record found with this treatment_date
- GT[21] `05/31/2018 - 07/01/2018` — No extracted record found with this treatment_date
- GT[22] `07/02/2018 - 08/01/2018` — No extracted record found with this treatment_date
- GT[23] `08/02/2018 - 08/05/2018` — No extracted record found with this treatment_date
- GT[25] `09/02/2018 - 09/29/2018` — No extracted record found with this treatment_date
- GT[26] `09/30/2018 - 10/26/2018` — No extracted record found with this treatment_date
- GT[27] `10/27/2018 - 11/10/2018` — No extracted record found with this treatment_date
- GT[29] `12/08/2018 - 01/07/2019` — No extracted record found with this treatment_date
- GT[30] `01/08/2019 - 02/02/2019` — No extracted record found with this treatment_date
- GT[31] `02/03/2019 - 02/15/2019` — No extracted record found with this treatment_date
- GT[33] `03/15/2019 - 04/11/2019` — No extracted record found with this treatment_date
- GT[34] `04/12/2019 - 05/08/2019` — No extracted record found with this treatment_date
- GT[35] `05/09/2019 - 05/23/2019` — No extracted record found with this treatment_date
- GT[37] `06/20/2019 - 07/16/2019` — No extracted record found with this treatment_date
- GT[38] `07/17/2019 - 08/13/2019` — No extracted record found with this treatment_date
- GT[39] `08/14/2019 - 08/28/2019` — No extracted record found with this treatment_date
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
- GT[57] `10/18/2020 - 11/18/2020` — No extracted record found with this treatment_date
- GT[58] `11/19/2020 - 12/18/2020` — No extracted record found with this treatment_date
- GT[59] `12/19/2020 - 12/25/2020` — No extracted record found with this treatment_date
- GT[61] `01/21/2021 - 02/19/2021` — No extracted record found with this treatment_date
- GT[62] `02/20/2021 - 03/20/2021` — No extracted record found with this treatment_date
- GT[63] `03/21/2021 - 04/01/2021` — No extracted record found with this treatment_date
- GT[64] `04/02/2021 - 05/03/2021` — No extracted record found with this treatment_date
- GT[65] `05/04/2021 - 06/04/2021` — No extracted record found with this treatment_date
- GT[66] `06/05/2021 - 07/04/2021` — No extracted record found with this treatment_date
- GT[69] `08/09/2021 - 09/04/2021` — No extracted record found with this treatment_date
- GT[70] `09/05/2021 - 10/07/2021` — No extracted record found with this treatment_date
- GT[71] `10/08/2021 - 10/12/2021` — No extracted record found with this treatment_date
- GT[73] `11/11/2021 - 12/12/2021` — No extracted record found with this treatment_date
- GT[74] `12/13/2021 - 01/13/2022` — No extracted record found with this treatment_date
- GT[75] `01/14/2022 - 01/17/2022` — No extracted record found with this treatment_date
- GT[76] `01/18/2022 - 02/14/2022` — No extracted record found with this treatment_date
- GT[77] `02/15/2022 - 03/17/2022` — No extracted record found with this treatment_date
- GT[78] `03/18/2022 - 04/12/2022` — No extracted record found with this treatment_date
- GT[80] `04/25/2022 - 05/20/2022` — No extracted record found with this treatment_date
- GT[81] `05/21/2022 - 06/18/2022` — No extracted record found with this treatment_date
- GT[82] `06/19/2022 - 07/14/2022` — No extracted record found with this treatment_date
- GT[84] `07/31/2022 - 08/26/2022` — No extracted record found with this treatment_date
- GT[85] `08/27/2022 - 09/28/2022` — No extracted record found with this treatment_date
- GT[86] `09/29/2022 - 10/26/2022` — No extracted record found with this treatment_date
- GT[87] `10/27/2022 - 11/04/2022` — No extracted record found with this treatment_date
- GT[89] `12/06/2022 - 01/06/2023` — No extracted record found with this treatment_date
- GT[90] `01/07/2023 - 02/02/2023` — No extracted record found with this treatment_date
- GT[91] `02/03/2023 - 02/09/2023` — No extracted record found with this treatment_date
- GT[93] `03/13/2023 - 04/14/2023` — No extracted record found with this treatment_date
- GT[94] `04/15/2023 - 05/14/2023` — No extracted record found with this treatment_date
- GT[95] `05/15/2023 - 05/17/2023` — No extracted record found with this treatment_date
- GT[97] `06/17/2023 - 07/18/2023` — No extracted record found with this treatment_date
- GT[98] `07/19/2023 - 08/19/2023` — No extracted record found with this treatment_date
- GT[99] `08/20/2023 - 08/22/2023` — No extracted record found with this treatment_date
- GT[100] `08/23/2023 - 09/19/2023` — No extracted record found with this treatment_date
- GT[101] `09/20/2023 - 10/15/2023` — No extracted record found with this treatment_date
- GT[102] `10/16/2023 - 11/13/2023` — No extracted record found with this treatment_date
- GT[104] `11/28/2023 - 12/24/2023` — No extracted record found with this treatment_date
- GT[105] `12/25/2023 - 01/25/2024` — No extracted record found with this treatment_date
- GT[106] `01/26/2024 - 02/23/2024` — No extracted record found with this treatment_date
- GT[107] `02/24/2024 - 03/03/2024` — No extracted record found with this treatment_date
- GT[108] `03/04/2024 - 04/05/2024` — No extracted record found with this treatment_date
- GT[109] `04/06/2024 - 05/05/2024` — No extracted record found with this treatment_date
- GT[111] `06/06/2024 - 06/08/2024` — No extracted record found with this treatment_date
- GT[112] `06/09/2024 - 07/04/2024` — No extracted record found with this treatment_date
- GT[114] `08/05/2024 - 09/02/2024` — No extracted record found with this treatment_date
- GT[115] `09/03/2024 - 09/13/2024` — No extracted record found with this treatment_date
- GT[117] `10/15/2024 - 11/14/2024` — No extracted record found with this treatment_date
- GT[118] `11/15/2024 - 12/10/2024` — No extracted record found with this treatment_date
- GT[119] `12/11/2024 - 12/19/2024` — No extracted record found with this treatment_date

**Extra extracted records (3):**
- `06/07/2021 - 07/04/2021` — Extracted record has no GT counterpart
- `09/30/2022 - 10/26/2022` — Extracted record has no GT counterpart
- `12/29/2023 - 02/23/2024` — Extracted record has no GT counterpart

**Field mismatches (53):**

| GT# | Field | Date | Detail |
|---|---|---|---|
| 0 | `cpt_codes` | 01/01/2017 - 01/30/2017 | extra=['36831', '82565', '82728', '83540', '84132', '84295', '85025', '90935', '90940', '99213', 'A4690', 'A4706', 'A4730', 'A4750', 'A4755', 'A4920', 'J0885', 'J2916', 'J3370'] |
| 0 | `description` | 01/01/2017 - 01/30/2017 | extracted='Hemodialysis, office visit, lab tests, injections, supplies'  expected='Dialysis — 10 treatments' |
| 4 | `cpt_codes` | 04/08/2017 - 05/03/2017 | extra=['36821', '36831', '82728', '83036', '84100', '84295', '90937', 'A4690', 'A4706', 'A4750', 'A4802', 'A4920'] |
| 4 | `description` | 04/08/2017 - 05/03/2017 | extracted='Hemodialysis, supplies, blood tests, injections'  expected='Dialysis — 12 treatments' |
| 8 | `cpt_codes` | 07/14/2017 - 08/12/2017 | extra=['36821', '82310', '82565', '82728', '84100', '84132', '84295', '85025', '90935', '90940', '99213', 'A4690', 'A4730', 'A4750', 'A4755', 'A4802', 'A4920', 'J3370'] |
| 8 | `description` | 07/14/2017 - 08/12/2017 | extracted='Hemodialysis, supplies, blood tests, injections'  expected='Dialysis — 9 treatments' |
| 12 | `cpt_codes` | 10/19/2017 - 11/15/2017 | extra=['36831', '82310', '82565', '83540', '84100', '84132', '86000', '90935', '90937', '99213', 'A4690', 'A4706', 'A4730', 'A4750', 'A4755', 'A4802', 'A4860', 'A4920', 'J2916'] |
| 12 | `description` | 10/19/2017 - 11/15/2017 | extracted='Hemodialysis, supplies, blood tests, injections, access management'  expected='Dialysis — 13 treatments' |
| 16 | `cpt_codes` | 01/24/2018 - 02/22/2018 | extra=['82310', '82565', '83540', '84295', '85025', '90935', '90937', '90940', '99213', 'A4706', 'A4750', 'A4802', 'A4920', 'G0491', 'J2916', 'J3370'] |
| 16 | `description` | 01/24/2018 - 02/22/2018 | extracted='Hemodialysis, lab tests, injections, office visit'  expected='Dialysis — 11 treatments' |
| 20 | `cpt_codes` | 05/01/2018 - 05/30/2018 | extra=['36831', '82565', '82728', '83036', '84295', '86000', '90935', '90937', '90940', '93975', 'A4690', 'A4706', 'A4730', 'A4750', 'A4802', 'A4920', 'J2916', 'J3370'] |
| 20 | `description` | 05/01/2018 - 05/30/2018 | extracted='Hemodialysis, supplies, injections, lab and imaging'  expected='Dialysis — 8 treatments' |
| 24 | `cpt_codes` | 08/06/2018 - 09/01/2018 | extra=['82565', '82728', '83036', '83540', '84132', '85025', '90935', '90937', '90940', '99213', 'A4706', 'A4730', 'A4755', 'A4802', 'A4860', 'J0885', 'J2916', 'J3370'] |
| 24 | `description` | 08/06/2018 - 09/01/2018 | extracted='Hemodialysis, supplies, lab, injections'  expected='Dialysis — 11 treatments' |
| 28 | `cpt_codes` | 11/11/2018 - 12/07/2018 | extra=['82310', '83036', '84132', '85025', '90935', '90937', 'A4706', 'A4920', 'J0885', 'J2916', 'J3370'] |
| 28 | `description` | 11/11/2018 - 12/07/2018 | extracted='Hemodialysis, lab, injections'  expected='Dialysis — 8 treatments' |
| 32 | `cpt_codes` | 02/16/2019 - 03/14/2019 | extra=['36821', '82310', '82565', '84100', '86000', '90935', '90937', '90940', '93975', '99213', 'A4690', 'A4706', 'A4730', 'A4750', 'A4755', 'A4802', 'J0885', 'J2916'] |
| 32 | `description` | 02/16/2019 - 03/14/2019 | extracted='Hemodialysis, access, bloodwork, imaging, injections'  expected='Dialysis — 8 treatments' |
| 36 | `cpt_codes` | 05/24/2019 - 06/19/2019 | extra=['36821', '82565', '82728', '83036', '83540', '84295', '85025', '86000', '93975', '99213', 'A4706', 'A4730', 'A4755', 'A4802', 'A4860', 'J0885'] |
| 36 | `description` | 05/24/2019 - 06/19/2019 | extracted='Hemodialysis, access, injections, lab'  expected='Dialysis — 8 treatments' |
| 40 | `cpt_codes` | 08/29/2019 - 09/25/2019 | extra=['36821', '36831', '82310', '82728', '83036', '83540', '84100', '86000', '90937', '99213', 'A4690', 'A4706', 'A4750', 'A4802', 'A4860', 'A4920', 'J0885', 'J2916'] |
| 40 | `description` | 08/29/2019 - 09/25/2019 | extracted='Hemodialysis, access, imaging, lab, injections'  expected='Dialysis — 8 treatments' |
| 56 | `cpt_codes` | 09/20/2020 - 10/17/2020 | extra=['82565', '82728', '84100', '84132', '86000', '90935', '90937', '99213', 'A4706', 'A4730', 'A4750', 'A4860', 'J2916'] |
| 56 | `description` | 09/20/2020 - 10/17/2020 | extracted='Hemodialysis, supplies, testing, injections'  expected='Dialysis — 12 treatments' |
| 60 | `cpt_codes` | 12/26/2020 - 01/20/2021 | extra=['36821', '82310', '82565', '84100', '84132', '86000', '90937', '90940', 'A4690', 'A4706', 'A4730', 'A4802', 'A4920', 'G0491', 'J0885', 'J2916'] |
| 60 | `description` | 12/26/2020 - 01/20/2021 | extracted='Hemodialysis, supplies, injections, office visit, labs'  expected='Dialysis — 12 treatments' |
| 67 | `cpt_codes` | 07/05/2021 - 07/07/2021 | extra=['36831', '82310', '82565', '83540', '84132', '84295', '85025', '86000', '90935', '90937', 'A4750', 'A4755', 'A4920', 'J0885', 'J2916', 'J3370'] |
| 67 | `description` | 07/05/2021 - 07/07/2021 | extracted='Hemodialysis, supplies, lab, injections, access'  expected='Dialysis — 9 treatments' |
| 68 | `cpt_codes` | 07/08/2021 - 08/08/2021 | extra=['36821', '36831', '82310', '82565', '83540', '84132', '84295', '86000', '93975', 'A4706', 'A4750', 'A4755', 'A4920', 'G0491', 'J2916'] |
| 68 | `description` | 07/08/2021 - 08/08/2021 | extracted='Hemodialysis, supplies, lab, imaging, access, injections'  expected='Dialysis — 9 treatments' |
| 72 | `cpt_codes` | 10/13/2021 - 11/10/2021 | extra=['36831', '82565', '82728', '83036', '84295', '85025', '86000', '90935', '90937', '90940', '93975', 'A4730', 'A4750', 'G0491', 'J0885', 'J2916', 'J3370'] |
| 72 | `description` | 10/13/2021 - 11/10/2021 | extracted='Hemodialysis, supplies, imaging, injections, labs'  expected='Dialysis — 12 treatments' |
| 79 | `cpt_codes` | 04/13/2022 - 04/24/2022 | extra=['36821', '82310', '83036', '83540', '85025', '86000', '90937', '90940', '93975', 'A4706', 'A4730', 'A4750', 'A4755', 'A4920', 'G0491', 'J0885', 'J2916', 'J3370'] |
| 79 | `description` | 04/13/2022 - 04/24/2022 | extracted='Hemodialysis, imaging, supply, labs, injections'  expected='Dialysis — 8 treatments' |
| 83 | `cpt_codes` | 07/15/2022 - 07/30/2022 | extra=['83036', '83540', '84132', '90940', '99213', 'A4690', 'A4755', 'A4920', 'G0491', 'J0885', 'J2916', 'J3370'] |
| 83 | `description` | 07/15/2022 - 07/30/2022 | extracted='Hemodialysis, supplies, lab, injections, office visit'  expected='Dialysis — 9 treatments' |
| 88 | `cpt_codes` | 11/05/2022 - 12/05/2022 | extra=['82728', '84295', '86000', '90935', '90937', '90940', 'A4690', 'A4706', 'A4750', 'A4755', 'A4920', 'J2916'] |
| 88 | `description` | 11/05/2022 - 12/05/2022 | extracted='Hemodialysis, supplies, lab, injections, access devices'  expected='Dialysis — 8 treatments' |
| 92 | `cpt_codes` | 02/10/2023 - 03/12/2023 | extra=['84100', '84295', '86000', '90940', '93975', 'A4690', 'A4730', 'A4750', 'A4802', 'A4860', 'A4920', 'J0885', 'J3370'] |
| 92 | `description` | 02/10/2023 - 03/12/2023 | extracted='Hemodialysis, supplies, imaging, lab, injections'  expected='Dialysis — 10 treatments' |
| 96 | `cpt_codes` | 05/18/2023 - 06/16/2023 | extra=['36831', '84100', '84132', '85025', '86000', '90935', '90937', '90940', '93975', '99213', 'A4690', 'A4706', 'A4730', 'A4750', 'A4755', 'A4920', 'G0491', 'J0885', 'J2916', 'J3370'] |
| 96 | `description` | 05/18/2023 - 06/16/2023 | extracted='Hemodialysis, supplies, imaging, injections, lab'  expected='Dialysis — 10 treatments' |
| 103 | `cpt_codes` | 11/14/2023 - 11/27/2023 | extra=['36831', '84100', '84132', '84295', '85025', '86000', '90935', '90937', '99213', 'A4690', 'A4860', 'J0885', 'J3370'] |
| 103 | `description` | 11/14/2023 - 11/27/2023 | extracted='Hemodialysis, supplies, imaging, lab, injections'  expected='Dialysis — 11 treatments' |
| 110 | `cpt_codes` | 05/06/2024 - 06/05/2024 | extra=['36821', '36831', '82310', '82728', '83036', '84100', '84132', '90937', '90940', '99213', 'A4690', 'A4755', 'A4802', 'A4920', 'J3370'] |
| 110 | `adjustment` | 05/06/2024 - 06/05/2024 | extracted=None  expected=1948.12 |
| 110 | `payments` | 05/06/2024 - 06/05/2024 | extracted=0.0  expected=None |
| 110 | `balance` | 05/06/2024 - 06/05/2024 | extracted=None  expected=0.0 |
| 110 | `description` | 05/06/2024 - 06/05/2024 | extracted='Hemodialysis, access, imaging, labs, injections'  expected='Dialysis — 9 treatments' |
| 113 | `cpt_codes` | 07/05/2024 - 08/04/2024 | extra=['36821', '36831', '82565', '82728', '83036', '84100', '85025', '86000', '93975', '99213', 'A4750', 'A4755', 'J0885', 'J3370'] |
| 113 | `description` | 07/05/2024 - 08/04/2024 | extracted='Hemodialysis, imaging, access, supplies, labs'  expected='Dialysis — 10 treatments' |
| 116 | `cpt_codes` | 09/14/2024 - 10/14/2024 | extra=['36821', '82565', '82728', '83036', '83540', '84132', '86000', '90940', '99213', 'A4690', 'A4730', 'A4750', 'A4755', 'A4802', 'A4920', 'G0491', 'J2916'] |
| 116 | `description` | 09/14/2024 - 10/14/2024 | extracted='Hemodialysis, labs, imaging, supplies, injections'  expected='Dialysis — 11 treatments' |

---

_Generated by `scripts/eval_extraction.py`_
