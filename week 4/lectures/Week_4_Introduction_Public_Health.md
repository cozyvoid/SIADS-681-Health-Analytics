# Module 4 (Week 4): Introduction — Public Health

## Lecture at a Glance

This lecture frames public health analytics as a pipeline connecting **population-level data generation**, **machine learning/statistical analysis**, and **decision makers**. The central message is that model choice should be driven by the kind of information a public-health decision maker actually needs—not simply by which model produces the best single point estimate.

---

## Key Points

1. Public health analytics operates at the **population level**, not only at the individual-patient level.
2. Public-health data are generated through surveys, reporting systems, hospitals, laboratories, and other institutions, then collated by agencies.
3. Machine-learning pipelines can be used to **estimate**, **discover**, and **forecast** population-level health outcomes.
4. Public-health ML pipelines face challenges involving **data collection**, **coordination**, **privacy**, **variable inclusion/exclusion**, **causal interpretation**, and **uncertainty**.
5. Public policy can either reduce or worsen inequity, so data inclusion and modeling decisions have real downstream consequences.
6. There is an important trade-off between **probabilistic models**, which represent a range of plausible outcomes, and models optimized for a **single best estimate**.
7. The recommended workflow is:
   - First determine what information the decision maker needs.
   - Then select the highest-performing model that provides that type of information.

---

# 1. Public Health as a Data-to-Decision Pipeline

The lecture presents public health as a three-stage process:

**Data Generation → ML Pipeline → Decision Makers**

### Data generation

Public-health data may come from:

- Surveys
- Hospitals and health-care providers
- Laboratories
- Local, state, and national reporting systems
- Agencies and institutions that aggregate data across geographic regions

The goal is often to produce **population-level statistics**, such as COVID-19 case counts.

### Machine-learning pipeline

The ML/analytics stage can be used to:

- **Estimate** current quantities
- **Discover** patterns or relationships
- **Forecast** future outcomes

### Decision makers

Outputs may be used by:

- Policymakers
- CDC
- NIH
- FDA
- Public-health service organizations

The important implication is that the value of a model depends partly on whether its output is useful for a real policy or operational decision.

---

# 2. Population-Level Data and COVID-19 Case Counts

The lecture uses COVID-19 case counts as a concrete example of population-level surveillance.

The diagram on **page 8** shows the case-surveillance reporting chain:

1. Hospitals, health-care providers, and laboratories report cases.
2. Reports flow to local, state, territorial, or tribal public-health authorities.
3. Public-health authorities notify the CDC.
4. Internationally important public-health events may also connect with the World Health Organization (WHO).

A key feature is that different stages of the reporting system may handle **identified** versus **de-identified** data.

### Why this matters

A case count may look like a simple number, but it is the product of a multi-organization reporting system. Any weakness in collection or coordination can affect the final data used for modeling.

---

# 3. Challenges to Public-Health ML Pipelines

## Data collection issues

The slides highlight three major concerns:

### Burden and inequity

Collecting data may be burdensome, and that burden may not fall equally across groups. If some populations are harder to reach or less likely to be represented, the resulting dataset can become systematically biased.

### Coordination

Public-health data often cross:

- Agencies
- Organizations
- Geographic jurisdictions

Coordination failures can create inconsistent definitions, reporting lags, incomplete coverage, or incompatible datasets.

### Privacy

Public-health systems must balance the usefulness of detailed health data against privacy risks.

---

## Data transformation issues

The lecture emphasizes that **including or excluding variables can have different implications and consequences**.

Feature selection is therefore not only a technical decision. It may affect:

- Who is represented
- What disparities are visible
- Which relationships a model can detect
- Whether a model reinforces or obscures inequity

---

## Model training issues

Two concerns are emphasized:

### Causal interpretation

A model may identify a predictive association without establishing that one factor causes another.

**Important distinction:**

- **Prediction:** What outcome is likely?
- **Causation:** What would happen if we intervened on a factor?

These are not interchangeable.

### Uncertainty

Public-health decisions often require an understanding of uncertainty, not merely a single forecast.

The slides also note that **coarse data** can be difficult for machine-learning models. Aggregated data may hide meaningful within-group variation.

---

# 4. Data Inclusion and Equity

The lecture states that public policy has major potential to **alleviate or create inequity**.

Examples include policy affecting:

- Access to insurance
- Access to food
- Access to clean drinking water

This connects data science to public-health ethics: decisions about data, models, and policies can influence the distribution of health resources and risks.

### Main idea

A technically accurate model can still produce poor public-health outcomes if the data or policy context is inequitable.

---

# 5. Modeling Decisions: Point Estimates vs. Uncertainty

The diagram on **page 15** contrasts:

- **Estimates of uncertainty**
- **Point estimates**

A point estimate gives one predicted value.

A probabilistic or uncertainty-aware model gives a **range or distribution of plausible values**.

## Probabilistic models

The lecture describes probabilistic models as useful when the goal is to estimate a **likely range of values** rather than one single number.

This can be valuable when decision makers need to plan for:

- Best-case outcomes
- Worst-case outcomes
- Thresholds
- Risk levels

## ML models focused on a point estimate

Many ML approaches are especially good at finding the best single estimate for a quantity of interest or label.

This is useful when a decision requires a precise predicted value, but it may be less informative when uncertainty is central to the decision.

---

# 6. Choosing the Right Model for the Decision

The lecture concludes with a practical two-step strategy:

1. **Find out what kind of information the decision maker needs to make a good decision.**
2. **Find a model that provides that information with the highest performance.**

This reverses a common mistake in modeling.

Instead of asking:

> Which model performs best?

Ask:

> Which model provides the type of information needed for the decision, and among those models, which performs best?

---

# Important Definitions

| Term | Meaning |
|---|---|
| **Population-level statistics** | Measures describing health patterns across groups or populations rather than one individual. |
| **Point estimate** | A single predicted value for an outcome. |
| **Estimate of uncertainty** | A range or distribution describing multiple plausible values for an outcome. |
| **Data transformation** | Processing or modifying raw data before modeling, including variable selection and aggregation. |
| **Causal interpretation** | Interpreting a relationship as cause-and-effect rather than merely predictive association. |
| **Public-health surveillance** | Ongoing collection and analysis of health data for monitoring and decision-making. |

---

# Main Argument / Conclusion

The lecture argues that public-health analytics is not simply about building the most accurate predictive model. Models sit inside a broader system of data collection, institutional coordination, equity considerations, and policy decisions.

The most appropriate model is therefore the model that provides the **right information for the decision maker**, while also accounting for the limitations and consequences of the data and modeling process.

---

# Quick Review

- Public health focuses heavily on **population-level** health.
- Data move through complex reporting systems before reaching analysts.
- ML can estimate, discover, and forecast.
- Public-health data pipelines face equity, privacy, coordination, and uncertainty challenges.
- Feature inclusion/exclusion can have policy consequences.
- Prediction is not the same as causal inference.
- Point predictions and uncertainty estimates answer different decision-making needs.
- Choose the model based on the decision maker’s information needs first, then performance.
