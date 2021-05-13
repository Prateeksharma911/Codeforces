x=list(map(int,input().split()))
value=0
mini=0
for i in range(x[0]):
    n=list(map(int,input().split()))
    mini=n[0]
    for j in range(x[1]):
        if mini>n[j]:
            mini=n[j]
    if value<mini:
        value=mini
print(value)