def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. Exit")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        itemPrice = int(input("ราคาสินค้า"))
        print("ราคาร่วมภาษี",vatCalculator(itemPrice))
    elif userSelected == 2:
        print("ราคารวมสินค้าร่วมภาษี",priceCalculator())
    elif userSelected == 3:
        print("Thank You")
    else :
        print("Try Again")
        return showMenu()

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)
login()