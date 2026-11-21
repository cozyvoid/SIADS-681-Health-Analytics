# Module 4 (Week 4): Forecasting COVID Cases

## Lecture at a Glance

This lecture introduces the CDC COVID-19 forecasting ensemble and uses it to motivate the Week 4 modeling assignment. The key idea is that outbreak forecasting benefits from combining many different models and data sources rather than depending on a single forecasting method.

The lecture also connects ensemble forecasting to **LSTM models**, **quantile outputs**, **regional-vs-aggregated models**, and the standard machine-learning pipeline.

---

## Key Points

1. From roughly April 2020 through March 2022, the CDC used an **ensemble of forecast models** to predict COVID-19 cases.
2. New data were released weekly, and participating teams generated forecasts for the following four weeks.
3. Roughly 45 teams contributed forecasts.
4. Forecasts came from very different model families, including deep learning, epidemiological, statistical, and agent-based models.
5. Ensembles combine individual forecasts into one aggregate forecast, often using weights.
6. A CU Boulder model used an **LSTM architecture** and produced **quantiles instead of only point estimates**.
7. The Week 4 assignment asks students to implement and evaluate this type of forecasting workflow.
8. One major modeling question is the trade-off between **county-specific** and **state-level/aggregated** models.

---

# 1. CDC COVID Forecasting

The lecture describes the CDC COVID forecasting system used from approximately:

**April 2020 → March 2022**

The workflow was organized around a weekly forecasting cycle.

### Weekly process

- Every Saturday, new data were released from Johns Hopkins University.
- Forecasting teams uploaded predictions by Monday.
- Forecasts covered the next **four weeks**.
- Around **45 teams** contributed.
- Individual forecasts were combined into an aggregate forecast.

This structure allowed the CDC to draw from many independent approaches.

---

# 2. The Ensemble Concept

The diagram on **pages 7–8** shows the core ensemble idea.

A common input dataset \(X\) is sent to multiple forecasting models, such as:

- **ARIMA**
- **SEIR**
- **LSTM**

Each model produces a forecast:

- \(\hat{y}_a\)
- \(\hat{y}_s\)
- \(\hat{y}_l\)

The ensemble applies weights such as:

- \(W_a\)
- \(W_s\)
- \(W_l\)

to combine them into an aggregate forecast:

\[
\hat{y}_e
\]

### Why use an ensemble?

Different models make different assumptions and fail in different ways.

Combining them can reduce dependence on any single model’s weaknesses.

---

# 3. Diversity of Forecasting Teams

Participants included:

### Universities

- University of Michigan
- University of Colorado Boulder
- UCLA

### Organizations

- Federal Reserve Bank of San Francisco
- Los Alamos National Laboratory

### Individuals

The lecture also lists independent forecasters.

### Main lesson

Forecasting was not limited to one discipline or institution. A large public-health forecasting effort can benefit from methodological diversity.

---

# 4. Range of Models and Data

## Model families

The lecture lists:

- Deep learning
- Epidemiological models
- Statistical forecasting models
- Agent-based models

## Data sources

Possible inputs included:

- Mobility data
- Social networks
- Demographics
- Policy decisions

### Why this matters

COVID transmission is driven by many interacting factors. Different models may capture different parts of the process.

For example:

- Epidemiological models may encode disease-transmission assumptions.
- Statistical models may detect time-series structure.
- Deep-learning models may learn nonlinear temporal patterns.
- Agent-based models may simulate individual interactions.

---

# 5. CU Boulder LSTM Model

The figure on **page 12** shows an LSTM-based architecture.

### Architecture

**Input:** multivariate time series

Then:

- LSTM layer — 64 units
- LSTM layer — 64 units
- Dense layer — 32 neurons
- Prediction output \(\hat{y}\)

This architecture is designed to model temporal dependencies in multivariate data.

---

# 6. Quantile Outputs Instead of Only Point Estimates

The CU Boulder approach also:

