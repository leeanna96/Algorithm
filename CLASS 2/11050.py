def fact(n):
    sum=1
    for i in range(n,0,-1):
        if i==1:
            sum*=1
        else:
            sum*=i
    return sum

n,k=map(int,input().split())
res=fact(n)/(fact(n-k)*fact(k))
print(int(res))
