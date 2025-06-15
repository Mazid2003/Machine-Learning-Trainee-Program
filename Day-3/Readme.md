# 🚀 Day 3 – NumPy: Arrays, Indexing, Slicing, Operations

**Date:11/06/2025**

**✅ Topics Covered:**

Introduction to NumPy and Arrays

Creating NumPy Arrays

Array Attributes

Indexing and Slicing of Arrays

Array Operations and Broadcasting

Useful NumPy Functions

Practice Exercises

# 🔷 1. Introduction to NumPy

**🔹 What is NumPy?**

NumPy (Numerical Python) is a fundamental Python library for scientific computing.

It provides support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

It is much faster and more efficient than Python’s built-in lists for numerical data processing.

**🔹 Why use NumPy?**

Efficient storage and manipulation of numerical data.

Support for multi-dimensional arrays.

Vectorized operations that execute very fast.

Tools for integrating C/C++ and Fortran code.

Useful linear algebra, random number generation, Fourier transforms, and more.

**🔹 Importing NumPy**
```
import numpy as np
```
# 🔷 2. Creating NumPy Arrays

**🔸 What is a NumPy Array?**

A NumPy array (or ndarray) is a grid of values, all of the same type, indexed by a tuple of nonnegative integers.

Unlike Python lists, NumPy arrays are homogeneous (all elements are the same data type), which allows efficient processing.

**🔸 Creating Arrays from Python Lists**
**1D Array**
```
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
```
**2D Array (matrix)**
```
import numpy as np
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
```
**🔸 Creating Special Arrays**

**Zeros Array**
```
import numpy as np
zeros_arr = np.zeros((3, 4))  # 3 rows, 4 columns filled with 0.0
print(zeros_arr)
```
**Ones Array**
```
import numpy as np
ones_arr = np.ones((2, 5))  # 2 rows, 5 columns filled with 1.0
print(ones_arr)
```

**Empty Array (uninitialized values)**
```
import numpy as np
empty_arr = np.empty((3, 3))
print(empty_arr)
```

**Identity Matrix**
```
import numpy as np
eye_arr = np.eye(4)  # 4x4 identity matrix
print(eye_arr)
```
**Range Array**
```
import numpy as np
range_arr = np.arange(10)  # 0 to 9
print(range_arr)
```

**Linspace Array**
```
import numpy as np
linspace_arr = np.linspace(0, 1, 5)  # 5 numbers evenly spaced between 0 and 1
print(linspace_arr)
```
# 🔷 3. Array Attributes

Understanding array properties helps in manipulating data effectively.
```
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr.shape — Tuple representing array dimensions (rows, columns)

print(arr.shape)  # Output: (2, 3)
arr.size — Total number of elements in the array

print(arr.size)  # Output: 6
arr.dtype — Data type of the elements

print(arr.dtype)  # Output: int64 or int32 depending on system
arr.ndim — Number of array dimensions

print(arr.ndim)  # Output: 2 (since it is a 2D array)
arr.itemsize — Size (in bytes) of each element

print(arr.itemsize)  # Output: typically 8 bytes for int64
```
# 🔷 4. Indexing and Slicing of Arrays

NumPy arrays support powerful and flexible indexing and slicing techniques, similar to Python lists but extended for multiple dimensions.

**🔸 Indexing 1D Arrays**
```
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])  # 10
print(arr[3])  # 40
Negative indexing supported (counts from the end)

print(arr[-1])  # 50
print(arr[-3])  # 30
```

**🔸 Indexing 2D Arrays**
```
import numpy as np
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(arr2d[0, 1])  # 2 (first row, second column)
print(arr2d[2, 0])  # 7 (third row, first column)
You can access a whole row or column:

print(arr2d[1])      # [4 5 6]  (second row)
print(arr2d[:, 2])   # [3 6 9]  (third column)
```

