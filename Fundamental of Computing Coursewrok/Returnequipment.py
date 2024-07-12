from datetime import datetime, timedelta
from Operation import readItems, writeTransaction, updateItems, readTransaction, calculateFine


def returnEquipment():
    itemsData = readItems("Items.txt")
    transactionsData = readTransaction("Transactions.txt")

    print("Items available in Kathmandu Equipment Shop")
    print("----------------------------------------")
    print("SN\tName\tBrand\tQuantity\tPrice")

    for item in itemsData:
        print("{0}\t{1}\t{2}\t{3}\t${4:.2f}".format(item["SN"], item["Name"], item["Brand"], item["Quantity"], item["Price"]))

    selectedProduct = int(input("Enter the product index to return: ")) - 1

    if 0 <= selectedProduct < len(itemsData):
        selectedItems = itemsData[selectedProduct]
        customerName = input("Enter your name: ")
        quantityToReturn = int(input("Enter the quantity to return: "))
        daysRented = int(input("Enter the days rented: "))

        # Search for the transaction in the Invoice.txt file
        invoiceFile = "Invoice.txt"
        transactionFound = None
        with open(invoiceFile, "r") as f:
            for line in f:
                if f"Customer: {customerName}" in line and f"Equipment Rented: {selectedItems['Name']} ({quantityToReturn} pcs)" in line:
                    transactionFound = line
                    break

        returnDate = datetime.now()
        dueDate = returnDate - timedelta(days=5)
        finePerDay = 10
        fine = calculateFine(returnDate, dueDate, finePerDay)
        
        # Calculate fine based on days rented
        if daysRented > 5:
            additionalDays = daysRented - 5
            fine += finePerDay * additionalDays

        totalFine = fine * quantityToReturn
        
        selectedItems["Quantity"] += quantityToReturn
        if transactionFound is not None:
            transactionFoundParts = transactionFound.split(',')
            transactionFoundParts[3] = str(int(transactionFoundParts[3]) - quantityToReturn)
            updatedTransaction = ','.join(transactionFoundParts)

            with open(invoiceFile, "r") as f:
                lines = f.readlines()
            with open(invoiceFile, "w") as f:
                for line in lines:
                    if line.strip() != transactionFound.strip():
                        f.write(line)
                if int(transactionFoundParts[3]) > 0:
                    f.write(updatedTransaction + "\n")
        
        return_summary(selectedItems, customerName, fine, totalFine)
        confirm = input('Confirm the rental (yes/no): ').lower()
        if confirm == "yes":
            writeTransaction("Transactions.txt", f"{selectedItems['SN']},{selectedItems['Name']},{selectedItems['Brand']},{quantityToReturn},{selectedItems['Price']}")
            updateItems("Items.txt", itemsData)
            bill_invoice(selectedItems, totalFine, quantityToReturn,fine)
        else:
            print("Return canceled.")    
    else:
        print("Invalid product index.")

def return_summary(product, name, fine, totalFine):
    print("Return Summary\tDate: {}".format(str(datetime.now())))
    print("Customer Name: {}".format(name))
    print("Product Name: {}".format(product["Name"]))
    print("Fine: ${}".format(fine))
    print("Total Fine: ${}".format(totalFine))

def bill_invoice(product, totalFine, quantityToReturn, fine):
    print("\n" + "-" * 40)
    print("Bill Invoice for Returned Product")
    print("\n" + "-" * 40)
    print("Product Name: {}".format(product["Name"]))
    print("Brand: {}".format(product["Brand"]))
    print("Returned Quantity: {}".format(quantityToReturn))
    print("Price per Quantity: ${:.2f}".format(product["Price"]))
    print("Fine: ${:.2f}".format(fine))
    totalAmount = product["Price"] * quantityToReturn + totalFine
    print("Total Amount: ${:.2f}".format(totalAmount))
    print("," * 40)