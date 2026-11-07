# Module 2 — Glucose Prediction and Assignment 2

**Lecturer:** Sabina Tomkins  
**Source:** *Week 2 - Glucose Prediction*, 32 slides.

## Key points
1. The Blood Glucose Prediction Challenge uses real-world type 1 diabetes sensor data to forecast blood glucose **30 and 60 minutes ahead**.
2. Repeated glucose measurements form an ordered **time series**, not independent observations.
3. A **sliding window** turns a long series into multiple input–target training examples.
4. The assignment compares pooled, person-specific, and transfer-learning approaches using LSTMs.
5. Data cleaning and clinically meaningful evaluation are as important as model training.

## 1. Forecasting problem (slides 2–5)
The lecture describes **eight weeks of data from 12 people with type 1 diabetes**, with prediction horizons of **30 minutes** and **60 minutes**. Graphs show observed glucose versus a predicted future trajectory that can drop dangerously low.

**Forecasting horizon:** Amount of time between the latest available input and the target prediction (e.g., 30 minutes into the future).

**Clinical significance:** A prediction should help anticipate a low or high glucose event, not merely minimize numerical error.

## 2. Representing sensor readings as data (slides 6–9)
The slides lay out sequential values `r1, r2, ..., r30`, with **5 minutes between readings**.

**Time series:** Observations indexed in temporal order. **Feature matrix X:** Input histories used for prediction. **Target vector y:** True future measurements to predict.

The order matters: recent glucose trajectory can be informative in a way that a shuffled set of readings is not.

## 3. Sliding windows and labeled examples (slides 10–17)
A long timeline is cut into overlapping sequences:

```text
Time:     r1  r2  r3 ... r24  r25  r26 ... r30  r31
Window 1: [r1 ... r24]    -> future target(s)
Window 2:     [r2 ... r25] -> shifted future target(s)
Window 3:         [r3 ... r26] -> shifted future target(s)
```

The actual slide diagram uses **24 prior readings** as input and the subsequent **6 readings (r25–r30)** as the displayed output segment for the first 30-reading span. It then shifts one reading for the next example. The final reading in that segment is at the 30-minute horizon.

**Important distinction:** This example shows a *sequence* of future output readings; the 30-minute endpoint is not the only future observation stored in the depicted `y` block.

## 4. Assignment data layout (slide 18)
For the provided processed dataset:
- An input `x` vector has **24** glucose observations (2 hours at 5-minute intervals).
- An output `y` vector has **12** observations (1 hour at 5-minute intervals).
- Files add a **patient ID column** to each (`x`: 25th column; `y`: 13th column).

**Interpretation:** The 30-minute target corresponds to the sixth future 5-minute reading; the 60-minute target corresponds to the twelfth future reading, assuming the slide's regular sampling convention.

## 5. Assignment 2 roadmap (slides 19–24)
| Part | Task | Core skill |
|---|---|---|
| **2a** | Data manipulation and cleaning | Pandas / real sensor-data quality |
| **2b** | Population LSTM | Fit one model to the whole population |
| **2c** | Person-specific LSTM | Fit a separate model per person |
| **2d** | Transfer learning | Initialize/fine-tune with prior trained knowledge |
| **2e** | Glucose error prediction grid | Interpret clinical consequences of prediction error |

**LSTM (long short-term memory):** A recurrent neural network architecture designed to learn dependencies across a sequence.

## 6. Machine-learning workflow (slides 25–31)
The lecture outlines data collection → cleaning/transformation → splitting → training → evaluation → model selection → communication of results. The stated learning goals include extracting a procedure from a research paper, handling genuine sensor-data problems, comparing personalization with population and pre-trained approaches, using PyTorch for transfer learning, and interpreting a clinical error grid.

**Time-series caution (explanatory):** Adjacent overlapping windows share observations. Avoid evaluating a model on windows whose underlying source observations were also used for training; otherwise leakage may inflate apparent performance. The deck emphasizes dataset splitting but does not prescribe this exact rule in its overview slides.

## Main argument / conclusion
**Blood-glucose prediction turns noisy, high-frequency sensor histories into a clinical time-series forecasting task. The assignment is designed to compare training strategies and interpret errors in terms of patient safety.**

## Study-check questions
1. At 5-minute sampling, how many past readings make two hours of input?
2. How is a training example formed by shifting the window one time step?
3. Which assignment section compares person-specific and pretrained modeling?
