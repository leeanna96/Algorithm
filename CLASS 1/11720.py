n=int(input())
number=int(input())
sum=0
for i in range(n):
    sum+=number%10
    number//=10
print(sum)
