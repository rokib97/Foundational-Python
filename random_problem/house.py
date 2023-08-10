name = input("Whats your name? ")

match name.lower():
    case "rokib":
        print("Rokib is doing good..")
    case "shakib":
        print("shakib is doing good..")
    case "sajid":
        print("shakib is doing good..")
    case _:
        print("who?..")