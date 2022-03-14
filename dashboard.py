from tkinter import *
import tkinter
import pymysql
import tkinter.messagebox as msg
from datetime import datetime

with open('current_login.txt','r') as f:
    data = f.read()
    userdata = data.split('=')
    account = userdata[0]
    phoneNumber = userdata[1]
    print(account)
    print(phoneNumber)
    
#MYSQL CONNECTION GLOBALLY 
connect = pymysql.connect(host="localhost", user="root",password="",db="proger_bank")
connect_cursor = connect.cursor()


# Getting Data from Database, So that we can updates my fields like dashboard of other websites
connect_cursor.execute("SELECT * FROM customers_data WHERE account_no=%s and phoneno=%s",(account,phoneNumber))
row = connect_cursor.fetchone()

# Here Storing data in local variables

username = row[1]
password = row[3]
email = row[4]
user_id = row[0]
print(user_id)
current_amount = row[6]
print(current_amount)



if(row==None):
    msg.showerror("Please Try to login", "Please try to login, instead of directly accessing the dashboard")
    
else:
    pass


def logout():
    window.destroy()
                
    # Linking for Login Pages
    import login
    lg = tkinter.TopLevel()
                
    login

def add_money():
    amount = int(money.get())
    
    # Try and Exception , Exception handling is necessary
    
    if(amount>0):
        # Here Adding old amount + new Amount
        new_amount = (amount) + current_amount
        
        # Money Adding to account
        # "INSERT into customers_data(amount) values('"+new_amount+"') WHERE account_no=%s",account
        sql_query = f"UPDATE `customers_data` SET  `amount` = {new_amount} WHERE `customers_data`.`sno` = {user_id}"
        connect_cursor.execute(sql_query)
        # connect_cursor.execute("UPDATE customers_data SET '"+new_amount+"' WHERE account_no=%s",account)
                
        #Commiting for any changes
        connect.commit()
        
        msg.showinfo("Sucess","Successfully added the money")
        print(amount)
        
        money.set("")
        
    else:
        msg.showerror("Unvalid Amount","Please enter the valid amount")
        money.set("")

def transaction_history():
    print("Transaction history")


def transfer_money():
    
    

    def Submit():
        reciever_account = transfer_account.get()
        t_amount = int(transfer_amount.get())
        # Checking if the user has a account on our bank 
        
        sql_query = f"SELECT * FROM customers_data WHERE account_no={reciever_account}"
        connect_cursor.execute(sql_query)
        row = connect_cursor.fetchone()
        rec_user_id = row[0]
        
        
        if(row==None):
            msg.showerror("Invalid Account number", "Please enter valid valid account number")
        
        else:
            
            
            if(t_amount <= current_amount):
                # fetching this amount from the database
                
                reciever_account_balance = row[6]
                recv_bank_balance = int(reciever_account_balance)
                
                reciver_amount = recv_bank_balance + t_amount
                
                # print(reciver_amount)
                # Updating the table of the reciever_account
                
                sql_query = f"UPDATE `customers_data` SET  `amount` = {reciver_amount} WHERE `customers_data`.`sno` = {rec_user_id}"
                connect_cursor.execute(sql_query)
                
                sender_amount = current_amount - t_amount
                
                # Updating the table of the sender_account
                sql_query = f"UPDATE `customers_data` SET  `amount` = {sender_amount} WHERE `customers_data`.`sno` = {user_id}"
                connect_cursor.execute(sql_query)
                
                # Inserting data into Transaction table
                connect_cursor.execute("INSERT into transfers(sno,s_account_no,r_account_no,amount,time) values('"++"','"+reciever_account+"','"+t_amount+"','"++"')")
                
                #Commiting for any changes
                connect.commit()
                
                transfer_account.set("")
                transfer_amount.set("")
                
                msg.showinfo("Success", "Sucessfully Tranfered the Amount")
                
                window.destroy()
                import dashboard
                dashboard_pannel = tkinter.TopLevel()
                dashboard
                
            else:
                print("Insufficient Balance in your account.")
    
    # Opening New window
            
    top= Toplevel(window)
    top.geometry("400x250+200+200")
    Label(top,text="Transfering Money").pack(pady=10)
    
    Label(top,text="Reciever's account no. ").place(x=10,y=40)
    Entry(top,textvariable=transfer_account).place(x=150,y=40)
    
    Label(top,text="Amount ").place(x=80,y=80)
    Entry(top,textvariable=transfer_amount).place(x=150,y=80)
    
    Button(top,command=Submit, text="Submit").place(x=170,y=120)
    
    
    


