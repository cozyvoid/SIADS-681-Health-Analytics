# Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges
**Authors:** Cynthia Rudin, Chaofan Chen, Zhi Chen, Haiyang Huang, Lesia Semenova, Chudi Zhong (2021)  
**Type:** Survey / research agenda | **Course:** SIADS 681 Health Analytics

## 5 key points
1. **Prefer inherently interpretable models for high-stakes decisions when feasible.** Understanding how a model actually works is different from attaching a post-hoc explanation to a black box.
2. **Accuracy and interpretability are not necessarily opposites.** A constrained, understandable model can sometimes perform comparably to a complex black box; the tradeoff must be tested rather than assumed.
3. **Interpretability depends on the task and users.** A physician may find a short point score or intelligible risk curve useful; a researcher may need examples, domain constraints, or transparent mechanisms.
4. **Interpretability supports debugging, trust, and oversight.** Models can exploit spurious shortcuts, change behavior under distribution shift, or embed harmful biases without obvious warning.
5. **Ten research challenges remain.** The paper maps concrete directions for developing accurate, transparent models across tabular data, images, science, and sequential decision-making.

## 1. Core argument and fundamental principles
- **Interpretable model:** Its prediction mechanism is constrained to be understandable in its application domain (e.g., a small decision tree, point score, or additive risk curve).
- **Black-box model:** Its internal decision process is too complicated or inaccessible for meaningful inspection.
- **Post-hoc explanation:** An approximation or visualization describing a black-box prediction; it may not faithfully reflect the actual decision logic.
- **Domain-specific constraints (Principle 1):** Interpretability is not one universal mathematical property; define what a relevant human can understand and use.
- **Principle 2:** Interpretability is not automatically the same as causality, and does not by itself establish fairness or other desirable properties.
- **Principle 3:** Do not assume an accuracy–interpretability tradeoff without empirical evidence.
- **Principle 4:** Evaluate model performance and interpretability as part of the full data science workflow, not as an afterthought.
- **Principle 5:** In high-stakes settings, favor interpretable models over black-box explanations when possible.

**Healthcare example:** A small clinical risk score showing how age, symptoms, and lab values contribute to a decision can be checked for errors and challenged by clinicians. A visually persuasive explanation for a complex model does not guarantee that the complex model truly uses those factors.

## 2. Ten grand challenges
### Challenge 1 — Sparse logical models
**What:** Learn compact decision trees, rule lists, and decision sets that capture interactions while remaining readable.  
**Open problems:** Efficiently optimize sparse trees; handle continuous variables without exploding the search space; incorporate practical constraints.  
**Example:** A short set of rules identifying which patients require a follow-up evaluation.

### Challenge 2 — Scoring systems
**What:** Learn simple integer point systems (add points for risk factors, then compare with a threshold).  
**Open problems:** Scale optimization and translate clinician preferences into mathematical constraints.  
**Example:** A bedside score that can be calculated without software.

### Challenge 3 — Generalized additive models (GAMs)
**What:** Model a prediction as a sum of understandable contributions from individual features, optionally with selected interactions: `prediction = intercept + f1(x1) + f2(x2) + ...`.  
**Open problems:** Control model complexity and interpretability; use learned feature-shape curves to detect problems in datasets.  
**Example:** Inspect whether predicted risk increases smoothly with a lab measurement or jumps suspiciously at a data-entry boundary.

### Challenge 4 — Modern case-based reasoning
**What:** Explain predictions using representative examples, prototypes, or similar prior cases rather than only feature coefficients.  
**Open problems:** Extend to complex data; incorporate expert guidance; repair misleading prototypes.  
**Example:** A medical-image model points to comparable annotated cases or clinically meaningful image regions.

### Challenge 5 — Supervised disentanglement
**What:** Align neural-network components with *predefined*, human-recognizable concepts.  
**Open problems:** Make entire layers concept-aligned, avoid mixed concepts, select meaningful concepts, and make the concept-to-prediction mapping interpretable.  
**Example:** Separate image features for shape, tissue appearance, and lesion boundaries.

### Challenge 6 — Unsupervised disentanglement
**What:** Discover distinct concepts without supplying a full concept-label vocabulary in advance.  
**Open problems:** Quantitatively evaluate discovery; build appropriate compositional architectures; learn complex part–whole structure.  
**Example:** Discover previously unrecognized patterns in medical images or scientific materials. **Caution:** A discovered latent factor is not automatically a valid clinical concept.

### Challenge 7 — Dimensionality reduction for visualization
**What:** Map high-dimensional data into 2D or 3D for inspection.  
**Open problems:** Preserve meaningful structure, choose hyperparameters responsibly, and interpret what the plotted axes or distances actually mean.  
**Example:** A 2D embedding of patient profiles may suggest clusters, but visible separation alone does not prove real clinical subgroups.

### Challenge 8 — Physics- and knowledge-constrained models
**What:** Build domain laws, equations, or causal/generative constraints into model construction; physics-informed neural networks (PINNs) are one example.  
**Open problems:** Stable training, efficient experimental design, and incorporating constraints in alternative architectures.  
**Example:** Require a physiological model to respect known relationships rather than fitting implausible trajectories.

### Challenge 9 — The Rashomon set
**What:** Study the collection of *different models with similarly good predictive performance*.  
**Open problems:** Characterize this set, visualize its diversity, and choose a suitable transparent model from it.  
**Example:** If many models predict readmission equally well, choose one with fewer features and more clinically credible behavior.

### Challenge 10 — Interpretable reinforcement learning
**What:** Learn understandable decision policies for sequential actions.  
**Open problems:** Find useful policy constraints, determine when accurate interpretable policies exist, and simplify complex state spaces.  
**Example:** A transparent sequence of monitoring and intervention decisions, subject to clinical review and safety constraints.

## 3. Important distinctions and definitions
| Term | Meaning | Why it matters |
|---|---|---|
| **Sparsity** | Few active rules/features/terms | Easier to inspect and audit |
| **Fidelity** | How accurately an explanation reflects the model being explained | A plausible explanation can still be unfaithful |
| **Distribution/domain shift** | Deployment data differ from training data | Shortcuts can fail in new hospitals or populations |
| **Prototype** | Representative example used in reasoning | Makes evidence concrete, but can be misleading |
| **Rashomon set** | Many models with near-equivalent performance | May permit a simpler, more transparent choice |
| **Disentanglement** | Separation of meaningful factors in learned representations | Helps inspect what a network encodes |

## 4. Implications for health analytics
- **Model selection:** Compare interpretable baselines against more complex alternatives before assuming a black box is needed.
- **Clinical review:** Ask whether practitioners can verify feature effects, thresholds, and edge cases.
- **Fairness and safety:** Examine subgroup behavior, proxy variables, and distribution shift; transparency helps investigation but is not proof of fairness.
- **Research design:** Define interpretability requirements before training; measure prediction quality and usability separately.

## Main conclusion
The authors advocate **building transparency into models themselves**, especially for consequential decisions. Their ten challenges demonstrate that interpretability is a substantive technical research field—not merely a visualization applied after training.

## Study questions
1. Why can a post-hoc explanation be convincing but unfaithful?
2. When would a point score be preferable to a GAM, and vice versa?
3. How does a large Rashomon set challenge the assumed accuracy–simplicity tradeoff?
4. Why does interpretable not automatically mean fair or causal?

**Source:** Rudin et al., *Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges*, uploaded PDF (2021), especially the principles, Challenges 1–10, and conclusion.
