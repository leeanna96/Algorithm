s_list=[0,0,0,0]
sum=0
for i in range(4):
    s_list[i]=int(input())
    sum+=s_list[i]
print(int(sum/60), sum%60)
