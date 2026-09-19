'Function for calculate simple intrest'
def simple_intrest(p, r, t):
    SI = (p * r * t)/100
    return SI

print(simple_intrest(10, 20, 30))  #example


'Find Largest no.'
def largest_number(a, b, c, d):
    LN = max(a, b, c, d)
    return LN

print(largest_number(1, 2, 3, 4))   #example

'OR'

def largest_no():
    numbers = list(map(int, input("Enter numbers: ").split()))
    Ln = max(numbers)
    return Ln

print(largest_no())    #example


'function for factorial'
def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return(factorial)

print(factorial(5))   #example


'function count digits that returns the number of digits.'
def count_digit(n):
    count = 0
    while n > 0:
       n = n//10
       count += 1
    return(count) 

print(count_digit(123345676))  # example


'function for prime that checks whether a number is prime.'
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# example
n = int(input("Enter a number: "))  
if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")


