h,m=input().split()
h=int(h)
m=int(m)
if h==0 and m<45:
    h=23
    m+=15
elif m<45:
    h-=1
    m+=15
else:
    m-=45
print(h,m)
