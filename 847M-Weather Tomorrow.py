n=int(input())
days=list(map(int,input().split()))
change=0
for i in range(n-1):
    if i==0:
        diff=days[i]-days[i+1]
    else:
        if diff!=days[i]-days[i+1]:
            change=1

if change==0:
    print(days[n-1]-diff)
else:print(days[n-1])