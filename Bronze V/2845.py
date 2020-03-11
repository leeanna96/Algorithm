n=[1,2,3,4,5]
p,s=input().split()
num=int(p)*int(s)
n[0],n[1],n[2],n[3],n[4]=input().split()
for i in range(5):
    n[i]=int(n[i])
for i in range(5):
    n[i]-=num
    print(n[i], end=" ")
