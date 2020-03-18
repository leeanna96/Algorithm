s=[]
x,y,w,h=map(int, input().split())
s.append(abs(w-x))
s.append(abs(0-x))
s.append(abs(h-y))
s.append(abs(0-y))
print(min(s))

