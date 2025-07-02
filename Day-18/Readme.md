# 📅 Day 18 – Optimization Techniques in Deep Learning

**Date:01/07/2025**

**🎯 Learning Objectives**

By the end of this notebook or document, you will:

- ✅ Understand optimization in machine learning.
- ✅ Learn about loss functions and their role.
- ✅ Explore basic to advanced optimization algorithms (SGD, Momentum, RMSProp, Adam).
- ✅ Grasp challenges like local minima, saddle points, and vanishing gradients.
- ✅ Understand adaptive learning rate methods.
- ✅ Learn how to apply learning rate schedules, early stopping, and initialization techniques.

## 1️⃣ What is Optimization in ML?

👉 Optimization is the process of adjusting model parameters (weights & biases) to minimize the loss function.

The goal is to find:

**θ∗=arg θmin​ L(θ)**

where:

θ = model parameters

L(θ) = loss function

**✅ Outcome: Better predictions on training and unseen data.**

## 2️⃣ Role of the Loss Function

The loss function quantifies how well a model performs.

**Common examples:**

**MSE (Mean Squared Error)** → for regression

**Cross-Entropy Loss** → for classification

👉 The optimizer works to minimize this loss.

## 3️⃣ Gradient Descent: The Foundation

Gradient Descent updates parameters in the opposite direction of the gradient:

**θ:=θ−η∇θL(θ)**

where:

𝜂 = learning rate

∇𝜃𝐿(𝜃)= gradient of loss w.r.t parameters

| Type                    | Description             | Pros         | Cons               |
| ----------------------- | ----------------------- | ------------ | ------------------ |
| **Batch GD**            | Uses all data each step | Stable       | Slow for big data  |
| **Stochastic GD (SGD)** | 1 sample at a time      | Fast updates | Noisy, less stable |
| **Mini-batch GD**       | Small batches (32, 64)  | Fast, stable | Standard in DL     |

## 4️⃣ Learning Rate: Critical Hyperparameter

**Too large** → divergence

**Too small**→ slow convergence

**✅ Learning rate schedules or adaptive methods help!**

## 5️⃣ Challenges in Optimization

| Challenge                     | Description                       | Example Fix                 |
| ----------------------------- | --------------------------------- | --------------------------- |
| Local minima                  | Stuck in suboptimal valleys       | SGD noise, momentum         |
| Saddle points                 | Flat + curved directions          | Momentum, adaptive methods  |
| Vanishing/exploding gradients | Tiny/huge updates → slow/unstable | Batch norm, good init, LSTM |

## 6️⃣ Advanced Optimization Algorithms

| Optimizer | Key Idea                    | Advantage             | Drawback              |
| --------- | --------------------------- | --------------------- | --------------------- |
| SGD       | Vanilla GD                  | Simple                | Noisy, slow           |
| Momentum  | Adds velocity               | Faster, smoother      | Needs tuning γ        |
| Nesterov  | Lookahead                   | Precise updates       | Slightly more complex |
| Adagrad   | Per-parameter LR            | Good for sparse data  | LR decays too much    |
| RMSProp   | Moving avg of squared grads | Stable LR             | Needs decay tuning    |
| Adam      | Combines momentum + RMSProp | Robust, fast, popular | Slight memory cost    |

## 7️⃣ Mathematics

GD is an iterative scheme:

**𝜃(𝑡+1)=𝜃(𝑡)−𝜂∇𝜃𝐿(𝜃^(𝑡)**

**✅ Convergence depends on:**

Smoothness of L

Learning rate

Convexity (rare in DL)

## 8️⃣ Practical Tips

- ✅ Use good initialization (He for ReLU, Xavier for tanh).
- ✅ Normalize inputs.
- ✅ Use batch norm, dropout, early stopping.
- ✅ Use learning rate schedulers.

## 9️⃣ Optimization in Deep Learning Frameworks

👉 Example (Keras / TensorFlow):
```
from tensorflow.keras.optimizers import Adam, SGD
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

## 🔟 Summary Table

| Optimizer | Key Idea                    | Pros         | Cons               |
| --------- | --------------------------- | ------------ | ------------------ |
| SGD       | Basic GD                    | Simple       | Slow, noisy        |
| Momentum  | Adds velocity               | Faster       | Needs γ            |
| NAG       | Lookahead                   | Accurate     | Slightly complex   |
| Adagrad   | Per-param LR                | Sparse data  | LR decay too much  |
| RMSProp   | Moving avg of grads         | Stable LR    | Needs decay tuning |
| Adam      | Combines Momentum + RMSProp | Fast, robust | Slight memory cost |

## 1️⃣1️⃣ Beyond Gradient-Based

- Genetic Algorithms

- Bayesian Optimization

- Second-Order Methods (Newton, quasi-Newton)

## 1️⃣2️⃣ Trends

- 🚀 New optimizers that generalize better
- 🚀 Adaptive methods with guarantees
- 🚀 Architecture-specific optimizers

## 1️⃣3️⃣ Practice Project

🟣 Goal: Compare optimizers on CIFAR-10

🟣 Plan:

**✅ Implement models with:**

SGD

SGD + Momentum

RMSProp

Adam

**✅ Visualize:**

Loss + accuracy curves

**✅ Experiment:**

Learning rates (0.01, 0.001, etc)

Batch sizes (32, 64, 128)

**✅ Apply:**

EarlyStopping

ReduceLROnPlateau

**✅ Analyze:**

glorot_uniform vs he_normal init

👉 Code Reference: [See my notebook link / repo file]

**📌 Example Code Snippet**
```
train_model(tf.keras.optimizers.Adam, lr=0.001, batch_size=64, initializer='he_normal')
```
👉 Produces validation accuracy/loss curves + test accuracy.

### 📈 Visuals

👉 Include:

Validation accuracy vs epoch for each optimizer

Loss vs epoch for each optimizer

Effect of LR / batch size in plots

Effect of init in plots










