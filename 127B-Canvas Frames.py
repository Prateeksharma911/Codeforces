n=int(input())
x=list(map(int,input().split()))
sum=0
s=[0 for i in range(101)]
for i in range(n):
    s[x[i]]+=1
    if s[x[i]]%2==0 and s[x[i]]>0:
        sum+=1
print(sum//2)