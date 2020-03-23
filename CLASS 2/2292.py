import math
def fac(n):
    i=0
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for j in range(n):
            if n<3*j**2-3*j+2:
                i=j
                break
        return math.trunc(i)
        
n=int(input())
print(fac(n))
