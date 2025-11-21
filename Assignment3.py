# num = 1

# while num <= 100:

#     if num % 7 == 0:

#         print(num)

#     num += 1

# total = 0

# while True:

#     num = int(input("Enter a number: "))

#     total += num

#     if total > 100:

#         print("Sum exceeded 100. Stopping...")

#         break

# print("Final Sum:", total)

# text = input("Enter a string: ")

# for ch in text:

#     if ch == 'a':

#         continue

#     print(ch)

# correct_password = "python123"

# attempt = 0



# while attempt < 3:

#     password = input("Enter password: ")

#     if password == correct_password:

#         print("Login Successful")

#         break

#     else:

#         print("Incorrect password.")

#         attempt += 1

# else:

#     print("Account Locked")

# num = int(input("Enter a number: "))



# if num > 1:

#     for i in range(2, num):

#         if num % i == 0:

#             print(num, "is not a prime number")

#             break

#     else:

#         print(num, "is a prime number")

# else:

#     print("Number must be greater than 1")
# for i in range(1, 51):

#     if i % 2 == 0:

#         continue

#     print(i)


# for i in range(1, 11):

#     if i == 5:

#         pass  # Does nothing, just a placeholder​

#     print(i)


# num = int(input("Enter a positive integer: "))

# factorial = 1

# i = 1



# while i <= num:

#     factorial *= i

#     i += 1



# print("Factorial of", num, "is", factorial)

# for i in range(10, 0, -1):

#     print(i)

# print("Liftoff!")


# skip_num = int(input("Enter a number from 1 to 20: "))



# for i in range(1, 21):

#     if i == skip_num:

#         continue

#     print(i)
# def convert_temperature(temp):
#     celsius = (temp - 32) * 5/9
#     return celsius

# # Example
# f = float(input("Enter temperature in Fahrenheit: "))
# print("Temperature in Celsius:", convert_temperature(f))

# Explanation:
# Applies the formula (F - 32) x 5/9 to convert Fahrenheit to Celsius.
