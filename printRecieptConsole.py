# This prints out the details of transaction to console, for debug purposes

def printReceipt(receipt):
    print("item cost: " + str(receipt["item cost"]))
    print("shipping: " +  str(receipt["shipping"]))
    print("______________________________+")
    print("subtotal: ", end="")
    print(receipt["subtotal"])
    print("Tax %: ", end="")
    unformatedTaxPrecent = receipt["taxPercent"]
    percentage = round(unformatedTaxPrecent * 100, 2)
    print(f"{percentage:.2f}%")
    print("Tax amnt: ", end="")
    print(receipt["taxAmnt"])
    print("______________________________+")
    print("total: ", end="")
    print(receipt["total"])