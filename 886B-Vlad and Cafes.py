n=int(input())
x=list(map(int,input().split()))
distfind = [n for i in range(20000000)]
minimumnum=n
for i in range(len(x)):
    distfind[x[i]]=i
distfind.sort()
print(x[distfind[0]])