t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    abc=[0,0]
    note=0
    for j in range(n):
        if x[j]>y[j] and abc[0]==0:
            print('NO')
            note=1
            break
        elif x[j]<y[j] and abc[1]==0:
            print('NO')
            note=1
            break
        if x[j]==-1:abc[0]=1
        if x[j]==1:abc[1]=1
    if note==0:print('YES')