count=int(input())
s1=[]
s2=[]
for i in range(count):
    height,width,num=map(int,input().split())
    if num%height==0:
        a=height
        b=int(num/height)
    else:
        a=num%height
        b=int(num/height)+1
    s1.append(str(b))
    s2.append(str(a))

for i in range(count):
    print(s2[i]+s1[i].zfill(2))

