from datetime import datetime
from Operation import readItems, writeTransaction, updateItems, writeInvoice

def rentEquipments():
    itemsData = readItems("Items.txt")

    print("Items available in Kathmandu Equipment Shop")
    print("---------------------------")
    print("Sn, Name, Brand, Price, Quantity")

    for item in itemsData:
        print("{0}\t{1}\t{2}\t${3:.2f}\t{4}".format(item["SN"], item["Name"], item["Brand"], item["Price"], item["Quantity"]))

    selectedProduct = int(input("Enter the product index (SN) to rent: ")) - 1
    try:
        if 0 <= selectedProduct < len(itemsData):
            selectedItems = itemsData[selectedProduct]
            availableQuantity = selectedItems["Quantity"]

            quantityToRent = int(input("Enter the quantity to rent: "))

            if 1 <= quantityToRent <= availableQuantity:
                customerName = input("Enter your name: ")

                totalAmount = selectedItems["Price"] * quantityToRent
                order_summary(selectedItems, customerName, quantityToRent, totalAmount)

                confirmation = input('Confirm the rental (yes/no): ').lower()

                if confirmation == "yes":
                    selectedItems["Quantity"] -= quantityToRent
                    writeTransaction("Transactions.txt", f"{selectedItems['SN']},{selectedItems['Name']},{selectedItems['Brand']},{quantityToRent},{totalAmount}")
                    updateItems("Items.txt", itemsData)
                    invoice = f"Customer: {customerName}\nEquipment Rented: {selectedItems['Name']} ({quantityToRent} pcs)\nDate: {str(datetime.now())}\nAmount: ${totalAmount:.2f}\n"
                    writeInvoice("Invoice.txt", invoice)  # Append invoice to "Invoice.txt"
                    print("Rental successful. Invoice generated.")
                    print(invoice)
                else:
                    print("Rental canceled.")
            else:
                print("Insufficient stock.")
        else:
            print("Invalid product index.")
    except Exception as e:   
        print("An error ocurred.", e)
        
def order_summary(item, customerName, quantityToRent, totalAmount):
    print("---------------")
    print("\t\t Kathmandu Equipments Shop")
    print("-----------------------------")
    print("Order Summary\tDate: {}".format(str(datetime.now())))
    print("Customer Name: {}".format(customerName))
    print("Product Name: {}".format(item["Name"]))
    print("Brand: {}".format(item["Brand"]))
    print("Quantity Rented: {}".format(quantityToRent))
    print("Price: ${}".format(item["Price"]))
    print("Total Amount: ${}".format(totalAmount))
    print("-------------------------------------")