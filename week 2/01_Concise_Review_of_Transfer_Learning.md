# A Concise Review of Transfer Learning
**Authors:** Farahani, Pourshojae, Rasheed & Arabnia  
**Course:** SIADS 681 — Health Analytics | Module 2

## Five key points
1. **Transfer learning (TL)** improves a target model by reusing relevant knowledge from a related source task or domain, especially when labeled target data are scarce.
2. Unlike conventional ML, transfer learning allows source and target feature spaces, tasks, or probability distributions to differ.
3. By label availability and task relationship, the paper distinguishes **inductive**, **transductive**, and **unsupervised** transfer learning.
4. It also distinguishes **homogeneous** transfer (same feature and label spaces but different distributions) from **heterogeneous** transfer (different feature and/or label spaces).
5. Four principal strategies are **instance-based, feature-based, parameter-based, and relational-based** transfer; the appropriate choice depends on how the domains differ.

## 1. Motivation: why transfer learning?
Traditional supervised ML often assumes that training and test observations have the same feature representation and distribution. In real applications, this assumption may fail, and collecting enough labeled data for a new target population may be expensive. Transfer learning reuses related source knowledge instead of starting entirely from scratch.

**Healthcare example (illustrative):** Learn common glucose dynamics from an existing group of patients, then apply or adapt that model to a new patient with limited data.

## 2. Important definitions
- **Source domain/task:** The dataset/problem supplying existing knowledge.
- **Target domain/task:** The dataset/problem whose performance we want to improve.
- **Domain:** `D = {X, P(X)}`; `X` is the feature space and `P(X)` the marginal feature distribution.
- **Task:** `T = {Y, f(.)}`; `Y` is the output/label space and `f` is a prediction function (often represented as `P(Y|X)`).
- **Transfer learning:** Uses knowledge from the source domain and task to improve target prediction when source and target domains or tasks are not identical.
- **Domain adaptation:** A subset of TL in which the prediction task is shared across different domains.

## 3. What can differ across domains?
- **Feature-space difference:** Source and target measure or represent features differently.
- **Marginal distribution shift:** `P_S(X) != P_T(X)` (for example, daytime vs. nighttime street images).
- **Conditional distribution shift:** The feature-to-label relationship differs: `P_S(Y|X) != P_T(Y|X)` (for example, a word having different sentiment in different contexts).
- **Label-space difference:** Source and target predict different categories or outcomes.

## 4. Main categories of transfer learning
### By labeled-data availability
- **Inductive TL:** Labeled target examples are available, and source and target tasks differ.
- **Transductive TL:** Same task, different domains; labeled source data are available, but target labels generally are not.
- **Unsupervised TL:** Neither source nor target has labeled data.

### By source–target representation
- **Homogeneous TL:** Same feature and label spaces; distributions may differ. The goal is often to align distributions.
- **Heterogeneous TL:** Feature spaces and/or label spaces differ; data must be mapped between representations.

## 5. Four transfer mechanisms
1. **Instance-based:** Reweight source observations so more target-relevant examples have greater influence. Example technique: Kernel Mean Matching (KMM).
2. **Feature-based:** Transform or align source and target into useful common representations. Examples: Transfer Component Analysis (TCA), Feature Augmentation Method (FAM), Joint Distribution Adaptation (JDA).
3. **Parameter-based:** Reuse parameters/weights learned from source tasks in a target model; pretrained-model fine-tuning is an intuitive example.
4. **Relational-based:** Transfer patterns or relationships between observations/concepts rather than only raw features or weights.

**Distribution-alignment measures mentioned:** Maximum Mean Discrepancy (MMD), Kullback–Leibler divergence (KL), and CORAL.

## 6. Related approaches
- **Semi-supervised learning:** Uses labeled and unlabeled observations, typically under a common-domain assumption.
- **Multi-view learning:** Combines complementary representations of the same underlying subject (for example, text and images).
- **Multi-task learning:** Trains related tasks together to help all of them; TL prioritizes the target task.

## Main argument / conclusion
Transfer learning helps overcome a lack of target labels and differences between datasets by transferring related knowledge. The key decision is identifying **how** source and target differ, then choosing a strategy that transfers relevant information without introducing misleading source patterns.

## Course connection
The glucose-forecasting papers use population data, pretraining, and patient-specific fine-tuning—concrete examples of the ideas described in this review.

**Source:** *A Concise Review of Transfer Learning* (uploaded reading), pp. 1–7.
