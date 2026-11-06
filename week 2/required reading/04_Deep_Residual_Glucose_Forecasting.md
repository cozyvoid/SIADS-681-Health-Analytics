# Deep Residual Time-Series Forecasting: Application to Blood Glucose Prediction
**Authors:** Harry Rubin-Falcone, Ian Fox & Jenna Wiens  
**Course:** SIADS 681 — Health Analytics | Module 2

## Five key points
1. The authors adapt **N-BEATS**, a residual time-series forecasting architecture, to blood-glucose prediction.
2. They replace fully connected network blocks with **bidirectional LSTMs**, add context features, and supervise intermediate block outputs with extra losses.
3. Pretraining on the 2018 OhioT1DM and Tidepool datasets followed by fine-tuning improves final results.
4. The proposed model reaches approximately **RMSE 18.22 / MAE 12.83** at 30 minutes and **RMSE 31.66 / MAE 23.60** at 60 minutes.
5. Accuracy is worse during the onset of dangerous glucose events than it is overall; the paper therefore also evaluates **Clarke Error Grid** clinical risk.

## 1. Problem and baseline
The challenge is to forecast glucose 30 or 60 minutes ahead from recent measurements and relevant context. The baseline is based on **N-BEATS**, which learns through several successive residual blocks.

## 2. Residual forecasting: backcasts and forecasts
Each block produces:
- **Backcast (`b_i`):** Reconstructs some of the historical signal.
- **Forecast (`f_i`):** Predicts some of the future signal.

The remaining history passed onward is:

`x_(i+1) = x_i - b_i`

The final forecast is a sum of block forecasts:

`ŷ = Σ_i f_i`

**Intuition:** One block explains part of the pattern, and the next concentrates on what remains unexplained.

## 3. Architectural modifications
### A. Bidirectional LSTM blocks
Replace N-BEATS fully connected blocks with recurrent blocks so the network better reflects time ordering. Mean 30-minute RMSE improves from **21.2 → 20.1**.

### B. Additional variables
Relevant inputs include CGM, finger-stick glucose, bolus insulin, carbohydrate data, time of day, and missingness indicators. Only glucose is residual-backcast; sparse meal/insulin events remain contextual inputs.

With the LSTM structure plus auxiliary inputs, 30-minute RMSE improves from approximately **20.1 → 18.94**.

### C. Auxiliary loss functions
Extra supervision encourages useful intermediate representations:
- **Reconstruction loss:** Backcasts should explain past input accurately.
- **Per-block forecast loss:** Running forecasts should improve through the blocks.
- **Magnitude loss:** Discourages trivial, negligible backcast outputs.

These added losses helped only slightly on the 2020 data.

### D. Pretraining
The authors pretrained on larger source data—2018 OhioT1DM plus approximately 100 Tidepool participants—then trained a global 2020 model and fine-tuned patient-specific models.

## 4. Ablation study: which change helped?
An **ablation study** examines how performance changes when components are introduced or removed.

| Model version | Mean 30-min RMSE (mg/dL) |
|---|---:|
| Baseline N-BEATS | 21.2 |
| + LSTM blocks | 20.1 |
| + added variables | 18.94 |
| + auxiliary losses | 18.87 |
| + pretraining | **18.2** |

**Takeaway:** Input features are not independently useful across architectures: contextual variables benefited the LSTM block structure much more than the original fully connected baseline.

## 5. Study data and missingness
The 2020 OhioT1DM cohort contributed approximately 10,000 training and 2,500 test samples per person. Approximately 15% of CGM time steps were missing; the model used a missingness indicator and excluded missing target values from loss and evaluation calculations.

## 6. Event-based vs. overall evaluation
- **Overall 30-minute RMSE:** ~**18.2**.
- **30-minute RMSE at onset of hypo-/hyperglycemic events:** ~**27.9**.
- Errors were particularly difficult for hyperglycemic event windows.

The paper defines event transitions from a starting euglycemic value of **70–180 mg/dL** into hypoglycemia (**<70**) or hyperglycemia (**>180**).

**Why it matters:** Models can look accurate averaged over all points while still missing difficult, clinically important transitions.

## 7. Clarke Error Grid
A **Clarke Error Grid** evaluates potential clinical consequences of glucose prediction errors rather than measuring numeric error alone.

Reported outcomes:
- **~90% in region A**: close to reference glucose.
- **~9% in region B**: numerically less accurate but unlikely to trigger inappropriate treatment.
- **99% in regions A or B** combined.
- No points in the opposite-treatment **region E**.

These results are encouraging, but they do not eliminate the elevated errors around event onset.

## Main argument / conclusion
A residual forecasting architecture can be improved by capturing temporal structure, adding contextual signals, training intermediate blocks, and pretraining on related populations. However, **clinical validation needs more than average RMSE**; event-based accuracy and treatment consequences are key to judging practical value.

**Source:** *Deep Residual Time-Series Forecasting: Application to Blood Glucose Prediction* (uploaded reading), pp. 1–5.
