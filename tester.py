from tkinter import *

root=Tk()

currenthp=IntVar()
currenthp.set(8)
maxhp="8"

def Addhp():
	print("Add one:")
	print("	" + str(currenthp.get()))
	#print("	" + currenthp)
	print("	" + str(int(currenthp.get())+1))
def Subtracthp():
	print("Subtract one")

maxhplabel=Label(root,text="Max HP: " + maxhp)
currenthplabel=Label(root,text="Current HP: " + str(currenthp.get()))
addhpbutton=Button(root,text="+",command=Addhp)
subtracthpbutton=Button(root,text="-",command=Subtracthp)

maxhplabel.pack()
currenthplabel.pack()
addhpbutton.pack()
subtracthpbutton.pack()

mainloop()