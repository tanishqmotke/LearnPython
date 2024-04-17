
User = str(input("Enter the name:"))

match User:
    case "Om":
        print("You dont have the access Om")
    case "Tanu":
        print("You have the access")
    case _ :
        print("You dont have the access")