# KDH @ ECAI 2020 — BGLP Challenge Papers
**Reading scope:** **Only** the section titled “BGLP Challenge Papers,” not the rest of the workshop introduction.  
**Course:** SIADS 681 — Health Analytics | Module 2

## Five key points
1. The challenge compared forecasting systems on the updated **OhioT1DM** dataset, evaluating blood glucose **30 and 60 minutes ahead**.
2. Of 16 accepted system papers, **eight conformed to the challenge rules**, allowing comparison on identical test points across six participants.
3. Ranking summed **four lower-is-better errors**: 30-minute RMSE, 30-minute MAE, 60-minute RMSE, and 60-minute MAE.
4. **LSTMs and GRUs** were dominant, but the submissions also included CNN/RNN hybrids, GANs, genetic programming, forests, latent-variable models, and PLS-based models.
5. The winning system used modified **N-BEATS** residual forecasting, and most systems were personalized; the notable exception was Bevan & Coenen's **non-personalized** LSTM.

## 1. Goal of the challenge
Use a shared, realistic dataset and standardized test observations to compare the effectiveness of approaches for blood glucose level prediction (BGLP).

## 2. Standardized metrics and ranking
Each qualifying system received four metric values:

`Overall score = RMSE_30 + MAE_30 + RMSE_60 + MAE_60`

**Definitions:**
- **RMSE:** Root Mean Squared Error; large errors are penalized especially strongly.
- **MAE:** Mean Absolute Error; mean absolute size of a prediction miss.
- **Prediction horizon:** Time between the last available observation and the forecast target.

**Lower scores ranked better.** Eight qualifying models were evaluated using the exact same test points for six contributors, making the ranking internally comparable.

## 3. Selected official leaderboard results
| System (paper reference) | 30-min RMSE | 30-min MAE | 60-min RMSE | 60-min MAE | Overall |
|---|---:|---:|---:|---:|---:|
| Rubin-Falcone et al. [29] | 18.22 | 12.83 | 31.66 | 23.60 | **86.31** |
| Hameed & Kleinberg [11] | 19.21 | 13.08 | 31.77 | 23.09 | 87.15 |
| Zhu et al. [32] | 18.34 | 13.37 | 32.21 | 24.20 | 88.12 |
| Yang et al. [31] | 19.05 | 13.50 | 32.03 | 23.83 | 88.41 |
| Bevan & Coenen [2] | 18.23 | 14.37 | 31.10 | 25.75 | 89.45 |

*These values reproduce the workshop overview's ranking table. The article on the non-personalized model provides additional experiment-specific MAE results; for the official challenge ranking, use the overview table above.*

## 4. Architecture families represented
- **LSTM / GRU recurrent models:** Frequent choices for time-series dependencies.
- **CRNN:** Combines convolutional feature extraction and recurrence.
- **Fully connected neural networks:** Another recurring approach.
- **GAN:** A generator forecasts glucose, while a discriminator assesses generated against observed glucose.
- **N-BEATS / residual blocks:** Gradual reconstruction and forecasting.
- **Non-neural approaches:** Genetic programming/symbolic regression, random forests, latent-variable models, Partial Least Squares Regression and stacking.

## 5. Why the winning method matters
Rubin-Falcone et al. improved an N-BEATS-inspired approach by:
1. Replacing fully connected blocks with LSTMs.
2. Adding intermediate supervision/loss terms.
3. Including sparse context variables, such as meals and bolus insulin.
4. Backcasting only the main target variable, glucose.

This connects directly to the separate *Deep Residual Time-Series Forecasting* assigned reading.

## 6. Interpretability and decision support
- **SHAP (SHapley Additive exPlanations):** Used in another LSTM submission to estimate input-feature contributions to predictions.
- **What-if evaluations:** Explored forecast consequences under assumed future insulin decisions, moving from pure prediction toward decision support.

## 7. Personalized vs. non-personalized modeling
- **Most systems:** Trained or fine-tuned a different model per individual.
- **Bevan & Coenen:** Used a shared LSTM for all patients, testing population-level generalization.

**Exam connection:** A good forecasting architecture is only one dimension of comparison. Other decisions include feature selection, missing-data treatment, transfer/pretraining, personalization, and clinically meaningful evaluation.

## Main argument / conclusion
The section documents a controlled benchmark in which temporal deep-learning models were especially common and a modified residual-LSTM system ranked first. It also shows substantial methodological diversity and highlights the contrast between **patient-specific prediction** and **population-level prediction**.

**Source:** Uploaded *KDH @ ECAI 2020* overview, **“BGLP Challenge Papers” section only** (page 1; includes leaderboard and continuation of the section in the right column).
