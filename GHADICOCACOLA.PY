amount_maney=50
accepted_coins=[25,10,5]
while amount_maney>0 :
    print(amount_maney)
    coin= int(input("enter value of coin(25,10,5)"))
    if coin in accepted_coins :
        amount_maney-=coin
    if amount_maney<=0 :
        break
change=abs(amount_maney)
if change>0 :
    print(f"change is:{change}cents")
else :
    print("no change is owed:")