# Explainable Prediction of Medical Codes from Clinical Text
**Authors:** James Mullenbach, Sarah Wiegreffe, Jon Duke, Jimeng Sun, Jacob Eisenstein (NAACL 2018)  
**Type:** Clinical NLP methods and evaluation | **Course:** SIADS 681 Health Analytics

## 5 key points
1. **Assigning ICD codes from clinical notes is a large-scale multi-label classification problem.** One discharge summary may warrant many diagnosis and procedure codes.
2. **CAML combines a convolutional neural network with attention for each possible code.** Different labels can focus on different snippets in the same note.
3. **Per-label attention substantially improved coding accuracy** over the compared CNN, Bi-GRU, and logistic regression baselines on the full MIMIC-III label set.
4. **Attention provides candidate explanations** by highlighting relevant phrases; a physician judged many extracted snippets informative, but this is not proof of full clinical correctness.
5. **Rare codes remain challenging.** Description-regularized CAML (DR-CAML) uses code descriptions to share information, but it did not outperform ordinary CAML on most full-label MIMIC-III metrics.

## 1. Clinical problem and definitions
- **Clinical notes/discharge summaries:** Free-text documentation of a patient's hospital stay.
- **ICD codes:** Standardized labels for diagnoses and procedures, used for billing, reporting, and research.
- **Multi-label classification:** Each document can have multiple correct labels simultaneously; unlike multiclass classification, labels are not mutually exclusive.
- **Long-tail labels:** Many codes occur rarely, making their prediction and evaluation difficult.
- **MIMIC-II / MIMIC-III:** De-identified ICU datasets used for model development and benchmarking.

**Example:** One discharge summary may support codes for pneumonia, heart failure, and a procedure. The text evidence for each code may appear in entirely different paragraphs.

## 2. CAML architecture (Figure 1, p. 3)
1. **Word embeddings:** Convert note tokens into numeric vectors (pretrained word2vec in the paper).
2. **Convolutional layer (CNN):** Extracts local patterns of adjacent words (**n-grams**) throughout the document.
3. **Per-label attention:** For each ICD code, assign higher weights to the text locations most relevant to that code, instead of applying the same max-pooling representation to every label.
4. **Code-specific representation:** Compute a weighted combination of local CNN features for that code.
5. **Sigmoid output:** Estimate a separate probability for each code; train using **binary cross-entropy** across labels.

**Plain-English intuition:** The model reads a long note once to find local text features, then effectively asks a different question for each code: *Which parts of this note are most relevant to this diagnosis or procedure?*

### DR-CAML extension
**Description-Regularized CAML** also embeds official text descriptions of ICD codes and penalizes prediction parameters that stray too far from corresponding description embeddings. Intended benefit: improve learning for rarely seen codes through semantic similarity. **Important result:** It is not universally better than CAML.

## 3. Dataset and evaluation design
- **MIMIC-III full-label:** 47,724 training discharge summaries; roughly 8,900 unique ICD-9 diagnosis/procedure labels. The paper reports 8,922 total labels in its summary table.
- **Patient-level split:** No patient appears in both training and test sets, reducing patient leakage.
- **Additional comparisons:** Top 50 frequent MIMIC-III codes and the MIMIC-II full-label setting.
- **Baselines:** Bag-of-words logistic regression, conventional CNN, bidirectional GRU (Bi-GRU).
- **Preprocessing:** Lowercase/token normalization, vocabulary handling, pretrained word embeddings, and truncation at 2,500 tokens.

## 4. Metrics: know what each measures
| Metric | Meaning | Why it matters |
|---|---|---|
| **Micro-F1** | Aggregate true/false positives/negatives across all note–code pairs, then compute F1 | Reflects overall performance; frequent labels exert greater influence |
| **Macro-F1** | Compute F1 per code, then average codes equally | Exposes poor performance on rare codes |
| **ROC-AUC** | Measures ranking discrimination across classification thresholds | Useful complement to threshold-based F1 |
| **Precision@8 (P@8)** | Fraction of the eight highest-scoring proposed codes that are correct | Relevant when a human reviews a short suggestion list |

**Example:** P@8 = 0.71 means approximately 5.7 of the top eight suggestions are correct on average; it does **not** mean 71% of all required codes were recovered.

## 5. Main quantitative results (Table 4, p. 6)
**MIMIC-III full-label evaluation:**

| Model | Micro-F1 | Macro-F1 | P@8 |
|---|---:|---:|---:|
| Logistic regression | 0.272 | 0.011 | 0.542 |
| CNN | 0.419 | 0.042 | 0.581 |
| Bi-GRU | 0.417 | 0.038 | 0.585 |
| **CAML** | **0.539** | **0.088** | **0.709** |
| DR-CAML | 0.529 | 0.086 | 0.690 |

**Interpretation:** Code-specific attention improved both overall coding and top-ranked suggestions compared with the tested baselines. Yet **macro-F1 remained very low**, emphasizing the persistent rare-label problem.

**Secondary experiments:** On the MIMIC-III 50-code task, DR-CAML achieved micro-F1 **0.633**, while the CNN baseline had the best P@5 (**0.620**). On MIMIC-II full-label data, DR-CAML achieved micro-F1 **0.457** versus CAML **0.442** (Tables 5–6). This shows model rankings depend on dataset and metric.

## 6. Interpretability study (Table 1, p. 2; Table 7, p. 8)
A physician evaluated snippets proposed as evidence for **100 sampled predicted codes**, comparing CAML against other extraction approaches. The methods' selected counts were:

| Method | Highly informative | Informative |
|---|---:|---:|
| CAML | 46 | 22 |
| Code-description similarity | 48 | 20 |
| Logistic regression | 41 | 18 |
| CNN | 36 | 13 |

The categories are reported separately as in the paper. CAML produced many clinically informative snippets and more combined informative/highly-informative judgments than the CNN and logistic regression methods. However, **code-description similarity had slightly more “highly informative” selections (48 vs. 46)**; do not overstate CAML's superiority on every interpretability measure.

**Example from Table 1:** For a code concerning a bronchial foreign body, a snippet about bronchoscopy revealing a large mucus plug can help a reviewer understand why the code was suggested.

### Interpretability caveats
- A highlighted phrase can be **plausible** without proving that the model reasons correctly in every case.
- One physician and 100 sampled predictions provide limited evidence of explanation quality.
- A suggested code can be incorrect even if the attention-highlighted snippet looks relevant.
- This is decision support, not evidence that automated coding can safely replace professional review.

## 7. Healthcare analytics implications
- **Clinical NLP:** Unstructured notes contain actionable information not easily represented by structured fields alone.
- **Human-in-the-loop coding:** Ranked suggestions with supporting snippets can focus coder review time.
- **Evaluation:** Report both micro and macro metrics so common-code success does not hide rare-code failures.
- **Deployment:** Evaluate note truncation, documentation quality, patient-population differences, and code-system changes before use.

## Main conclusion
**CAML shows that label-specific attention can improve large-scale ICD code prediction while surfacing potentially useful text evidence.** Its strongest contribution is combining predictive performance with a practical form of explanation, while rare labels and explanation reliability remain unresolved.

## Study questions
1. Why is ICD prediction multi-label rather than multiclass?
2. How does per-label attention differ from max pooling?
3. Why might P@8 be more useful than recall for a coding suggestion interface?
4. Why can high micro-F1 coexist with low macro-F1?
5. What does the physician evaluation establish—and what does it not establish?

**Source:** Mullenbach et al., *Explainable Prediction of Medical Codes from Clinical Text*, uploaded PDF (2018), especially Figure 1 and Tables 1, 4–7.
