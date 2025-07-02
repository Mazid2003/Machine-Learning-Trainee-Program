
# 🚀 Day 17 – Build a Neural Network with Keras: Detailed Deep Dive

**Date: 29/06/2025**

**🎯 Learning Objectives**

- ✅ Understand what Keras is and why it’s widely used for deep learning.
  
- ✅ Learn core concepts of layers, models, loss functions, and optimizers in Keras.

- ✅ Build, train, and evaluate a neural network for digit classification.

- ✅ Explore saving/loading models, tuning hyperparameters, and debugging strategies.

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

**📌 Step 1: Import Required Libraries**
```
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
```
**📌 Step 2: Load and Prepare the Data**
```
# Load MNIST dataset (28x28 grayscale digit images)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize images to [0, 1]
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# One-hot encode labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
```
**✅ Why?**

Normalization helps **models converge faster.**

One-hot encoding **is required for categorical_crossentropy** loss.

**📌 Step 3: Define the Neural Network**
```
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])
```
**✅ Explanation**

**Flatten:** Converts 28×28 image to 784-dim vector.

**Dense(128):** Fully connected with ReLU activation.

**Dropout(0.2):** Drops 20% of neurons during training to reduce overfitting.

**Dense(10):** 10 outputs → one per digit (0–9), with softmax to give probabilities.

**📌 Step 4: Compile the Model**
```
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

- ✅ Adam → Adaptive optimizer combining RMSProp + momentum.
- ✅ Categorical crossentropy → Good for multi-class classification.

**📌 Step 5: Train the Model**
```
history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
```
✅ Details

- epochs=10 → Train over data 10 times.

- batch_size=32 → Updates weights after 32 samples.

- validation_split=0.2 → 20% of training data for validation.

**📌 Step 6: Evaluate the Model**
```
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
```
✅ This shows how well the model generalizes to unseen data.

**📌 Step 7: Make Predictions**
```
predictions = model.predict(x_test)
predicted_classes = predictions.argmax(axis=1)
```
✅ Each prediction is a 10-element vector → argmax picks the class with the highest probability.

**📌 Step 8: Saving and Loading the Model**
```
# Save model
model.save('mnist_model.h5')

# Load model
from tensorflow.keras.models import load_model
model = load_model('mnist_model.h5')
```
✅ Allows reuse without retraining.

## Advanced Tips

- **EarlyStopping:** Stop training when validation loss stops improving.

- **BatchNormalization:** Normalize layer inputs → faster convergence.

- **LearningRateScheduler:** Dynamically adjust learning rate during training.

- **Data Augmentation:** For image data, generate more samples via transformations.

## Common Pitfalls:

| Issue          | Solution                                      |
| -------------- | --------------------------------------------- |
| Overfitting    | Use Dropout, get more data, use EarlyStopping |
| Underfitting   | Increase model size, train longer             |
| Shape mismatch | Check input/output shapes carefully           |
| Poor accuracy  | Normalize data, tune hyperparameters          |

## ✅ Summary

| Step             | What you did                                 |
| ---------------- | -------------------------------------------- |
| Import Libraries | TensorFlow + Keras essentials                |
| Load Data        | MNIST dataset, normalization, one-hot labels |
| Define Model     | Flatten + Dense + Dropout layers             |
| Compile          | Set optimizer, loss, metrics                 |
| Train            | Fit with validation                          |
| Evaluate         | Test set accuracy                            |
| Save/Load        | Reuse the trained model                      |


