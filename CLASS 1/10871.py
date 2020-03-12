n,mini=input().split()
number=list(map(int, input().split()))
for i in range(int(n)):
    if number[i]<int(mini):
        print(number[i], end=" ")
