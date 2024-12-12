newpass=input("Enter your password: ")

while len(newpass)<8 or len(newpass)>12:
    print ("Error. Your password must be between 8 and 12 chr.")
    newpass=input("Re-Enter your password: ")

print("Your password is: ",newpass)