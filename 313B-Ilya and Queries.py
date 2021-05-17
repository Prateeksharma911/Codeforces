s=input()
n=int(input())
counting=[0 for i in range(len(s)+1)]
count=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    counting[i+1]=count
for i in range(n):
    x=list(map(int,input().split()))
    print(counting[x[1]-1]-counting[x[0]-1])