def vatCalculete(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print(vatCalculete(int(input("Price"))))