from tkinter import*
t=Tk()
t.title("Khana Khazana Restaurant")

order_items=[]
bill_text="Restaurant Bill\n" + "-" * 40 + "\n"
bill_text+="Item\t\tQty.\tRate\t\tPrice\n"

t.geometry("400x700")
t.minsize(400,700)
t.maxsize(400,700)

welcome=Label(text="Welcome to Khana Khazana Restaurant",font=" 12 12 bold")
welcome.pack(pady=10)

# Table Booking
table_var=StringVar()
table_var.set("Select Table")
table=["Table 1","Table 2","Table 3","Table 4"]
table_option=OptionMenu(t,table_var,*table)
table_option.pack(pady=10)

def book_table():
    selected_table=table_var.get()
    table_status.configure(text=f"{selected_table} booked succesfully")
table_btn=Button(t,text="Book Table",command=book_table)
table_btn.pack()
table_status=Label(t)
table_status.pack()


# Order Booking
menu_var=StringVar()
qty=IntVar()
menu_var.set("Menu")
menu=['Pizza   ₹ 100','Steam Momos   ₹ 50','Fried Momos   ₹ 60','Sandwich   ₹ 40','Veg Burger   ₹ 30','Chicken Burger   ₹ 50','Patties   ₹ 15','Kachori   ₹ 15','Samosa   ₹ 15','Cold Coffee   ₹ 40','Hot Coffee   ₹ 20','Tea   ₹ 10','Mojito   ₹ 40','Lemon soda   ₹ 40']
selected_menu=OptionMenu(t,menu_var,*menu)
selected_menu.pack()
qty_lbl=Label(t,text="Quantity")
qty_lbl.pack()
quantity=Entry(t,textvariable=qty,width=5)
quantity.pack(pady=10)

def add():
    item=menu_var.get()
    quant=qty.get()
    if item:
        for i in range(quant):
            order_items.append(item)
        item=item.split("   ₹ ")
        your_order.insert(0,f"{item[0]}\t*{quant}")    
order=Button(t,text='Add to Order',command=add)
order.pack(pady=10)

your_order=Listbox(t,width=30)
your_order.pack()


# Remove item from order list 
def del_item():
    global bill_text
    quant=qty.get()
    your_order.delete(0)
    for i in range(quant):
        order_items.pop(len(order_items)-1)
del_btn=Button(t,text="Remove Item",command=del_item)
del_btn.pack()

# Generating Bill
def Bill():
    bill_amt=0
    for x in order_items:
        x=x.split("   ₹ ")
        bill_amt+=int(x[1])
    global bill_text
    coun=1
    for i in range(0,len(order_items)-1):
        if(order_items[i]==order_items[i+1]):
            coun+=1
        if(order_items[i]!=order_items[i+1]):
            item=order_items[i]
            item=item.split("   ₹ ")
            bill_text+=f"{item[0]}\t\t{coun}\t{item[1]}\t\t₹{int(item[1])*coun}\n"
            coun=1
    item=order_items[len(order_items)-1].split("   ₹ ")
    bill_text+=f"{item[0]}\t\t{coun}\t{item[1]}\t\t₹{int(item[1])*coun}\n"
    bill_text += "-" * 40 + "\n"
    bill_text+= f"Total Amount: ₹{bill_amt}\n"
    bill_display.configure(state=NORMAL)
    bill_display.delete(1.0,END)
    bill_display.insert(END,bill_text)
    bill_display.configure(state=DISABLED)
Button(t,text="Generate Bill",command=Bill).pack(pady=10)

bill_display=Text(t,state=DISABLED)
bill_display.pack()

t.mainloop()