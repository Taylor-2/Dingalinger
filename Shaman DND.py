from tkinter import *
import os
import time
from random import *
import tkinter.messagebox as msg

root=Tk()
#Initialization variables
dieroll=[]

def roll(event=None):
	global dieroll
	ctr=0
	dieroll=""
	total=0
	if (dietype.get() == "Pick"):
		msg.showinfo('Error', "Please select a die type.")
	while(ctr<numdies.get()):
		roll = randint(1,int(dietype.get()[1:len(dietype.get())]))
		dieroll += str(roll)
		total += roll
		if(ctr != numdies.get()-1):
			dieroll += ", "
		ctr += 1
	if (numdies.get() != 1):
		dieroll += "\nTotal: " + str(total)
	rollresult.set(dieroll)
def reset_roll(event=None):
	dietype.set("Pick")
	numdies.set(1)
	rollresult.set("Result")
def Addhp():
	currenthp=currenthp.get()
	currenthp=int(currenthp)
	currenthp += 1
	currenthp=str(currenthp)
	currenthp.set(currenthp)
def Subtracthp():
	currenthp.set(str(int(currenthp.get() -1)))

#######################################################################
#Temporary Variables
firstname="Beppo"
lastname="McLastname"
race="Gnome"
classvar="Wizard"
maxhp="8"
currenthp=4
temp=45678
########################################################################

#Initializing variable for Tkinter
numdies=IntVar()
numdies.set(1)
dietype=StringVar()
dietype.set("Pick")
rollresult=StringVar()
rollresult.set("Result")
experiencepoints=IntVar()
experiencepoints.set(temp)
currenthp=StringVar()
currenthp.set("8")

#########################################################################
#Creating Tkinter modules
#Name + Class + Race
name=Label(root,text=firstname + " " + lastname)
info=Label(root,text="The " + classvar + " " + race)

#Die Roller
numberofdies=Entry(root,textvar=numdies,width=3)
thedietype=OptionMenu(root, dietype, "D4", "D6", "D8", "D12", "D10", "D20")
rollbutton=Button(root,text="Roll", command=roll)
rollresultlabel=Label(root,textvar=rollresult)
numberofdies.bind("<Return>", roll)
numberofdies.bind("<Delete>", reset_roll)

#Health
maxhplabel=Label(root,text="Max HP: " + maxhp)
currenthplabel=Label(root,text="Current HP: " + str(currenthp.get()))
addhpbutton=Button(root,text="+",command=Addhp)
subtracthpbutton=Button(root,text="-",command=Subtracthp)

#Experience
experiencelabel=Label(root,text="Experience:")
experiencefield=Entry(root,textvar=experiencepoints,width=8)
levelupbutton=Button(root,text="Level Up")

#Inventory
'''scrollbar = Scrollbar(root)
scrollbar.grid(column=8,rowspan=2,row=0)

ctr =0
while(ctr < 50):
	inventory.append(ctr)
	ctr += 1

inventory = Listbox(root)
inventory.grid(column=7,rowspan=2,row=0)

inventory.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=inventory.yview)'''

###################################################################################################
#Display Tkinter modules
'''name.grid(row=0,columnspan=2,column=0,sticky=W,padx=20)
info.grid(row=1,columnspan=2,column=0,sticky=W,padx=20)

numberofdies.grid(row=0,column=2)
thedietype.grid(row=0,column=3)
rollbutton.grid(row=1,column=3)
rollresultlabel.grid(row=1,column=2)

maxhplabel.grid(row=0,column=4)
currenthplabel.grid(row=1,column=4)

experiencelabel.grid(row=0,columnspan=2,column=5)
experiencefield.grid(row=1,columnspan=2,column=6)
#levelupbutton.pack()'''

maxhplabel.pack()
currenthplabel.pack()
addhpbutton.pack()
subtracthpbutton.pack()


mainloop()