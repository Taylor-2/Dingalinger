from tkinter import *
import os
import time
from random import *
import tkinter.messagebox as msg
###########################################################################################################################
#"Global" variables
info=[]
moneylist=[]
###########################################################################################################################
#Setting up the window
root=Tk()

#Window parameters
root.title("Shaman DND V.3")
#root.geometry("350x200")

#Background
#background_image=PhotoImage(file= "back\\background.gif")
#background_label = Label(root, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

###########################################################################################################################
#Creating the functions
#Startup
def initial():
	#Character Info
	global info
	file=open("back\\Info.txt","r")
	info=file.readlines()
	file.close()

	#Money
	global moneylist
	file=open("back\\Wallet.txt","r")
	moneylist=file.readlines()
	file.close()
def remove_n(value):
	return value[0:len(value)-1]
#Update
def writeinfo():
	info[17] = str(currenthp.get()) + "\n"
	info[4]=str(experiencevalue.get())+"\n"
	file=open("back\\Info.txt","w")
	ctr=0
	while(ctr<len(info)):
		file.write(info[ctr])
		ctr+=1
	file.close()
#Money
def writemoney():
	file=open("back\\Wallet.txt","w")
	file.write(str(cp.get())+"\n"+str(sp.get())+"\n"+str(ep.get())+"\n"+str(gp.get())+"\n"+str(pp.get())+"\n")
	file.close()
def inputmoney(event=None):
	if(entery.get()[0] != "-") and (entery.get()[0] != "+"):
		msg.showinfo('Error', "First value in entry field must be an operator (+/-)")
	else:
		if (moneytype.get() == "Copper"):
			if (entery.get()[0] == "+"):
				cp.set(cp.get()+int(entery.get()[1:len(entery.get())]))
			if (entery.get()[0] == "-"):
				cp.set(cp.get()-int(entery.get()[1:len(entery.get())]))
		elif(moneytype.get() == "Silver"):
			if (entery.get()[0] == "+"):
				sp.set(sp.get()+int(entery.get()[1:len(entery.get())]))
			if (entery.get()[0] == "-"):
				sp.set(sp.get()-int(entery.get()[1:len(entery.get())]))
		elif(moneytype.get() == "Gold"):
			if (entery.get()[0] == "+"):
				gp.set(gp.get()+int(entery.get()[1:len(entery.get())]))
			if (entery.get()[0] == "-"):
				gp.set(gp.get()-int(entery.get()[1:len(entery.get())]))
		elif(moneytype.get() == "Electrum"):
			if (entery.get()[0] == "+"):
				ep.set(ep.get()+int(entery.get()[1:len(entery.get())]))
			if (entery.get()[0] == "-"):
				ep.set(ep.get()-int(entery.get()[1:len(entery.get())]))
		elif(moneytype.get() == "Platinum"):
			if (entery.get()[0] == "+"):
				pp.set(pp.get()+int(entery.get()[1:len(entery.get())]))
			if (entery.get()[0] == "-"):
				pp.set(pp.get()-int(entery.get()[1:len(entery.get())]))
		entery.set("")
		writemoney()
def highestvalue(event=None):
	while(cp.get()>=10):
		cp.set(int(cp.get()-10))
		sp.set(int(sp.get()+1))
	while(sp.get()>=5):
		sp.set(int(sp.get()-5))
		ep.set(int(ep.get()+1))
	while(ep.get()>=2):
		ep.set(int(ep.get()-2))
		gp.set(int(gp.get()+1))
	while(gp.get()>=10):
		gp.set(int(gp.get()-10))
		pp.set(int(pp.get()+1))
	writemoney()
#Roll
def roll(event=None):
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
#Health
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
	writeinfo()
#Experience
def experiencesubmit(event=None):
	experiencevalue.set(int(experiencevalue.get()+int(experienceentery.get())))
	experienceentery.set("")
	writeinfo()
#Inventory
def writenewitem(event=None):
	file=open("Back/Inventory.txt","a")
	file.write(str(inventoryentery.get()) + "\n")
	file.close()
	updateinventory()
def updateinventory():
	global items
	file=open("Back/Inventory.txt","r")
	raw=file.readlines()
	file.close()
	items=[]
	ctr=0
	while(ctr<len(raw)):
		items.append(remove_n(raw[ctr]))
		ctr+=1
	ctr=0
	while(ctr<len(items)):
		inventorybox.delete(0, END)
		ctr+=1
	ctr=0
	while(ctr<len(items)):
		inventorybox.insert(END,items[ctr])
		ctr+=1
	inventoryentery.set("")
def deleteitem(event=None):
	global items
	todelete=items[int(str(inventorybox.curselection())[1:len(str(inventorybox.curselection()))-2])]
	ctr=0
	old=items
	items=[]
	while(ctr<len(old)):
		temp=old[ctr]
		if (temp!=str(todelete)):
			items.append(temp)
		ctr+=1
	ctr=0
	file=open("Back/Inventory.txt","w")
	while(ctr<len(items)):
		file.write(str(items[ctr])+"\n")
		ctr+=1
	file.close()
	updateinventory()
#Spells
initial()

###########################################################################################################################
#Temporary Variables


