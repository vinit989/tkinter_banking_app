from tkinter import *
from turtle import title
from twilio.rest import Client
import random
from tkinter import messagebox as msg
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import pymysql
import tkinter



# (606) 530-0587 Phone Number used for demonstration purposes
#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 SendGrid Api key

 

def Register():
    # OTP Generation 
    number="0123456789"
    all=number   # concatinatination for all the data
    length=5
    otp="".join(random.sample(all,length)) #   .jon are used to verify all the given string
    temp_otp = otp
    
    # Account Number Generation 
    number="0123456789"
    all=number   # concatinatination for all the data
    length=10
    account="".join(random.sample(all,length)) #   .jon are used to verify all the given string
    temp_account = account
    
    # Input Validation
    if(username==''):
        msg.showerror("Username", "Please enter a username")
    elif(password==''):
        msg.showerror("Password", "Please enter a Password for your account")
    
    elif(password==''):
        msg.showerror("Email", "Please enter an email address")
        
    elif(ph_number==''):
        msg.showerror("Phone number", "Please enter a Phone number for your account")   
    
    else:
        
    
        # Sending Message to Phone number
        
        account_sid = 'xyz'
        auth_token = 'xyz'
        client = Client(account_sid, auth_token)
        client_message = f'OTP for phone number verification {otp}'
        client_phone_number = f'+91{ph_number.get()}'
        print(client_phone_number)
        message = client.messages.create(body=client_message,from_='+16065300587',to=client_phone_number)
        user_otp = StringVar()
        user_mail = email.get()
        
        # Mysql Connection
        connect = pymysql.connect(host="localhost", user="root",password="",db="proger_bank")
        connect_cursor = connect.cursor()
        
        # Making Function to check the otp 
        def check_otp():
            print(temp_otp)
            
            if(user_otp.get() == temp_otp):
                sg = sendgrid.SendGridAPIClient(api_key='SG.xyz')
                from_email = Email("vinitlakra634@gmail.com")  # Change to your verified sender
                to_email = To(user_mail)  # Change to your recipient
                subject = "Account Creation"
                content_message = f" Username = {username.get()} \n Your account number = {temp_account} \n Email = {email.get()} \n phone number = {ph_number.get()} "
                content = Content("text/plain", content_message)
                mail = Mail(from_email, to_email, subject, content)

                # Get a JSON-ready representation of the Mail object
                mail_json = mail.get()

                # Send an HTTP POST request to /mail/send
                response = sg.client.mail.send.post(request_body=mail_json)
                print(response.status_code)
                print(response.headers)
                
    
                # Getting data to insert the into database
                
                Username = username.get()
                Password = password.get()
                userEmail = email.get()
                Phone_no = ph_number.get()
                Amount = str(0)
                
                print(temp_account)
                # Inserting the value to the database 
                connect_cursor.execute("INSERT into customers_data(username,account_no,password,email,phoneno,amount) values('"+Username+"','"+temp_account+"','"+Password+"','"+userEmail+"','"+Phone_no+"','"+Amount+"')")
                
                #Commiting for any changes
                connect.commit()
                connect.close()

                # In we need to use the name of text Variables for setting their values to null 
                
                username.set("")
                password.set("")
                email.set("")
                ph_number.set("")
                

                msg.showinfo("Successfully","Thanks for Registration, you have also recieved a mail from us about the account details")
                
                #Destroying Root Instance
                window.destroy()
                
                # Linking for Login Pages
                import login
                lg = tkinter.TopLevel()
                
                login
                
                
            else:
                print("Wrong OTP")
        
        top= Toplevel(window)
        top.geometry("400x250")
        Entry(top,textvariable=user_otp).place(x=20,y=40)
        Button(top,command=check_otp, text="Submit").place(x=100,y=40)
        
        
        
        

    

window = Tk()



window.geometry("1100x644")
window.configure(bg = "#3af6b2")

# Declaring Variables  
username = StringVar()
password = StringVar()
email = StringVar()
ph_number = StringVar()



canvas = Canvas(
    window,
    bg = "#3af6b2",
    height = 644,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


canvas.create_rectangle(
    470, 0, 470+751, 0+644,
    fill = "#fcfcfc",
    outline = "")


canvas.create_rectangle(
    470, 0, 470+630, 0+644,
    fill = "#fcfcfc",
    outline = "")

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Register,
    relief = "flat")

b0.place(
    x = 756, y = 455,
    width = 180,
    height = 55)

canvas.create_text(
    225.5, 141.0,
    text = "Welcome to Proger Bank",
    fill = "#fcfcfc",
    font = ("Roboto-Bold", int(24.0)))

canvas.create_text(
    831.0, 50.0,
    text = "Registration ",
    fill = "#515486",
    font = ("Roboto-Bold", int(24.0)))


canvas.create_rectangle(
    92, 163, 92+60, 163+5,
    fill = "#fcfcfc",
    outline = "")

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    830.5, 135.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    textvariable=username,
    highlightthickness = 0)

entry0.place(
    x = 670.0, y = 116,
    width = 321.0,
    height = 37)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    830.5, 217.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    textvariable=password,
    highlightthickness = 0)

entry1.place(
    x = 670.0, y = 198,
    width = 321.0,
    height = 37)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    830.5, 299.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    textvariable=email,
    highlightthickness = 0)

entry2.place(
    x = 670.0, y = 280,
    width = 321.0,
    height = 37)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    830.5, 370.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    textvariable=ph_number,
    highlightthickness = 0)

entry3.place(
    x = 670.0, y = 351,
    width = 321.0,
    height = 37)

canvas.create_text(
    602.5, 137.5,
    text = "  Username",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    602.5, 217.5,
    text = "   Password",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    602.5, 299.5,
    text = "       Email",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    592.5, 370.5,
    text = "Phone Number   ",
    fill = "#8e97ea",
    font = ("Ribeye-Regular", int(14.0)))

canvas.create_text(
    241.5, 210.0,
    text = "We are very secure in terms of customer's data.",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(14.0)))

canvas.create_text(
    238.5, 245.0,
    text = "Using Our services make your life more easier.",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(14.0)))

canvas.create_text(
    213.5, 282.0,
    text = "We always take care of our customers.",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(14.0)))

window.resizable(False, False)
window.mainloop()
