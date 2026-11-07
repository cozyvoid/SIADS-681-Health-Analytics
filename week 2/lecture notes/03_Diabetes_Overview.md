# Module 2 — Diabetes: Clinical Background and Data

**Lecturer:** Neha Bhomia  
**Source:** *Week 2 - Diabetes*, 32 slides.

## Key points
1. Diabetes is a chronic disorder of glucose regulation involving insufficient insulin production and/or impaired insulin action.
2. It produces a large global and US burden, including hospital use, complications, mortality, and financial costs.
3. Major forms include type 1, type 2, prediabetes, gestational diabetes, and less common types.
4. Economic and social inequality shape diabetes risk and the feasibility of ongoing self-management.
5. Clinical management generates multiple data types, including glucose tests, A1C, EHR notes, and CGM observations.

## 1. What diabetes is (slides 2–3)
**Glucose:** Sugar used by cells for energy. **Insulin:** Hormone that helps regulate glucose availability and uptake. Diabetes arises when the pancreas does not make sufficient insulin and/or the body cannot use it effectively.

## 2. Scale and costs (slides 4–10)
Historical statistics **as presented in the lecture**:
- Worldwide in 2021: approximately **537 million adults** living with diabetes; projections of **643 million in 2030** and **783 million in 2045**.
- About three-quarters of adults with diabetes were in low- and middle-income countries; the lecture reports that nearly half were undiagnosed.
- United States: **37.3 million** people with diabetes (11.3% of the population); **8.5 million** undiagnosed.
- US 2017 estimates: **$327 billion** total cost of diagnosed diabetes, including **$237 billion** in direct medical costs and **$90 billion** in reduced productivity.

**Note:** These are the slides' year-specific figures, **not updated 2026 estimates**.

## 3. Different diabetes types (slides 11–12)
| Type | Main description in slides |
|---|---|
| **Type 1** | Little or no insulin production; frequently identified in children or adolescents, but can also present in adults |
| **Type 2** | Body becomes resistant to insulin; constitutes most diabetes cases |
| **Prediabetes** | Glucose above normal but below the threshold for diabetes |
| **Gestational** | Elevated blood glucose during pregnancy, with future type 2 risk |
| **Other** | Monogenic, cystic-fibrosis-related, and drug/chemical-induced diabetes |

## 4. Inequality and complications (slides 13–18)
The slides report higher diabetes prevalence in lower-income groups and emphasize how constrained resources affect chronic-condition management. They discuss **multimorbidity** (multiple coexisting conditions) and socioeconomic influences on diabetes risk.

Complications to recognize:
- **Cardiovascular disease:** Heart and blood-vessel injury.
- **Neuropathy:** Nerve damage, potentially affecting sensation in the feet.
- **Nephropathy:** Kidney damage.
- **Retinopathy:** Damage to the retina/vision.
- **Foot complications:** Related to impaired sensation, circulation, and healing.

## 5. Daily management challenges (slides 19–21)
Self-management may be limited by insufficient education, support, financial resources, or barriers to healthcare. Clinical challenges include controlling glucose, blood pressure and lipids; education; medication/lifestyle adherence; timely insulin when needed; and better chronic-care delivery.

## 6. Sources of diabetes data (slides 22–24)
- **Lab and diagnostic tests:** A1C, random glucose, fasting glucose, oral glucose tolerance.
- **Fingerstick glucose:** Individual blood glucose readings.
- **CGM:** Repeated sensor measurements across time.
- **EHR:** Illness history, clinician notes, monitoring information, and exams.

**Analytics implication:** These sources differ in temporal resolution and what they measure. A1C summarizes a longer period; a glucose reading describes a particular time.

## 7. Diagnostic test thresholds (slides 25–29)
| Test | Normal | Prediabetes | Diabetes |
|---|---|---|---|
| A1C | <5.7% | 5.7–6.4% | ≥6.5% |
| Fasting plasma glucose | ≤99 mg/dL | 100–125 mg/dL | ≥126 mg/dL |
| 2-hour oral glucose tolerance test | <140 mg/dL | 140–199 mg/dL | ≥200 mg/dL |

The slides also show **random glucose ≥200 mg/dL** in the diabetes row. Clinical interpretation of a random result depends on symptoms/context; see the companion Type 2 lecture for the explicitly stated symptomatic criterion.

## 8. Treatment pillars (slides 30–31)
Healthy eating; physical activity; blood-glucose monitoring; insulin where indicated; and oral or other medications.

## Main argument / conclusion
**Diabetes illustrates why health analytics must integrate physiology, patient self-management, diverse clinical data, and social context rather than relying on a single laboratory measurement.**

## Study-check questions
1. Which readings describe immediate glucose, and which summarize glucose over time?
2. Why do unequal resources affect both outcomes and dataset representativeness?
3. What is the difference between type 1 and type 2 diabetes in the lecture?
