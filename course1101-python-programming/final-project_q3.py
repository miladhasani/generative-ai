import math

n = int(input())
p = math.ceil(math.log2(n))
if p < 7: 
    print(2**7)
else:
    print(2**p)