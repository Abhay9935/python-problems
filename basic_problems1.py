'programe to make simple calculator'
print("=" * 40)
print(" " * 10, "DIGITAL CALCULATOR")
print("=" * 40)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Remainder")

choice = int(input("Enter your choice: "))

if choice == 1:
    result = num1 + num2
    print("Addition =", result)

elif choice == 2:
    result = num1 - num2
    print("Subtraction =", result)

elif choice == 3:
    result = num1 / num2
    print("Division =", result)

elif choice == 4:
    result = num1 * num2
    print("Multiplication =", result)

elif choice == 5:
    result = num1 % num2
    print("Remainder =", result)

else:
    print("Invalid choice")

'Write a program to calculate the sum of all even numbers from 1 to n.'
n = int(input("enter the no:"))
even_numbers = []
for i in range(1, n+1):
    if i % 2 == 0:
        even_numbers.append(i)
print("sum:",sum(even_numbers))

'Write a program to calculate the sum of the first n even numbers.'
n = int(input("enter the no :"))
sum = n*(n + 1)
print("sum:", sum)


'Write a program to count how many even and odd numbers are present in a list.'
n = list(map(int, input("enter the numbers with sapces:").split()))
even_count = 0
odd_count = 0
for i in range(1, len(n)+1):
    if i % 2 == 0:
       even_count += 1
    else:
        odd_count += 1
print("even count:", even_count, "odd count:", odd_count)

'Write a program to reverse a given number'
n = int(input("enter the no:"))
reversed = 0
while n > 0:
    digit = n % 10 
    reversed = reversed * 10 + digit
    n = n//10
print("reversed no:", reversed)


'Write a program to check whether a given number is a palindrome'
n = int(input("enter the no:"))
o = n
reversed = 0
while n > 0:
    digit = n % 10 
    reversed = reversed * 10 + digit
    n = n//10
if reversed == o:
    print("palindrome")
else:
    print("not palindrome")

'Write a Python program that takes a number from the user and checks whether it is a strong number.'
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

n = int(input("enter the no: "))
number = n
total = 0
while n > 0:
    digit = n % 10
    n = n//10

    total += factorial(digit)

if total == number:
    print("Strong No.")
else:
    print("not strong no")



'finds the sum of all digits of a number.'
n = int(input("enter the no"))
y = abs(n)
total = 0
while y > 0:
    digit = y % 10
    y = y//10
    total += digit
print(total)

'Check whether a number is an Armstrong number.'
n = int(input("enter the no: "))
y = abs(n)
digits = len(str(y))

def square(x):
    square = x**digits
    return square

number = y
total = 0
while y > 0:
    digit = y % 10
    y = y//10

    total += square(digit)

if total == number:
    print("Armstrong number")
else:
    print("Not Armstrong number")


'programe to print the first N Fibonacci numbers.'
n = int(input("Enter N: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


'check the no even or odd in list'
numbers = [12, 7, 8, 15, 20, 31, 44]
for i in range (len(numbers)):
    if numbers[i] % 2 ==0:
        print("even")
    else:
        print("odd")


'Frequency of Every Element'
numbers = list(map(int, input("enter the number with spaces: ").split()))
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
for num in frequency:
    print(num, ":", frequency[num])


'programe to remove All Occurrences'
numbers = list(map(int, input("Enter numbers:").split()))
newlist = []
for num in numbers:
    if numbers.count(num) == 1:
        newlist.append(num)
print(newlist)


'programme to check no is even or odd by binary check'
num = int(input("Enter a number: "))
if num & 1:
    print("Odd")
else:
    print("Even")

'Write a Python program using & to check whether Read Permission is ON or OFF.'
permission = int(input("Enter permission: "))
if permission & 1:
    print("Read permission is ON")
else:
    print("Read permission is OFF")