def btn_clicked():
    pass


window = Tk()

# Declaring variables
ph_number = StringVar()
passwd = StringVar()
Email = StringVar()
money = StringVar()
transfer_amount = StringVar()
transfer_account = StringVar()

# money.set("0")

# After Defining, setting variables
ph_number.set(phoneNumber)
Email.set(email)
passwd.set(password)

window.geometry("1202x534")
window.configure(bg = "#3af6b2")
canvas = Canvas(
    window,
    bg = "#3af6b2",
    height = 534,
    width = 1202,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


canvas.create_rectangle(
    0, 0, 0+1202, 0+534,
    fill = "#fcfcfc",
    outline = "")

img0 = PhotoImage(file = f"dashboard/transfer.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = transfer_money,
    relief = "flat")

b0.place(
    x = 985, y = 155,
    width = 148,
    height = 33)

# Money Add Button   
img4 = PhotoImage(file = f"dashboard/img0.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = add_money,
    relief = "flat")

b4.place(
    x = 885, y = 355,
    width = 148,
    height = 33)




img1 = PhotoImage(file = f"dashboard/transaction_history.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = transaction_history,
    relief = "flat")

b1.place(
    x = 768, y = 152,
    width = 195,
    height = 34)

img2 = PhotoImage(file = f"dashboard/save.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 493, y = 452,
    width = 102,
    height = 34)

img3 = PhotoImage(file = f"dashboard/logout.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = logout,
    relief = "flat")

b3.place(
    x = 833, y = 452,
    width = 110,
    height = 34)

canvas.create_text(
    524.5, 39.0,
    text = "Welcome to Proger Bank",
    fill = "#3af6b2",
    font = ("Roboto-Bold", int(24.0)))


canvas.create_rectangle(
    92, 163, 92+60, 163+5,
    fill = "#fcfcfc",
    outline = "")

entry0_img = PhotoImage(file = f"dashboard/img_textBox0.png")
entry0_bg = canvas.create_image(
    541.5, 247.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0,
    textvariable=ph_number)

entry0.place(
    x = 381.0, y = 228,
    width = 321.0,
    height = 37)

entry1_img = PhotoImage(file = f"dashboard/img_textBox1.png")
entry1_bg = canvas.create_image(
    536.5, 316.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0,
    textvariable=passwd)

entry1.place(
    x = 376.0, y = 297,
    width = 321.0,
    height = 37)

entry2_img = PhotoImage(file = f"dashboard/img_textBox2.png")
entry2_bg = canvas.create_image(
    541.5, 385.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0,
    textvariable=Email)

entry2.place(
    x = 381.0, y = 366,
    width = 321.0,
    height = 37)

# Input Field for entring the amount
entry3_img = PhotoImage(file = f"dashboard/img_textBox0.png")
entry3_bg = canvas.create_image(
    541.5, 247.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0,
    textvariable=money)

entry3.place(
    x = 781.0, y = 295,
    width = 321.0,
    height = 37)

canvas.create_text(
    300.5, 125.5,
    text = "Username",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    274.5, 181.5,
    text = " Account Number",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    602.5, 217.5,
    text = " ",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    274.5, 243.5,
    text = "Phone Number",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    274.5, 316.5,
    text = "Password",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    274.5, 385.5,
    text = "Email",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    405.5, 123.5,
    text = username,
    fill = "#000000",
    font = ("RobotoRoman-Regular", int(14.0)))

canvas.create_text(
    455.5, 179.5,
    text = account,
    fill = "#000000",
    font = ("RobotoRoman-Regular", int(14.0)))

window.resizable(False, False)
window.mainloop()
