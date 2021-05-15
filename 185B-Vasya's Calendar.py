days=int(input())
months=int(input())
x=list(map(int,input().split()))
total=0
for i in range(months-1):
    total+=days-x[i]
print(total)