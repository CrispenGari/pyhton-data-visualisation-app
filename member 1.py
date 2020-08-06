
from tkinter import *
import tkinter.ttk as ttk
import  time
from  PIL import Image, ImageTk

root = Tk()


root.title("Client.IO")
width = 500; height = 280;
pad_x= int(root.winfo_screenwidth()/2 - width/2);
pad_y = int(root.winfo_screenheight()/2 - height/2)
root.geometry(f"{width}x{height}+{pad_x}+{pad_y}")
root.iconbitmap('strawberry.ico')
root.config(background ="#5D7690")
root.resizable(False, False)
main_icon = ImageTk.PhotoImage(Image.open('main.ico'))
loading=True
frame_first = Frame(root, height=height, bg="red", width=width/2)
picture_frame = Frame(frame_first, width =width/2, height=height, bg="#6D5566")
Label(picture_frame, font=("Arial", 10, "bold"), fg="white", image=main_icon, bg="#6D5566").grid(row=0, column=0, columnspan =3)
Label(picture_frame, font=("Arial", 10, "italic"), fg="white",
      text ="Empowered By Strawberry.com", bg="#6D5566").grid(row=2, column=0, columnspan=3, sticky=W)
picture_frame.grid(row=0, column = 0, columnspan =5)
frame_first.grid(row=0, column=0, columnspan =5, rowspan=5)
Label(root, font=("Times New Roman", 16, "bold"), fg="white", text ="DATA VISUALISATION", bg='#5D7690').grid(row=0, column=5, columnspan=5)
Label(root, font=("Times New Roman", 16, "bold"), fg="white", text ="STATISTICS", bg='#5D7690').grid(row=1, column=5, columnspan=5)

while loading:
    for i in range(1, 2):
        Label(root, font=("Arial", 11, "bold"), fg="white", text ="Loading .",
              bg="#5D7690").grid(row=4, column=9,sticky=E)
        time.sleep(2)
        root.update_idletasks()
        Label(root, font=("Arial", 11, "bold"), fg="white", text="Loading . .", bg="#5D7690").grid(row=4, column=9,
                                                                                            sticky=E)
        time.sleep(2)
        root.update_idletasks()
        Label(root, font=("Arial", 11, "bold"), fg="white", text="Loading . . .", bg="#5D7690").grid(row=4, column=9,
                                                                                          sticky=E)
        time.sleep(2)
        root.update_idletasks()
    loading =False
root.mainloop()

