from tkinter import *
import os
import time
from random import *
import tkinter.messagebox as msg
info=[]
###########################################################################################################################
root=Tk()

#background for tkinter
#background_image=PhotoImage(file= "background.gif")
#background_label = Label(root, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

dieroll=[]

def initial():
	global info
	#Character Info
	file=open("back\\Info.txt","r")
	info=file.readlines()
	file.close
def remove_n(value):
	return value[0:len(value)-1]
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
def HP(event=None):
	hp = int(currenthp.get())
	if(hpentery.get()[0] == "+"):
		hp += int(hpentery.get()[1:len(hpentery.get())])
	elif(hpentery.get()[0] == "-"):
		hp -= int(hpentery.get()[1:len(hpentery.get())])
	if(hp > int(maxhp)):
		msg.showinfo('Error', "Health cannot go past max value (" + maxhp + ")")
	else:
		currenthp.set(hp)
	hpentery.set("")
	if(int(currenthp.get()) < (-1*int(maxhp))):
		msg.showinfo('Uh-Oh', "You are dead! :(")
	elif(int(currenthp.get())<0):
		pass
		#This is where we will put in the stuff to make saving throws

def experiencesubmit(event=None):
	experiencevalue.set(int(experiencevalue.get()+int(experienceentery.get())))
	experienceentery.set("")
initial()

###########################################################################################################################
#Temporary Variables
cp=1
sp=1
gp=1
ep=1
pp=1

###########################################################################################################################
#Initializing variable for Tkinter
maxhp=remove_n(info[16])
numdies=IntVar()
numdies.set(1)
dietype=StringVar()
dietype.set("Pick")
rollresult=StringVar()
rollresult.set("Result")
experienceentery=StringVar()
experienceentery.set("")
experiencevalue=IntVar()
experiencevalue.set(remove_n(info[4]))
currenthp=StringVar()
currenthp.set(remove_n(info[17]))
hpentery=StringVar()
hpentery.set("")

###########################################################################################################################
#Creating Tkinter modules

#Name + Class + Race
name=Label(root,text=remove_n(info[0]) + " " + remove_n(info[1]))
raceandclass=Label(root,text="The " + remove_n(info[2]) + " " + remove_n(info[3]))

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
hpedit=Entry(root,textvariable=hpentery,width=10)
hpedit.bind("<Return>",HP)


#Experience
experiencelabel=Label(root,text="Experience:")
experiencevaluelabel=Label(root,textvariable=experiencevalue)
experiencefield=Entry(root,textvar=experienceentery,width=8)
experiencesubmitbutton=Button(root,text="Submit",command=experiencesubmit)
experiencefield.bind("<Return>", experiencesubmit)

#Money

#Inventory

#Spells

#Armor Class
armorlabel=Label(root,text="Armor\nClass")
armor=Label(root,text=str(remove_n(info[13])))


#Speed
speedlabel=Label(root,text="Speed")
speed=Label(root,text=remove_n(info[15]))

#Initiative
initiativelabel=Label(root,text="Initiative")
initiative=Label(root,text=str(remove_n([14])))

#Modifiers


#Traits


###########################################################################################################################
#Display Tkinter modules

#Name
name.grid(row=0,columnspan=4,column=0,sticky=SW)
raceandclass.grid(row=1,columnspan=4,column=0,sticky=NW)

#Dice
numberofdies.grid(row=0,column=4)
thedietype.grid(row=0,column=5,columnspan=2)
#rollbutton.grid(row=1,column=5,columnspan=2)
rollresultlabel.grid(row=1,column=4,columnspan=3)

#Health
hplabel.grid(row=0,column=7,columnspan=2)
currenthplabelvar.grid(row=0,column=9,sticky=SW)
hpedit.grid(row=1,column=7,columnspan=3)

#Experience
experiencelabel.grid(row=0,column=10,columnspan=2)
experiencefield.grid(row=1,column=10,columnspan=2)
experiencesubmitbutton.grid(row=1,column=12)
experiencevaluelabel.grid(row=0,column=12,sticky=W)

#Initiative brick
armorlabel.grid(row=2,column=0)
armor.grid(row=3,column=0)
initiativelabel.grid(row=2,column=1,columnspan=2)
initiative.grid(row=3,column=1,columnspan=2)
speedlabel.grid(row=2,column=3)
speed.grid(row=3,column=3)

#Money


mainloop()