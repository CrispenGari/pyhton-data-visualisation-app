"""# installing module
modules=['matplotlib', 'numpy', 'pillow', 'openpyxl','sqlite3', 'mysql.connector']
try:
    import matplotlib,numpy,PIL
except ImportError:
    from pip._internal import main as install
    for i in modules:
         install(["install",i])"""


# importing modules
import tkinter.ttk as ttk
from tkinter import *
from ttkthemes import ThemedTk
import urllib
import webbrowser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import random, datetime
import tkinter.font, tkinter.colorchooser
import os, sys, subprocess, time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog, font, scrolledtext

# icons
strawberry_icon = "strawberry.ico"
cut_icon = "cut.png"
copy_icon = 'copy.png'
refresh_icon = 'refresh.png'
database_icon = 'database.png'
open_icon = 'open.png'
paste_icon = "paste.png"
forward_icon = "forward.png"
backward_icon = 'backward.png'
exit_icon = "exit.png"
undo_ico = "undo.png"
redo_icon = 'redo.png'
refresh_icon = 'refresh.png'
save_ico = 'save.png'
help_icon = 'help.png'
settings_ico = 'settin'
excel_icon = "excel.png"
# Fonts
fonts = [("arial", 15, "bold"), ("Times", 10, "bold"),
         ("Helvetica", 10, "bold italic"),
         ("Symbol", 8), ("Times New Roman", 10, "bold"), ('Tahoma', 12, "bold", "italic"),
        ("arial", 12, "bold")

         ]

# Colors
colors = ["green", "black", "white", "gray"]
theme =["black", "aquativo", "equilux", "arc", "blue", "breeze",
         "clearlooks", "elegance", "itfti","karamic","kroc","plastik",
         "radience","scid themes","smog","winxpblue", "radiance"]
global themes
themes = [theme[0],theme[3], theme[6], theme[7], theme[10], theme[11], theme[15]]
root = ThemedTk(theme=themes[1])
title = "Strawberry Data Visualiser"
root.title(title)
width = 1200; height = 700;
pad_x= int(root.winfo_screenwidth()/2 - width/2);
pad_y = int(root.winfo_screenheight()/2 - height/2)
root.geometry(f"{width}x{height}+{pad_x}+{pad_y}")
root.config(bg="white")
root.iconbitmap(strawberry_icon)
def colorChooser():
    color_chosen = tkinter.colorchooser.askcolor( title="Data Visualiser Font Color",initialcolor="black")
    return color_chosen
def closeSettings(tab):
    choice = messagebox.askyesnocancel("Data Visualiser Setting", "Are you sure you want to close Preference Settings?")
    if(choice):
        tab.destroy()
    else:
        tab.focus()
    return
imgSettings= ImageTk.PhotoImage(Image.open("settings.png"))
imgProfile = ImageTk.PhotoImage(Image.open('profile.png')),
def find_Function(taget):
    find_Window =Toplevel(root)
    find_Window.title("Data Visualiser Finder")
    find_Window.iconbitmap(strawberry_icon)
    find_Window.geometry("558x280+700+200")
    find_Window.resizable(False,False)
    find_noteBook = ttk.Notebook(find_Window, width =555, height=254)
    find_tab = Frame(find_noteBook)
    select_tab = Frame(find_noteBook)
    replace_tab = Frame(find_noteBook)
    find_noteBook.add(select_tab, text="Select")
    find_noteBook.add(replace_tab, text="Replace")
    find_noteBook.add(find_tab, text="Find")
    # find_tab
    Label(find_tab, text="Select Options Find",font=("Arial", 11,"bold")).grid(row=1,column=0, columnspan=7, pady=5)
    Label(find_tab, text="Text",underlin=0, font=("Arial", 11, "bold")).grid(row=2, column=0, sticky=W, pady=3)
    textFind= Entry(find_tab, font=("Arial", 11), width =62)
    textFind.grid(row=2, column=1, columnspan=6, sticky=W, pady=3)

    match_case = ttk.Checkbutton(find_tab, text="Match Case")
    match_case.grid(row=3, column=1, sticky=W, pady=3)
    whole_word = ttk.Checkbutton(find_tab, text="Find the whole word")
    whole_word.grid(row=4, column=1, sticky=W, pady=3)
    use_wirldcards = ttk.Checkbutton(find_tab, text="Use wirldcards")
    use_wirldcards.grid(row=5, column=1, sticky=W, pady=3)
    use_regEx = ttk.Checkbutton(find_tab, text="Use Regular Expressions")
    use_regEx.grid(row=6, column=1, sticky=W, pady=3)

    match_prefix = ttk.Checkbutton(find_tab, text="Match Prefix")
    match_prefix.grid(row=3, column=2, sticky=W, pady=3)
    match_sufix = ttk.Checkbutton(find_tab, text="Match Suffix")
    match_sufix.grid(row=4, column=2, sticky=W, pady=3)
    ignore_punctuation = ttk.Checkbutton(find_tab, text="Ignore Punctuation Characters")
    ignore_punctuation.grid(row=5, column=2, sticky=W, pady=3)
    ignore_whitespaces = ttk.Checkbutton(find_tab, text="Ignore White Space Characters")
    ignore_whitespaces.grid(row=3, column=3, columnspan =2, sticky=W, pady=3)
    Button(find_tab, text="Find", width=10,font=("Arial", 10,"bold"), bg="green").grid(row=9, column=1, sticky=W, pady=3)
    Button(find_tab, text="Close", width=10,font=("Arial", 10, "bold"), bg="red", command=lambda :find_Window.destroy()).grid(row=9, column=2, sticky=W, pady=3)
    Button(find_tab, text="Reset", width=10,font=("Arial", 10, "bold"), bg="orange").grid(row=9, column=3, sticky=W, pady=3)
    find_noteBook.grid(row=0, column=0, columnspan=6)
    find_Window.focus()

    # Replace Tab
    Label(replace_tab, text="Select Options Replace", font=("Arial", 11, "bold")).grid(row=1, column=0, columnspan=7, pady=5)
    Label(replace_tab, text="Find What: ", underlin=0, font=("Arial", 11, "bold")).grid(row=2, column=0, sticky=W, pady=3)
    Label(replace_tab, text="Replace With: ", underlin=0, font=("Arial", 11, "bold")).grid(row=3, column=0, sticky=W, pady=3)
    textFindW = Entry(replace_tab, font=("Arial", 11), width=50)
    textFindW.grid(row=2, column=1, columnspan=6, sticky=W, pady=3)
    textReplace = Entry(replace_tab, font=("Arial", 11), width=50)
    textReplace.grid(row=3, column=1, columnspan=6, sticky=W, pady=3)

    match_case1 = ttk.Checkbutton(replace_tab, text="Match Case")
    match_case1.grid(row=4, column=1, sticky=W, pady=3)
    whole_word1 = ttk.Checkbutton(replace_tab, text="Find the whole word")
    whole_word1.grid(row=5, column=1, sticky=W, pady=3)
    use_wirldcards1 = ttk.Checkbutton(replace_tab, text="Use wirldcards")
    use_wirldcards1.grid(row=6, column=1, sticky=W, pady=3)
    use_regEx1 = ttk.Checkbutton(replace_tab, text="Use Regular Expressions")
    use_regEx1.grid(row=7, column=1, sticky=W, pady=3)
    uppercase = ttk.Checkbutton(replace_tab, text="UPPER CASE ALL", underline=0)
    uppercase.grid(row=4, column=3, columnspan=2, sticky=W, pady=3)
    lowercase = ttk.Checkbutton(replace_tab, text="lower case all", underline=0)
    lowercase.grid(row=5, column=3, sticky=W, pady=3)

    match_prefix1 = ttk.Checkbutton(replace_tab, text="Match Prefix")
    match_prefix1.grid(row=4, column=2, sticky=W, pady=3)
    match_sufix1 = ttk.Checkbutton(replace_tab, text="Match Suffix")
    match_sufix1.grid(row=5, column=2, sticky=W, pady=3)
    ignore_punctuation1 = ttk.Checkbutton(replace_tab, text="Ignore Punctuation Characters")
    ignore_punctuation1.grid(row=6, column=2, sticky=W, pady=3)
    ignore_whitespaces1 = ttk.Checkbutton(replace_tab, text="Ignore White Space Characters")
    ignore_whitespaces1.grid(row=7, column=2, sticky=W, pady=3)
    Button(replace_tab, text="Replace", width=10, font=("Arial", 10, "bold"), bg="green").grid(row=9, column=1, sticky=W,
                                                                                           pady=3)
    Button(replace_tab, text="Close", width=10, font=("Arial", 10, "bold"), bg="red",
           command=lambda: find_Window.destroy()).grid(row=9, column=2, sticky=W, pady=3)
    Button(replace_tab, text="Reset", width=10, font=("Arial", 10, "bold"), bg="orange").grid(row=9, column=3, sticky=W,
                                                                                           pady=3)
    find_noteBook.grid(row=0, column=0, columnspan=6)
    find_Window.focus()

    # Select Tab
    Label(select_tab, text="Select Options Select", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=7,
                                                                               pady=5)
    select_All = ttk.Checkbutton(select_tab, text="Select All")
    select_All.grid(row=1, column=1, sticky=W, pady=3)

    y = BooleanVar()
    x=BooleanVar()
    col= BooleanVar(); xv= BooleanVar(); yv= BooleanVar(); pt=BooleanVar();
    x_label = ttk.Checkbutton(select_tab, text="X-Label Text",variable=x )
    x_label.grid(row=2, column=3, sticky=W, pady=3, padx=10)
    y_label = ttk.Checkbutton(select_tab, text="Y-Label Text",variable=y)
    y_label.grid(row=3, column=3, sticky=W, pady=3, padx=10)
    colors = ttk.Checkbutton(select_tab, text="Plot Colors", variable =col)
    colors.grid(row=4, column=3, sticky=W, pady=3, padx=10)

    x_values = ttk.Checkbutton(select_tab, text="X-Values", variable=xv)
    x_values.grid(row=2, column=4, sticky=W, pady=3, padx=10)
    y_values = ttk.Checkbutton(select_tab, text="Y-Values", variable=yv)
    y_values.grid(row=3, column=4, sticky=W, pady=3, padx=10)
    plot_title = ttk.Checkbutton(select_tab, text="Graph Title", variable=pt)
    plot_title.grid(row=4, column=4, sticky=W, pady=3, padx=10)

    Button(select_tab, text="Copy", width=10, font=("Arial", 10, "bold"), bg="green").grid(row=9, column=1,
                                                                                               sticky=W,
                                                                                               pady=3)
    Button(select_tab, text="Cut", width=10, font=("Arial", 10, "bold"), bg="gray").grid(row=9, column=2,
                                                                                               sticky=W,
                                                                                               pady=3)
    Button(select_tab, text="Close", width=10, font=("Arial", 10, "bold"), bg="red",
           command=lambda: find_Window.destroy()).grid(row=9, column=4, sticky=W, pady=3)
    Button(select_tab, text="Reset", width=10, font=("Arial", 10, "bold"), bg="orange").grid(row=9, column=3, sticky=W, pady=3)
    if taget=="find":
        find_noteBook.select(find_tab)
    elif taget=="replace":
        find_noteBook.select(replace_tab)
    else:
        find_noteBook.select(select_tab)
    return
def moreSettings():
    moreSett = Toplevel(root)
    moreSett.focus()
    moreSett.title("Data Visualiser Settings")
    moreSett.iconbitmap('settings.ico')
    moreSett.geometry("500x200+500+200")
    moreSett.resizable(False, False)
    return
