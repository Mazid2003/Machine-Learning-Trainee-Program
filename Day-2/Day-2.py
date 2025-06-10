'''
EX-1
Write a program that takes two numbers from the user and divides them, handling division by zero and invalid input errors.

def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print("Result:", result)
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
divide_numbers()


EX-2
Create a function that reads a file path from the user, attempts to open and print the file content, and handles file not found or permission errors gracefully.

def read_file():
    file_path = input("Enter the file path: ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("\n📄 File Content:\n")
            print(content)
    except FileNotFoundError:
        print("❌ File not found! Please check the path and try again.")
    except PermissionError:
        print("❌ Permission denied! You are not allowed to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

read_file()



EX-3
Write a program that asks the user for a filename and some text, writes the text to that file, and then reads it back to display.

def write_and_read_file():
    filename = input("Enter the filename: ")
    text = input("Enter the text you want to write to the file:\n")

    try:
        # Write text to file
        with open(filename, 'w') as file:
            file.write(text)
        print("\n✅ Text written to file successfully.")

        # Read the file back
        with open(filename, 'r') as file:
            content = file.read()
            print("\n📄 File Content:\n" + content)
    except Exception as e:
        print(f"❌ Error occurred: {e}")

write_and_read_file()


EX-4

Create a program to count the number of words in a text file.
to programs


def count_words_in_file():
    file_path = input("Enter the path to the text file: ")

    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"\n📝 Total number of words: {len(words)}")
    except FileNotFoundError:
        print("❌ File not found!")
    except PermissionError:
        print("❌ Permission denied!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
count_words_in_file()

EX-5

Create a list of all vowels from a string using list comprehension.

input_str = "Hello, I am learning Python list comprehension!"
vowels = [char for char in input_str if char.lower() in 'aeiou']
print("Vowels in the string:", vowels)

EX-6

Generate a list of numbers from 1 to 50 divisible by 3 and 5.

divisible_by_3_and_5 = [num for num in range(1, 51) if num % 3 == 0 and num % 5 == 0]
print("Numbers divisible by 3 and 5:", divisible_by_3_and_5)

EX-7

Create a list of tuples containing number and its square for numbers from 1 to 10.

squares = [(num, num ** 2) for num in range(1, 11)]
print("Number and its square:", squares)
'''















