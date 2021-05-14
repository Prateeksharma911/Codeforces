n=int(input())
b=[0]*1000000000

total=0
for i in range(n):
    m=list(map(int,input().split()))
    if b[m[0]]<m[1]:
        total+=m[1]-b[m[0]]
        b[m[0]]=m[1]
k=int(input())
for i in range(k):
    m=list(map(int,input().split()))
    if b[m[0]]<m[1]:
        total+=m[1]-b[m[0]]
        b[m[0]]=m[1]
print(total)

#In this i have no idea how to get a bigger list without getting runtime error.. sorry