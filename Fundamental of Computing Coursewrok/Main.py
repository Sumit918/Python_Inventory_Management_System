from Rentequipment import rentEquipments
from Returnequipment import returnEquipment

def mainmenu():
    print ("""
    ................................
    Welcome to Kathmandu Equipments Shop
    ................................
    1.Rent Equipments
    2.Return Equipments
    3.exit
    .................""")
    choice = int (input("Enter Your Option = "))
    selectedchoice(choice)
    
def selectedchoice(choice):
    try:
        if choice == 1:
            rentEquipments()
            mainmenu()
        elif choice == 2:
            returnEquipment()
            mainmenu()
        elif choice == 3:
            exit()
        else:
            print("invalid input.")
            mainmenu()
    except Exception as e:   
        print("An error ocurred.", e)
        mainmenu()
def exit():
    print("Exited Sucessfully")
    
if __name__ == "__main__":
    mainmenu()