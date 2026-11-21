# Module 4 (Week 4): Quantile Prediction

## Lecture at a Glance

This lecture explains how to predict **quantiles** rather than only a single expected value. The motivating example is COVID-19 forecasting, where public-health decisions may depend on high-confidence upper or lower bounds rather than on the average forecast.

The lecture introduces percentiles, deciles, quantile-specific loss, and implementation of a custom quantile loss function in PyTorch.

---

## Key Points

1. Public-health decisions often need a **range of plausible outcomes**, not only a point prediction.
2. A percentile identifies a value below which approximately a specified fraction of observations fall.
3. Quantile prediction can be used to estimate lower and upper bounds for future outcomes.
4. Decile prediction divides possible outcomes into ten regions using nine cut points.
5. Different quantiles require different penalties for overprediction versus underprediction.
6. Quantile regression uses an asymmetric loss function, often called **quantile loss** or **pinball loss**.
7. In PyTorch, quantile prediction can be implemented by defining a custom loss function and using it as the training criterion.

---

# 1. Motivation: Predicting COVID-19 Cases

A single prediction might say:

> Next week there will be 300 cases.

But public-health decisions may require more than one number.

The slide on **page 3** illustrates a range between:

- A **best-case** case count
- A **worst-case** case count

The purpose of quantile prediction is to describe such uncertainty more directly.

---

# 2. Why Prediction Intervals Matter

Suppose a decision maker says:

> I can only loosen mask mandates if I have high confidence that cases will be less than 500 next week.

A point estimate of 300 is not enough.

The decision maker wants an upper bound \(X_{90}\) such that about 90% of outcomes fall below it.

Similarly, another decision might depend on whether cases are likely to remain high. That could require a lower bound \(X_{10}\).

### Decision-oriented interpretation

- **Upper quantile:** helps answer “How bad could things plausibly get?”
- **Lower quantile:** helps answer “How low could things plausibly fall?”

---

# 3. Percentiles

Given a dataset of size \(n\), for a number \(p\) between 0 and 1:

> The \((100p)\)th sample percentile is the observation such that approximately \(np\) observations are less than that value.

## Example: 90th percentile

Let:

\[
p = 0.9
\]

Then \(X_{90}\) is the value where approximately **90% of observations are below \(X_{90}\)**.

## Example: 10th percentile

Let:

\[
p = 0.1
\]

Then \(X_{10}\) is the value where approximately **10% of observations are below \(X_{10}\)**.

Equivalently, about 90% are above it.

---

# 4. Quantiles and Deciles

The lecture next extends percentile logic to predictive modeling.

Suppose potential predictions are:

\[
\{y_i \mid i = 1,\ldots,n\}
\]

To divide these values into **10 buckets**, we need **9 deciles**.

These are:

- \(d_1\): about 10% of values are below it
- \(d_2\): about 20% are below it
- \(d_3\): about 30% are below it
- ...
- \(d_9\): about 90% are below it

### Why nine deciles?

Ten buckets require nine internal boundaries.

---

# 5. Predicting Multiple Quantiles

The lecture proposes:

1. Create multiple models.
2. Have each model predict a different decile.
3. Use a specialized loss function that depends on the quantile being predicted.

Conceptually, each model is learning a different part of the predictive distribution.

For example:

- One model predicts the 10th percentile.
- One predicts the 50th percentile.
- One predicts the 90th percentile.

Together, they provide a richer description of uncertainty than one point estimate.

---

# 6. Quantile Loss / Pinball Loss

The core idea is that underprediction and overprediction should not always be penalized equally.

For a quantile \(p\), the lecture defines the error:

\[
e = y_i - \hat{y}_i
\]

Then the loss for a single prediction is:

\[
\text{loss} = \max\left((p-1)e,\; pe\right)
\]

The average loss is computed across all datapoints.

This is a standard quantile-regression objective.

---

# 7. Why the Loss Is Asymmetric

For ordinary squared error, positive and negative errors are penalized symmetrically.

Quantile prediction is different.

Suppose the goal is the **90th percentile**:

\[
p = 0.9
\]

The loss gives a larger penalty to predictions that are too low than to predictions that are too high.

That makes sense because the model is trying to locate a value with roughly 90% of observations below it.

For the **10th percentile**:

\[
p = 0.1
\]

the direction of the asymmetry reverses.

### Main intuition

The value of \(p\) determines which side of the prediction error is penalized more strongly.

This pushes the fitted model toward the desired quantile.

---

# 8. Quantile Optimization

The lecture shows the estimated decile as the value \(q\) that minimizes an asymmetric objective.

Conceptually:

- Observations below the candidate quantile receive one weight.
- Observations above the candidate quantile receive another.
- The weights depend on \(p\).

The result is not the mean of the data. It is the value corresponding to the desired portion of the distribution.

---

# 9. Implementing Quantile Loss in PyTorch

Ordinary PyTorch training often looks like:

```python
loss = criterion(outputs, y_train_tensors)
loss.backward()
```

The lecture explains that quantile prediction can use the same training structure, but `criterion` is replaced with a **custom quantile loss function**.

Conceptual pseudocode:

```python
def quantile_loss(pred, y, p):
    e = y - pred
    return mean(max((p - 1) * e, p * e))
```

The model can then be trained for a specific quantile.

### Important implementation idea

The model architecture does not necessarily need to change.

The key change can be the **loss function**, because the loss determines what type of estimate the network learns.

---

# Important Definitions

| Term | Meaning |
|---|---|
| **Percentile** | A value below which a specified percentage of observations fall. |
| **Quantile** | A generalized cut point dividing a probability distribution into regions. |
| **Decile** | One of nine cut points dividing data into ten equal-probability groups. |
| **Prediction interval** | A range intended to contain a specified proportion of future outcomes. |
| **Point estimate** | A single predicted value. |
| **Quantile loss / pinball loss** | An asymmetric loss used to estimate a specified quantile. |
| **\(p\)** | The target quantile level, such as 0.1, 0.5, or 0.9. |
| **Residual / error** | Difference between the observed and predicted value. |

---

# Example

Suppose a health department wants to estimate next week’s COVID-19 case count.

Three models produce:

- 10th percentile: 220 cases
- 50th percentile: 310 cases
- 90th percentile: 480 cases

Interpretation:

- Roughly 10% of outcomes are expected below 220.
- The median forecast is around 310.
- Roughly 90% of outcomes are expected below 480.

A policymaker deciding whether a hospital-capacity threshold of 500 cases is likely to be exceeded may care much more about the **90th percentile** than the median.

---

# Main Argument / Conclusion

The lecture argues that in many public-health settings, the most useful prediction is not a single number but a description of uncertainty.

Quantile prediction solves this by directly estimating different parts of the outcome distribution. The method uses an asymmetric loss function so that the model learns the desired percentile.

The practical takeaway is that **changing the loss function changes the statistical quantity a neural network learns to predict**.

---

# Quick Review

- Percentiles tell us what fraction of observations fall below a value.
- \(X_{90}\): about 90% fall below it.
- \(X_{10}\): about 10% fall below it.
- Nine deciles divide outcomes into ten buckets.
- Quantile models predict different positions in the outcome distribution.
- Quantile loss is asymmetric.
- \(p\) controls the asymmetry.
- A custom quantile-loss function can be used directly as the PyTorch training criterion.
