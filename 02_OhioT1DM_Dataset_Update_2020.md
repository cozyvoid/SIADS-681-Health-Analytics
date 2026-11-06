# The OhioT1DM Dataset for Blood Glucose Level Prediction: Update 2020
**Authors:** Cindy Marling & Razvan Bunescu  
**Course:** SIADS 681 — Health Analytics | Module 2

## Five key points
1. The **OhioT1DM dataset** provides real-patient, multimodal information for developing and comparing blood-glucose forecasting models.
2. It contains approximately **eight weeks of data for 12 people with Type 1 diabetes**: six in the 2018 release and six more in the 2020 update.
3. The dataset includes five-minute CGM readings, insulin dosing, meals, self-reported life events, and wearable-sensor signals.
4. Sampling frequencies differ across modalities, creating challenges involving alignment, missingness, and preprocessing.
5. The dataset includes separate training and test files, a visualization tool, and privacy restrictions intended to support credible, responsible research.

## 1. Motivation and use cases
Forecasting glucose before a dangerous rise or fall may support proactive diabetes management, decision support, and artificial-pancreas systems. The authors assembled a real-patient dataset because many earlier studies were limited by a lack of rich, shareable clinical data.

## 2. Participants and cohorts
- **12 anonymized data contributors**, all with Type 1 diabetes.
- **Eight weeks** of monitoring per person.
- All used insulin pump therapy and continuous glucose monitors (CGMs).
- **2018 cohort:** six patients, Basis Peak wearable bands.
- **2020 cohort:** six additional patients, Empatica Embrace wearable bands.

## 3. Data types and definitions
| Variable | Meaning / example |
|---|---|
| **CGM glucose** | Interstitial-glucose measurements approximately every 5 minutes |
| **Finger-stick glucose** | Periodic self-monitored glucose readings |
| **Basal insulin** | Insulin infused continuously at a specified rate |
| **Temporary basal** | Temporary adjustment or suspension of usual basal delivery |
| **Bolus insulin** | A dose generally associated with meals or correction of high glucose |
| **Meals** | Self-reported times, meal types, and estimated carbohydrates |
| **Life events** | Exercise, sleep, work, stress, illness, hypoglycemic events |
| **Wearable signals** | Heart rate, galvanic skin response, skin/air temperature, steps, acceleration and sleep detection, depending on cohort |

**Galvanic skin response (GSR):** A measure of skin conductance/electrodermal activity.

## 4. Dataset organization and evaluation
- Each patient has **one XML training/development file and one XML testing file**: 24 XML files in total.
- Different cohorts have somewhat different sensor fields and recording intervals.
- For the 2020 challenge, the first hour of each test file is **excluded from scoring** to avoid evaluation points too close in time to training data.
- **Time-series caution:** Avoid using future observations when constructing predictors for earlier time points.

## 5. Preprocessing challenges
- **Asynchronous observations:** Meals and bolus doses occur as events; CGM is approximately regular.
- **Missing data:** Sensor readings and life-event entries may be absent.
- **Different sample rates:** Some wearable values are aggregated every minute, others every five minutes.
- **De-identification:** Dates were shifted by a random amount for each person while preserving clock time and weekday; therefore, true month/season/holiday effects cannot be reliably analyzed.

**Example:** For a predictor using measurements every five minutes, a meal at 12:03 and a glucose reading at 12:05 need a carefully defined method of alignment. An absent meal record should not automatically be interpreted as a certain absence of food intake.

## 6. Privacy and dataset access
- Data contributors gave consent for de-identified research sharing.
- The researchers used the HIPAA Safe Harbor de-identification method.
- A **Data Use Agreement (DUA)** is required for research access.

## 7. OhioT1DM Viewer
The paper describes a graphical tool that displays glucose, insulin, life events, and wearable measurements together. Researchers can inspect periods of unexpectedly poor model performance—possibly spotting a reported illness, stressor, or missed meal entry.

## Main argument / conclusion
The OhioT1DM dataset gives researchers a shared, clinically meaningful benchmark for forecasting blood glucose from real-world multimodal time series. Its value depends on consistent evaluation, thoughtful preprocessing, and protection of participant privacy.

**Source:** *The OhioT1DM Dataset for Blood Glucose Level Prediction: Update 2020* (uploaded reading), pp. 1–4.
