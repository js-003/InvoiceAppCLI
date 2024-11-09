import datetime
_invoice = []
_service = []
_overallTotal = 0
_overallHours = 0
_overallDiscount = 0
_overallTax = 0
_tax = 0
_formatted = ""
_printter = ""
_invoiceNumber = 1
_prevInvoiceName = ""

def application():
    global _tax
    anotherService=""
    while anotherService.upper()!="N":
        print("Enter a service name: ")
        serviceName = input()
        print("Enter a hourly rate: ")
        rate = input()
        while(True):
            try:
                if(isinstance(float(rate),float)):
                    while(float(rate) <= 0):
                        print("Please enter a valid rate, any positive number:")
                        rate = input()
                break
            except: 
                print("Please enter a valid rate, any positive number:")
                rate = input()
        print("Enter the hours worked on this service:")
        hours = input()
        while(True):
            try:
                if(isinstance(float(hours),float)):
                    while(float(hours) <= 0):
                        print("Please enter a valid number of hours worked, any positive number:")
                        hours = input()
                break
            except:
                print("Please enter a valid number of hours worked, any positive number:")
                hours = input()
        print("Do you want to add a discount for this service? Y/N:")
        YN = input()
        while(True):
            if(YN.upper() == "Y"):
                print("Enter the discount without the % sign (eg. 20):")
                discount = input()
                while(True):
                    try:
                        if(isinstance(float(discount),float)):
                            while(float(discount) <= 0 or float(discount) > 100):
                                print("Please enter a valid discount amount, any positive number between 0 and 100:")
                                discount = input()
                        break
                    except:
                        print("Please enter a valid discount amount, any positive number between 0 and 100:")
                        discount = input()
                break
            elif(YN.upper() == "N"):
                discount = 0
                break
            else: 
                print("Incorrect input, please enter Y/N:")
                YN = input()        
        print("Do you want to add another service to the invoice? Y/N:")
        anotherService = input()
        while(anotherService.upper()!="N"):
            if(anotherService.upper()=="Y"):
                _service.append(serviceName +", "+str(rate)+", "+str(hours)+", "+str(discount))
                break
            else:
                print("Incorrect input, please enter Y/N:")
                anotherService = input()
    _service.append(serviceName +", "+str(rate)+", "+str(hours)+", "+str(discount))
    print("Do you want to add tax to the entire invoice? Y/N")
    YN = input()
    while(True):
        if(YN.upper()=="Y"):
            print("Enter the tax amount for the invoice without the % sign (eg. 10)")
            _tax = input()
            while(True):
                try:
                    if(isinstance(float(_tax),float)):
                        while(float(_tax) <= 0 or float(discount) > 100):
                            print("Please enter a valid tax amount, any positive number between 0 and 100: ")
                            _tax = input()
                    break
                except:
                    print("Please enter a valid discount amount, any positive number between 0 and 100:")
                    _tax = input()
            break
        elif(YN.upper()=="N"):
            _tax = 0
            break
        else:
            print("Incorrect input, please enter Y/N")
            YN = input()
    calculations()
    printing()

def calculations():
    global _overallTotal 
    global _overallHours
    global _overallDiscount
    global _formatted

    for entry in _service:
        result = entry.split(", ")
        total = (float(result[1]) * float(result[2]))
        
        _overallTotal += total
        _overallHours += float(result[2])
        if(float(result[3])!=0):
            _overallDiscount += float(total) * (float(result[3])/100) 
        rate = "€"+str(round(float(result[1]), 2))
        hours = str(round(float(result[2]), 2))
        discount = str(round(float(result[3]), 2))+"%"
        cost = "€"+str(round(total))+"\n"
        _formatted += f"{result[0] : <30}{rate : ^15}{hours : ^15}{discount : >12}{cost : >19}"

def printing():
    global _overallTotal 
    global _overallDiscount
    global _overallTax 
    global _overallHours
    global _formatted
    global _printter
    global _invoiceNumber
    global _prevInvoiceName
    date = datetime.datetime.now()
    splitter = '-'*90 + "\n"
    
    name = str(date.year)+str(date.month)+str(date.day)
    if(name == _prevInvoiceName):
        if(len(str(_invoiceNumber)) == 1):
            name += "-00"+str(_invoiceNumber)
        elif(len(str(_invoiceNumber)) == 2):
            name += "-0"+str(_invoiceNumber)
        else:
            _invoiceNumber = 1
            name += "-00"+str(_invoiceNumber)
    else: 
        _invoiceNumber = 1
        name += "-00"+str(_invoiceNumber)
    _prevInvoiceName = str(date.year)+str(date.month)+str(date.day)
    _invoiceNumber += 1
    headers = "Invoice Summary:\nInvoice Name: {0}\nInvoice Date: {1} \n\nService Details\n\n".format(name, date.strftime("%x"))+f"{'Service Name' : <30}{'Rate' : ^15}{'Hours' : ^15}{'Discount' : >15}{'Cost' : >15}"+"\n"
    subtotal = _overallTotal - _overallDiscount
    if(_tax !=0):
        _overallTax += subtotal*(int(_tax)/100)
    amountDue= subtotal+_overallTax
    end = "Total Hours Worked: {0}\nSubtotal: €{1}\nDiscount -€{2}\nAdjusted Subtotal: €{3}\nTax: €{4}\nAmount Due: €{5}\n".format(round(_overallHours,2),round(_overallTotal,2),round(_overallDiscount,2),round(subtotal,2),round(_overallTax,2),round(amountDue,2))
    _printter = headers + splitter + _formatted + splitter + end
    if(len(_invoice)>0):
        for invoice in _invoice:
            print(invoice)
    print(_printter)

application()

while(True):
    print("Do you want to create another invoice? Y/N")
    YN = input()
    if(YN.upper() == "Y"):
        _invoice.append(_printter)
        _service = []
        _overallTotal = 0
        _overallHours = 0
        _overallDiscount = 0
        _overallTax = 0
        _tax = 0
        _formatted = ""
        _printter = ""
        application()
    elif(YN.upper() == "N"):
        break
    else:
        print("Incorrect input, please enter Y/N")
        YN = input()