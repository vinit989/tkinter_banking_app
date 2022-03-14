from tkinter import *
import tkinter
import pymysql
import tkinter.messagebox as msg
import random
from twilio.rest import Client

def btn_clicked():
    print("Button Clicked")

def login():
    
    # OTP Generation 
    number="0123456789"
    all=number   # concatinatination for all the data
    length=5
    otp="".join(random.sample(all,length)) #   .jon are used to verify all the given string
    temp_otp = otp
    
    account = accountNo.get()
    phoneNumber = ph_number.get()
    print(account)
    print(phoneNumber)
    
    # Mysql Connection
    connect = pymysql.connect(host="localhost", user="root",password="",db="proger_bank")
    connect_cursor = connect.cursor()
    if(accountNo.get() == ''):
        msg.showerror("Error","Please enter the account")
    elif (ph_number.get() == ''):
        msg.showerror("Error","Please enter the phone number")
    else:
        connect_cursor.execute("SELECT * FROM customers_data WHERE account_no=%s and phoneno=%s",(account,phoneNumber))
        row = connect_cursor.fetchone()
        
        if(row==None):
            msg.showerror("Invalid Credentials", "Please enter valid credentials")
            accountNo.set("")
            ph_number.set("")
        else:
            # Sending Message to Phone number
        
            account_sid = 'AC9a50e9b8ab6fa4889380f57b7c38d727'
            auth_token = '993cd45b59095d08ada3542c67397ea2'
            client = Client(account_sid, auth_token)
            client_message = f'OTP for phone number verification {otp}'
            client_phone_number = f'+91{phoneNumber}'
            print(client_phone_number)
            message = client.messages.create(body=client_message,from_='+16065300587',to=client_phone_number)
            user_otp = StringVar()
            
            def check_otp():
                if(user_otp.get() == temp_otp):
                    with open('current_login.txt','w') as f:
                        text= account+"="+phoneNumber
                        f.write(text)
            
                window.destroy()
                import dashboard
                dashboard_pannel = tkinter.TopLevel()
                dashboard

            # Opening New window
            
            top= Toplevel(window)
            top.geometry("400x250")
            Entry(top,textvariable=user_otp).place(x=20,y=40)
            Button(top,command=check_otp, text="Submit").place(x=100,y=40)
           
           
            
                     


def register_page():
    window.destroy()
    import Register
    lg = tkinter.TopLevel()
    Register


window = Tk()

# Text Variable  
accountNo = StringVar()
ph_number = StringVar()

window.geometry("1212x534")
window.configure(bg = "#3af6b2")
window.title("Login")
canvas = Canvas(
    window,
    bg = "#3af6b2",
    height = 534,
    width = 1212,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


canvas.create_rectangle(
    578, -3, 578+634, -3+537,
    fill = "#fcfcfc",
    outline = "")

img0 = PhotoImage(file = f"login/login.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b0.place(
    x = 820, y = 334,
    width = 110,
    height = 34)

img1 = PhotoImage(file = f"login/forgetpass.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 1016, y = 334,
    width = 144,
    height = 34)

img2 = PhotoImage(file = f"login/register.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = register_page,
    relief = "flat")

b2.place(
    x = 978, y = 412,
    width = 110,
    height = 34)

canvas.create_text(
    909.5, 46.0,
    text = "  Login",
    fill = "#8e97ea",
    font = ("Roboto-Bold", int(36.0)))


canvas.create_rectangle(
    94, 165, 94+65, 165+8,
    fill = "#fcfcfc",
    outline = "")

entry0_img = PhotoImage(file = f"login/img_textBox0.png")
entry0_bg = canvas.create_image(
    992.5, 192.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0,
    textvariable=accountNo)

entry0.place(
    x = 832.0, y = 173,
    width = 321.0,
    height = 37)

entry1_img = PhotoImage(file = f"login/img_textBox1.png")
entry1_bg = canvas.create_image(
    992.5, 270.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0,
    textvariable=ph_number)

entry1.place(
    x = 832.0, y = 251,
    width = 321.0,
    height = 37)

canvas.create_text(
    705.0, 192.5,
    text = " Account Number",
    fill = "#8e97ea",
    font = ("RobotoRoman-Regular", int(18.0)))

canvas.create_text(
    705.0, 270.5,
    text = "Phone Number",
    fill = "#8e97ea",
    font = ("RobotoRoman-Regular", int(18.0)))

canvas.create_text(
    826.0, 431.5,
    text = "Don't have an account ? ",
    fill = "#8e97ea",
    font = ("RobotoRoman-Regular", int(18.0)))

canvas.create_text(
    285.0, 133.0,
    text = "Weclome to Proger Bank",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(36.0)))

canvas.create_text(
    293.0, 222.5,
    text = "We are very secure in terms of customer's data.",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(18.0)))

canvas.create_text(
    288.0, 256.5,
    text = "Using our services make your life more easier.",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(18.0)))

canvas.create_text(
    300.0, 300.5,
    text = "We always take care of our customer.",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(18.0)))

window.resizable(False, False)
window.mainloop()
