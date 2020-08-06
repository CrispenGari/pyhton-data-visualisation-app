''''from pip._internal import main
main(['install', 'pillow'])'''
""""from tkinter import  *
from tkinter import filedialog, messagebox
import tkinter.ttk as ttk
import PyPDF2
from PIL import ImageTk, Image
from ttkthemes import ThemedTk


strawberry =ImageTk.PhotoImage(Image.open("main.ico"))
exit_ico = ImageTk.PhotoImage(Image.open('exit.png'))
team = ImageTk.PhotoImage(Image.open('team.png'))
contact_suport = ImageTk.PhotoImage(Image.open('contactSuport.png'))
manager = ImageTk.PhotoImage(Image.open('manager.png'))
setting = ImageTk.PhotoImage(Image.open('settings.png'))
account = ImageTk.PhotoImage(Image.open('account.png'))
def exitFunc():
    conf = messagebox.askyesnocancel("PDF DOCUMENT MERGER", "ARE YOU SURE YOU WANT TO EXIT PDF DOCUMENT MERGER?")
    if(conf):
        root.destroy()
    else:
        root.focus()
# classes
class mainMenu:
    def __init__(self):
        return
    def fileMenu(self, menubar):
        self.menubar = menubar
        fileMenu = Menu(self.menubar, tearoff =0)
        fileMenu.add_command(label ="Open", underline=0)
        fileMenu.add_command(label="Close")
        fileMenu.add_command(label="Settings")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command =exitFunc, image=exit_ico, underline=0, compound=LEFT)
        self.menubar.add_cascade(label="File", menu=fileMenu, underline=0)

        return
    def viewMenu(self, menubar):
        self.menubar = menubar
        viewMenu = Menu(self.menubar, tearoff=0)
        viewMenu.add_command(label ="Themes")
        viewMenu.add_command(label="Preference")
        self.menubar.add_cascade(label="View", menu=viewMenu)
        return
    def aboutMenu(self,menubar):
        self.menubar =menubar
        about_menu = Menu(self.menubar, tearoff=0)
        about_menu.add_command(label="About Strawberry", image= strawberry, compound =LEFT)
        about_menu.add_command(label="Join Team", image =team, comound=LEFT)
        about_menu.add_command(label="Manager", image = manager, compound=LEFT)
        about_menu.add_separator()
        about_menu.add_command(label="Contact Support", image=contact_suport, compound=LEFT)
        about_menu.add_command(label="Account", image=account, compound=LEFT)
        self.menubar.add_cascade(menu=about_menu, label="About")
        return
    def helpMenu(self, menubar):
        self.menubar = menubar
        help_menu = Menu(self.menubar, tearoff=0)
        help_menu.add_command(label="Strawberry Help")
        help_menu.add_command(label="Documentation")
        help_menu.add_command(label="Online Help")
        self.menubar.add_cascade(label="Help")
        return

root = ThemedTk(theme='black')
root.iconbitmap('main2.ico')
root.title("PDF DOCUMENT MERGER")
width = 700; height =500;
padx = int((root.winfo_screenwidth() -width)/2)
pady= int((root.winfo_screenheight() - height)/2)

root.geometry(f'{width}x{height}+{padx}+{pady}')
menubar = Menu(root)
menu_ob = mainMenu()
menu_ob.fileMenu(menubar)
menu_ob.viewMenu(menubar)
menu_ob.aboutMenu(menubar)
menu_ob.viewMenu(menubar)
root.config(menu= menubar)
root.mainloop(0)"""

import  pytube
url = 'http://youtube.com/watch?v=9bZkp7q19f0'

pytube.YouTube(url).streams.first().download()