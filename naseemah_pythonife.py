item_names= {}
item_cp= {}
item_qty= {}
item_sp= {}
item_stock= {}
sales= {}
cart= {}   

def createStock():
    global item_names
    global item_cp
    global item_qty
    global item_sp

    sn= 1
    fo = open("data.csv","r")
    for line in fo.readlines():
        data= line.split(",")
        item_names[sn]= data[0].strip().replace("'","")
        item_qty[sn]= int(data[1].strip().replace("'",""))
        item_cp[sn]= float(data[2].strip().replace("'",""))
        item_sp[sn]= 1.1 * item_cp[sn]  #10% profit
        sn+=1
    fo.close()
    

def updateStock(serial, qty):
    global item_qty
    item_qty[serial] -= qty
    

def printStock():
    print("Stock with Cost price- ADMIN ONLY!!!!")
    print("SN"+ ". "+ "Name" + " "+ "CP" + " "+ "SP" + "  "+ "Qty")
    for key in item_names.keys():
         print(str(key)+ ". "+ item_names[key] + " "+ str(item_cp[key]) + " "+ str(item_sp[key]) + "  "+ str(item_qty[key]))

def printAvalableItems():
    print("SN"+ ". "+ "Name" + " "+ "Price")
    for key in item_names.keys():
        print(str(key)+ ". "+ item_names[key] + " "+ str(item_sp[key]))


def fillCart():
    global cart
    i= input("Please type serial of item you want to buy\t")
    q= input("What quantity?\t")
    try:
        i_= int(i)
        q_= int(q)
        cart[i_]= q_
    except:
        print("Incorrect item or quantity entry\t")

    reply= "Y"
    while reply=="Y" or reply=="y" :
        reply= input("Do you want to buy another item (Y/N)\t")
        if reply=="Y" or reply=="y" :
            i= input("Please type SN of item you want to buy\t")
            q= input("What quantity?\t")
            try:
                i_= int(i)
                q_= int(q)
                cart[i_]= q_
            except:
                print("Incorrect item or quantity entry\t")
        else :
            break
    
def receipt():
    total = 0
    numItems= 0
    vat= 0.0
    vatp=0
    lp=0
    global sales
    global item_names
    global item_cp
    global item_qty
    global item_sp
    global cart

    print("Name    Price   Quantity    Total ")
    for serial in cart.keys():
        try :
            current= sales[serial]
            sales[serial] += cart[serial]
        except :
            sales[serial]= cart[serial]
            
        total += item_sp[serial] * cart[serial]
        numItems+= cart[serial]
        updateStock(serial,cart[serial])
        if lp==0 :
            lp = item_sp[serial]
        elif item_sp[serial]<lp :
            lp = item_sp[serial]
            
        print(item_names[serial]+ "      "+ str(item_sp[serial]) +"       " + str(cart[serial]) + "       "+ str(item_sp[serial] * cart[serial]))

    if numItems<5 :
        vatp= 20
        vat= 0.2 * total
    elif numItems>=10 :
        vatp= 30
        vat= 0.3 * total
    
    print("Total Amount without VAT =               " + str(total))
    print("VAT at " + str(vatp) + "% =               " + str(vat))
    print("Total Amount with VAT =               " + str(total + vat))

    if (lp>=100 and numItems>=10):
        print("You qualify for a Bonus of N800")


def computeGain():
    gain=0.0
    for key in sales.keys():
        
        try :
            costpr = item_cp[key]
            sellpr= item_sp[key]
            qty= sales[key]
            gain+= (sellpr-costpr)* qty
        except :
            print("Item " + item_name[key]+ " does not exist in stock\t")

    print("\n\n\n Profit made = " + str(gain))

createStock()
printStock()

print("/n/nStock Available for Sale!!!!")
printAvalableItems()
fillCart()
receipt()
printStock()
computeGain()




