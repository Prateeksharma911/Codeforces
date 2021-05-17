import math
n=int(input())
x=list(map(int,input().split()))
sumnum=0
number=[0,0,0,0]
for i in range(n):
    if x[i]==4:
        sumnum+=1
    elif x[i]==3:
        number[3]+=1
    elif x[i]==2:
        number[2]+=1
    elif x[i]==1:
        number[1]+=1

sumnum+=number[3]
sumnum+=number[2]//2
r=number[2]%2
if number[1]>number[3]:
    sumnum+=math.ceil(((r*2)+(number[1]-number[3]))/4)
else:
    sumnum+=r
print(sumnum)