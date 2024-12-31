import pandas as pd
try:
    df=pd.read_csv("school.csv")
except:
    df=pd.DataFrame(columns=['id','name','english','nepali','maths','science','percentage'])

def add_data():
  l=len(df)
  id=int(input("Enter id: "))
  name=input("Enter name: ")
  english=float(input("Enter marks of English: "))
  nepali=float(input("Enter marks of Nepali: "))
  maths=float(input("Enter marks of Maths: "))
  science=float(input("Enter marks of Science: "))
  percentage=round((english+nepali+maths+science)/400 * 100,2)
  df.loc[l]=[id,name,english,nepali,maths,science,percentage]
  print(df)

def remove_data(id):
  global df
  if id in list(df['id']):
    df=df.drop(df[df['id']==id].index)
    print("Data Removed!!!")
    print(df)
  else:
    print("Invalid id, Enter again\n")

def access_data(id):
  if id in list(df['id']):
    print(df[df['id']==id])
  else:
    print("Invalid id, Enter again\n")


def sorting_data():
  choice=input("Which way do you want to sort\n1. ascending\n2. descending\nEnter: ")
  if choice=='1':
    print(df.sort_values('percentage',ascending=True))
  elif choice=='2':
    print(df.sort_values('percentage',ascending=False))
  else:
    print("Invalid Syntax!!!")

def topper():
  print("The topper of the class is: ",df[df['percentage']==(df['percentage'].max())])

def view():
  print(df)
  
def average_marks():
  print("The average marks is: ",df['percentage'].mean())

while True:
  choice=input("Welcome to pandas school\n1. Add data\n2. Remove data\n3. Access data by id\n4. Sort the data and display\n5. Topper of the class\n6. Average marks\n7. View the data\n8. Quit\nEnter: ")
  if choice=='8':
    df.to_csv('school.csv',index=False)
    break
  elif choice=='1':
    add_data()
  elif choice=='2':
    id=int(input("Enter your id to remove the data: "))
    remove_data(id)
  elif choice=='3':
    id=int(input("Enter your id to access the data: "))
    access_data(id)
  elif choice=='4':
    sorting_data()
  elif choice=='5':
    topper()
  elif choice=='6':
    average_marks()
  elif choice=='7':
    view()
  else:
    print("Invalid!! enter again\n")