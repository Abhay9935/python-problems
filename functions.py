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

print(largest_no())