def hideShow(target, label):
    if target.cget("show")=="*":
        target.config(show="normal")
        label ="Hide"
    else:
        target.config(show="*")
        label="Show"
    return
class preferenceClass:
    def __init__(self, text):
        self.text = text
        return
    def fontConfig(self,  family, size):
        self.family = family; self.size=size;
        self.text.config(font=(self.family,self.size))
        return
def setFontFunction(text, f_family, f_size):
    obFont = preferenceClass(text=text)
    obFont.fontConfig(f_family, f_size)
    return
def preferences():
    prefereS = Toplevel(root)
    global  themes
    prefereS.focus()
    prefereS.title("Data Visualiser Settings")
    prefereS.iconbitmap('settings.ico')
    prefereS.geometry("577x320+500+200")
    prefereS.resizable(False, False)

    prefferenceNotebook = ttk.Notebook(prefereS, height=315)
    generalTab = Frame(prefferenceNotebook)
    personaliseCopy = Frame(prefferenceNotebook)
    appearenceTab = Frame(prefferenceNotebook)
    prefferenceNotebook.add(personaliseCopy, text="Personlise Copy Settings")
    prefferenceNotebook.add(generalTab, text="General Settings")
    prefferenceNotebook.add(appearenceTab, text="Appearance")
    prefferenceNotebook.select(generalTab)

    Label(generalTab, text="Font Size",font=("arial", 10, "bold")).grid(row=2, column =0, pady=2)
    Label(generalTab, text="Font Family", font=("arial", 10, "bold")).grid(row=1, column=0, pady=2)
    Label(generalTab, text="Font Color", font=("arial", 10, "bold")).grid(row=3, column=0, pady=2)
    Button(generalTab, text="Select Color" , compound=LEFT,command =lambda :colorChooser()).grid(row=3, pady=2, column=1, sticky=W, columnspan=2)

    bold_check = ttk.Checkbutton(generalTab, text="Bold", underline=0)
    bold_check.grid(row=4, column=0, pady=2)
    italic_check = ttk.Checkbutton(generalTab, text="Italic", underline=0)
    italic_check.grid(row=4, column=1, pady=2)
    underline_check = ttk.Checkbutton(generalTab, text="Underline", underline=0)
    underline_check.grid(row=4, column=2, pady=2)
    font_family = StringVar()
    font_options = []
    font = tkinter.font.families()
    for i in font:
        font_options.append(i)
    font_family.set(font_options[10])
    font_size = IntVar()
    font_size.set(10)
    font_fam = ttk.OptionMenu(generalTab,font_family, *font_options)
    font_fam.grid(row=1, column=1, ipadx=35, columnspan=2, pady=2)
    font_s = ttk.Spinbox(generalTab,from_ =8, to=25,increment=1, textvariable=font_size, width=5)
    font_fam.config(textvariable=font_family,direction="below")
    font_s.grid(row=2, column =1, columnspan=2, pady=2)
    Label(generalTab, text="Sample Text", font=("arial", 10, "bold")).grid(row=0, column=3, columnspan=2)
    txtSample = Text(generalTab, width =40, heigh =5)
    txtSample.grid(row=1, column=3, columnspan=3, rowspan=4)
    Button(generalTab, text="Test",bg="sea green",activebackground="blue",width=10 ,font=("arial", 10, "bold")).grid(row=5, column=2, pady=20, padx=3)
    Button(generalTab, text="Close",bg="red",activebackground="blue", width=10, font=("arial", 10, "bold"), command=lambda: closeSettings( prefereS)).grid(row=5, column=3, pady=20, padx=3)
    Button(generalTab, text="Restore",bg="orange",activebackground="blue", width=10,font=("arial", 10, "bold")).grid(row=5, column=4, pady=20, padx=3)
    Button(generalTab, text="Apply",bg="green",activebackground="blue", width=10,font=("arial", 10, "bold")).grid(row=5, column=5, pady=20, padx=3)

    Label(personaliseCopy, text="User Profile", font=("arial", 11, "bold")).grid(columnspan =2, row=0, column=0)
    Label(personaliseCopy, text="Username: ",font=("arial", 10, "bold")).grid( row=1, column=0)
    username_ =Entry(personaliseCopy,font=("arial", 10))
    username_.grid(row=1, column=1)
    photo_frame= Frame(personaliseCopy)
    canvas = Canvas(photo_frame, width=150, height=110)
    Label(photo_frame, text="Profile Picture", font=("arial", 10, "bold")).pack(pady=1)
    canvas.create_image(75,55, image=imgProfile)
    canvas.pack(pady=1)
    photo_frame.grid(row=2, column=0,columnspan=2, pady=2)
    ttk.Separator(personaliseCopy, orient=VERTICAL).grid(row=0, column=3, rowspan=5, ipady=130, padx=2)
    other_credentials = Frame(personaliseCopy)
    Label(other_credentials, text="Other Credentials", font=("arial", 11, "bold")).grid(columnspan=2, row=0, column=0, pady=1)
    Label(other_credentials, text="Email: ", font=("arial", 10, "bold")).grid(row=1, column=0, pady=1)
    email_ = Entry(other_credentials, font=("arial", 10))
    email_.grid(row=1, column =1, pady=1)
    Label(other_credentials, text="Phone: ", font=("arial", 10, "bold")).grid(row=2, column=0, pady=1)
    phone_ = Entry(other_credentials, font=("arial", 10))
    phone_.grid(row=2, column=1, pady=1)
    label = "Show"
    Label(other_credentials, text="Password: ",font=("arial", 10, "bold")).grid(row=3, column=0, pady=1)
    pass_ = Entry(other_credentials, font=("arial", 10), show="*")
    pass_.grid(row=3, column=1, pady=1)

    hide_show= ttk.Checkbutton(other_credentials, text=f"{label}", command=lambda :hideShow(pass_, label))
    hide_show.grid(row=3, column=2, pady=1, sticky=W)
    hide_showC = ttk.Checkbutton(other_credentials, text=f"{label}", command=lambda :hideShow(passC_, label))
    hide_showC.grid(row=4, column=2, pady=1, sticky=W)
    Label(other_credentials, text="Confirm: ", font=("arial", 10, "bold")).grid(row=4, column=0, pady=1)
    passC_ = Entry(other_credentials, font=("arial", 10), show="*")
    passC_.grid(row=4, column=1, pady=1)
    Label(other_credentials, text="Product ID: ", font=("arial", 10, "bold")).grid(row=5, column=0, pady=1)
    productID_ = Entry(other_credentials, font=("arial", 10))
    productID_.grid(row=5, column=1, pady=1)
    Label(other_credentials, text="Gender: ", font=("arial", 10, "bold")).grid(row=6, column=0, pady=1)

    genders =["Male","Female", "Trans-Gender"]
    gender = StringVar()
    gender_ = ttk.OptionMenu(other_credentials,gender, *genders)
    gender_.grid(row=6, column=1, pady=1)
    other_credentials.grid(row=0, column=4, rowspan=3)
    Button(personaliseCopy, text="Set", width=10,bg="light blue",activebackground="blue",font=("arial", 10, "bold")).grid(row=3, column=0, pady=1, padx=3)
    Button(personaliseCopy, text="Close",bg="red",activebackground="blue", width=10, font=("arial", 10, "bold"),
           command=lambda: closeSettings( prefereS)).grid(row=3, column=1, pady=1, padx=3)
    Button(other_credentials, text="Restore",bg="orange",activebackground="blue", width=10, font=("arial", 10, "bold")).grid(row=7, column=0, pady=10,)
    Button(other_credentials, text="Apply",bg="green",activebackground="blue", width=10, font=("arial", 10, "bold")).grid(row=7, column=1, pady=10, sticky=E)

    themes_Available = themes
    Label(appearenceTab, text="Work Place Configuration and Preference",font=("arial", 12, "bold")).grid(row=0, column=0, columnspan=5)
    Label(appearenceTab, text="Font Size", font=("arial", 10, "bold")).grid(row=2, column=0, pady=2)
    Label(appearenceTab, text="Font Family", font=("arial", 10, "bold")).grid(row=1, column=0, pady=2)
    Label(appearenceTab, text="Theme Choice", font=("arial", 10, "bold")).grid(row=3, column=0, pady=2)
    font_family = StringVar()
    font_options = []
    font = tkinter.font.families()
    for i in font:
        font_options.append(i)
    font_family.set(font_options[10])
    font_size = IntVar()
    theme = StringVar()
    font_size.set(10)
    font_fam = ttk.OptionMenu(appearenceTab, font_family, *font_options)
    font_fam.grid(row=1, column=1, ipadx=35, columnspan=2, pady=2)
    font_s = ttk.Spinbox(appearenceTab, from_=8, to=25, increment=1, textvariable=font_size, width=5)
    font_fam.config(textvariable=font_family, direction="below")
    font_s.grid(row=2, column=1, columnspan=2, pady=2)
    themes = ttk.OptionMenu(appearenceTab, theme, *themes_Available)
    themes.grid(row=3, column=1, columnspan=2, pady=2)
    Label(appearenceTab, text="Sample Text", font=("arial", 10, "bold")).grid(row=5, column=0, columnspan=5)
    txtSample = Text(appearenceTab, insertwidth=10, width=45, height=5)
    txtSample.grid_propagate(False)
    for i in txtSample.keys():
        print(i)
    testString = """ABCDEFGHIJ KLMNOPQRST 
                    123456 7890
                    abcdefghi jklmnopqrs   
                    !#%&(]{=+\\//$*^"""
    txtSample.insert(END,testString)
    txtSample.grid(row=6, column=0, columnspan=5)
    print(font_size.get())
    print(font_family.get())
    Button(appearenceTab, text="Test", bg="sea green", activebackground="blue", width=10,
           font=("arial", 10, "bold"), command=lambda : setFontFunction(text=txtSample,f_family=font_family.get()
                                  , f_size=font_size.get())).grid(
        row=7, column=0, padx=3)
    Button(appearenceTab, text="Close", bg="red", activebackground="blue", width=10, font=("arial", 10, "bold"),
           command=lambda: closeSettings(prefereS)).grid(row=7, column=1,  padx=3)
    Button(appearenceTab, text="Restore", bg="orange", activebackground="blue", width=10, font=("arial", 10, "bold")).grid(
        row=7, column=2, padx=3)
    Button(appearenceTab, text="Apply", bg="green", activebackground="blue", width=10, font=("arial", 10, "bold")).grid(
        row=7, column=3, padx=3, pady=10)
    greetingMessage = ttk.Checkbutton(appearenceTab, text="Greeting Msg", underline=0)
    greetingMessage.grid(row=1, column=3, pady=2, sticky=W)
    spellingCheck = ttk.Checkbutton(appearenceTab, text="Spelling Check", underline=0)
    spellingCheck.grid(row=1, column=4, pady=2, sticky=W)
    autoCorrect = ttk.Checkbutton(appearenceTab, text="Auto-Correct", underline=0)
    autoCorrect.grid(row=2, column=3, pady=2, sticky=W)
    autoCapitalisation = ttk.Checkbutton(appearenceTab, text="Auto-Capitalisation", underline=0)
    autoCapitalisation.grid(row=2, column=4, pady=2, sticky=W)
    autoComplete = ttk.Checkbutton(appearenceTab, text="Auto-Completion", underline=0)
    autoComplete.grid(row=3, column=3, pady=2, sticky=W)
    suggestions = ttk.Checkbutton(appearenceTab, text="Suggestions", underline=0)
    suggestions.grid(row=3, column=4, pady=2, sticky=W)
    whiteSpaceTrim= ttk.Checkbutton(appearenceTab, text="Auto-Trim", underline=0)
    whiteSpaceTrim.grid(row=4, column=3, pady=2, sticky=W)
    prefferenceNotebook.grid(row=0, column=0, columnspan =5)
    return
