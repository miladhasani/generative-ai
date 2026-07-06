import math

prime_factors = {}
n = int(input())
factor = 2

while factor <= math.ceil(math.sqrt(n)):
    while n % factor == 0:
        prime_factors[factor] = prime_factors.get(factor, 0) + 1
        n //= factor
    factor += 1

if n > 1:
    prime_factors[n] = prime_factors.get(n, 0) + 1

i = len(prime_factors)
for b, p in prime_factors.items():
    print(b , "^", p , sep="", end="")
    if i - 1 > 0: 
        print("*", end="", sep="")
    i -= 1