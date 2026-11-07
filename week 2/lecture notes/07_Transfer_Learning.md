# Module 2 — Transfer Learning

**Lecturer:** Sabina Tomkins  
**Source:** *Week 2 - Transfer Learning*, 39 slides.

## Key points
1. **Transfer learning** reuses knowledge learned from a **source** setting to help a **target** setting.
2. Source and target may differ in feature spaces, feature distributions, label spaces, or label distributions.
3. A **domain** describes the feature space and input distribution; a **task** describes the label space and prediction function.
4. Common families discussed are **instance-based**, **mapping-based**, and **network-based** transfer.
5. Neural-network transfer can initialize a target model using source-trained weights and then fine-tune on the target data.

## 1. From ordinary ML to transfer learning (slides 2–7)
The lecturer first depicts a model learning a task—predicting **liver cancer** from medical history—and then another task—predicting **stroke**. Reusing the first task's learned representation for the second illustrates the transfer-learning idea.

**Source:** Where the initial knowledge was learned. **Target:** New setting where the knowledge will be applied.

**Intuition:** Learning starts from a useful pretrained state instead of an entirely untrained model.

## 2. What can differ? (slides 8–14)
- Feature spaces: different variables are available.
- Feature distributions: the same variables occur at different frequencies.
- Label spaces: the set or meaning of output labels changes.
- Label distributions: outcome frequencies differ.

The slide's formal condition is **source domain ≠ target domain OR source task ≠ target task**.

## 3. Domain = feature space + input distribution (slides 15–21)
**Domain:** Defined by feature space `X` and marginal distribution `P(X)`.

**Different feature spaces (slide 16):** One database contains age, billing codes, and gender; another contains age, pharmacy codes, and race.

**Same features, different distributions (slides 17–21):** The same age-group representation can be more prevalent in a source dataset than a target dataset. The teaching example gives `P(X = elder)_source = 2/3` and `P(X = elder)_target = 1/3`.

**Marginal probability:** Overall probability of an input characteristic after accounting for possible labels:

`P(X=x) = Σ_y P(X=x | Y=y) P(Y=y)`

This is the law of total probability, as displayed on slide 20.

## 4. Task = labels + prediction relationship (slides 22–24)
**Task:** Output label space `Y` and the predictive relationship `f(X) → Y` or conditional distribution `P(Y | X)`.

**Different labels:** Binary stroke/no stroke versus a graded risk scale (slide 23).

**Same labels but changed distribution:** The outcome proportions or relationship may change between settings (slide 24). The lecture distinguishes task changes from domain changes.

## 5. Three transfer-learning approaches (slides 25–29)
| Approach | Lecture definition | Plain-language interpretation |
|---|---|---|
| **Instance-based** | Include informative source observations in target training | Reuse selected examples |
| **Mapping-based** | Merge datasets in a shared representation space | Translate both datasets into comparable features |
| **Network-based** | Reuse aspects of a neural network trained in source setting | Reuse trained model weights or layers |

## 6. Weight transfer and fine-tuning (slides 30–35)
The slides illustrate random/initial weights, source training, transfer of source weights to target initialization, and further training. For instance, a source weight `W11` changes from **0.5** initially to **1.5** after source training; the transferred target may later update it to **1.2**.

**PyTorch illustration from slide 34:**

```python
model.load_state_dict(torch.load(path_to_saved_model))
```

This illustrates restoring learned model parameters before target training. Practical loading requires a compatible architecture and appropriate model-file handling.

## 7. Fine-tuning pretrained models (slides 36–38)
The slides give **ResNet** (images) and **GPT-3** (language) as examples of large pretrained models and describe fine-tuning output layers. They preview using pretrained embeddings with medical text in the following week.

**Fine-tuning:** Continuing training on target data, typically updating some or all network parameters.

**Link to glucose assignment:** A population/pretrained model can provide initialization for a person-specific model; the resulting model can then adapt to that individual's observations (see the separate Glucose Prediction lecture, assignment 2d).

## Main argument / conclusion
**Transfer learning can exploit useful shared patterns while adapting to a new patient, dataset, or prediction task; understanding how source and target differ determines whether and how transfer is appropriate.**

## Study-check questions
1. What are the two components of a domain? Of a task?
2. Is changing only the distribution of patient ages enough to produce a different domain?
3. What changes when you initialize a target LSTM from pretrained weights rather than random weights?
