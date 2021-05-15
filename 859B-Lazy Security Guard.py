import math
n=int(input())
total=0
if n==1:
    print(4)
elif n==2:
    print(6)
else:
    s=math.sqrt(n)
    snumber=math.floor(s)
    block=snumber*4
    noofblock=snumber**2
    noofblock=n-noofblock
    if noofblock>1:
        x=noofblock//snumber
        f=math.floor(noofblock/(snumber+1))+1
        block+=f*2
    elif noofblock==1:
        block+=2
    print(block)