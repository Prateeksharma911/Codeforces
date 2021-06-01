t=int(input())
for i in range(t):
    s=input()
    last=0
    maxn=0
    for j in range(len(s)):
        if s[j]=="R":
            if maxn<j+1-last:
                maxn=j+1-last
            last=j+1
    if maxn<len(s)+1-last:
        maxn=len(s)+1-last
    if maxn==0:
        print(len(s)+1)
    else:
        print(maxn)