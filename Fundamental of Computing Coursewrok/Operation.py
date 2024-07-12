def readItems(itemsFile):
    itemsData = []
    with open(itemsFile, "r") as data:
        for line in data:
            sn, name, brand, price, quantity = line.strip().split(",")
            itemsData.append({"SN": int(sn), "Name": name, "Brand": brand, "Price": float(price), "Quantity": int(quantity)})
    return itemsData

def writeTransaction(transactionFile, transaction):
    with open(transactionFile, "a") as f:
        f.write(transaction + "\n")

def updateItems(itemFile, updateItemData):
    with open(itemFile, "w") as data:
        for item in updateItemData:
            line = "{},{},{},{},{}".format(item["SN"], item["Name"], item["Brand"],  item["Price"],item["Quantity"])
            data.write(line + "\n")

def readTransaction(transactionFile):
    transactionData = []
    with open(transactionFile, "r") as data:
        for line in data:
            try:
                sn, name, brand, quantity, price = line.strip().split(",")
                transactionData.append({"SN": int(sn), "Name": name, "Brand": brand, "Quantity": int(quantity), "Price": float(price)})
            except ValueError:
                print("Error processing line: ", line.strip())
    return transactionData

def writeInvoice(invoiceFile, invoice):
    with open(invoiceFile, "a") as f:
        f.write(invoice + "\n")

def calculateFine(returnDate, dueDate, finePerDay):
    daysLate = (returnDate - dueDate).days
    if daysLate > 0:
        return daysLate * finePerDay
    return 0
