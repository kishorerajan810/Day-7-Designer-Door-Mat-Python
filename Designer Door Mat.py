a,b=map(int,input("enter :").split())
for i in range(1,(a//2)+1):
    x=(b//3)-(i*3)+7
    y=((i*3)-2+i)//2
    print(x*'-',end="")
    print('.|.'*y,end="")
    print(x*'-',end="")
    print()
print(a*'-'+'WELCOME'+a*'-')
for i in reversed(range(1,(a//2)+1)):
    x=(b//3)-(i*3)+7
    y=((i*3)-2+i)//2
    print(x*'-',end="")
    print('.|.'*y,end="")
    print(x*'-',end="")
    print()
