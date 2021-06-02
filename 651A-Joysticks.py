x=list(map(int,input().split()))
if x[0]==1 and x[1]==1:
    print(0)
else:
    count=0
    while x[0]>0 and x[1]>0:
        if x[0]>x[1]:
            x[0]-=2
            x[1]+=1
        else:
            x[0]+=1
            x[1]-=2
        count+=1
    print(count)