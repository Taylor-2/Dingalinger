from tkinter import *
import os
import time
from random import *
import tkinter.messagebox as msg

root=Tk()
#background for tkinter
background_image=PhotoImage(file= "C:\\Users\\Mark\\Documents\\GitHub\\Dingalinger\\background.gif")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
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
	if (int(currenthp.get()) == int(maxhp)):
		msg.showinfo('Error', "Health cannot go past max value (" + maxhp + ")")
	else:
		currenthp.set(int(currenthp.get())+1)
def Subtracthp():
	if (int(currenthp.get()) == 0):
		msg.showinfo('Error', "Health cannot go past 0")
	else:
		currenthp.set(int(currenthp.get())-1)
def experiencesubmit(event=None):
	experiencevalue.set(int(experiencevalue.get()+int(experienceentery.get())))
	experienceentery.set("")

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
experienceentery=StringVar()
experienceentery.set("")
experiencevalue=IntVar()
experiencevalue.set(45678)
currenthp=StringVar()
currenthp.set("3")

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
hplabel=Label(root,text="Max HP: %s \nCurrent HP: " % maxhp)
currenthplabelvar=Label(root,textvariable=currenthp)
#currenthplabel=Label(root,text="Current HP: ")
addhpbutton=Button(root,text="+",command=Addhp)
subtracthpbutton=Button(root,text="-",command=Subtracthp)

#Experience
experiencelabel=Label(root,text="Experience:")
experiencevaluelabel=Label(root,textvariable=experiencevalue)
experiencefield=Entry(root,textvar=experienceentery,width=8)
experiencesubmitbutton=Button(root,text="Submit",command=experiencesubmit)
experiencefield.bind("<Return>", experiencesubmit)

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
name.grid(row=0,columnspan=4,column=0,sticky=SW)
info.grid(row=1,columnspan=4,column=0,sticky=NW)

numberofdies.grid(row=0,column=4)
thedietype.grid(row=0,column=5,columnspan=2)
rollbutton.grid(row=1,column=5,columnspan=2)
rollresultlabel.grid(row=1,column=4)

hplabel.grid(row=0,column=7,columnspan=2)
currenthplabelvar.grid(row=0,column=9,sticky=SW)
addhpbutton.grid(row=1,column=7,sticky=EW)
subtracthpbutton.grid(row=1,column=8,columnspan=2,sticky=EW)

experiencelabel.grid(row=0,column=10)
experiencefield.grid(row=1,column=10)
experiencesubmitbutton.grid(row=1,column=11)
experiencevaluelabel.grid(row=0,column=11,sticky=W)



mainloop()