**🔸 Slicing 1D Arrays**
```
import numpy as nnp
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])   # [20 30 40] (elements from index 1 to 3)
print(arr[:3])    # [10 20 30] (start to index 2)
print(arr[2:])    # [30 40 50] (index 2 to end)
print(arr[::2])   # [10 30 50] (every second element)
print(arr[::-1])  # [50 40 30 20 10] (reversed)
```

**🔸 Slicing 2D Arrays**
```
import numpy as np
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

print(arr2d[:2, 1:3])
# Output:
# [[2 3]
#  [6 7]]
This extracts rows 0 and 1, and columns 1 and 2.
```

**🔸 Boolean Indexing**

Use boolean arrays to select elements conditionally.
```
import numpy as np
arr = np.array([10, 15, 20, 25, 30])
mask = arr > 20
print(mask)        # [False False False  True  True]
print(arr[mask])   # [25 30]
Or directly:

print(arr[arr > 20])  # [25 30]
```

**🔸 Fancy Indexing**

Index arrays with lists or arrays of indices.
```
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
indices = [1, 3, 4]
print(arr[indices])  # [20 40 50]
```

# 🔷 5. Array Operations

NumPy supports element-wise operations and matrix operations.

**🔸 Arithmetic Operations (element-wise)**
```
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # [5 7 9]
print(a - b)  # [-3 -3 -3]
print(a * b)  # [4 10 18]
print(a / b)  # [0.25 0.4 0.5]
print(a ** 2) # [1 4 9]
```

**🔸 Broadcasting**

Allows operations between arrays of different shapes.
```
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([1, 0, 1])

print(a + b)
# [[2 2 4]
#  [5 5 7]]
```
Here b is broadcast (copied) across each row of a automatically.

**🔸 Aggregation Functions**

Calculate statistics over arrays:
```
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))      # 15
print(np.mean(arr))     # 3.0
print(np.median(arr))   # 3.0
print(np.min(arr))      # 1
print(np.max(arr))      # 5
print(np.std(arr))      # Standard deviation
```

**🔸 Matrix Multiplication**

Use np.dot or @ operator for matrix multiplication.
```
import numpy as np
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print(np.dot(A, B))
# [[19 22]
#  [43 50]]

print(A @ B)
Same result as np.dot(A, B)
```
**🔸 Transpose of an Array**
```
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr.T)
# [[1 4]
#  [2 5]
#  [3 6]]
```

**🔸 Reshaping Arrays**

Change the shape without changing data:
```
import numpy as np
arr = np.arange(12)
print(arr.reshape(3, 4))
Output:

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

**🔸 Flattening Arrays**

Convert multi-dimensional array to 1D:
```
import numpy as np
arr2d = np.array([[1, 2], [3, 4]])
flat = arr2d.flatten()
print(flat)  # [1 2 3 4]
```

# 🔷 6. Useful NumPy Functions
| **Function**                         | **Description**                                                         |
| ------------------------------------ | ----------------------------------------------------------------------- |
| `np.arange(start, stop, step)`       | Create array with values from `start` to `stop-1` with step size `step` |
| `np.linspace(start, stop, num)`      | Create array with `num` evenly spaced values between `start` and `stop` |
| `np.zeros(shape)`                    | Create array filled with zeros                                          |
| `np.ones(shape)`                     | Create array filled with ones                                           |
| `np.eye(n)`                          | Identity matrix of size `n x n`                                         |
| `np.random.rand(d0, d1, ...)`        | Random floats in the range \[0, 1) with given shape                     |
| `np.random.randint(low, high, size)` | Random integers between `low` (inclusive) and `high` (exclusive)        |
| `np.sum(arr, axis=None)`             | Sum of elements (controlled by `axis`)                                  |
| `np.mean(arr, axis=None)`            | Mean (average) of elements                                              |
| `np.std(arr, axis=None)`             | Standard deviation of elements                                          |
| `np.min(arr, axis=None)`             | Minimum value of elements                                               |
| `np.max(arr, axis=None)`             | Maximum value of elements                                               |
| `np.dot(a, b)`                       | Dot product or matrix multiplication                                    |
| `arr.reshape(new_shape)`             | Reshape array to `new_shape`                                            |

