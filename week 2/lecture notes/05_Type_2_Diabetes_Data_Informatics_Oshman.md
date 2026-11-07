# Module 2 — Type 2 Diabetes: A Data and Informatics Approach

**Lecturer:** Lauren Oshman, MD, MPH  
**Source:** *Week 2 - Type 2 Diabetes: A Data and Informatics Approach*, 36 slides.

## Key points
1. Type 2 diabetes involves impaired glucose regulation, often including insulin resistance; diagnosis and management rely on symptoms, A1C, and glucose measurements.
2. Diabetes care pursues both glycemic control and reduction of cardiovascular, kidney, eye, nerve, and foot complications.
3. Individualized A1C treatment goals are not the same as the threshold used to diagnose diabetes.
4. Diabetes care produces structured and unstructured information spanning lab results, clinical notes, CGM readings, exams, and questionnaires.
5. Informatics can support quality measurement and equitable intervention, but must handle inconsistent definitions, patient attribution, and disparate data types.

## 1. Goals, language, and initial case (slides 2–6)
The lecture emphasizes **person-first language**: prefer 'person with diabetes' over defining someone as 'a diabetic.'

**Case CK:** A 35-year-old woman with fatigue, thirst, and increased urination; BMI 35. Initial labs include **A1C 11.0%**, **fasting glucose 232 mg/dL**, and **post-meal glucose 490 mg/dL**. The lecturer uses this to illustrate a type 2 diagnosis.

## 2. Diabetes physiology and burden (slides 7–10)
The pancreas is central to insulin/glucose regulation. The lecture contrasts different forms of diabetes and lists symptoms such as thirst, frequent urination, hunger, unintended weight loss, fatigue, vision changes, numbness, infections—or no symptoms.

Its population and cost figures are **historical lecture estimates**, not necessarily current surveillance numbers.

## 3. Measuring and diagnosing diabetes (slides 11–15)
**Measurement approaches:**
- **Glucometer:** Point-in-time blood glucose.
- **A1C/HbA1c:** Approximately three-month average exposure to glucose.
- **CGM:** A wearable with repeated glucose measurements and possible low-glucose alerts.

**Diagnostic thresholds presented:**
| Measure | Diabetes threshold |
|---|---|
| A1C | ≥6.5% |
| Fasting plasma glucose (FPG) | ≥126 mg/dL |
| 2-hour plasma glucose after 75-g oral glucose tolerance test | ≥200 mg/dL |
| Random plasma glucose | ≥200 mg/dL **with classic hyperglycemia symptoms or hyperglycemic crisis** |

A1C interpretation in slides: **normal <5.7%**, **prediabetes 5.7–6.4%**, **diabetes ≥6.5%**.

**CGM/AGP (ambulatory glucose profile):** Summarizes sensor data and *time in range* (percentage of time in a glucose target interval); slide 15 gives an example report showing 78% time in the displayed target range. It is an example, not a universal patient's result.

## 4. Treatment goals versus diagnostic cutoffs (slides 16–20)
The lecture presents differing historical recommendations: many nonpregnant adults may target **A1C <7%** (ADA slides), while less stringent targets may be appropriate for severe hypoglycemia, comorbidities, complications, or limited life expectancy. Other organizations recommend somewhat different ranges.

**Distinction:** A1C **≥6.5%** may support diagnosis, while the *treatment target* is individualized to avoid excessive treatment burden and harm.

Approaches include education, medical nutrition therapy, physical activity, medications, and follow-up. Drug classes listed: metformin, DPP-4 inhibitors, GLP-1 receptor agonists, insulin, SGLT2 inhibitors, sulfonylureas, and thiazolidinediones.

## 5. Monitoring complications and team-based care (slides 21–25)
Monitor cardiovascular risk, blood pressure, cholesterol, depression, retinal health, foot/nerve health, and kidney function; consider immunizations.

**Team:** Primary care, dietitian, diabetes educator, podiatry, endocrinology, nephrology, ophthalmology, and the patient/family. CK returns every 3–6 months; visits track symptoms, lifestyle, adherence, complications, and A1C.

## 6. Understanding clinical documentation (slides 26–30)
The multi-slide **progress note** is a useful informatics example:
- **Chief complaint + HPI:** Why the patient is visiting and history of current symptoms/management.
- **Exam:** Blood pressure, weight, and foot examination.
- **Labs:** A1C, kidney function, urine albumin, lipids.
- **A/P (assessment and plan):** Interpretation and next steps.

CK's follow-up note shows **A1C 8%** after an initial **11%**: improved but not at the target set in the scenario. The treatment plan adds another medication, while continuing surveillance for complications.

**Key analytic issue:** Important facts can appear in both coded measurements and free-text notes; neither representation is guaranteed to be complete alone.

## 7. Disparities, data sources, and quality measurement (slides 31–35)
The lecture links unequal diabetes burden to structural racism, social determinants of health, neighborhood conditions, food/activity access, and healthcare coverage. It lists data sources: progress notes, patient questionnaires/flowsheets, vitals, diagnosis codes, CGM, laboratory and point-of-care tests, and consultant reports.

**HEDIS/NCQA measures shown for 2022** (adults 18–75 with diabetes): A1C control **<8%**, poor control **>9%**, blood pressure **<140/90**, and retinal-eye-exam completion. These are lecture-era reporting examples, not asserted as current 2026 specifications.

**Key unresolved data questions posed by lecture:**
- Who counts as having diabetes: diagnostic code, problem list, or lab criterion?
- Which clinician is accountable for a patient?
- How can CGM be integrated with A1C?
- How do we identify inequity and target services appropriately?

## Important terms
- **HbA1c:** Glycated hemoglobin; proxy for longer-term glucose exposure.
- **FPG:** Fasting plasma glucose.
- **CGM:** Continuous glucose monitoring.
- **AGP:** Ambulatory glucose profile.
- **HEDIS:** Healthcare Effectiveness Data and Information Set.
- **NCQA:** National Committee for Quality Assurance.
- **PCP:** Primary care provider.
- **ASCVD:** Atherosclerotic cardiovascular disease.

## Main argument / conclusion
**Effective type 2 diabetes informatics must connect clinically meaningful measurements, longitudinal care, quality-improvement metrics, and equity while acknowledging fragmented data sources and individualized goals.**

## Study-check questions
1. What is the difference between an A1C diagnostic threshold and a target for ongoing treatment?
2. What information is in the narrative progress note that may not be captured by A1C alone?
3. Why can multiple reasonable definitions of a 'diabetes patient' yield different quality-report denominators?
