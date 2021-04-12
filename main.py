from LoginInfo import LoginInfo
import random
import string

def generatePassword(obj):
    l=int(input("Enter length of password: "))
    upper=int(input("Enter number of uppercase characters: "))
    lower=int(input("Enter number of lowercase characters: "))
    digits=int(input("Enter number of digits: "))
    special=int(input("Enter number of special characters: "))
    password=""
    length=0
    for i in range(upper):
      length+=1
      char=random.choice(string.ascii_uppercase)
      password+=char
    for i in range(lower):
      length+=1
      char=random.choice(string.ascii_lowercase)
      password+=char
    for i in range(digits):
      length+=1
      char=random.choice(string.digits)
      password+=char
    for i in range(special):
      length+=1
      char=random.choice(string.punctuation)
      password+=char

    # This loop will fill the password with random letters if it is less than the minimum length
    for i in range(l-length):
      char=random.choice(string.ascii_letters)
      password+=char

    print("Your password is " + password + " and is now stored in the valut")
    obj.setPassword(password)


logins = []
selection = 0
while(selection!=(-1)):
  print("1 - Generate Password")
  print("2 - Lookup Password")
  selection=int(input("Enter choice (-1 to exit): "))
  if selection==1:
    site=input("Enter site: ")
    login = input("Enter login: ")
    loginInfo = LoginInfo(site,login)
    generatePassword(loginInfo)
    logins.append([loginInfo.getSiteName(),loginInfo.getLogin(),loginInfo.getPassword()])
  elif selection==2:
    site=input("Enter site: ")
    found = False
    for info in logins:
      if info[0]==site:
        print("Your login for " + site + " is " + info[1] + " and the password is " + info[2])
        found=True
        break
    if not found:
      print("Site is not in the list")
