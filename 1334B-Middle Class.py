t=int(input())
for i in range(t):
    n=list(map(int,input().split()))
    x=list(map(int,input().split()))
    x.sort()
    count=0
    s=0
    sum=0
    for j in range(n[0]-1,-1,-1):
        sum+=x[j]
        s+=1
        if (sum/s)>=n[1]:
            count+=1
        else:
            break
    print(count)