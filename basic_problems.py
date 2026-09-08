# How to find the average of "n" numbers in Python
# n = int(input("enter the no of elements: "))
# total = 0
# for i in range(n):
#     num = float(input("enter the number: "))
#     total+= num
#     average = total/n
# print("the average of the no. is : ", average)

# How to find the sum of first "n" natural numbers in Python
# n = int(input("enter the value of n: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print("the sum of first n natural numbers is: ", total)

#OR

# n = int(input("enter the value of n: "))
# total = n * (n + 1) // 2
# print("the sum of first n natural numbers is: ", total)

#find and calculate the factorial of a number in Python


n = int(input("enter the number to calculate factorial: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print("the factorial of the number is: ", factorial)
