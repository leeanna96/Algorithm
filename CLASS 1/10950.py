n=int(input())
num=[]
for i in range(n):
    a,b=map(int,input().split())
    num.append(a+b)
for i in range(n):
    print(num[i])
