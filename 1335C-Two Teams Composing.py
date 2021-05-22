from collections import Counter
n=int(input())
for i in range(n):
    sizelist=int(input())
    x=list(map(int,input().split()))
    distinctcount=len(set(x))
    dublicate = Counter(x)
    minimum=0
    for j in dublicate:
        if minimum<dublicate[j]:
            minimum=dublicate[j]
            key=j
    if len(x)==1:
        print(0)
    else:
        if minimum==distinctcount:
            print(min(minimum,distinctcount)-1)
        else:
            print(min(minimum,distinctcount))