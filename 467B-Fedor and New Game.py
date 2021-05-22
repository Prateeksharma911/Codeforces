def decimalToBinary(n):
    return bin(n).replace("0b", "")

def split(word):
    return list(word)

x=list(map(int,input().split()))
binary=[0]*x[0]
inputnumber=[0]*(x[1]+1)
for i in range(x[1]+1):
    inputnumber[i]=int(input())
realnumber=inputnumber[x[1]]
count=0
for i in range(x[1]):
    diff=0
    f=decimalToBinary(realnumber^inputnumber[i])
    # print('f',f)
    for y in range(len(f)):
        if f[y]=='1':
            diff+=1
    if diff<=x[2]:
        count+=1
print(count)