def exitFunction():
    root.bell()
    choice = messagebox.askyesnocancel(title, "Are you sure you want to exit {}?".format(title))
    if (choice):
        root.destroy()
    else:
        root.focus()
    return
def barGraph():
    Label(root, text="Frequency (f)",background="white", font=fonts[6]).grid(row=5, column =1, sticky=E, padx=5)
    Label(root, text="Label Names (x)",background="white", font=fonts[6]).grid(row=4, column=1, sticky=E, padx=5)
    Label(root, text="Colors For Bars", background="white", font=fonts[6]).grid(row=6, column=1, sticky=E, padx=5)
    enableKey = ttk.Checkbutton(root, text="Enable Key")
    enableKey.grid(row=4, column =7, sticky=W, pady=5, padx=5)
    coloredBars = ttk.Checkbutton(root, text="Colored Bars")
    coloredBars.grid(row=4, column=8, sticky=W, pady=5, padx=5)
    horizontalBars = ttk.Checkbutton(root, text="Horizontal Bars")
    horizontalBars.grid(row=4, column=9, sticky=W, pady=5, padx=5)
    morePlots = ttk.Checkbutton(root, text="Enable N-plots")
    text1 = scrolledtext.ScrolledText(root, height=2, width= 80, font = ("Times New Roman", 12, "normal"))
    text2 = Text(root, height=0, width=80,font=("Times New Roman", 12, "normal"))
    text3 =scrolledtext.ScrolledText(root, height=0, width=80,font=("Times New Roman", 12, "normal"))

    Label(root, text="Graph Title", background="white", font=('Arial', 10,"bold")).grid(row=5, column=7, sticky=W, padx=5)
    Label(root, text="Graph (X) Label", background="white", font=('Arial', 10,"bold")).grid(row=4, column=0, sticky=W, padx=5)
    Label(root, text="Graph (Y) Label", background="white", font=('Arial', 10,"bold")).grid(row=6, column=0, sticky=W, padx=5)
    graphTitle = Entry(root, width=30)
    graphTitle.grid(row=5, column=8, sticky=E, padx=5, columnspan=2)

    graphXLabel = Entry(root)
    graphXLabel.grid(row=5, column=0, sticky=E, padx=5)
    graphYLabel = Entry(root)
    graphYLabel.grid(row=7, column=0, sticky=E, padx=5)

    btnPlot = Button(root, text ="Plot Figure", width =15)
    btnAddPlot= Button(root, text ="Add Plot", width =15)
    btnReset = Button(root, text="Reset", width=15)
    btnPlot.grid(row=6, column=7, sticky=W,padx=5)
    text1.grid(row=4, column =2, sticky=W, columnspan=5, pady=5)
    text2.grid(row=5, column =2, sticky=W, columnspan=5, pady=5)
    text3.grid(row=6, column =2, sticky=W, columnspan=5, pady=5)
    btnReset.grid(row=6, column=8, sticky=W,padx=5)
    morePlots.grid(row=6, column=9, sticky=W,padx=5)
    btnAddPlot.grid(row=9, column=9, sticky=W, padx=5)
    root.update()
    return
def histGraph():
    Label(root, text="Bins(n) [range width] ", background="white", font=fonts[6]).grid(row=5, column=1, sticky=E, padx=5)
    Label(root, text="Values (x)", background="white", font=fonts[6]).grid(row=4, column=1, sticky=E, padx=5)
    Label(root, text="Colors For Bars", background="white", font=fonts[6]).grid(row=6, column=1, sticky=E, padx=5)
    enableKey = ttk.Checkbutton(root, text="Enable Key")
    enableKey.grid(row=4, column=7, sticky=W, pady=5, padx=5)
    coloredBars = ttk.Checkbutton(root, text="Colored Bars")
    coloredBars.grid(row=4, column=8, sticky=W, pady=5, padx=5)
    horizontalBars = ttk.Checkbutton(root, text="Horizontal Bars")
    horizontalBars.grid(row=4, column=9, sticky=W, pady=5, padx=5)
    morePlots = ttk.Checkbutton(root, text="Enable N-plots")
    text1 = scrolledtext.ScrolledText(root, height=2, width=80, font=("Times New Roman", 12, "normal"))
    text2 = Text(root, height=0, width=80, font=("Times New Roman", 12, "normal"))
    text3 = scrolledtext.ScrolledText(root, height=0, width=80, font=("Times New Roman", 12, "normal"))

    Label(root, text="Graph Title", background="white", font=('Arial', 10, "bold")).grid(row=5, column=7, sticky=W,
                                                                                         padx=5)
    Label(root, text="Graph (X) Label", background="white", font=('Arial', 10, "bold")).grid(row=4, column=0, sticky=W,
                                                                                             padx=5)
    Label(root, text="Graph (Y) Label", background="white", font=('Arial', 10, "bold")).grid(row=6, column=0, sticky=W,
                                                                                             padx=5)
    graphTitle = Entry(root, width=30)
    graphTitle.grid(row=5, column=8, sticky=E, padx=5, columnspan=2)

    graphXLabel = Entry(root)
    graphXLabel.grid(row=5, column=0, sticky=E, padx=5)
    graphYLabel = Entry(root)
    graphYLabel.grid(row=7, column=0, sticky=E, padx=5)

    btnPlot = Button(root, text="Plot Figure", width=15)
    btnAddPlot = Button(root, text="Add Plot", width=15)
    btnReset = Button(root, text="Reset", width=15)
    btnPlot.grid(row=6, column=7, sticky=W, padx=5)
    text1.grid(row=4, column=2, sticky=W, columnspan=5, pady=5)
    text2.grid(row=5, column=2, sticky=W, columnspan=5, pady=5)
    text3.grid(row=6, column=2, sticky=W, columnspan=5, pady=5)
    btnReset.grid(row=6, column=8, sticky=W, padx=5)
    morePlots.grid(row=6, column=9, sticky=W, padx=5)
    btnAddPlot.grid(row=9, column=9, sticky=W, padx=5)
    root.update()
    return
def pieChat():
    Label(root, text="Frequency (f)",background="white", font=fonts[6]).grid(row=5, column =1, sticky=E, padx=5)
    Label(root, text="Label Names (x)",background="white", font=fonts[6]).grid(row=4, column=1, sticky=E, padx=5)
    Label(root, text="Colors For Sectors", background="white", font=fonts[6]).grid(row=6, column=1, sticky=E, padx=5)
    enableKey = ttk.Checkbutton(root, text="Enable Key")
    enableKey.grid(row=4, column =7, sticky=W, pady=5, padx=5)
    coloredBars = ttk.Checkbutton(root, text="Colored Sectors")
    coloredBars.grid(row=4, column=8, sticky=W, pady=5, padx=5)
    horizontalBars = ttk.Checkbutton(root, text="Horizontal Bars", state=DISABLED)
    horizontalBars.grid(row=4, column=9, sticky=W, pady=5, padx=5)
    morePlots =ttk.Checkbutton(root, text="Enable N-plots", state=DISABLED)
    text1 = scrolledtext.ScrolledText(root, height=2, width= 80, font = ("Times New Roman", 12, "normal"))
    text2 = Text(root, height=0, width=80,font=("Times New Roman", 12, "normal"))
    text3 =scrolledtext.ScrolledText(root, height=0, width=80,font=("Times New Roman", 12, "normal"))

    Label(root, text="Graph Title", background="white", font=('Arial', 10,"bold")).grid(row=5, column=7, sticky=W, padx=5)
    Label(root, text="Graph (X) Label", background="white", font=('Arial', 10,"bold")).grid(row=4, column=0, sticky=W, padx=5)
    Label(root, text="Graph (Y) Label", background="white", font=('Arial', 10,"bold")).grid(row=6, column=0, sticky=W, padx=5)
    graphTitle = Entry(root, width=30)
    graphTitle.grid(row=5, column=8, sticky=E, padx=5, columnspan=2)

    graphXLabel = Entry(root, state=DISABLED)
    graphXLabel.grid(row=5, column=0, sticky=E, padx=5)
    graphYLabel = Entry(root, state=DISABLED)
    graphYLabel.grid(row=7, column=0, sticky=E, padx=5)

    btnPlot = Button(root, text ="Plot Figure", width =15)
    btnAddPlot= Button(root, text ="Add Plot", width =15, state=DISABLED)
    btnReset = Button(root, text="Reset", width=15)
    btnPlot.grid(row=6, column=7, sticky=W,padx=5)
    text1.grid(row=4, column =2, sticky=W, columnspan=5, pady=5)
    text2.grid(row=5, column =2, sticky=W, columnspan=5, pady=5)
    text3.grid(row=6, column =2, sticky=W, columnspan=5, pady=5)
    btnReset.grid(row=6, column=8, sticky=W,padx=5)
    morePlots.grid(row=6, column=9, sticky=W,padx=5)
    btnAddPlot.grid(row=9, column=9, sticky=W, padx=5)
    root.update()
    return
def lineGraph():
    Label(root, text="Values (x)", background="white", font=fonts[6]).grid(row=5, column=1, sticky=E, padx=5)
    Label(root, text="Values (y)", background="white", font=fonts[6]).grid(row=4, column=1, sticky=E, padx=5)
    Label(root, text="Colors For Lines", background="white", font=fonts[6]).grid(row=6, column=1, sticky=E, padx=5)
    enableKey = ttk.Checkbutton(root, text="Enable Key")
    enableKey.grid(row=4, column=7, sticky=W, pady=5, padx=5)
    coloredBars = ttk.Checkbutton(root, text="Colored Lines")
    coloredBars.grid(row=4, column=8, sticky=W, pady=5, padx=5)
    horizontalBars = ttk.Checkbutton(root, text="Horizontal Lines")
    horizontalBars.grid(row=4, column=9, sticky=W, pady=5, padx=5)
    morePlots = ttk.Checkbutton(root, text="Enable N-plots")
    text1 = scrolledtext.ScrolledText(root, height=2, width=80, font=("Times New Roman", 12, "normal"))
    text2 = Text(root, height=0, width=80, font=("Times New Roman", 12, "normal"))
    text3 = scrolledtext.ScrolledText(root, height=0, width=80, font=("Times New Roman", 12, "normal"))

    Label(root, text="Graph Title", background="white", font=('Arial', 10, "bold")).grid(row=5, column=7, sticky=W,
                                                                                         padx=5)
    Label(root, text="Graph (X) Label", background="white", font=('Arial', 10, "bold")).grid(row=4, column=0, sticky=W,
                                                                                             padx=5)
    Label(root, text="Graph (Y) Label", background="white", font=('Arial', 10, "bold")).grid(row=6, column=0, sticky=W,
                                                                                             padx=5)
    graphTitle = Entry(root, width=30)
    graphTitle.grid(row=5, column=8, sticky=E, padx=5, columnspan=2)

    graphXLabel = Entry(root)
    graphXLabel.grid(row=5, column=0, sticky=E, padx=5)
    graphYLabel = Entry(root)
    graphYLabel.grid(row=7, column=0, sticky=E, padx=5)

    btnPlot = Button(root, text="Plot Figure", width=15)
    btnAddPlot = Button(root, text="Add Plot", width=15)
    btnReset = Button(root, text="Reset", width=15)
    btnPlot.grid(row=6, column=7, sticky=W, padx=5)
    text1.grid(row=4, column=2, sticky=W, columnspan=5, pady=5)
    text2.grid(row=5, column=2, sticky=W, columnspan=5, pady=5)
    text3.grid(row=6, column=2, sticky=W, columnspan=5, pady=5)
    btnReset.grid(row=6, column=8, sticky=W, padx=5)
    morePlots.grid(row=6, column=9, sticky=W, padx=5)
    btnAddPlot.grid(row=9, column=9, sticky=W, padx=5)
    # creating a frame
    frame_plot = Frame(root)
    fig = plt.figure(num=None, figsize=(7, 3), facecolor='white', edgecolor='k')
    plots = fig.add_subplot(111)


    # creating data
    riding = [(17, 18, 21, 22, 19, 21, 25, 22, 25, 24),
              (3, 6, 3.5, 4, 5, 6.3, 4.5, 5, 4.5, 4)]
    swimming = ((17, 18, 20, 19, 22, 21, 23, 19, 21, 24),
                (8, 9, 7, 10, 7.5, 9, 8, 7, 8.5, 9))
    sailing = ((31, 28, 29, 36, 27, 32, 34, 35, 33, 39),
               (4, 6.3, 6, 3, 5, 7.5, 2, 5, 7, 4))
    plots.scatter(riding[0], riding[1], marker="o", edgecolors="black", label="Ridding")
    plots.scatter(swimming[0], swimming[1], marker="*", edgecolors="g", color="red", label="Swimming")
    plots.scatter(sailing[0], sailing[1], marker="^", color="black", label="Snailing")
    plt.legend(title="Key")
    plt.ylabel("Number of Hours")
    plt.xlabel("Age")
    plt.title("The Scatter Plot Title")


    canvas = FigureCanvasTkAgg(figure=fig, master=frame_plot)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar =NavigationToolbar2Tk(canvas=canvas, window= frame_plot)
    toolbar.update()
    canvas.get_tk_widget().pack(pady=5)
    frame_plot.grid(row=10, column=1, columnspan =8)
    root.update()
    return
