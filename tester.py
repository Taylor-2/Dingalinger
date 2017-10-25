from tkinter import *
import tkinter.messagebox as msg

root=Tk()

currenthp=StringVar()
currenthp.set("3")
maxhp="8"

def Addhp():
	if (int(currenthp.get()) == int(maxhp)):
		msg.showinfo('Error', "Health cannot go past max value (" + maxhp + ")")
	else:
		currenthp.set(int(currenthp.get())+1)
def Subtracthp():
	if (int(currenthp.get()) == 0):
		msg.showinfo('Error', "Health cannot go past 0")
	else:
		currenthp.set(int(currenthp.get())-1)

maxhplabel=Label(root,text="Max HP: " + maxhp)
currenthplabelvar=Label(root,textvariable=currenthp)
currenthplabel=Label(root,text="Current HP: ")
addhpbutton=Button(root,text="+",command=Addhp)
subtracthpbutton=Button(root,text="-",command=Subtracthp)

maxhplabel.pack()
currenthplabel.pack()
currenthplabelvar.pack()
addhpbutton.pack()
subtracthpbutton.pack()

mainloop()