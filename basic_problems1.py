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