###########################################################################################################################
#Initializing variable for Tkinter
#Dice
numdies=IntVar()
numdies.set(1)
dietype=StringVar()
dietype.set("Pick")
rollresult=StringVar()
rollresult.set("Result")
#Experience
experienceentery=StringVar()
experienceentery.set("")
experiencevalue=IntVar()
experiencevalue.set(remove_n(info[4]))
#HP
maxhp=remove_n(info[16])
currenthp=StringVar()
currenthp.set(remove_n(info[17]))
hpentery=StringVar()
hpentery.set("")
#Money
cp=IntVar()
cp.set(remove_n(moneylist[0]))
sp=IntVar()
sp.set(remove_n(moneylist[1]))
ep=IntVar()
ep.set(remove_n(moneylist[2]))
gp=IntVar()
gp.set(remove_n(moneylist[3]))
pp=IntVar()
pp.set(remove_n(moneylist[4]))
entery=StringVar()
entery.set("")
moneytype=StringVar()
moneytype.set("Gold")
#Traits
strength=IntVar()
strength.set(remove_n(info[5]))
dexterity=IntVar()
dexterity.set(remove_n(info[6]))
constitution=IntVar()
constitution.set(remove_n(info[7]))
intelligence=IntVar()
intelligence.set(remove_n(info[8]))
wisdom=IntVar()
wisdom.set(remove_n(info[9]))
charisma=IntVar()
charisma.set(remove_n(info[10]))
proficiency=IntVar()
proficiency.set(remove_n(info[11]))
passivewisdom=IntVar()
passivewisdom.set(remove_n(info[12]))
#Inventory
inventoryentery=StringVar()
inventoryentery.set("")


###########################################################################################################################
#Creating Tkinter modules
#Name + Class + Race
name=Label(root,text=remove_n(info[0]) + " " + remove_n(info[1]))
raceandclass=Label(root,text="The " + remove_n(info[2]) + " " + remove_n(info[3]))

#Die Roller
numberofdies=Entry(root,textvar=numdies,width=3)
thedietype=OptionMenu(root, dietype, "D4", "D6", "D8", "D12", "D10", "D20","D100")
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
experiencefield=Entry(root,textvariable=experienceentery,width=8)
experiencesubmitbutton=Button(root,text="Submit",command=experiencesubmit)
experiencefield.bind("<Return>", experiencesubmit)

#Money
amount=Entry(root,textvariable=entery,width=10)
amount.bind("<Return>",inputmoney)
amount.bind("<Shift Return>",highestvalue)
typedrop=OptionMenu(root, moneytype, "Copper", "Silver", "Electrum", "Gold", "Platinum")
cpvaluelabel=Label(root,textvariable=str(cp))
cplabel=Label(root,text="Copper:")
spvaluelabel=Label(root,textvariable=str(sp))
splabel=Label(root,text="Silver:")
epvaluelabel=Label(root,textvariable=str(ep))
eplabel=Label(root,text="Electrum:")
gpvaluelabel=Label(root,textvariable=str(gp))
gplabel=Label(root,text="Gold:")
ppvaluelabel=Label(root,textvariable=str(pp))
pplabel=Label(root,text="Platinum:")

#Inventory
inventorybox = Listbox(root,width=25,height=8)
inventorybox.bind("<Delete>",deleteitem)
invscroll = Scrollbar(root)
invscroll.config(command=inventorybox.yview)
inventorybox.config(yscrollcommand=invscroll.set)
inventery=Entry(root,textvariable=inventoryentery)
inventery.bind("<Return>",writenewitem)

#Spells
spellplaceholder=Entry(root)

#Armor Class
armorlabel=Label(root,text="Armor")
armor=Label(root,text=str(remove_n(info[13])))

#Speed
speedlabel=Label(root,text="Speed")
speed=Label(root,text=remove_n(info[15]))

#Initiative
initiativelabel=Label(root,text="Initiative")
initiative=Label(root,text=str(remove_n(info[14])))

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
typedrop.grid(row=2,column=12)
amount.grid(row=2,column=10,columnspan=2)
cpvaluelabel.grid(row=3,column=12,sticky=W)
cplabel.grid(row=3,column=10,columnspan=2,sticky=E)
spvaluelabel.grid(row=4,column=12,sticky=W)
splabel.grid(row=4,column=10,columnspan=2,sticky=E)
epvaluelabel.grid(row=5,column=12,sticky=W)
eplabel.grid(row=5,column=10,columnspan=2,sticky=E)
gpvaluelabel.grid(row=6,column=12,sticky=W)
gplabel.grid(row=6,column=10,columnspan=2,sticky=E)
ppvaluelabel.grid(row=7,column=12,sticky=W)
pplabel.grid(row=7,column=10,columnspan=2,sticky=E)

#Inventory
#inventoryplaceholder.grid(row=2,column=4,columnspan=3)
invscroll.grid(column=6,rowspan=10,row=3)#side=RIGHT, fill=Y)
inventorybox.grid(column=4,columnspan=2,row=2,rowspan=10)
inventery.grid(column=4,columnspan=3,row=7)

#Spells
spellplaceholder.grid(row=2,column=7,columnspan=3)

updateinventory()
mainloop()