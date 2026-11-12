# Multimodal Deep Learning
**Authors:** Jiquan Ngiam, Aditya Khosla, Mingyu Kim, Juhan Nam, Honglak Lee, Andrew Y. Ng (ICML 2011)  
**Type:** Methods and experiments | **Course:** SIADS 681 Health Analytics

## 5 key points
1. **Multimodal learning combines complementary signals.** Speech sounds and lip movements encode related information that is not always obvious from raw input alone.
2. **Three tasks differ by what data are available at each stage:** multimodal fusion, cross-modality feature learning, and shared representation learning.
3. **Deep autoencoders learn cross-modal structure** by reconstructing audio and video, sometimes when only one is supplied.
4. **Cross-modal training improved visual speech classification.** Audio can help learn useful video features even if the final classifier uses video alone.
5. **Fusion is context-dependent.** Joint audio–visual features helped in noisy conditions, but adding a modality did not universally improve results.

## 1. Motivation: complementary modalities
- **Modality:** A type/source of data, such as audio, video, text, or physiological sensors.
- **Multimodal learning:** Learning relationships among multiple modalities.
- **Phoneme:** A distinguishable speech sound; **viseme:** corresponding visible mouth shape/movement.
- **McGurk effect:** Seeing one articulation while hearing another can change perceived speech (e.g., visual /ga/ plus audio /ba/ is often perceived as /da/).

**Health analytics analogy:** ECG signals and clinical notes may contain different but related information about a patient. Their joint usefulness must be validated; this paper itself studies speech, **not** clinical data.

## 2. Three learning settings (Figure 1, p. 2)
| Setting | Feature learning | Supervised training | Testing | Question |
|---|---|---|---|---|
| **Multimodal fusion** | Audio + video | Audio + video | Audio + video | Does combining both improve prediction? |
| **Cross-modality learning** | Audio + video | One modality | Same single modality | Does extra information improve single-modality features? |
| **Shared representation learning** | Audio + video | Audio **or** video | The **other** modality | Do features transfer across modalities? |

**Remember:** Cross-modality learning is *not* the same as training a classifier on audio and testing on video; that is the **shared representation** experiment.

## 3. Architecture and training
### Restricted Boltzmann machine (RBM)
An unsupervised probabilistic model with visible and hidden units; the paper uses **sparse RBMs** to initialize features layer by layer. Sparse activations encourage a small number of hidden units to activate for a given input.

### Deep belief network (DBN)
Separate lower-level audio and video feature learners feed a higher-level representation. This helps capture nonlinear relationships that a shallow concatenated RBM struggles to discover (Figure 2, p. 3).

### Deep autoencoder
An **encoder** compresses input into a learned representation; a **decoder** reconstructs target signals. A video-only autoencoder learns to reconstruct **both** video and audio from video input, forcing it to learn cross-modal predictive features (Figure 3a, p. 3).

### Bimodal denoising autoencoder
Training examples are deliberately modified: approximately one-third video only, one-third audio only, and one-third both; the network must still reconstruct **both modalities** (Figure 3b, p. 3; discussion p. 4). This makes it more robust when one source is missing.

### Preprocessing
- Audio: spectrograms plus temporal derivatives; PCA whitening for dimensionality reduction.
- Video: mouth region of interest, resized to 60 × 80 pixels, then PCA features and motion information.
- A **linear SVM** evaluates the learned features so that the feature-learning contribution can be compared more directly.

## 4. Datasets and experimental results
- **AVLetters:** 10 speakers saying letters A–Z; used for visual-only classification (original audio unavailable).
- **CUAVE:** 36 speakers saying digits 0–9; speaker-independent evaluation.
- **AVLetters2, Stanford speech data, TIMIT:** Additional sources for unsupervised feature learning/pretraining.
- The authors report keeping test data out of unsupervised feature learning.

### Cross-modality results (Table 1, p. 5)
| Visual classification | Preprocessed video | Video RBM | Video-only deep autoencoder | Bimodal deep autoencoder |
|---|---:|---:|---:|---:|
| AVLetters | 46.2% | 54.2% | **64.4%** | 59.2% |
| CUAVE | 58.5% | 65.4% | **68.7%** | 66.7% |

**Interpretation:** Training video representations to reconstruct audio provided a useful learning signal. The fully bimodal autoencoder did **not** beat the specialized video-only autoencoder on these visual-only tasks.

### Fusion under noisy audio (Table 2, p. 6)
| Features | Clean audio | Noisy audio |
|---|---:|---:|
| Audio RBM | **95.8%** | 75.8% |
| Bimodal deep autoencoder | 90.0% | 77.3% |
| Bimodal + audio RBM | 94.4% | **82.2%** |

The noisy condition adds white Gaussian noise at 0 dB signal-to-noise ratio. Fusion improved robustness relative to audio RBM alone under noise, but the audio-only baseline remained best among these rows for clean audio.

### Shared representations (Table 4, p. 7)
- **CCA (canonical correlation analysis):** Finds projections of two modalities whose transformed features are maximally correlated.
- RBM features + CCA reached **57.3%** when trained on audio and tested on video, and **91.7%** in the reverse direction.
- Bimodal deep autoencoder achieved **30.7%** and **24.3%**, respectively; chance was 10%.

**Interpretation:** Learned nonlinear features followed by linear CCA worked better for this particular cross-modal transfer task. No single architecture won every experiment.

### McGurk demonstration (Table 3, p. 6)
For mismatched visual /ga/ and audio /ba/, the model predicted /da/ **58.7%** of the time—an interesting demonstration of integrated representations, not proof of human-equivalent speech perception.

## 5. Limitations and healthcare relevance
- Findings are from relatively constrained audio–visual speech datasets, not general clinical multimodal prediction.
- Dataset size, preprocessing, alignment, and missing modalities influence performance.
- Better representations do not guarantee higher accuracy in every setting; clean and noisy evaluations can differ.
- For health analytics, test **single-source baselines**, missing-data robustness, subgroup generalization, and fusion under realistic noise.

## Main conclusion
Deep learning can exploit unlabeled paired modalities to learn features that transfer and complement each other. **Reconstruction objectives and training with missing modalities** are especially useful ideas, but the best approach depends on the task and available data.

## Study questions
1. Distinguish multimodal fusion, cross-modality learning, and shared representation learning.
2. Why reconstruct audio from video during feature learning?
3. Why might audio–video fusion help under noise but hurt on clean data?
4. What is the role of CCA in the shared-representation experiment?

**Source:** Ngiam et al., *Multimodal Deep Learning*, uploaded PDF (2011), Figures 1–3 and Tables 1–4.
