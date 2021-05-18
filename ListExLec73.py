systemMenu = {"combo1": 120, "combo2": 150, "combo3": 200}
menuList = []


def showBill():
    totalPrice = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalPrice += int(menuList[number][1])
    print("total :", totalPrice)


while True:
    menuName = input("Pleae enter menu")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName.lower(), systemMenu[menuName.lower()]])

showBill()
