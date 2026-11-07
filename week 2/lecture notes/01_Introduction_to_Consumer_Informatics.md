# Module 2 — Introduction to Consumer Informatics

**Lecture:** Consumer Informatics (Sabina Tomkins)  
**Source:** *Week 2 - Introduction - Consumer Informatics*, 23 slides.

## Key points
1. Consumer informatics uses personal devices—wearables, fitness trackers, and phones—to generate data that can inform health decisions.
2. Real-world data collection is unreliable: sensors may fail, be removed, transmit incompletely, or record at an unsuitable frequency.
3. Data transformation, insufficient individual data, privacy, and transfer from laboratory settings to daily life complicate machine-learning pipelines.
4. Unequal device access means training data can underrepresent certain populations, creating inequitable performance.
5. Pooling across people offers more data and stability; person-specific modeling uses more relevant data but may have greater variance.

## 1. Consumer-generated health information (slides 2–5)
**Consumer informatics:** Here, technology that lets individuals monitor and learn from their own behavior; related labels include *mobile health*, *wearable technology*, and the *quantified self*.

**Pipeline:** fitness trackers/mobile devices → data generation → ML pipeline → decision makers. In consumer informatics, people may bring their own observations into the decision process.

**Example:** A wearable logs activity over a day; an algorithm summarizes patterns for the person or a clinician.

## 2. Data and ML-pipeline challenges (slides 6–8)
- **Collection failures:** missing readings due to sensor outages, non-wear, or failed cloud transmission.
- **Granularity mismatch:** data sampled too coarsely for the prediction target.
- **Transformation:** converting raw time series into usable features or training sequences.
- **Model training:** a single person may contribute too little data; privacy may restrict pooling; lab-trained models may not generalize to real-life behavior.

**Example:** An activity sensor records few readings while the user is charging it. Those gaps are not evidence that the person was inactive.

## 3. Inclusion and health equity (slides 9–12)
The lecture highlights that higher-income people are more likely to have certain wearables and CGMs. It illustrates representation failure with a skin-condition model trained less often on darker skin.

**Selection bias:** The observed device-owner sample differs systematically from the intended patient population. A model with high aggregate accuracy on this sample may perform poorly for excluded groups.

**Implication:** Evaluate who generated the data, who is missing, and whether subgroup outcomes differ.

## 4. Pooling versus personalization (slides 13–20)
| Strategy | Benefit | Risk / trade-off |
|---|---|---|
| **Pooled (population) model** | Uses all available observations; one model is simpler to maintain and more stable | May be biased for a person whose physiology or behavior differs from the pooled population |
| **Personalized model** | Trains on data most relevant to one person | Fewer observations; can change abruptly as new data arrive (higher variance) |

**Bias–variance intuition:** Pooling can stabilize predictions while sacrificing individual fit. Personalization can fit an individual better but become unstable when data are scarce. The slides use these as a conceptual trade-off, not a guarantee for every model.

**Data inclusion decisions:** Some people decline to share information, so pooling may not always be possible; storage and management constraints also matter.

## 5. Recommendations before deployment (slides 21–22)
- Consult stakeholders and domain experts.
- Evaluate performance under different data-inclusion scenarios before deployment, including pooled versus person-specific approaches.
- Consider both predictive quality **and** which people will benefit or be harmed.

## Important terms
- **CGM:** Continuous glucose monitor; a sensor that repeatedly measures glucose.
- **Time-series granularity:** Spacing between recorded observations.
- **Pooling:** Training one model on data from multiple individuals.
- **Personalization:** Fitting a model specifically to an individual.
- **Distribution shift:** A change in the data distribution between training and deployment environments.

## Main argument / conclusion
**Consumer devices make individualized health analytics possible, but missing data, privacy constraints, unequal access, and the pooling–personalization trade-off must be evaluated before a health ML model is deployed.**

## Study-check questions
1. Why can a wearable dataset misrepresent the patient population?
2. What do you gain and risk when switching from pooled to individualized models?
3. Why is device non-wear a data-quality issue rather than automatically a behavioral signal?
