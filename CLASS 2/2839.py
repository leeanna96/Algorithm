n=int(input())
t=0
f=0
if n%5==0:
    f=int(n/5)
    print(f)
else:
    f=int(n/5)
    n-=5*f
    if n%3==0:
        t=int(n/3)
        print(f+t)
    else:
        f-=1
        if f<0:
            print("-1")
        else:
            n+=5
            if n%3==0:
                t=int(n/3)
                print(f+t)
            else:
                f-=1
                if f<0:
                    print("-1")
                else:
                    n+=5
                    if n%3==0:
                        t=int(n/3)
                        print(f+t)
                    else:
                        print("-1")
