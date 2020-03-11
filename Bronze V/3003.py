num_list=[1,1,2,2,2,8]
a,b,c,d,e,f=input().split()
num_list[0]-=int(a)
num_list[1]-=int(b)
num_list[2]-=int(c)
num_list[3]-=int(d)
num_list[4]-=int(e)
num_list[5]-=int(f)

for i in range(6):
    print(num_list[i], end=" ")