- Built its own ensemble
- Output **quantiles**
- Did not rely only on a single point estimate

This is important because public-health decision makers often need to understand uncertainty.

A point forecast might say:

> 500 cases are expected.

A quantile-based forecast can instead describe a range of plausible outcomes, such as:

- Lower quantile
- Median
- Upper quantile

This provides information about forecast uncertainty.

---

# 7. Week 4 Assignment Structure

The lecture directly connects the concepts to Assignment 4.

## 4a — Correlation analysis

Inspect correlations between:

- Diabetes
- COVID-19 cases

This explores relationships between a chronic-health factor and infectious-disease outcomes.

## 4b — Implement the CU Boulder method

Students reproduce a method from the research literature.

This requires translating a published modeling approach into code.

## 4c — Compare county-specific vs. state-level models

This evaluates a key geographic modeling trade-off.

### County-specific model

Potential advantage:

- More locally tailored

Potential disadvantage:

- Less data per model
- More noise

### State-level model

Potential advantage:

- More pooled data
- Potentially more stable estimates

Potential disadvantage:

- Can hide local variation

## 4d — Bonus: ensemble improvement

Attempt to improve predictions using an ensemble.

---

# 8. Machine-Learning Pipeline

The lecture connects the assignment to a general ML workflow.

1. **Data collection** — already completed
2. **Data cleaning / transformation** — already completed
3. **Dataset splitting** — already completed
4. **Model training** — student task
5. **Model evaluation** — student task
6. **Repeat steps for model selection** — student task
7. **Present findings / visualization** — student task

### Key lesson

Modeling is iterative.

A strong workflow does not stop after fitting one model. It compares alternatives and evaluates trade-offs.

---

# 9. Intended Learning Experience

The lecture lists four major goals.

Students should learn to:

1. Analyze relationships between socioeconomic factors and illness.
2. Implement a **quantile prediction loss function**.
3. Extract and implement a model from a research paper.
4. Evaluate trade-offs between regional and aggregated forecasting models.

These goals combine:

- Public-health reasoning
- Machine learning
- Scientific reading
- Model implementation
- Model evaluation

---

# Important Definitions

| Term | Meaning |
|---|---|
| **Forecast** | A prediction about a future value, often in a time series. |
| **Ensemble** | A method that combines predictions from multiple models into one final prediction. |
| **Weight** | A coefficient controlling how much an individual model contributes to the ensemble. |
| **ARIMA** | A statistical time-series forecasting model based on autoregression, differencing, and moving averages. |
| **SEIR** | An epidemiological compartment model representing Susceptible, Exposed, Infectious, and Recovered populations. |
| **LSTM** | Long Short-Term Memory network; a recurrent neural network architecture designed for sequential data. |
| **Multivariate time series** | A time series containing multiple variables measured over time. |
| **Point estimate** | One predicted value. |
| **Quantile forecast** | A forecast for a specified percentile of the outcome distribution. |
| **Aggregate model** | A model using data pooled across a larger region or group. |

---

# Main Argument / Conclusion

The lecture argues that COVID forecasting is a multi-model, multi-data-source problem in which uncertainty and geographic scale matter.

Rather than searching for a single universally best model, effective public-health forecasting can combine complementary approaches and evaluate how model structure, uncertainty estimates, and geographic aggregation affect performance.

The Week 4 assignment is designed to make students reproduce this process by implementing a research-based model, adding quantile prediction, and comparing local versus aggregated forecasting strategies.

---

# Quick Review

- CDC used an ensemble of many COVID forecasting models.
- Weekly data fed forecasts for the next four weeks.
- Around 45 teams contributed.
- Models included deep learning, epidemiological, statistical, and agent-based approaches.
- Ensembles combine forecasts with weights.
- CU Boulder used LSTMs and quantile outputs.
- Quantile forecasts express uncertainty better than a single point estimate.
- Assignment 4 compares county-specific and state-level modeling strategies.
