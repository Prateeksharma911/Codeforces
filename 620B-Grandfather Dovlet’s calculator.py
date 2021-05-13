num=[6,2,5,5,4,5,6,3,7,6]
x=list(map(int,input().split()))
total=0
for i in range(x[0],x[1]+1):
    if i > 9:
        number=i
        while(number):
            r=number%10
            total+=num[r]
            number=number//10
    else:
        total+=num[i]
print(total)