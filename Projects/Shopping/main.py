import pandas as pd
import json

class Shopping():
    def __init__(self):
        try:
            with open("data.json", "r") as f:
                self.item=json.load(f)
        except:
            self.item={'Snacks':{'Lays':[40,100],'Biscuit':[50,100],'Chocolate':[80,100],'Juice':[20,100],'Coke':[65,100]},
                    'Personal Care':{'Soap':[30,100],'Shampoo':[100,100],'Toothpaste':[30,100],'Face Wash':[120,100],'Deodorant':[130,100]},
                    'Grocery':{'Milk':[50,100],'Rice':[1500,100],'Oil':[120,100],'Coffee':[70,100],'Butter':[40,100]},
                    'Electronics':{'Mobile':[3000,100],'Charger':[150,100],'Mouse':[130,100],'Laptop':[15000,100],'Battery':[200,100]}}
            with open("data.json", "w") as f:
                    json.dump(self.item, f, indent=4)
        self.ItemName=None
        self.price=None
        self.quantity=None
        self.boughtSomething=False
        self.purchaseList=[]
        self.isbillPaid=False

    def role(self):
        choice=int(input("Enter as Customer/Owner: \n1.Owner\t2.Customer\nEnter: "))
        if choice==1:
            self.ownerRoles()
        elif choice==2:
            self.customerRoles()
        else:
            print("Invalid Option Selected!!!")
            self.role()

    def ownerRoles(self):
        choice=int(input("What do you want to do\n1.Edit\t2.Check Transactions\t3.Exit\nEnter: "))
        if choice==1:
            self.editStock()
        elif choice==2:
            self.checkTransactions()
        elif choice==3:
            self.saveStocks()
            exit()
        else:
            print("Invalid option selected!!!")
            self.ownerRoles()

    def customerRoles(self):
        choice=int(input("What do you want to do\n1.Purchase\t2.Billing\t3.Exit\nEnter: "))
        if choice==1:
            self.makePurchase()
        elif choice==2:
            self.billing()
        elif choice==3:
            if self.isbillPaid:
                self.saveStocks()
                exit()
            else:
                print("First make your bill and pay the amounts.")
                self.customerRoles()
        else:
            print("Invalid number clicked!")
            self.customerRoles()

    def editStock(self):
        print("Choose Category: ")
        count=1
        for x,y in self.item.items():
            print(f"{count}.{x}",end="\t")
            count+=1
        index=int(input("\nEnter: "))
        while(index>=count):
            print("Invalid Input!!!")
            index=int(input("Enter again: "))

        stock=list(self.item.keys())
        print("What do you want to edit: ")
        counts=1
        for x,y in self.item[stock[index-1]].items():
            print(f"{counts} {x}",end="\t")
            counts+=1
        finalStock=list(self.item[stock[index-1]].keys())
        finalIndex=int(input("Enter: "))

        while(finalIndex>=counts):
            print("Invalid Input!!!")
            index=int(input("Enter again: "))

        valueChange=int(input("Enter what do you want to change: \n1.Price\t2.Stock\t3.Exit\nEnter: "))
        if valueChange==1:
            newprice=int(input("Enter the new price: "))
            if(newprice>0):
                self.item[stock[index-1]][finalStock[finalIndex-1]][0]=newprice
                print("Price has been set to ",newprice)
                self.saveStocks()
            else:
                print("Invalid self.price")
        
        elif valueChange==2:
            newStock=int(input("Enter the new stock remaining: "))
            self.item[stock[index-1]][finalStock[finalIndex-1]][1]=newStock
            print("Stock has been set to ",newStock)
            self.saveStocks()
        
        elif valueChange==3:
            self.saveStocks()
            self.ownerRoles()
        else:
            print("Invalid Code Entered!!!")

    def makePurchase(self):
        lst=[]
        print("Choose a Category: ")
        count=1
        for x,y in self.item.items():
            print(f"{count}.{x}",end="\t")
            count+=1
        index=int(input("\nEnter: "))
        stock=list(self.item.keys())

        while(index>=count):
            print("Invalid Input!!!")
            index=int(input("Enter again: "))

        print("What do you want to buy: ")
        counts=1
        for x,y in self.item[stock[index-1]].items():
            print(f"{counts} {x} (Price: {y[0]})",end="\t")
            counts+=1
        
        finalStock=list(self.item[stock[index-1]].keys())
        finalIndex=int(input("Enter: "))
        while(finalIndex>=counts):
            print("Invalid Input!!!")
            finalIndex=int(input("Enter again: "))

        self.ItemName=finalStock[finalIndex-1]
        self.price=self.item[stock[index-1]][finalStock[finalIndex-1]][0]
        stockQuantity=self.item[stock[index-1]][finalStock[finalIndex-1]][1]
        self.quantity=int(input("Enter quantity: "))
        
        if(self.quantity>stockQuantity):
            self.quantity=int(input(f"Sorry we donot have that much stock remaining! We only have {stock} remaining.\nEnter new quantity: "))
        
        print(f"You have purchased {self.quantity} {self.ItemName}")
        if self.quantity>0:
            lst.append(self.ItemName)
            lst.append(self.price)
            lst.append(self.quantity)
        self.item[stock[index-1]][finalStock[finalIndex-1]][1]=self.quantity
        self.boughtSomething=True
        
        self.purchaseList.append(lst)
        choiceyn=input("Do you want to make another purchase(y/n): ").lower()
        if(choiceyn=='y'):
            self.makePurchase()
        else:
            self.customerRoles()

    def saveStocks(self):
        with open("data.json", "w") as f:
            json.dump(self.item, f, indent=4)

    def billing(self):
        if self.boughtSomething:
            print("Your bill: ")
            print("Item | Price | Quantity | Amount")
            print("----------------------------------------")
            total=0
            for x in self.purchaseList:
                print(x[0],"|",x[1],"|",x[2],"|",x[1]*x[2])
                total+=x[1]*x[2]
            print("Total: ",total)

            payment=int(input("\nEnter the cash enter: "))
            returns=payment-total

            while(returns<0):
                payment=int(input("This amount is less than your bill amount.Enter again: "))
                returns=payment-total

            self.isbillPaid=True
            if returns>0:
                print("Here is your returns! $",returns)
            try:
                df=pd.read_csv("billing.csv")
                Billno=sorted((df['Billno'].unique()).tolist())[-1]+1
            except:
                df=pd.DataFrame(columns=['Billno','Amount'])
                Billno=101
            l=len(df)
            df.loc[l]=[Billno,total]
            df.to_csv('billing.csv',index=False)
            # print(df)
            self.saveStocks()

        else:
            print("Purchase something for Bill.")

        # print(self.ItemName,self.price,self.quantity)
    def checkTransactions(self):
        try:
            df=pd.read_csv('billing.csv')
            print(df)
        except:
            print("No transaction detected")
    


s1=Shopping()
s1.role()
# s1.billing()