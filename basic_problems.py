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

