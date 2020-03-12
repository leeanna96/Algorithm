n=int(input())
score=[]
sum=0
total_sum=0
score=list(map(int, input().split()))
for i in range(n):
    sum+=score[i]
total_sum=sum*100/max(score)
print(total_sum/n)