###############################################################################################
imgCopy = ImageTk.PhotoImage(Image.open(copy_icon))
imgPaste = ImageTk.PhotoImage(Image.open(paste_icon))
imgOpen = ImageTk.PhotoImage(Image.open(open_icon))
imgExit = ImageTk.PhotoImage(Image.open(exit_icon))
imgExcel = ImageTk.PhotoImage(Image.open(excel_icon))
imgCut = ImageTk.PhotoImage(Image.open(cut_icon))
imgBar = ImageTk.PhotoImage(Image.open("bar.png"))
img = ImageTk.PhotoImage(Image.open("bar.png"))
imgPie = ImageTk.PhotoImage(Image.open("pie.png"))
imgLine = ImageTk.PhotoImage(Image.open("line.png"))
imgHist = ImageTk.PhotoImage(Image.open("histogram.png"))
imgScatter = ImageTk.PhotoImage(Image.open("scatter.png"))
img3D = ImageTk.PhotoImage(Image.open("3Dplots.png"))
imgBoxW = ImageTk.PhotoImage(Image.open("boxplot.png"))
imgCumulative = ImageTk.PhotoImage(Image.open("cumulative.png"))
imgWord = ImageTk.PhotoImage(Image.open("wordfile.png"))
imgText = ImageTk.PhotoImage(Image.open("textfile.png"))
imgQuatile = ImageTk.PhotoImage(Image.open("quatile.png"))
imgSave = ImageTk.PhotoImage(Image.open("save.png"))
imgSaveAll = ImageTk.PhotoImage(Image.open("saveAll.png"))
imgSaveAs = ImageTk.PhotoImage(Image.open("saveAs.png"))
imgshare = ImageTk.PhotoImage(Image.open("share.png"))
imgSettings= ImageTk.PhotoImage(Image.open("settings.png"))
imgprint = ImageTk.PhotoImage(Image.open("print.png"))
imgHome = ImageTk.PhotoImage(Image.open("home.png"))
imgdatabase = ImageTk.PhotoImage(Image.open("database1.png"))
imgGallery = ImageTk.PhotoImage(Image.open("gallery.png"))
imgAboutS = ImageTk.PhotoImage(Image.open("aboutUs.png"))
imgAboutDevelopers = ImageTk.PhotoImage(Image.open("about.png"))
imgJoinDevelopers = ImageTk.PhotoImage(Image.open("about.png"))
imgManagerDevelopers = ImageTk.PhotoImage(Image.open("join.png"))
imgTeamDevelopers = ImageTk.PhotoImage(Image.open("team.png"))
imgHelp = ImageTk.PhotoImage(Image.open("help.png"))
imgHelpOnline = ImageTk.PhotoImage(Image.open("helpOnline.png"))
imgNotesHelp = ImageTk.PhotoImage(Image.open("notes.png"))
imageFrame =ImageTk.PhotoImage(Image.open("formular2.png"))
imgData=ImageTk.PhotoImage(Image.open("data.png"))
imgSeach=ImageTk.PhotoImage(Image.open("search.png"))
imgView=ImageTk.PhotoImage(Image.open("moresettings.png"))
imgInsert=ImageTk.PhotoImage(Image.open("insert.png"))
imgMoreFomulars = ImageTk.PhotoImage(Image.open("more_formular.png"))

imgEmail=ImageTk.PhotoImage(Image.open("email.png"))
imgOnlineServices=ImageTk.PhotoImage(Image.open("onlineservices.png"))
imgCVS=ImageTk.PhotoImage(Image.open("cvs.png"))
imgPostgre=ImageTk.PhotoImage(Image.open("postgreSQL.png"))
imgSQL=ImageTk.PhotoImage(Image.open("sql.png"))

imgPublish=ImageTk.PhotoImage(Image.open("publish.png"))
imgMySQL=ImageTk.PhotoImage(Image.open("mysql.png"))
imgFax=ImageTk.PhotoImage(Image.open("fax.png"))
imgJson=ImageTk.PhotoImage(Image.open("json.png"))
imgXML=ImageTk.PhotoImage(Image.open("xml.png"))

imgZip=ImageTk.PhotoImage(Image.open("zip.png"))
imgBluetooth=ImageTk.PhotoImage(Image.open("bluetooth.png"))
imgWhatNew=ImageTk.PhotoImage(Image.open("whatsnew.png"))
imgOracle=ImageTk.PhotoImage(Image.open("oracle.png"))
imgFax=ImageTk.PhotoImage(Image.open("fax.png"))
imgFav =ImageTk.PhotoImage(Image.open("favourite.png"))

imgAaccess=ImageTk.PhotoImage(Image.open("acess2.png"))
imgDBA=ImageTk.PhotoImage(Image.open("databaseAdd.png"))
imgDBD=ImageTk.PhotoImage(Image.open("databaseDelete.png"))
imgDBQ=ImageTk.PhotoImage(Image.open("databaseQuery.png"))
imgMongo=ImageTk.PhotoImage(Image.open("mong.png"))
imgSQL3=ImageTk.PhotoImage(Image.open("sqlite3.png"))

imgContactSupport=ImageTk.PhotoImage(Image.open("contactSuport.png"))
imgAccess=ImageTk.PhotoImage(Image.open("access.png"))
imgFeedback=ImageTk.PhotoImage(Image.open("feedback.png"))
imgGoogle=ImageTk.PhotoImage(Image.open("google.png"))
imgRaccess=ImageTk.PhotoImage(Image.open("removeacess.png"))

imgFontPlus=ImageTk.PhotoImage(Image.open("fontplus.png"))
imgFontMinus=ImageTk.PhotoImage(Image.open("fontminus.png"))
imgFontColor=ImageTk.PhotoImage(Image.open("fontColor.png"))
imgFontCaps=ImageTk.PhotoImage(Image.open("fontCaps.png"))
imgReplace=ImageTk.PhotoImage(Image.open("replace.png"))
imgSelect=ImageTk.PhotoImage(Image.open("select.png"))

imgOpenLocation=ImageTk.PhotoImage(Image.open("default_location.png"))
imgSaveLocation=ImageTk.PhotoImage(Image.open("default_location.png"))
imgfileProp=ImageTk.PhotoImage(Image.open("fileProperties.png"))
imgMacros=ImageTk.PhotoImage(Image.open("macro.png"))
imgUpdates =ImageTk.PhotoImage(Image.open("updates.png"))
imageProfiles =ImageTk.PhotoImage(Image.open("profileMe.png"))

imagEditMacro =ImageTk.PhotoImage(Image.open("recordmacro.png"))
imagPlayMacro =ImageTk.PhotoImage(Image.open("play.png"))
imagRecordMacro =ImageTk.PhotoImage(Image.open("record.png"))
imgThisPC =ImageTk.PhotoImage(Image.open("thisPc.png"))
imgCurrentSubFolders =ImageTk.PhotoImage(Image.open("subfolder.png"))
imgCurrentFolders =ImageTk.PhotoImage(Image.open("currentFolder.png"))
imgFileLocation=ImageTk.PhotoImage(Image.open("file_location.png"))
imgDateModified=ImageTk.PhotoImage(Image.open("datemodified.png"))
imgOtherProp =ImageTk.PhotoImage(Image.open("fileProperties.png"))
imgRecentOpened =ImageTk.PhotoImage(Image.open("recendOpened.png"))
imgFileLocation =ImageTk.PhotoImage(Image.open("file_location.png"))
imgSaveSearch =ImageTk.PhotoImage(Image.open("saveAll.png"))
exit_ico = ImageTk.PhotoImage(Image.open('exit.png'))
# Menu
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
# Notebook:
notebookmain = ttk.Notebook(root, height=95)
# tabs
HomeMenu = Frame(notebookmain)
DataBase = Frame(notebookmain)
Gallery = Frame(notebookmain)
Share= Frame(notebookmain)
Print=Frame(notebookmain)
Fomular = Frame(notebookmain)
Data = Frame(notebookmain)
More = Frame(notebookmain)
Search =Frame(notebookmain)
ttk.Style().configure("TFrame", background="seagreen")
ttk.Style().configure("TButton", background="blue",)
notebookmain.add(Fomular, text="    Formulae   ", image=imageFrame, compound=LEFT)
notebookmain.add(HomeMenu, text="   Home     ", image=imgHome, compound=LEFT)
notebookmain.add(DataBase, text="   Database     ", image=imgdatabase, compound=LEFT)
notebookmain.add(Gallery, text="    Gallery  ", image=imgGallery, compound=LEFT)
notebookmain.add(Data, text="    Data   ", image=imgData, compound=LEFT)
notebookmain.add(Print, text="  Print   ", image=imgprint, compound=LEFT)
notebookmain.add(Share, text="  Share    ", image=imgshare, compound=LEFT, underline=2)
notebookmain.add(More, text="   More     ", image=imgView, compound=LEFT)
notebookmain.add(Search, text="     Search   ", image=imgSeach, compound=LEFT)

###########################################################################
##########################################################################
## File Menu
def fileMenu():
    open_submenu = Menu(file_menu, tearoff=0)
    open_submenu.add_command(label="   Excel File", image=imgExcel, compound=LEFT)
    open_submenu.add_command(label="   Text File", image=imgText, compound=LEFT)
    open_submenu.add_command(label="   Word File", image=imgWord, compound=LEFT)
    open_submenu.add_separator()
    open_submenu.add_command(label="   Close", image=imgExit, compound=LEFT)
    file_menu.add_cascade(label="   Open", menu=open_submenu, image=imgOpen, compound=LEFT)
    file_menu.add_command(label="   Copy", image=imgCopy, compound=LEFT)
    file_menu.add_command(label="   Cut", image=imgCut, compound=LEFT)
    file_menu.add_command(label="   Paste", image=imgPaste, compound=LEFT)
    file_menu.add_separator()
    file_menu.add_command(label="   Save As", image=imgSaveAs, compound=LEFT)
    file_menu.add_command(label="   Save All", image=imgSaveAll, compound=LEFT)
    file_menu.add_command(label="   Save", image=imgSave, compound=LEFT)
    file_menu.add_separator()
    file_menu.add_command(label=" Exit", image=imgExit, compound=LEFT, command=exitFunction)
    menubar.add_cascade(label="   File  ", menu=file_menu)
    return
