house = int(input("What is your addmission number? "))

match house % 4:
    case 1:
        print("You are in house Maroon")
    case 2:
        print("You are in house Blue")
    case 3:
        print("You are in house Yellow")
    case 4:
        print("You are in house Green")
    case _: 
        print("Invalid addmission number")