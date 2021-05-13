n=int(input())
x=list(map(int,input().split()))
distfind = [n for i in range(n)]

for i in range(n):
    distfind[x[i]-1]=i

distfind.sort()
print(x[distfind[0]])