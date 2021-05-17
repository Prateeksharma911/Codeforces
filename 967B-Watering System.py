x=list(map(int,input().split()))
holes=list(map(int,input().split()))
total=0
sum=0
for i in range(x[0]):
    total+=holes[i]
initialhole=holes[0]
holes.sort()
point=0
for i in range(x[0]-1,-1,-1):
    if holes[i]==initialhole and point==0:
        point=1
    else:
        if ((initialhole*x[1])/total)<x[2]:
            total-=holes[i]
            sum+=1
        else:
            break
print(sum)