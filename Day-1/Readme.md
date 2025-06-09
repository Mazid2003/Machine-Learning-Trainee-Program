
**🚀 Day 1 – Python Basics**

Welcome to Day 1 of my Python learning journey! Here's a concise and comprehensive overview of the essential concepts I covered.

**✅ Topics Covered:**

Introduction to Python

Variables and Data Types

Control Flow with Loops

Functions in Python

Working with Lists

Using Dictionaries

**🔹 1. Introduction to Python**

Python is a high-level, interpreted, and general-purpose programming language known for its clear syntax and wide range of applications:

**🔸 Why Learn Python?**

Simple and readable syntax (like English)

Large, active community

Cross-platform support

Extensive libraries (NumPy, Pandas, Flask, TensorFlow, etc.)

Used by top tech giants (Google, Netflix, NASA)

**🧪 Example:**

print("Hello, Python World!")

**🔹 2. Variables and Data Types**

🔸 What is a Variable?

A variable stores information to be referenced and manipulated in a program.

**🧪 Example:**

name = "Aashutosh"
age = 24
height = 5.7
is_student = True

**🔸 Common Data Types:**

| Type    | Example          |
| ------- | ---------------- |
| `int`   | `10`             |
| `float` | `10.5`           |
| `str`   | `"Hello"`        |
| `bool`  | `True` / `False` |


**🔸 Type Checking:**

print(type(name))  # <class 'str'>

**🔹 3. Control Flow with Loops**

Loops let us execute a block of code multiple times.

**🔸 for Loop:**

for i in range(5):
    print("Iteration", i)

**🔸 while Loop:**

count = 0
while count < 5:
    print("Count is", count)
    count += 1
**🔸 Loop Control Statements:**

break – Exit the loop

continue – Skip current iteration

pass – Do nothing

for i in range(10):
    if i == 5:
        break
    print(i)
    
**🔹 4. Functions in Python**

Functions make code modular, reusable, and organized.

🔸 Defining and Calling Functions:

def greet(name):
    return f"Hello, {name}!"

print(greet("Soni"))
🔸 Default & Keyword Arguments:

def greet(name="User"):
    print("Hello", name)

greet()           # Hello User
greet("Ranjan")   # Hello Ranjan
🔹 5. Lists
Lists are ordered, mutable collections of items.

🔸 Creating and Accessing Lists:

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
🔸 Modifying Lists:

fruits.append("orange")
fruits.remove("banana")
print(len(fruits))  # 3
🔸 Iterating Over a List:

for fruit in fruits:
    print(fruit)

**🔸 List Slicing:**

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])  # [20, 30, 40]

**🔹 6. Dictionaries**

Dictionaries are unordered collections of key-value pairs.

**🔸 Creating a Dictionary:**

student = {
    "name": "Aashu",
    "age": 24,
    "course": "Python"
}
**🔸 Accessing and Updating:**

print(student["name"])         # Aashu
print(student.get("age"))      # 24
student["grade"] = "A"

**🔸 Looping Through Dictionary:**


for key, value in student.items():
    print(key, ":", value)

**🌟 Summary**

On Day 1, I got hands-on experience with the core building blocks of Python. These fundamentals form the base for advanced topics like data analysis, web development, and machine learning.