## Plots Menu
def plotsMenu():
    plots_menu = Menu(menubar, tearoff=0)
    plots_menu.add_command(label=" Bar Graph", image=imgBar, compound=LEFT, command =barGraph)
    plots_menu.add_command(label=" Line Graph", image=imgLine, compound=LEFT, command=lineGraph)
    plots_menu.add_command(label=" Pie Plot", image=imgPie, compound=LEFT, command =pieChat)
    plots_menu.add_command(label=" Histogram", image=imgHist, compound=LEFT, command=histGraph)
    plots_menu.add_separator()
    plots_menu.add_command(label=" Scatter Plot", image=imgScatter, compound=LEFT)
    plots_menu.add_command(label=" Box Whisker Plot", image=imgBoxW, compound=LEFT)
    plots_menu.add_command(label=" Cumulative Plot", image=imgCumulative, compound=LEFT)
    plots_menu.add_separator()
    plots_menu.add_command(label=" 3-D Plot", image=img3D, compound=LEFT)
    menubar.add_cascade(label="  Plots  ", menu=plots_menu)
    return
### Central tendency Menu
def centralTendencyMenu():
    central_tendency = Menu(menubar, tearoff=0)
    central_tendency.add_command(label="    Mean")
    central_tendency.add_command(label="    Median")
    central_tendency.add_command(label="    Mode")
    central_tendency.add_separator()
    quatile = Menu(central_tendency, tearoff=0)
    quatile.add_command(label="Lower Quartile")
    quatile.add_command(label="Upper Quartile")
    central_tendency.add_cascade(label="   Quartile", menu=quatile, image=imgQuatile, compound=LEFT)
    menubar.add_cascade(label="Central Tendency", menu=central_tendency)
    return
## Setting menu
def settingMenu():
    setting_menu = Menu(menubar, tearoff=0)
    setting_menu.add_command(label="Preferences", image=imgSettings, compound=LEFT, command=preferences)
    setting_menu.add_command(label="More Settings", image=imgSettings, compound=LEFT, command=moreSettings)
    menubar.add_cascade(label="   Settings   ", menu=setting_menu)
    return
## View menu
def viewMenu():
    view_menu = Menu(menubar, tearoff=0)
    view_menu.add_command(label="Minimise")
    view_menu.add_command(label="Maximise")
    view_menu.add_separator()
    view_menu.add_checkbutton(label="Main Menu")
    view_menu.add_checkbutton(label="Status Bar", command=print(5))
    view_menu.add_separator()
    view_menu.add_command(label="Exit", command=exitFunction, compound=LEFT, image=imgExit)
    menubar.add_cascade(label="   View  ", menu=view_menu)
    return
## Help
def helpMenu():
    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="   Strawbery Help", image = imgHelp, compound=LEFT)
    help_menu.add_command(label="   Online Help", image = imgHelpOnline, compound=LEFT)
    help_menu.add_separator()
    help_menu.add_command(label="   Notes", image = imgNotesHelp, compound=LEFT)
    menubar.add_cascade(label="  Help    ", menu=help_menu)
    return
# About Menu
def aboutMenu():
    aboutmenu = Menu(menubar, tearoff=0)
    aboutmenu.add_command(label="   Strawberry", image=imgAboutS, compound=LEFT)
    developer = Menu(aboutmenu, tearoff=0)
    developer.add_command(label="   Team", image=imgTeamDevelopers, compound=LEFT)
    developer.add_command(label="   Manager", image=imgManagerDevelopers, compound=LEFT)
    developer.add_command(label="   Join Team", image=imgJoinDevelopers, compound=LEFT)
    aboutmenu.add_cascade(label="   Developers", menu=developer, image=imgAboutDevelopers, compound=LEFT)
    menubar.add_cascade(label="About", menu=aboutmenu, compound=LEFT, command=root.destroy)
    return
# FOMULAR TAB AND IT'S FUNCTIONALITY
def formularTab(Fomular):
    estimation = StringVar()
    linear_trans= StringVar()
    discrete_probab = StringVar()

    Label(Fomular, text="Estimation", font =("Arial", 10,"bold")
          ).grid(row=0, column=0, sticky=W)
    estimation_values =["confidence interval", "margin of error"]
    estimation_formula= ttk.OptionMenu(Fomular,estimation,estimation_values[1], *estimation_values)
    estimation_formula.grid(row=0, sticky=W, column=1)
    Label(Fomular, text="Linear \nTransformation", font =("Arial", 10,"bold")
          ).grid(row=1, column=0, sticky=W)
    linear_transformation_values =["Mean of linear \ntransformation", "Varience of linear\n transformation"
                                   ,"Standardized Score", "T-Statistics"]
    linear_transformation= ttk.OptionMenu(Fomular,linear_trans,linear_transformation_values[1], *linear_transformation_values)
    linear_transformation.grid(row=1, sticky=W, column=1)

    Label(Fomular, text="Discrete \nProbability", font =("Arial", 10,"bold")
          ).grid(row=0, column=6, sticky=W)
    discrete_probab_values =["Bionomial Fomular", "Mean of \nBion Dist",
                             "Varience of \nBiono Dist",
                             "(-ve) \nBion Fomular", "Mean of (-ve)\n Bion- F",
                             "varience of\n (-ve) Bion- F", "Geometric Fom", "Mean of Geo-F",
                             "varience of\n Geo Dist", "Hyper-Geo Dist", "varience of\n Hyper-Geo",
                             "Poison Fomular", "Mean of\ Poison Dist",
                             "Varience of\n Poison Dist", "Mutinomial\n formular"]
    discrete_probab_= ttk.OptionMenu(Fomular,discrete_probab,discrete_probab_values[1], *discrete_probab_values)
    discrete_probab_.grid(row=0, sticky=W, column=7)
    ttk.Separator(Fomular, orient=VERTICAL).grid(row=0, column=2, rowspan =2, ipady=45)

    hypothesis_value = StringVar()
    degreeOfFredom = StringVar()
    Label(Fomular, text="Hypothesis Testing", font =("Arial", 10,"bold")
          ).grid(row=0, column=3, sticky=W)
    hypothesis_testing_values=["Standard Test\n Stats", "1-sample 2-test\n for propotions",
                               "2-sample 2 \ntest for propotions", "1-sample t-test\n for means",
                               "2-sample t-test\n for means", "method-sample \nt-sample for means",
                               "Chi-square test Stats"]
    hypothesis_testing=ttk.OptionMenu(Fomular,hypothesis_value,hypothesis_testing_values[1], *hypothesis_testing_values)
    hypothesis_testing.grid(row=0, column=4, sticky=W)
    Label(Fomular, text="Degrees of\n Freedom (df)", font =("Arial", 10,"bold")
          ).grid(row=1, column=3, sticky=W)
    df_values =["1-sample t-test", "2-sample t-test",
                "2-sample t-test\n pooled standard error",
                "simple linear \nregression test slope",
                "Chi-Square test \nHomogenety",
                "Chi-Square test\n Independence"]
    df=ttk.OptionMenu(Fomular,degreeOfFredom,df_values[1], *df_values)
    df.grid(row=1, column=4, sticky=W)
    sample_size= StringVar()
    ttk.Separator(Fomular, orient=VERTICAL).grid(row=0, column=5, rowspan =2, ipady=45)
    Label(Fomular, text="Sample Size (n)", font =("Arial", 10,"bold")
          ).grid(row=1, column=6, sticky=W)
    sample_size_values =["Mean simple \n random sampling", "Propotion \n(random sampling) ",
                         "Propotionate \n Stratified sampling", "Neyma allocation", "Opitmum alocation"]
    n=ttk.OptionMenu(Fomular,sample_size,sample_size_values[1], *sample_size_values)
    n.grid(row=1, column=7, sticky=W)
    ttk.Separator(Fomular, orient=VERTICAL).grid(row=0, column=8, rowspan =2, ipady=45)
    frame_formula = Frame(Fomular)

    parameter = StringVar()
    parameters = ["population mean", "population varience", "population standard\n deviation",
                  "population propotion\n varience", "starndard score (Z)", "population correlation\n coefficient"]
    Label(frame_formula, text="Parameters",underline=0, font =("Arial", 10,"bold")
          ).grid(row=0, column=0, sticky=W)
    params= ttk.OptionMenu(frame_formula,parameter,parameters[1], *parameters)
    params.grid(row=0, sticky=W, column=1)
    stats = StringVar()
    stats_values=["sample mean","sample standard \ndeviation (s)", "sample variance",
                  "propotion varience", "pooled sample (s)", "sample correlation\n coefficient"]
    Label(frame_formula, text="Statistics",underline=0, font =("Arial", 10,"bold")
          ).grid(row=1, column=0, sticky=W)
    params= ttk.OptionMenu(frame_formula,stats,stats_values[1], *stats_values)
    params.grid(row=1, sticky=W, column=1)
    ttk.Separator(frame_formula,orient=VERTICAL).grid(row=0, column=3, rowspan =2, ipady=45)
    correletion = StringVar()
    Label(frame_formula, text="Correlation",underline=0, font =("Arial", 10,"bold")
          ).grid(row=0, column=4, sticky=W)
    correletion_values=["Pearson product-\n moment correlation", "linear correlation\n (sample data)",
                        "linear correlation\n (population data)"]
    corr= ttk.OptionMenu(frame_formula,correletion,correletion_values[1], *correletion_values)
    corr.grid(row=0, sticky=W, column=5)
    regression = StringVar()
    Label(frame_formula, text="Simple Linear \nRegression",underline=0, font =("Arial", 10,"bold")
          ).grid(row=1, column=4, sticky=W)
    regression_values=["Simple Linear\n Regression Line", "Regression Coeef", "Regression Slope\n Intercept",
                       "Standard error \n(Regression Slope)", ""]
    regre= ttk.OptionMenu(frame_formula,regression,regression_values[1], *regression_values)
    regre.grid(row=1, sticky=W, column=5)
    ttk.Separator(frame_formula,orient=VERTICAL).grid(row=0, column=6, rowspan =2, ipady=45)

    more_Menu = Menu(frame_formula, tearoff=0)
    more_Menu.add_command(label="Factorials (n!)")
    more_Menu.add_command(label="Permutations")
    more_Menu.add_command(label="Combinations")
    more_Menu.add_cascade(label="Counting")
    more_Menu.add_separator()
    more_Menu.add_command(label="Standard Error Propotion")
    more_Menu.add_cascade(label="Standard error of difference proportions")
    more_Menu.add_command(label="Standard Error of the mean paired")
    more_Menu.add_cascade(label="Standard error of difference sample means")
    more_Menu.add_command(label="Pooled sample standard error")
    more_Menu.add_cascade(label="Standard error of diff(sample proportions)")
    more_Menu.add_separator()
    more_Menu.add_command(label="Rule of Addition")
    more_Menu.add_command(label="Rule of Multplication")
    more_Menu.add_command(label="Rule of Subtraction")
    more_Menu.add_separator()
    more_Menu.add_command(label="Expected Value E(x)")
    more_Menu.add_command(label="Varience of x Var(x)")
    more_Menu.add_command(label="Normal Random Distribution (Z score)")
    more_Menu.add_command(label="Chi-square Distribution")
    more_Menu.add_command(label="F- Statistics")
    more_Menu.add_command(label="E(X - Y) or E(X) - E(Y)")
    more_Menu.add_command(label="E(X + Y) or E(X) + E(Y)")
    more_Menu.add_command(label="Var(X + Y) or Var(X) + Var(y)")
    more_Menu.add_command(label="Var(X - Y) or Var(X) + Var(y)")
    more_Menu.add_separator()
    more_Menu.add_command(label="Mean of Sampling Dist of the mean")
    more_Menu.add_command(label="Mean of Sampling Dist of the propotion")
    more_Menu.add_command(label="Standard Deviation of the propotion")
    more_Menu.add_command(label="Standard Deviation of the mean")
    more_Menu.add_command(label="Standard deviation of diffrence of sample means")
    more_Menu.add_command(label="Standard deviation of diffrence of sample")
    def moreFomulars(event):
        more_Menu.tk_popup(x=event.x_root, y=event.y_root)
        more_Menu.grab_release()
        print(7)
        return
    btn_moreFomulars= Button(frame_formula, text="More Formulars", font=("Arial", 10, "bold"),
           underline=0, compound=BOTTOM,state=DISABLED, relief=FLAT,image=imgMoreFomulars)
    btn_moreFomulars.grid(row=0, column=7, rowspan=2, ipady=20)
    ttk.Separator(frame_formula,orient=VERTICAL).grid(row=0, column=8, rowspan =2, ipady=45)
    btn_moreFomulars.bind('<Button-3>', moreFomulars)
    frame_formula.grid(row=0, rowspan=2, column=9, columnspan =2)
    return
