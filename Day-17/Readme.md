
# 🚀 Day 17 – Build a Neural Network with Keras: Detailed Deep Dive

**🎯 Learning Objectives**

✅ Understand what Keras is and why it’s widely used for deep learning.
✅ Learn core concepts of layers, models, loss functions, and optimizers in Keras.
✅ Build, train, and evaluate a neural network for digit classification.
✅ Explore saving/loading models, tuning hyperparameters, and debugging strategies.

## 1️⃣ What is Keras?
Keras is a high-level API for building and training deep learning models.
It runs on top of backends like TensorFlow (default in TensorFlow 2.x), Theano, or CNTK.

## ✨ Why use Keras?

**User-friendly:** Simple, clean syntax makes model building fast and easy.

**Modular:** Build models layer by layer or flexibly using the functional API.

**Extensible:** Easily add custom layers, loss functions, or metrics.

**Scalable:** Works with CPUs, GPUs, and TPUs — small-scale to production.

**Large community:** Tons of tutorials, pre-trained models, and help.

## 2️⃣ Core Keras Concepts

### 🔹 Layers

The basic building blocks of neural networks.

**Examples:**

**Dense:** Fully connected layer.

**Conv2D:** Convolution layer for images.

**LSTM:** For sequence data.

**Dropout:** Prevents overfitting by randomly dropping units.

**Flatten:** Converts multi-dimensional input into 1D.

### 🔹 Models

Two ways to build models:

**Sequential API** → Stack layers one after another.

**Functional API** → For complex models (multi-input/output, shared layers).

### 🔹 Compilation

Set how the model learns:

**Loss function →** What the model tries to minimize.

**Optimizer →** Algorithm to update weights (e.g., Adam, SGD).

**Metrics →** For evaluation during training (e.g., accuracy).

## 3️⃣ Building an MNIST Digit Classifier: Step-by-Step

**📌 Step 1:** Import Required Libraries
```
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
```

