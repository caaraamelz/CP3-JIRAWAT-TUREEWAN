snack = 10
water = 7
soda = 15
candy = 3
username = input("USERNAME : ")
password = input("PASSWORD : ")
if username == "hello" and password == "55555" :
    print("WELCOME !!")
    print("1. snack = 10 THB")
    print("2. water = 7 THB")
    print("3. soda  = 15 THB")
    print("4. candy = 3 THB")
    userSelected = int(input("pick "))
    if userSelected == 1:
        price1 = snack*int(input("amout :"))
        print(price1,"THB")
    elif userSelected == 2:
        price2 = water*int(input("amout :"))
        print(price2,"THB")
    elif userSelected == 3:
        price3 = soda*int(input("amout :"))
        print(price3,"THB")
    elif userSelected == 2:
        price4 = candy*int(input("amout :"))
        print(price4,"THB")
else:
    print("Try Again !!")