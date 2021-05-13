n=int(input())
x=input()
position=[0,0]
for i in range(n):
    if x[i]=='U':
        position[1]+=1
    if x[i]=='D':
        position[1]-=1
    if x[i]=='L':
        position[0]-=1
    if x[i]=='R':
        position[0]+=1
print(n-abs(position[0])-abs(position[1]))