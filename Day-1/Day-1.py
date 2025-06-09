'''
1. function

def greet(name):
    print("hello",name)
greet("Mazid")    

2. using list to printing even numbers

b=list(map(int, input().split()))
a=[]
for i in b:
    if i%2==0:
        a.append(i)
print(a)    
        
3. quiz
print("2"+"3")

4. Dictionary
student={
    "name":"Mazid",
    "age": 23,
    "course": "B.Tech"
    }
print(student["name"])
student["grade"]:"A"
for key, value in student.items():
    print(key,":",value)
'''
a simple calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

# Main program
print("Welcome to the Calculator!")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid Input")

    
    
    
