**🚀Day 2 – Exception Handling, File Handling, List Comprehension**

**✅ Topics Covered:**

Exception Handling

File Handling

List Comprehension

**🔷 1. Exception Handling in Python**

**🔹 What is an Exception?**

An exception is an error detected during execution of a program that interrupts the normal flow of the program. When Python encounters a problem it cannot handle, it raises an exception and stops the program unless you handle it.

**🔸 Why Handle Exceptions?**

Prevent the program from crashing unexpectedly

Gracefully manage error situations (e.g., invalid user input)

Provide meaningful error messages

Allow the program to continue or shut down safely

**🔸 Common Types of Exceptions**

| **Exception Name**     | **Description**                                  | **Example**                    |
|------------------------|--------------------------------------------------|--------------------------------|
| `ZeroDivisionError`    | Division or modulo by zero                       | `x = 10 / 0`                   |
| `ValueError`           | Invalid value for a function argument            | `int("abc")`                   |
| `TypeError`            | Unsupported operation between incompatible types | `len(5)`                       |
| `FileNotFoundError`    | Trying to open a file that doesn’t exist         | `open("nofile.txt")`          |
| `IndexError`           | Index out of range in a list or string           | `mylist[5]` (if length < 6)    |
| `KeyError`             | Accessing a non-existent dictionary key          | `mydict['missing_key']`       |


**🔸 Basic Try-Except Block**
```
try:
    # code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
```
The try block contains code that might cause an exception.

The except block contains code that runs if that exception occurs.

**🔸 Handling Multiple Exceptions**
```
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input, please enter a number.")
```
Multiple except blocks allow different handling depending on exception type.

**🔸 Catching All Exceptions**
```
try:
    # risky code
    pass
except Exception as e:
    print(f"An error occurred: {e}")
```
Exception is the base class of all exceptions.

Useful for logging or generic error messages.

**🔸 Using else with try-except**
```
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid number!")
else:
    print(f"You entered {num}")
```
else runs only if no exceptions occur in try.

**🔸 The finally Block**
```
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()
    print("File closed.")
```
finally always executes regardless of exceptions.

Often used to clean up resources (files, network connections).

**🔸 Raising Exceptions Manually**
```
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print(e)
```
Use raise to throw exceptions intentionally for invalid conditions.

**🔹 Best Practices for Exception Handling**

Only catch exceptions you expect or can handle properly.

Avoid bare except: which catches everything silently.

Use specific exception classes.

Always clean up resources (use finally or context managers).

Provide helpful error messages to users.

**🔷 2. File Handling in Python**

**🔹 Introduction**

Files are essential for storing data permanently outside the program. Python provides simple and powerful methods to create, read, update, and delete files.

**🔸 Opening a File**

file = open("example.txt", mode)

mode determines the operation:

| **Mode** | **Description**                         |
|----------|-----------------------------------------|
| `'r'`    | Read (default mode)                     |
| `'w'`    | Write (creates or overwrites a file)    |
| `'a'`    | Append (adds content to the end)        |
| `'r+'`   | Read and Write                          |
| `'b'`    | Binary mode (combine with other modes)  |


**🔸 Reading Files**

Read entire content
```
with open("example.txt", "r") as f:
    content = f.read()
print(content)
```
Read line by line
```
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
```
Read specified number of characters
```
with open("example.txt", "r") as f:
    partial = f.read(10)
    print(partial)
```
**🔸 Writing to Files**

Writing text to a file (overwrites existing content):
```
with open("example.txt", "w") as f:
    f.write("Hello, this is a test file.n")
```
**Appending text:**
```
with open("example.txt", "a") as f:
    f.write("Adding a new line.n")
```
**🔸 Working with Files – Full Example**
```
filename = "user_data.txt"

# Write user input to file
with open(filename, "w") as file:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    file.write(f"Name: {name}nAge: {age}n")
```
# Read and display file contents
```
with open(filename, "r") as file:
    print("nFile Contents:")
    print(file.read())
```
**🔸 File Handling with Exception Management**
```
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist.")
except Exception as e:
    print("An error occurred:", e)
```
**🔸 Context Managers (with statement)**

The with statement automatically closes the file after the block finishes, even if exceptions occur. This prevents resource leaks.
```
with open("example.txt", "r") as f:
    data = f.read()
```
# File is automatically closed here

**🔸 Binary File Handling**

Files like images, videos need to be read/written in binary mode:
```
with open("image.jpg", "rb") as f:
    data = f.read()

with open("copy.jpg", "wb") as f:
    f.write(data)
```

**🔷 3. List Comprehension**

**🔹 What is List Comprehension?**

List comprehension provides a concise way to create or transform lists using a clear and readable syntax. It’s often faster and cleaner than using loops.

**🔸 Basic Syntax**
```
new_list = [expression for item in iterable if condition]
```
expression: The output expression for each element

item: Variable representing each element from iterable

iterable: A sequence (like list, range, string)

condition (optional): Filters elements based on True/False
```
🔸 Example 1: Squares of Numbers
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, ..., 81]
🔸 Example 2: Filtering Even Numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, ..., 18]
🔸 Example 3: From String to List of Characters
chars = [char for char in "Python"]
print(chars)  # ['P', 'y', 't', 'h', 'o', 'n']
🔸 Example 4: Conditional Expressions in Output
marks = [50, 80, 90, 45, 70]
result = ["Pass" if score >= 50 else "Fail" for score in marks]
print(result)  # ['Pass', 'Pass', 'Pass', 'Fail', 'Pass']
```
**🔸 Nested List Comprehension**

Create a multiplication table (2D list):
```
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)
```
**🔸 List Comprehension vs Loop**

**Using loop:**
```
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)
```
**Using list comprehension:**
```
squares = [i**2 for i in range(10)]
print(squares)
```
**🔹 Advantages of List Comprehension**

Compact and expressive

Usually faster than loops

Easy to read once familiar

**🔹 Practice Exercises**

Create a list of all vowels from a string using list comprehension.

Generate a list of numbers from 1 to 50 divisible by 3 and 5.

Create a list of tuples containing number and its square for numbers from 1 to 10.

**🏁 Summary Table**

| **Concept**     | **Description**                          | **Example**                                  |
|------------------|------------------------------------------|----------------------------------------------|
| `try-except`     | Handle exceptions                        | `try: ... except ZeroDivisionError:`         |
| `raise`          | Manually throw exceptions                | `raise ValueError("Invalid")`                |
| `open()`         | Open a file                              | `open("file.txt", "r")`                       |
| `with open()`    | Context manager for file handling        | `with open("file.txt") as f:`                 |
| `read()` / `write()` | Read/write file content             | `f.read()` / `f.write("Hello")`               |


