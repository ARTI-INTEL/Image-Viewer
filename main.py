from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("images\Faiq Icon.ico")

img1 = ImageTk.PhotoImage(Image.open("images\Calculator.png"))
img2 = ImageTk.PhotoImage(Image.open("images\Clock.png"))
img3 = ImageTk.PhotoImage(Image.open("images\Stop Watch.png"))
img4 = ImageTk.PhotoImage(Image.open("images\Text to Speech.png"))
img5 = ImageTk.PhotoImage(Image.open("images\To-do.png"))

img_list = [img1,img2,img3,img4,img5]

img_label = Label(image=img1)
status = Label(text=f"Image 1 out of {len(img_list)}.", bd=1, relief=SUNKEN, anchor=E)

def forward(img_num):
    global img_label
    global btn_back
    global btn_forward

    img_label.config(image=img_list[img_num+1])
    btn_forward.config(command=lambda: forward(img_num+1))
    btn_back.config(command=lambda: back(img_num+1), state=NORMAL)

    status.config(text=f"Image {img_num+2} out of {len(img_list)}")

    if (img_num + 2) == len(img_list):
        btn_forward.config(state=DISABLED)

def back(img_num):
    global img_label
    global btn_back
    global btn_forward

    img_label.config(image=img_list[img_num-1])
    btn_forward.config(command=lambda: forward(img_num-1), state=NORMAL)
    btn_back.config(command=lambda: back(img_num-1))

    status.config(text=f"Image {img_num} out of {len(img_list)}")

    if (img_num - 1)  == 0:
        btn_back.config(state=DISABLED)

btn_back = Button(root, text="<--", command=lambda: back(0), state=DISABLED)
btn_close = Button(root, text="X", command=root.quit)
btn_forward = Button(root, text="-->", command=lambda: forward(0))

img_label.grid(row=0,column=0,columnspan=3)
btn_back.grid(row=1,column=0)
btn_close.grid(row=1,column=1)
btn_forward.grid(row=1,column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()