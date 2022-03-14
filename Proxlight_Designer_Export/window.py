from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1212x534")
window.configure(bg = "#3af6b2")
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

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 815, y = 334,
    width = 132,
    height = 34)

img1 = PhotoImage(file = f"img1.png")
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

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
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

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    992.5, 192.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entry0.place(
    x = 832.0, y = 173,
    width = 321.0,
    height = 37)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    992.5, 270.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entry1.place(
    x = 832.0, y = 251,
    width = 321.0,
    height = 37)

canvas.create_text(
    725.0, 192.5,
    text = " Account Number",
    fill = "#8e97ea",
    font = ("RobotoRoman-Regular", int(18.0)))

canvas.create_text(
    730.5, 270.5,
    text = "Phone Number",
    fill = "#8e97ea",
    font = ("RobotoRoman-Regular", int(18.0)))

canvas.create_text(
    826.0, 431.5,
    text = "Don’t have an account ? ",
    fill = "#8e97ea",
    font = ("RobotoRoman-Regular", int(18.0)))

canvas.create_text(
    285.0, 133.0,
    text = "Weclome to Proger Bank",
    fill = "#ffffff",
    font = ("Roboto-Bold", int(36.0)))

canvas.create_text(
    293.0, 222.5,
    text = "We are very secure in terms of customer’s data.",
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
