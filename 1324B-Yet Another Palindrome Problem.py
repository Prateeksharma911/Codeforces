t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    palin=[0]*(n+1)
    non=0
    for j in range(n):
        if palin[x[j]]==0:
            palin[x[j]]=j+1
        else:
            if palin[x[j]]!=j:
                print('YES')
                non=1
                break
    if non==0:
        print('NO')

