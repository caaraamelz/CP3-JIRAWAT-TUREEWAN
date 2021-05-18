menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
    print("total :", totalPrice)

while True :
    menuName = input("Pleae enter menu")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price")
        menuList.append([menuName,menuPrice])

showBill()

