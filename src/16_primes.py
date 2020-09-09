"""
Prime numbers:
    - greater than 1
    - can only be divided evenly by themselves

Requirements:
    - Take in inputed num
    - Make sure it's greater than 1
    - loop through all nums from 2 to itself seeing if they are factors of inputed num (range and %)
    - if yes, return false, if no return true.
"""

def factorsOf(num):
    factors = []
    for x in range(2, num):
        if (num % x) == 0:
            factors.append(x)
    return factors

#print(factorsOf(25))

def isPrime(num):
    #need to add check to make sure num is greater than 1
    if len(factorsOf(num)) <= 0:
        return "Prime!"
    else:
        return "Not Prime!"

print(isPrime(17))


    