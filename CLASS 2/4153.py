def triangle(a,b,c):
    if a**2==(b**2+c**2):
        return True
    elif b**2==(a**2+c**2):
        return True
    elif c**2==(a**2+b**2):
        return True
    else:
        return False
a=1
b=1
c=1
s=[]
while True:
    a,b,c=map(int,input().split())
    if a==0 or b==0 or c==0:
        break
    if triangle(a,b,c)==True:
        s.append("right")
    else:
        s.append("wrong")
for i in s:
    print(i)

