
"""import win32api
filename = "C:\\Users\\garid\\Documents\\app.js"
win32api.ShellExecute(0, "print", filename, None, '.', 0)

"""


from tqdm import tqdm

from time import sleep

for i in tqdm(range(10)):
    sleep(1)



'''num='1,2,3,4,5,6,7,8,9,11.2'
arr =num.split(',')

final_list =[]
for i in arr:
    final_list.append(float(i))

print(final_list)
'''
from tkinter import  *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from tkinter.ttk import  *
'''root = Tk()
root.wm_title("Embedding in Tk")
sep = Separator(root, orient=VERTICAL)
sep.pack(ipady=100)
btn = Button(root,text ="gggggggggggggggggggggg", command =print(9))
for i in btn.keys():
    print(i)
btn.pack()
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
root.mainloop()'''

"""
root = Tk()
root.geometry("500x200+200+200")
root.title("Tooltip")
btn1 = Button(root, text="Exit", command=root.destroy())
btn1.pack()

tip = ListboxToolTip(btn1, ["Hello", 'world'])

root.mainloop()"""


"""Given a string of the following nature:

names="'Crispen', 'Gari', 'Liya', 'Strawberry','Data','Visualisation','Statistics'"

this function must be in a class, write a function that convert the string 
name to array of string ! of characters when the function is called using an object 
then array name will have the following elements in it.


arra_name = 'Crispen', 'Gari', 'Liya', 'Strawberry','Data','Visualisation','Statistics'
"""

names = "Crispen, Gari, Liya, Strawberry,Data,Visualisation,Statistics"
from array import *
'''
STUCK: python doesn't work effectively with array string
       therefore we have to use python list or python turples 
       instead
       The following is an example of arrays of integers which 
        num_list =[2, 3,9,10,-5,17,100,678]
'''
"""num_list = [2, 3, 9, 10, -5, 17, 100, 678]
def myArray(num):
     my_arr = array('i', num);
     for i in my_arr:
         print(i,end=" ")
myArray(num=num_list)
print()
class Name_Class:
    # a constructor
    def __init__(self):
        return
    # a function that converts the string to list
    def calllback(self, names):
        self.names = names
        arr = list(self.names.split(','))
        for i in arr:
            print(i.upper(), end=', ')
ob1 = Name_Class()
ob1.calllback(names=names)"""

"""from pip._internal import main as install

try:
    from win10toast import ToastNotifier
except ImportError as e:
    install(["install","win10toast"])
from win10toast import  ToastNotifier
notif_ = ToastNotifier()
notif_.show_toast("Strawberry Notification","Strawberry Released New Documentation", duration=20,icon_path="strawberry.ico")
###############################################################
import psutil
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from  pip._internal import  main
main(["install", "psutil"])
battery = psutil.sensors_battery();
print(battery)
# checking if the charger is plugged
if battery.power_plugged:
    print("Charging: ", battery.percent)
else:
    print("Not Charging", battery.percent ,"%");
    print( "Discharge time ", int(battery.secsleft)," sec_lft")
################################################################
import psutil
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
fan = psutil.disk_usage(path="C:/")
print("Available: ", fan.total/1000000000)
print("Used: ", fan.used/1000000000)
print("Free: ", fan.free/1000000000)
print("Percentage Used: ", fan.percent, "%")

"""

"""
import psutil
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

sessions = AudioUtilities.GetAllSessions()

for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
    if session.Process and session.Process.name() == "vlc.exe":
        print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
        volume.SetMasterVolume(0.6, None)
"""





