'''
We are required to create saving deposit and withdrawal system similar to banking transation. Each client is registerned with name and phone number, the bank uses a 16 digit account number to identify the client and the bank offers basic deposit and withdrawal services. The bank requires a minimum balance of rs 500 across all accounts. In this system you are required to perform,
1.Help customers create their bank accounts
2.Enable customers to make deposits
3.Facilitae money withdrawal inbehalf of customer
'''
import json
import random
import pandas as pd
# df=pd.read_csv("data.csv")
try:
    df=pd.read_csv("data.csv")
except:
    df=pd.DataFrame(columns=['Accountnumber','Name','Age','PhoneNumber','Balance','Password'])
print(df.info())
choice=input("Enter what do you want to d\n1.Register\n2.Login\nEnter: ")
login=False
def account_number_generator():
    accountnumber=''
    for x in range(16):
        randomnum=random.randint(0,9)
        accountnumber+=str(randomnum)
    if accountnumber in df['Accountnumber']:
        account_number_generator()
    else:
        return accountnumber
def balance_check_alert(accountnumber):
    balance=0
    while True:
        if df.loc[accountnumber]['Balance']<500:
            balance=int(input(f"Insufficient Balance, Balace should be at least Rs. 500\nEnter(Current Balance: {df.loc[accountnumber]['Balance']}): "))

            df.loc[accountnumber,'Balance']+=balance
        else:
            break

if choice=='1':
    balance=0
    name=input("Enter your full name: ")
    age=int(input("Enter your age: "))
    phonenumber=input("Enter your phone number: ")
    password=input("Enter your 4pin password: ")
    accountnumber=account_number_generator()
    print("Your account number is",accountnumber)
    insert_df=[accountnumber,name,age,phonenumber,balance,password]
    l=len(df)
    df.loc[l]=insert_df
    df.set_index('Accountnumber',inplace=True)
    balance_check_alert(accountnumber)
    login=True

elif choice=='2':
    df.set_index('Accountnumber',inplace=True)
    while True:
        accountnumber=int(input("Enter your account number: "))
        password=int(input("Enter your password: "))
        try:
            if df.loc[accountnumber]['Password']==password:
                print('Login Successful!!!!!')
                login=True
                break
            else:
                print("Wrong password!!!!!")
                continueagain=input("Do you want to continue(y/n): ").lower()
        except:
            print("Account not found")
            continueagain=input("Do you want to continue(y/n): ").lower()
        if continueagain=='n':
            break


if login==True:
    choice1=input("Enter what do you want to do next\n1.Withdraw\n2.Deposit\n3.Transfer\n4.Quit\nEnter: ")
    if choice1=='1':
        amount=int(input("Enter the amount you want to deposit: "))
        password=int(input("Enter your password: "))
        while True:
            if df.loc[accountnumber]['Password']==password:
                df.loc[accountnumber,'Balance']-=amount
                print(f"Sucessfully added to your balance.\nYour current balance is {df.loc[accountnumber,'Balance']}")
                break
            else:
                password=int(input("Incorrect!!!! Enter your correct password: "))
        balance_check_alert(accountnumber)
    elif choice1=='2':
        amount=int(input("Enter the amount you want to withdraw: "))
        password=int(input("Enter your password: "))
        while True:
            if df.loc[accountnumber]['Password']==password:
                if amount<df.loc[accountnumber]['Balance']:
                    df.loc[accountnumber,'Balance']+=amount
                    print(f"Withdraw completed.\nYour current balance is {df.loc[accountnumber,'Balance']}")
                    break
                else:
                    print("No sufficient balance.")
            else:
                password=int(input("Incorrect!!!! Enter your correct password: "))
    elif choice1=='3':
        sender=accountnumber
        reciever=int(input("Enter the account number of reciever: "))
        amount=int(input("Enter the amount you want to transfer: "))
        password=int(input("Enter your password: "))
        while True:
            if df.loc[sender]['Password']==password:
                if amount < df.loc[sender]['Balance']:
                    df.loc[sender,'Balance']-=amount
                    df.loc[reciever,'Balance']+=amount
                    break
                else:
                    print("Insufficient Balance!!! Transcation Not completed")
                    break
            else:
                print("Wrong password!!!!")
                password=int(input("Enter your password: "))
        balance_check_alert(sender)
    elif choice1=='4':
        pass

df=df.reset_index()

print(df)
df.to_csv('data.csv',index=False)    