#PRINT AND ITS FUNCTIONALITIES
def printTab(Print):
    Label(Print, text="DEFAULT PRINTERS", font =("Arial", 10,"bold")).grid(row=0, column=0, sticky=W, columnspan=2)
    Button(Print, text="PRINT ", image=imgprint, compound =BOTTOM, state="disabled",relief=FLAT,).grid(row=1, column=0, sticky=W, ipadx=15, ipady=5)
    Button(Print, text="FAX ", image=imgFax, compound =BOTTOM, state="disabled", relief=FLAT,).grid(row=1, column=1, sticky=W, ipadx=15, ipady=5)
    ttk.Separator(Print, orient=VERTICAL).grid(row=0, column=2, rowspan =2, ipady=45)
    return
# SEARCH TAB AND ITS FUNCTIONALITIES
def searchTab(Search):
    Label(Search, text="Search From", font =("Arial", 10,"bold")).grid(row=0, column=0, sticky=W)
    Button(Search, text="This PC ", image=imgThisPC, compound =BOTTOM, relief=FLAT, state="disabled").grid(row=1, column=0, sticky=W, ipadx=15, ipady=2)
    Button(Search, text=" Current\n Folder ", image=imgCurrentFolders, compound =BOTTOM, relief=FLAT,state="disabled").grid(row=0,ipadx=4, column=1,ipady=12, sticky=W, rowspan=2)
    Button(Search, text="Current\n Subfolders", image=imgCurrentSubFolders, compound =BOTTOM, relief=FLAT,state="disabled").grid(row=0, column=2, ipady=12,sticky=W, rowspan=2)
    ttk.Separator(Search, orient=VERTICAL).grid(row=0, column=3, rowspan =2, ipady=45)
    Label(Search, text="Filter Files By Size Type And Property", font =("Arial", 11,"bold")).grid(row=0, column=4, columnspan=4)

    Label(Search, text="File Types", font =("Arial", 10,"bold"), underline=5).grid(row=1, column=5, sticky=W)
    Button(Search, text="Other \n Properties", image=imgOtherProp, compound
                =BOTTOM, relief=FLAT, state="disabled").grid(row=1, column=4, sticky=W)

    filetype= StringVar()
    file_types_Options = ["txt","cvs","excel", "xml", "json"]
    filetype.set("txt")
    file_type = ttk.OptionMenu(Search,filetype, *file_types_Options)
    file_type.grid(row=1, column=6)

    Label(Search, text="File Sizes", font =("Arial", 10,"bold"), underline=14, compound=TOP ).grid(row=1, column=7, sticky=W)
    filesize= IntVar()
    file_size_Options = [1,2,3,4,5]
    filesize.set(2)
    file_sizes = ttk.OptionMenu(Search,filesize, *file_size_Options)
    file_sizes.grid(row=1, column=8)
    ttk.Separator(Search, orient=VERTICAL).grid(row=0, column=9, rowspan =2, ipady=45)
    frame_dateModified = Frame(Search)
    Button(frame_dateModified, text="Date Modified", relief=FLAT, image=imgDateModified, compound=BOTTOM, state="disabled").grid(row=0,column=0)
    ttk.Separator(frame_dateModified, orient=VERTICAL).grid(row=0, column=1, rowspan =2, ipady=45)
    Button(frame_dateModified, text="Save Search",  relief=FLAT,image=imgSaveSearch, compound=BOTTOM, state="disabled").grid(row=0,column=3)
    Button(frame_dateModified, text="Close Search",  relief=FLAT,image=imgExit, compound=BOTTOM, state="disabled").grid(row=1,column=3)
    Button(frame_dateModified, text="Open File\n Location", relief=FLAT,image=imgFileLocation, compound=BOTTOM,state="disabled").grid(row=0,column=5, rowspan=2)
    ttk.Separator(frame_dateModified, orient=VERTICAL).grid(row=0, column=6, rowspan =2, ipady=45)
    frame_dateModified.grid(row=0, column=10, rowspan=2)
    return
# GALERY TAB AND IT'S FUNCTIONALITY
def galleryTab(Gallery):
    Label(Gallery, text="Favourites", font =("Arial", 11,"bold")).grid(row=0, column=0, sticky=W)
    Button(Gallery, text="Favourites", image=imgFav,relief=FLAT, compound=BOTTOM, font=("Arial", 10, "bold"), state="disabled").grid(row=1, column=0, ipadx=10, ipady=5)
    ttk.Separator(Gallery, orient=VERTICAL).grid(row=0, column=1, rowspan=2, ipady=45, padx=5)

    Label(Gallery, text="Open From PC", font =("Arial", 11,"bold")).grid(row=0, column=2, sticky=W)
    Button(Gallery, text="This PC", image=imgThisPC,relief=FLAT,
           compound=BOTTOM, font=("Arial", 10, "bold"),state="disabled").grid(row=1, column=2, ipadx=20, ipady=5)
    ttk.Separator(Gallery, orient=VERTICAL).grid(row=0, column=3, rowspan=2, ipady=45, padx=5)

    Label(Gallery, text="Resent Opened", font =("Arial", 11,"bold")).grid(row=0, column=4, sticky=W, columnspan =3)
    Button(Gallery, text="Saved", image=imgSave,relief=FLAT,
           compound=BOTTOM, font=("Arial", 10, "bold"), state="disabled").grid(row=1, column=4, ipadx=20, ipady=5)
    Button(Gallery, text="Shared", image=imgshare,relief=FLAT,
           compound=BOTTOM, font=("Arial", 10, "bold"),state="disabled").grid(row=1, column=5, ipadx=20, ipady=5)
    Button(Gallery, text="Opened", image=imgOpen,relief=FLAT,
           compound=BOTTOM, font=("Arial", 10, "bold"), state="disabled").grid(row=1, column=6, ipadx=20, ipady=5)

    ttk.Separator(Gallery, orient=VERTICAL).grid(row=0, column=7, rowspan=2, ipady=45, padx=5)
    return
def homeGoogle():
    try:
        webbrowser.open("www.google.com")
    except Exception as e:
        messagebox.showerror("Data Visualisation", "Enable to open Google error: {}". format(e))
    return
# MORE SETTINGS AND IT'S FUNCTIONALITY
def moreTab(More):
    Label(More, text="Default Locations", font =("Arial", 11,"bold")).grid(row=0, column=0, columnspan=2, sticky=W)

    Button(More, state="disabled",text="Save \nLocation", image=imgSaveLocation,relief=FLAT, compound=BOTTOM, font=("Arial", 10, "bold")).grid(row=1, column=0)
    Button(More, state="disabled", text="Open \nLocation", image=imgOpenLocation,relief=FLAT, compound=BOTTOM, font=("Arial", 10, "bold")).grid(row=1, column=1)
    ttk.Separator(More, orient=VERTICAL).grid(row=0, column=2, rowspan=2, ipady=45, padx=5)
    Label(More, text="File Properties", font =("Arial", 11,"bold")).grid(row=0, column=3, sticky=W)
    Button(More,state="disabled", text="File Properties", image=imgfileProp,relief=FLAT, compound=BOTTOM, font=("Arial", 10, "bold")).grid(row=1, column=3)
    ttk.Separator(More, orient=VERTICAL).grid(row=0, column=4, rowspan=2, ipady=45, padx=5)
    Label(More, text="Macros", font =("Arial", 11,"bold")).grid(row=0, column=5, sticky=W)
    btnMacros=Button(More, text="Macros", image=imgMacros,state=DISABLED,relief=FLAT, compound=BOTTOM, font=("Arial", 10, "bold"))
    btnMacros.grid(row=1, column=5, ipady=3, ipadx=2)
    ttk.Separator(More, orient=VERTICAL).grid(row=0, column=6, rowspan=2, ipady=45, padx=5)

    macro_popup = Menu(More, tearoff=0)
    macro_popup.add_checkbutton(label=" Play Last Macros", image=imagPlayMacro, underline=0, compound=LEFT)
    macro_popup.add_checkbutton(label=" Start Recording Macros", image=imagRecordMacro, underline=4,compound=LEFT)
    macro_popup.add_command(label=" Edit Macros", image=imagEditMacro, compound=LEFT,underline=-10 )
    macro_popup.add_checkbutton(label=" Play Recorded Macros", image=imagPlayMacro, underline=1,compound=LEFT)
    macro_popup.add_separator()
    macro_popup.add_command(label="Close", image=imgExit, compound=LEFT,underline=1 )
    def macro_popUP(evenkey):
        macro_popup.tk_popup(x=evenkey.x_root, y=evenkey.y_root)
        macro_popup.grab_release()
        return
    btnMacros.bind('<Button-3>', macro_popUP)
    btnMacros.bind('<Button-1>', macro_popUP)
    frame_left = Frame(More)
    Label(frame_left, text="Account Setting and Updates", font =("Arial", 11,"bold")).grid(row=0, column=0, sticky=W, columnspan=2)
    Button(frame_left, text="Account",underline=0, image=imageProfiles,relief=FLAT, compound=BOTTOM, font=("Arial", 10, "bold"), state="disabled").grid(row=1, column=0, ipady=3, ipadx=2)
    Button(frame_left, text="Updates",underline=0, image=imgUpdates,relief=FLAT, compound=BOTTOM, font=("Arial", 10, "bold"), state="disabled").grid(row=1, column=1, ipady=3, ipadx=2)
    frame_left.grid(row=0, column=7, rowspan=2)
    ttk.Separator(More, orient=VERTICAL).grid(row=0, column=10, rowspan=2, ipady=45, padx=5)
    return
