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