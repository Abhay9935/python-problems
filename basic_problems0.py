'How to find the average of "n" numbers in Python'
n = int(input("enter the no of elements: "))
total = 0
for i in range(n):
    num = float(input("enter the number: "))
    total+= num
    average = total/n
print("the average of the no. is : ", average)

'How to find the sum of first "n" natural numbers in Python'
n = int(input("enter the value of n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("the sum of first n natural numbers is: ", total)

'OR'

n = int(input("enter the value of n: "))
total = n * (n + 1) // 2
print("the sum of first n natural numbers is: ", total)

'find and calculate the factorial of a number in Python'
n = int(input("enter the number to calculate factorial: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print("the factorial of the number is: ", factorial)

'find and calculate square root of a number in Python'
n = float(input("enter the number to calculate the square root: "))
square_root = n ** 0.5
print("the square root of the number is: ", square_root)

'how to find the area of the triangle'
b = float(input("enter the length of the base"))
h = float(input("enter the lenght of height"))
area = 0.5 * b * h
print("area of triangle is: ", area)


'how to check a number is positive, negative or zero'
x = int(input("enter the no.: "))
if x == 0:
    print("the number is zero")
elif x > 0:
    print("the no. is positive")
else:
    print("the no. is negative")

'how to check leap year'
year = int(input("enter the year: "))
if year % 400 == 0:
    print("leap yaer")
elif year % 100 == 0:
    print("not leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("not leap year")


'how to check the no is prime or not'
n = int(input("enter the number:"))
if n == 1:
    print("not prime")
else:
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            print("not prime")
            break
    else:
     print("prime")


'print multiplication table'
n = int(input("enter the no.: "))
for i in range(1, 11):
    mul = i * n
    print(n, "X", i, "=", mul)

'program to find factors of a no.'
numbers = list(map(int, input("Enter the number: ").split()))
all_factor = []
for num in numbers:
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    all_factor.append(factors)
print("Factors: ", all_factor)


'find HCF or GCD'
Numbers input
numbers = list(map(int, input("Enter numbers: ").split()))

all_factors = []

for num in numbers:
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    all_factors.append(factors)

print("Factors:", all_factors)

common_factors = []

for factor in all_factors[0]:
    common = True

    for factors in all_factors:
        if factor not in factors:
            common = False
            break

    if common:
        common_factors.append(factor)

print("Common factors:", common_factors)

gcd = max(common_factors)

print("GCD:", gcd)