## HOME TAB AND IT'S FUNCTIONALITIES
def homeTab(Home):
    hello_msg = ''
    username="Crispen Gari"
    time = datetime.datetime.now().hour
    if time >= 0 and time <= 11:
        hello_msg = "Hello, Good Morning!"
    elif time >= 12 and time <= 17:
        hello_msg = "Hello, Good Afternoon!"
    else:
        hello_msg = "Hello, Good Evening!"
    Label(HomeMenu, text=f"{hello_msg}", font=fonts[0]).grid(row=0, column=5)
    Label(HomeMenu, text=f"{username}", font=("arial", 10, "bold")).grid(row=1, column=5)
    Button(HomeMenu, text= "Paste", image=imgPaste, compound=BOTTOM,activebackground='light blue',
           relief=FLAT, font=("Arial", 10,"bold"),state="disabled").grid(row=0, column=0, rowspan=3, ipady=23, ipadx=12)
    Button(HomeMenu, text= "CUT", image=imgCut, compound=BOTTOM,activebackground='light blue',
           relief=FLAT, font=("Arial", 10,"bold"),state="disabled").grid(row=1, column=1, ipadx=12)
    Button(HomeMenu, text= "Copy", image=imgCopy, compound=BOTTOM,activebackground='light blue',
           relief=FLAT, font=("Arial", 10,"bold"),state="disabled").grid(row=1, column=2, ipadx=12)
    Label(HomeMenu, text=f"{username}", font=("arial", 12, "bold")).grid(row=0, column=1, columnspan=2)
    Button(HomeMenu, text= "Save", image=imgSave, compound=BOTTOM,activebackground='light blue',
           relief=FLAT, font=("Arial", 10,"bold"),state="disabled").grid(row=0, column=3, rowspan=3,ipadx=12, ipady=27)
    ttk.Separator(HomeMenu, orient=VERTICAL, ).grid(row=0, rowspan=2 ,column=4, padx=1, ipady=50)
    ttk.Separator(HomeMenu, orient=VERTICAL, ).grid(row=0, rowspan=2 ,column=6, padx=1, ipady=50)


    frame_font = Frame(HomeMenu)
    font_family = StringVar()
    font_options = []
    font = tkinter.font.families()
    for i in font:
        font_options.append(i)
    font_family.set(font_options[10])
    font_size = IntVar()
    font_size.set(10)
    Button(frame_font, text="Bold",activebackground='light blue',underline=0,
           relief=FLAT, font=("Arial", 10,"bold"),state="disabled").grid(row=0, column=0,)
    Button(frame_font, text="Italic",activebackground='light blue',underline=0,
           relief=FLAT, font=("Arial", 10,"bold", "italic"),state="disabled").grid(row=0, column=1,)
    Button(frame_font, text="Underline",activebackground='light blue',underline=0,
           relief=FLAT, font=("Arial", 10,"bold", "underline"),state="disabled").grid(row=0, column=2,)
    Label(frame_font,text="Font Family", font=("Arial", 10,"bold")).grid(row=1, column=0)
    font_fam = ttk.OptionMenu(frame_font,font_family, *font_options)
    font_fam.grid(row=1, column=1, ipadx=20, pady=2)
    Label(frame_font,text="Font size", font=("Arial", 10,"bold")).grid(row=1, column=2)
    font_s = ttk.Spinbox(frame_font,from_ =8, to=25,increment=1, textvariable=font_size, width=6)
    font_fam.config(textvariable=font_family,direction="below")
    font_s.grid(row=1, column =3, pady=2)
    Button(frame_font, image=imgFontPlus,activebackground='light blue',
           relief=FLAT, font=("Arial", 10,"bold"),state="disabled").grid(row=0, column=3, ipadx=10)
    Button(frame_font, image=imgFontMinus,activebackground='light blue',
           relief=FLAT, font=("Arial", 10,"bold"),state="disabled").grid(row=0, column=4, ipadx=10)
    Button(frame_font,text="Aa",activebackground='light blue',
           relief=FLAT, font=("Arial", 15,"bold"),state="disabled",).grid(row=0, column=5, ipadx=10)
    Button(frame_font,text="Color", underline=0,compound=LEFT, image=imgFontColor,activebackground='light blue',
           relief=FLAT, font=("Arial", 10,"bold"),state="disabled",).grid(row=1, column=4, ipadx=10)
    frame_font.grid(row=0,rowspan=2, column=7, columnspan=2)
    ttk.Separator(HomeMenu, orient=VERTICAL, ).grid(row=0, rowspan=2 ,column=9, padx=1, ipady=50)
    frame_Find= Frame(HomeMenu)
    Button(frame_Find,text="    Find    ", underline=4,compound=RIGHT, image=imgSeach,activebackground='light blue',
           relief=FLAT, font=("Arial    ", 10,"bold"),command=lambda :find_Function("find"), state=DISABLED).grid(row=0, column=0)
    Button(frame_Find,text="Replace     ", underline=0,compound=RIGHT, image=imgReplace,activebackground='light blue',
           relief=FLAT, font=("Arial    ", 10,"bold"),command=lambda :find_Function("replace"), state="disabled").grid(row=1, column=0)
    Button(frame_Find,text="Select      ", underline=0,compound=RIGHT, image=imgSelect,activebackground='light blue',
           relief=FLAT, font=("Arial ", 10,"bold"),command=lambda :find_Function("lol"), state="disabled").grid(row=2, column=0)
    ttk.Separator(frame_Find, orient=VERTICAL, ).grid(row=0, rowspan=3 ,column=2, padx=1, ipady=50)
    frame_Find.grid(row=0,rowspan=2, column=10)
    return
