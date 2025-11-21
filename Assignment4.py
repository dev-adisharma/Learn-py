# Name: Aditya Sharma
# Q2: Sum of digits of a number

# def number_sum(num):
#     total = 0
#     while num > 0:
#         total += num % 10
#         num //= 10
#     return total

# # Example
# n = int(input("Enter a number: "))
# print("Sum of digits:", number_sum(n))


# def factorial(n):

#     fact = 1

#     for i in range(1, n + 1):

#         fact *= i

#     return fact



# # Example​

# num = int(input("Enter a number: "))

# print("Factorial:", factorial(num))

# def prime_number(n):
#     if n <= 1:
#         return "Not Prime"
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return "Not Prime"
#     return "Prime"

# # Example
# num = int(input("Enter a number: "))
# print(num, "is", prime_number(num))

# Explanation:
# Checks divisibility up to √n. If divisible by any number, it’s not prime.
# square = lambda x: x ** 2
# add = lambda a, b: a + b

# # Example
# print("Square of 5:", square(5))
# print("Addition of 10 and 20:", add(10, 20))

# Explanation:
# Anonymous (lambda) functions for quick single-line operations.
# numbers = [10, 20, 30]
# print("Original list:", numbers)

# # Append
# numbers.append(40)
# numbers.append(50)

# # Remove
# numbers.remove(20)

# # Sort descending
# numbers.sort(reverse=True)

# # Sum and Average
# total = sum(numbers)
# average = total / len(numbers)

# print("Updated list:", numbers)
# print("Sum:", total, "Average:", average)

# Explanation:
# Demonstrates basic list operations: add, remove, sort, and compute total and average.

# my_tuple = (10, 20, 30, 40, 50)

# # Indexing
# print("First item:", my_tuple[0])

# # Slicing
# print("Slice (1:4):", my_tuple[1:4])

# # Unpacking
# a, b, c, d, e = my_tuple
# print("Unpacked values:", a, b, c, d, e)

# Explanation:
# Shows tuple indexing, slicing a part of it, and unpacking into variables.
# fruits = {"apple", "banana", "mango", "apple"}  # Duplicate 'apple' ignored automatically
# print("Initial set:", fruits)

# # Add a new fruit
# fruits.add("orange")

# # Remove one fruit
# fruits.remove("banana")

# print("Updated set:", fruits)

# Explanation:
# Sets automatically remove duplicates. Demonstrates adding and removing elements.

# students = {"Ravi": 85, "Neha": 92, "Amit": 78}

# # Add new entry
# students["Kiran"] = 88

# # Update marks
# students["Ravi"] = 90

# # Delete entry
# del students["Amit"]

# # Highest scorer
# topper = max(students, key=students.get)

# print("Students data:", students)
# print("Topper:", topper, "with marks", students[topper])

# Explanation:
# Shows dictionary creation, update, deletion, and finding highest marks using max() with key.

def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return reverse

# Example
n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))

# Explanation:
# Extracts digits and rebuilds number in reverse order.





