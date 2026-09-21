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

'function that returns the second-largest unique number.'
def second_largest():
    numbers = list(map(int, input("Enter the numbers: ").split()))
    numbers.remove(max(numbers))  # remove largest
    second_largest_no = max(numbers)
    return second_largest_no


print(second_largest())


'defnition to check vowel and consonent in word'
s = input().lower()
def check_word(s):
    vowel_count = 0
    consonant_count = 0
    for i in s:
        if i in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)

check_word(s)


'Function that check word is palindrone or not'
s = input().lower()
def check_pel(s):
    if s[::-1] == s:
        print("palindone")
    else:
        print("not pallindrone")


check_pel(s)