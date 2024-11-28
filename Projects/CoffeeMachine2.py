total_price=1900
total_cash=0
money_dict={'Five':0,'Ten':0,'Twenty':0,'Fifty':0,'Hundred':0,'Five_Hundred':0}
return_dict={'count':{'Five':0,'Ten':0,'Twenty':0,'Fifty':0,'Hundred':0,'Five_Hundred':0},'value':{'Five':5,'Ten':10,'Twenty':20,'Fifty':50,'Hundred':100,'Five_Hundred':500}}
def money():
    global total_cash
    for key,values in money_dict.items():
        Note=int(input(f"Enter the {key} note: "))
        money_dict[key]=money_dict[key]+Note
    cash_entered=money_dict['Five']*5+money_dict['Ten']*10+money_dict['Twenty']*20+money_dict['Fifty']*50+money_dict['Hundred']*100+money_dict['Five_Hundred']*500
    total_cash=total_cash+cash_entered
    extra=total_price-total_cash
    if total_price>total_cash:
        print("cash you entered",total_cash)
        print(f"Its {extra} less than what it requires, add more")
        money()
    elif total_price<total_cash:
        print("cash you entered",total_cash)
        print(f"You had {-extra} extra money")
        extra=-extra
        print("Return money: ")
        for key,value in reversed(return_dict['value'].items()):
            while extra>=value:
                extra=extra-value
                return_dict['count'][key]=return_dict['count'][key]+1
                if extra==0:
                    break
        print(return_dict)
    else:
        print("Transaction Completed")
        for key,values in money_dict.items():
            print(key,values)
        pass


money()
