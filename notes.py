amount=int(input("enter amount:"))
if amount>=500:
    notes500=amount//500
    amount=amount%500
    print("500 notes:",notes500)
if amount>=200:
    notes200=amount//200
    amount=amount%200
    print("200 notes:",notes200)
if amount>=100:
    notes100=amount//100
    amount=amount%100
    print("100 notes:",notes100)
if amount>=50:
    notes50=amount//50
    amount=amount%50
    print("50 notes:",notes50)
if amount>=20:
    notes20=amount//20
    amount=amount%20
    print("20 notes:",notes20)
if amount>=10:
    notes10=amount//10
    amount=amount%10
    print("10 notes:",notes10)
if amount>=5:
    coins5 =amount//5
    amount=amount%5
    print("5 coins:",coins5)
if amount>=2:
    coins2=amount//2
    amount=amount%2
    print("2 coins:",coins2)
if amount>=1:
    coins1=amount//1
    amount=amount%1
    print("1 coins:",coins1)