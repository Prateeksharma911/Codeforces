t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    dp=[0]*(n+1)
    for j in range(len(x)-1,-1,-1):
        dp[j]=x[j]
        mn=j+x[j]
        if mn<n:
            dp[j]+=dp[mn]
    print(max(dp))