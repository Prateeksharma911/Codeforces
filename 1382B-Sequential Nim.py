t=int(input())
for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    number=0
    for j in range(n):
        number+=1
        if x[j]>1:
            break
    if number%2==0:
        print('Second')
    else:
        print('First')