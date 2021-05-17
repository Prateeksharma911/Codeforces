n=int(input())
drinkprices=list(map(int,input().split()))
drinkprices.sort()
prices=[0 for i in range(drinkprices[len(drinkprices)-1]+1)]
for i in range(n):
    prices[drinkprices[i]]+=1
sumi=0
for i in range(1,drinkprices[len(drinkprices)-1]+1):
    prices[i]+=prices[i-1]
x=int(input())
for i in range(x):
    coin=int(input())
    if coin>=len(prices):
        print(prices[len(prices)-1])
    else:print(prices[coin])