n=int(input())
num=[]
str=[]
for i in range(n):
    a,b=input().split()
    num.append(a)
    str.append(b)
for i in range(n):
    for j in str[i]:
        for t in range(int(num[i])):
            print(j, end="")
    print()
