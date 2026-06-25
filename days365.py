day=int(input("enter days:"))
if day>0:
    if day>=365:
        years=day//365
        day=day%365
        print("years :",years)
    if day>=30:
        months=day//30
        day=day%30
        print("months :",months)
    if day>=7:
        weeks=day//7
        day=day%7
        print("weeks :",weeks)
    if day>=1:
        print("days :",day)
else:
    print("enter valid days")
