Dict={'pass':'pass','Expresso':'30-60-40','Mocha':'10-70-20','Cappuccino':'40-30-70','Americano':'20-50-50'}
ChoiceDict={'1':'Custom','2':'Expresso','3':'Mocha','4':'Cappuccino','5':'Americano'}
CustomerDict={}
Total=0
Price=0
Sn=1
discount=0
total_cash=0
money_dict={'Five':0,'Ten':0,'Twenty':0,'Fifty':0,'Hundred':0,'Five_Hundred':0}
return_dict={'count':{'Five':0,'Ten':0,'Twenty':0,'Fifty':0,'Hundred':0,'Five_Hundred':0},'value':{'Five':5,'Ten':10,'Twenty':20,'Fifty':50,'Hundred':100,'Five_Hundred':500}}
Stock={'Coffee':1000,'Milk':1000,'Water':1000}
def CoffeeChoice():
    global Choice
    print("---Menu---")
    for key,values in ChoiceDict.items():
        print(f"{key}. {values}")
    Choice=input("Enter your coffee preference: ")
    return Choice

def CustomCoffee():
    global Choice
    NewCoffee=input("Enter the name of your custom coffee: ")
    Coffee=input("Enter the amount of Coffee: ")
    Milk=input("Enter the amount of Milk: ")
    Water=input("Enter the amount of Water: ")
    Dict[NewCoffee]=Coffee+"-"+Milk+"-"+Water
    ChoiceDict[f'{len(ChoiceDict)+1}']=NewCoffee
    print("---Menu---")
    for key,values in ChoiceDict.items():
        print(f"{key}. {values}")
    Choice=input("Enter your coffee preference: ")
    if Choice=='1':
        CustomCoffee()
    return Choice

def StockInMachine(coffee,milk,water,quantity):
    global Stock
    global Price
    global Total
    global CustomerDict
    Stock['Coffee']-=float(coffee)*quantity
    Stock['Milk']-=float(milk)*quantity
    Stock['Water']-=float(water)*quantity
    print("Remaining stock in the machine: ",Stock)
    if Stock['Coffee']<0 or Stock['Milk']<0 or Stock['Coffee']<0:
        print("Sorry the stock for making this coffee is not enough! ")
        Stock['Coffee']+=float(coffee)*quantity
        Stock['Milk']+=float(milk)*quantity
        Stock['Water']+=float(water)*quantity
    else:
        Price=float(coffee)*2 + float(milk) * 6 + float(water)*3
        Total=Total+Price*Quantity
        if ChoiceDict[Choice] in CustomerDict:
            CustomerDict[ChoiceDict[Choice]]=[Price,CustomerDict[ChoiceDict[Choice]][1]+Quantity]
        else: 
            CustomerDict[ChoiceDict[Choice]]=[Price,Quantity]
while True:
    CoffeeChoice()
    if int(Choice)<1 or int(Choice)>len(Dict):
        while int(Choice)<1 or int(Choice)>len(Dict):
            CoffeeChoice()
    if Choice=='1':
        CustomCoffee()
    Quantity=int(input("Enter the quantity: "))
    coffee=Dict[ChoiceDict[Choice]].split('-')[0]
    milk=Dict[ChoiceDict[Choice]].split('-')[1]
    water=Dict[ChoiceDict[Choice]].split('-')[2]
    StockInMachine(coffee,milk,water,Quantity)
    
    conti=input("Do you want to add more coffee (Y/N): ")
    if conti.lower()=='n':
        break
CouponCheck=input("Enter Coupon: ")
if CouponCheck=='myshop123':
    discount=15
DiscountAmount=(discount*Total)/100
total_price=Total-DiscountAmount

def money():
    global total_cash
    for key,values in money_dict.items():
        Note=int(input(f"Enter the {key} note: "))
        money_dict[key]=money_dict[key]+Note
    total_cash=money_dict['Five']*5+money_dict['Ten']*10+money_dict['Twenty']*20+money_dict['Fifty']*50+money_dict['Hundred']*100+money_dict['Five_Hundred']*500
    extra=total_price-total_cash
    if total_price>total_cash:
        print("-----------------------------------")
        print("Total cash you entered",total_cash)
        print(f"Its {extra} less than what it requires, add more")
        print(money_dict)
        money()
    elif total_price<total_cash:
        print("-----------------------------------")
        print("The total bill amount was: ",total_price)
        print("The Cash you entered Rs",total_cash)
        print(f"You had Rs.{-extra} extra money")
        extra=-extra
        for key,value in reversed(return_dict['value'].items()):
            while extra>=value:
                extra=extra-value
                return_dict['count'][key]=return_dict['count'][key]+1
                if extra==0:
                    break
        print("-----------------------------------")
        print("Return money: ")
        for key,value in return_dict['count'].items():
            print(f"Note {key} Rupee: {value}")
        print("---Transaction Completed---\n      Visit Again")
    else:
        print("---Transaction Completed---\n      Visit Again")
        pass
def printing():
    global Sn
    print(f"{'-'*64}")
    print(f"| {'SN':<3} | {'Product':<18} | {'Price':<10} | {'Quantity':<8} | {'Total':<9} |")
    print(f"|{'-'*62}|")
    for name,quat in CustomerDict.items():
        print(f'| {Sn:<3} | {name:<18} | {quat[0]:<10} | {quat[1]:<8} | {quat[0]*quat[1]:<9} |')
        Sn+=1
    print(f"|{'-'*62}|")
    print(f"| {'  Total: ':<26} | {   Total:<32}|")
    print(f"|{'-'*62}|")
    print(f"| {'  Discount: ':<26} | {   DiscountAmount:<32}|")
    print(f"|{'-'*62}|")
    print(f"| {'  Final Price: ':<26} | {   Total-DiscountAmount:<32}|")
    print(f"{'-'*64}")
printing()
money()

