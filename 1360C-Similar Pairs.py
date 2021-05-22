t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    even=0
    odd=0
    for j in range(len(x)):
        if x[j]%2==0:
            even+=1
        else:odd+=1
    if even%2!=odd%2:print('NO')
    else:
        if even%2==0:
            print('YES')
        else:
            out=0
            for i in range(n):
                for j in range(i+1,n):
                    if x[i]%2!=x[j]%2 and abs(x[i]-x[j])==1:
                        print('YES')
                        out=1
                        break
                if out==1:
                    break
            if out!=1:print("NO")