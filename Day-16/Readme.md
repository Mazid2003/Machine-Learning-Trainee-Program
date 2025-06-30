# 🚀 Day 16: Introduction to Deep Learning — Comprehensive Overview

## 1️⃣ What is Deep Learning?

Deep Learning is a subset of Machine Learning (ML) that uses artificial neural networks (ANNs) with multiple hidden layers to learn patterns in data.

**✅ Key points:**

Learns hierarchical feature representations directly from raw data (no need for manual feature engineering).

Especially effective for unstructured data: images, audio, text, video.

Scales well with big data and high-performance hardware (e.g., GPUs).

## 2️⃣ Relationship Between AI, ML, and DL

| Field                            | Description                                         | Example Algorithms                 |
| -------------------------------- | --------------------------------------------------- | ---------------------------------- |
| **Artificial Intelligence (AI)** | Building machines that can mimic human intelligence | Rule-based systems, robotics       |
| **Machine Learning (ML)**        | Subset of AI that learns patterns from data         | Decision Trees, SVM, Random Forest |
| **Deep Learning (DL)**           | Subset of ML using multi-layer neural networks      | CNNs, RNNs, Transformers           |

## 3️⃣ Historical Milestones

- 1940s-50s: McCulloch-Pitts neuron, Hebbian learning.
- 1980s: Backpropagation popularized for multi-layer networks.
- 1990s: Shift to SVMs and other ML due to compute/data limitations.
- 2006: Breakthroughs in unsupervised pretraining → coined “Deep Learning”.
- 2012: AlexNet wins ImageNet — revival of DL via GPUs, large datasets.

## 4️⃣ Core Components of a Neural Network

### A. Artificial Neuron (Perceptron)

Formula:

**output=σ(∑wixi+b)**

Where:

- 𝑥𝑖= inputs

- 𝑤𝑖= weights

- 𝑏= bias

- 𝜎= activation function

### B. Layers

**Input layer:** Raw data entry.

**Hidden layers:** Learn intermediate representations.

**Output layer:** Final prediction (classification, regression, etc).

### C. Activation Functions

| Function       | Formula                  | Output Range | Properties                          |
| -------------- | ------------------------ | ------------ | ----------------------------------- |
| **Sigmoid**    | $\frac{1}{1 + e^{-x}}$   | 0 to 1       | Good for probabilities              |
| **Tanh**       | $\tanh(x)$               | -1 to 1      | Zero-centered                       |
| **ReLU**       | $\max(0, x)$             | 0 to ∞       | Sparse activation, fast convergence |
| **Leaky ReLU** | small slope when $x < 0$ |              | Fixes dying ReLU issue              |

## 5️⃣ Training a Deep Neural Network

### ✅ Forward Pass
Data flows layer-by-layer, transformations applied.

### ✅ Loss Function
Measures error:

Cross-Entropy: For classification.

MSE: For regression.

### ✅ Backpropagation
Compute gradients using chain rule.

Update weights in the direction that reduces loss.

### ✅ Optimization

| Optimizer            | Description                                         |
| -------------------- | --------------------------------------------------- |
| **Gradient Descent** | Update along gradient of loss                       |
| **SGD**              | Gradient descent with mini-batches                  |
| **Adam**             | Adaptive learning rate, combines momentum + RMSProp |

## 6️⃣ Key Hyperparameters

Learning rate

Number of layers + neurons

Batch size

Epochs

Dropout / L2 regularization

## 7️⃣ Common DL Architectures
### 🔹 Feedforward Neural Networks (FNN)
Basic structure, data flows in one direction.

### 🔹 Convolutional Neural Networks (CNN)
Ideal for images

Convolution → Pooling → Fully Connected

### 🔹 Recurrent Neural Networks (RNN)
Sequence modeling (e.g., text, speech)

Maintain memory of past inputs

### 🔹 Transformers
Use attention mechanisms

State-of-the-art in NLP, also vision

## 8️⃣ Applications of Deep Learning

| Domain      | Example                                 |
| ----------- | --------------------------------------- |
| Vision      | Image classification, face recognition  |
| NLP         | Sentiment analysis, machine translation |
| Speech      | Voice assistants                        |
| Healthcare  | Medical imaging                         |
| Autonomous  | Self-driving vehicles                   |
| Recommender | Personalized suggestions                |

