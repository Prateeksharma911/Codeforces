t=int(input())
for i in range(t):
    n=list(map(int,input().split()))
    firstproduct=0
    secondproduct=0
    num1=max((n[0]-n[4]),n[2])
    remain1=n[4]-(n[0]-num1)
    num2=max((n[1]-remain1),n[3])
    firstproduct=num1*num2
    num22=max((n[1]-n[4]),n[3])
    remain11=n[4]-(n[1]-num22)
    num11=max((n[0]-remain11),n[2])
    secondproduct=num11*num22
    print(min(firstproduct,secondproduct))