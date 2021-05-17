n=list(map(int,input().split()))
start=1
start2=(n[0]*2)+1
sum=0
for i in range(n[0]*2):
    sum+=1
    if sum<=n[1]:
        if start2<=n[1]:
            print(start2,end=' ')
            start2+=1
        print(start,end=' ')
        start+=1
    else:break