# DATA TAB AND ITS FUNCTIONALITY
def dataTab(Data):
    Label(Data, text="Insert From File", font=fonts[6], justify=CENTER, relief=FLAT).grid(row=0, column=0)
    Button(Data, text= "EXCEL",state="disabled", image=imgExcel, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=1, column=0, ipady=4, ipadx=12)
    Button(Data, text= "TXT",state="disabled",  image=imgText, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold")).grid(row=0, column=1, rowspan=2, ipady=15)
    Button(Data, text= "CVS",state="disabled",  image=imgCVS, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold")).grid(row=0, column=2,  rowspan=2, ipady=15)
    Button(Data, text= "XML", state="disabled", image=imgXML, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold")).grid(row=0, column=3, rowspan=2, ipady=15)
    Button(Data, text= "JSON", state="disabled", image=imgJson, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold")).grid(row=0, column=4, rowspan=2, ipady=15)
    ttk.Separator(Data, orient=VERTICAL).grid(row=0, column=5, rowspan=2, ipady=40, padx=3)
    Label(Data, text="From Online Services", font=fonts[6], justify=CENTER).grid(row=0, column=6, columnspan=2)
    Button(Data, text= "Other Sources",state="disabled",  image=imgOnlineServices, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold")).grid(row=1,column=6, ipady=3)
    Button(Data, text= "Google",state="disabled",  image=imgGoogle, compound=BOTTOM,activebackground='light blue', command=homeGoogle,font=("Arial", 10,"bold"), relief=FLAT).grid(row=1, column=7, ipady=4, ipadx=3)
    ttk.Separator(Data, orient=VERTICAL).grid(row=0, column=8, rowspan=2, ipady=40, padx=3)
    return
# SHARE TAB AND IT'S FUNCTIONALITY
def shareTab(Share):
    Button(Share, text= "EMAIL",state="disabled",  image=imgEmail, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=0, ipady=15, rowspan=2,ipadx=10)
    Button(Share, text= "FAX",state="disabled",  image=imgFax, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=1, rowspan=2, ipady=15, ipadx=17)
    Button(Share, text= "BLUETOOTH",state="disabled",  image=imgBluetooth, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, rowspan=2, column=2, ipady=15)
    Button(Share, text= "ZIP FILE",state="disabled",  image=imgZip, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=3, rowspan=2, ipady=15)
    ttk.Separator(Share, orient=VERTICAL).grid(row=0, column=4, rowspan=2, ipady=40, padx=3)
    Label(Share, text="ACCESS OPTIONS", font=fonts[6], justify=CENTER, relief=FLAT).grid(row=0, column=5, columnspan=2)
    Button(Share, text= "REMOVE",state="disabled",  image=imgRaccess, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold")).grid(row=1, column=5, ipadx=10)
    Button(Share, text= "ADD",state="disabled",  image=imgAaccess, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=1, column=6, ipadx=15)
    ttk.Separator(Share, orient=VERTICAL).grid(row=0, column=7, rowspan=2, ipady=40, padx=3)
    return
# DATABASE TAB AND ITS FUNCTIONALITY
def databaseTab(Database):
    Label(DataBase, text="Local Database",state="disabled",  font=fonts[6], justify=CENTER, relief=FLAT).grid(row=0, column=0)
    Button(DataBase, text= "ADD",state="disabled",  image=imgDBA, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=1, column=0, ipady=4, ipadx=40)
    Button(DataBase, text= "DELETE", state="disabled", image=imgDBD, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=1, rowspan=2, ipady=15)
    Button(DataBase, text= "QUERY", state="disabled", image=imgDBQ, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=2,  rowspan=2, ipady=15)
    ttk.Separator(DataBase, orient=VERTICAL).grid(row=0, column=3, rowspan=2, ipady=40, padx=3)

    Label(DataBase, text="Other Database Servers", font=fonts[6], justify=CENTER, relief=FLAT).grid(row=0, column=4)
    Button(DataBase, text= "SQL SERVER",state="disabled",  image=imgSQL, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=1, column=4, ipady=4, ipadx=55)
    Button(DataBase, text= "MS ACCESS",state="disabled",  image=imgAccess, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=5, rowspan=2, ipady=13, ipadx=10)
    Button(DataBase, text= "ORACLE",state="disabled",  image=imgOracle, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=6,  rowspan=2, ipady=15, ipadx=10)
    Button(DataBase, text= "MySQL", state="disabled", image=imgMySQL, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=7, rowspan=2, ipady=15, ipadx=10)
    Button(DataBase, text= "PostgreSQL", state="disabled", image=imgPostgre, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=8,  rowspan=2, ipady=15, ipadx=10)
    Button(DataBase, text= "SQLite3", state="disabled", image=imgSQL3, compound=BOTTOM,activebackground='light blue', relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=9, ipady=14,  rowspan=2, ipadx=10)
    Button(DataBase, text= "MongoDB",state="disabled",  image=imgMongo,activebackground='light blue', compound=BOTTOM, relief=FLAT, font=("Arial", 10,"bold"),).grid(row=0, column=10, ipady=14,  rowspan=2, ipadx=10)
    return
###############################################
"""Label(root, text="Values (x)", background="white", font=fonts[6]).grid(row=4, column=1, sticky=E, padx=5, rowspan=2)
Label(root, text="Values (y)", background="white", font=fonts[6]).grid(row=6, column=1, sticky=E, padx=5, rowspan=2)
Label(root, text="Colors For Lines", background="white", font=fonts[6]).grid(row=8, column=1, sticky=E, padx=5)
enableKey = ttk.Checkbutton(root, text="Enable Key")
enableKey.grid(row=4, column=7, sticky=W, pady=5, padx=5)
coloredBars = ttk.Checkbutton(root, text="Colored Lines")
coloredBars.grid(row=4, column=8, sticky=W, pady=5, padx=5)
horizontalBars = ttk.Checkbutton(root, text="Horizontal Lines")
horizontalBars.grid(row=4, column=9, sticky=W, pady=5, padx=5)
morePlots = ttk.Checkbutton(root, text="Enable N-plots")
text1 = scrolledtext.ScrolledText(root, height=2, width=80, font=("Times New Roman", 12, "normal"))
text2 = Text(root, height=0, width=80, font=("Times New Roman", 12, "normal"))
text3 = scrolledtext.ScrolledText(root, height=0, width=80, font=("Times New Roman", 12, "normal"))

Label(root, text="Graph Title", background="white", font=('Arial', 10, "bold")).grid(row=5, column=7, sticky=W,
                                                                                     padx=5)
Label(root, text="Graph (X) Label", background="white", font=('Arial', 10, "bold")).grid(row=4, column=0, sticky=W,
                                                                                         padx=5)
Label(root, text="Graph (Y) Label", background="white", font=('Arial', 10, "bold")).grid(row=6, column=0, sticky=W,
                                                                                         padx=5)
graphTitle = Entry(root, width=35, font=('Arial', 11, "bold") )
graphTitle.grid(row=5, column=8, sticky=W, padx=5, columnspan=2, pady=5)

graphXLabel = Entry(root)
graphXLabel.grid(row=5, column=0, sticky=E, padx=5)
graphYLabel = Entry(root)
graphYLabel.grid(row=7, column=0, sticky=E, padx=5)

number_Of_plots = IntVar()
default_color = StringVar()
number_Of_plots.set(1)
Label(root, text="Number of plots", font=("Arial",10, "bold")).grid(row=8,column=8, sticky=E)
n_plots = ttk.Spinbox(root,textvariable=number_Of_plots, from_=1,to=10, increment=1, width=10)
default_Color = ttk.Checkbutton(root,text="Default Plot Color" )
default_Color.grid(row=8, column=7)
n_plots.grid(row=8, column=9)
btnPlot = Button(root, text="Plot Figure", width=15)
btnAddPlot = Button(root, text="Add Plot", width=15)
btnReset = Button(root, text="Reset", width=15)
btnPlot.grid(row=6, column=7, sticky=W, padx=5)
text1.grid(row=4, column=2, sticky=W, columnspan=5, pady=5, rowspan=2)
text2.grid(row=6, column=2, sticky=W, columnspan=5, pady=5, rowspan=2)
text3.grid(row=8, column=2, sticky=W, columnspan=5, pady=5)
btnReset.grid(row=6, column=8, sticky=W, padx=5)
morePlots.grid(row=6, column=9, sticky=W, padx=5)
btnAddPlot.grid(row=9, column=9, sticky=W, padx=5)
"""
"""# creating a frame
frame_plot = Frame(root, width=800, height =400, bg="black")
Label(frame_plot, text="Sample Plot", fg="white", bg="black", font=fonts[0]).pack()
fig = plt.figure(num=None, figsize=(7, 2.8), facecolor='white', edgecolor='k')
plots = fig.add_subplot(111)

# creating data
riding = [(17, 18, 21, 22, 19, 21, 25, 22, 25, 24),
          (3, 6, 3.5, 4, 5, 6.3, 4.5, 5, 4.5, 4)]
swimming = ((17, 18, 20, 19, 22, 21, 23, 19, 21, 24),
            (8, 9, 7, 10, 7.5, 9, 8, 7, 8.5, 9))
sailing = ((31, 28, 29, 36, 27, 32, 34, 35, 33, 39),
           (4, 6.3, 6, 3, 5, 7.5, 2, 5, 7, 4))
plots.scatter(riding[0], riding[1], marker="o", edgecolors="black", label="Ridding")
plots.scatter(swimming[0], swimming[1], marker="*", edgecolors="g", color="red", label="Swimming")
plots.scatter(sailing[0], sailing[1], marker="^", color="black", label="Snailing")
plt.legend(title="Key")
plt.ylabel("Number of Hours")
plt.xlabel("Age")
plt.title("The Scatter Plot Title")
canvas = FigureCanvasTkAgg(figure=fig, master=frame_plot)
canvas.draw()
canvas.get_tk_widget().pack(pady=5)
toolbar =NavigationToolbar2Tk(canvas=canvas, window= frame_plot)
toolbar.update()
canvas.get_tk_widget().pack(pady=5,)
frame_plot.grid(row=10, column=1, columnspan =8)
"""

def workingArea():
    Label(root, text="DATA FOR THE PLOTS", font=("Arial",10,"bold"), anchor=CENTER).grid(row=4, column=1, sticky=W)
    Label(root, text="X-Values", font=("Arial", 10, "bold"), anchor=CENTER).grid(row=5, column=0, sticky=W,padx=5)
    Label(root, text="Y-Values", font=("Arial", 10, "bold"), anchor=CENTER).grid(row=10, column=0, sticky=W,padx=5)
    Label(root, text="Colors", font=("Arial", 10, "bold"), anchor=CENTER).grid(row=15, column=0, sticky=W,padx=5)
    Label(root, text="Graph title", font=("Arial", 10, "bold"), anchor=CENTER).grid(row=20, column=0, sticky=W,padx=5)
    Label(root, text="X-Title", font=("Arial", 10, "bold"), anchor=CENTER).grid(row=23, column=0,padx=5, sticky=W)
    Label(root, text="Y-Title", font=("Arial", 10, "bold"), anchor=CENTER).grid(row=26, column=0, padx=5, sticky=W)
    workbook1_ = scrolledtext.ScrolledText(root, width=50, height = 5, font=("Arial", 10))
    workbook1_.grid(row=5, column =1, columnspan =5,sticky=W, rowspan =5 )
    workbook2_ = scrolledtext.ScrolledText(root, width=50, height=5, font=("Arial", 10))
    workbook2_.grid(row=10, column=1,columnspan =5, sticky=W, rowspan =5)
    workbook3_ = scrolledtext.ScrolledText(root, width=50, height=5, font=("Arial", 10))
    workbook3_.grid(row=15, column=1,columnspan =5, sticky=W, rowspan=5)
    workbook4_ = scrolledtext.ScrolledText(root, width=50, height=3, font=("Arial", 10))
    workbook4_.grid(row=20, column=1, columnspan =5,sticky=W,  rowspan=3)
    workbook5_ = scrolledtext.ScrolledText(root, width=50, height=2, font=("Arial", 10))
    workbook5_.grid(row=23, column=1,columnspan =5, sticky=W, rowspan=3)
    workbook6_ = scrolledtext.ScrolledText(root, width=50, height=2, font=("Arial", 10))
    workbook6_.grid(row=26, column=1,columnspan =5, sticky=W, rowspan=3)
    frame_controls = Frame(root,bg="gray" ,width=100, height=50);
    btn_Plot = Button(frame_controls, text='Plot', relief=SOLID, width=10, font=('arial', 10), )
    btn_Plot.grid(row=0, column=0, sticky=W, padx=5, pady=2)
    btn_Reset = Button(frame_controls, text='Reset', relief=SOLID, width=10, font=('arial', 10), )
    btn_Reset.grid(row=1, column=0, sticky=W,padx=5, pady=2)
    btn_Add = Button(frame_controls, text='Add Plot', relief=SOLID, width=10, font=('arial', 10), )
    btn_Add.grid(row=0, column=1, sticky=W, padx=5, pady=2)
    btn_Reset = Button(frame_controls, text='Chose Color', relief=SOLID, width=10, font=('arial', 10), )
    btn_Reset.grid(row=0, column=2, sticky=W, padx=5, pady=2)
    n_plot =IntVar()
    n_plot.set(2)
    Label(frame_controls, text="Number of plots", bg ="gray", font=("Arial",10)).grid(row=1, column=1, padx=5, pady=2)
    n_plots =Spinbox(frame_controls,textvariable=n_plot,increment=1, from_=1, to =10, width=2)
    n_plots.grid(row=1, column=2, sticky=W, padx=5, pady=2)
    enableKey = Checkbutton(frame_controls, text="Enable Key", font=("arial", 10), bg="gray")
    enableKey.grid(row=0, column=3, sticky=W, padx=5, pady=2)
    coloredBars = Checkbutton(frame_controls, text="Colored Bars", font=("arial", 10), bg="gray")
    coloredBars.grid(row=1, column=3, sticky=W, padx=5, pady=2)
    enable_n_plots = Checkbutton(frame_controls, text="N-Plots", font=("arial", 10), bg="gray")
    enable_n_plots.grid(row=1, column=4, sticky=W, padx=5, pady=2)
    horizontalBars = Checkbutton(frame_controls, text="Horizontal Bars", font=("arial", 10), bg="gray")
    horizontalBars.grid(row=0, column=4, sticky=W, padx=5, pady=2)
    Label(root, text="STYLES", font=("Arial", 10,"bold")).grid(row=4, column=6, padx=5, pady=2, sticky=W)

    frame_controls.grid(row =29, column=0, sticky=W, columnspan =7)

    styles =["STARS",'TRIAGLE 1', 'TRIAGLE 2', 'DOTS', 'X-STYLE', 'CIRCLE']
    listbox_stlyles = Listbox(root, font=("arial", 10, "bold"), height =10, justify=LEFT, relief =SOLID)
    for i in styles:
        listbox_stlyles.insert(END, i)
    listbox_stlyles.grid(row=5, column =6, rowspan=13,padx=5,ipady=20, sticky=W)
    error_msg = scrolledtext.ScrolledText(root, height=4, font=("consolas", 10), width=105, state=DISABLED)
    error_msg.grid(row=29, column=7, columnspan=2)
    frame_plotScreen =Frame(root,  bg="sea green", height=450, width=10)
    #################################################################
    #-------------------------------------------------------
    fig = plt.figure(num=None, figsize=(7.4, 4.1), facecolor='white', edgecolor='k')
    plots = fig.add_subplot(111)
    # creating data
    riding = [(17, 18, 21, 22, 19, 21, 25, 22, 25, 24),
              (3, 6, 3.5, 4, 5, 6.3, 4.5, 5, 4.5, 4)]
    swimming = ((17, 18, 20, 19, 22, 21, 23, 19, 21, 24),
                (8, 9, 7, 10, 7.5, 9, 8, 7, 8.5, 9))
    sailing = ((31, 28, 29, 36, 27, 32, 34, 35, 33, 39),
               (4, 6.3, 6, 3, 5, 7.5, 2, 5, 7, 4))
    plots.scatter(riding[0], riding[1], marker="o", edgecolors="black", label="Ridding")
    plots.scatter(swimming[0], swimming[1], marker="*", edgecolors="g", color="red", label="Swimming")
    plots.scatter(sailing[0], sailing[1], marker="^", color="black", label="Snailing")
    plt.legend(title="Key")
    plt.ylabel("Number of Hours")
    plt.xlabel("Age")
    plt.title("The Scatter Plot Title")
    canvas = FigureCanvasTkAgg(figure=fig, master=frame_plotScreen)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=5)
    toolbar = NavigationToolbar2Tk(canvas=canvas, window=frame_plotScreen)
    toolbar.update()
    canvas.get_tk_widget().pack(pady=5, )
    ##-----------------------------------------------------------------------------------------
    frame_plotScreen.grid(rowspan=22, columnspan =3, row=5, column=8, sticky=W, pady=5)
    return
homeTab(Home=HomeMenu)
formularTab(Fomular=Fomular)
dataTab(Data=Data)
galleryTab(Gallery=Gallery)
dataTab(Data=Data)
printTab(Print=Print)
shareTab(Share=Share)
moreTab(More=More)
databaseTab(Database=DataBase)
searchTab(Search=Search)
fileMenu()
workingArea()
plotsMenu()
centralTendencyMenu()
settingMenu()
viewMenu()
helpMenu()
aboutMenu()
notebookmain.grid(row=0, column=0, columnspan=10, ipadx=45, sticky=W)
notebookmain.select(HomeMenu)
root.config(menu=menubar)
root.mainloop(0)
