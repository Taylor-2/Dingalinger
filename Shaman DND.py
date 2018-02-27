from tkinter import *
import os
import time
from random import *
import tkinter.messagebox as msg
import tkinter as tk
###########################################################################################################################
#"Global" variables
info=[]
moneylist=[]
notes=""
raw1=[]
boxheight=15
###########################################################################################################################
#																												Window Setup
root=Tk()
root.title("Shaman DND V.3")
#root.geometry("350x200")
###########################################################################################################################
#																													Startup
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

	#Notes

	#Skills
	global allproficencies
	file=open("back\\Skills.txt","r")
	allproficencies=""
	for x in file.readlines():
		allproficencies += str(x)
	file.close()

initial()
def remove_n(value):
	return value[0:len(value)-1]
def writeinfo():
	info[17] = str(currenthp.get()) + "\n"
	info[4]=str(experiencevalue.get())+"\n"
	file=open("back\\Info.txt","w")
	ctr=0
	while(ctr<len(info)):
		file.write(info[ctr])
		ctr+=1
	file.close()
###########################################################################################################################
#Frame 																												Name
nameframe = Frame(root, bd=2, relief=GROOVE)
	#Widgets
name=Label(nameframe,text=remove_n(info[0]) + " " + remove_n(info[1]))
raceandclass=Label(nameframe,text="The " + remove_n(info[2]) + " " + remove_n(info[3]))
	#Setup
name.grid(row=0,column=0)
raceandclass.grid(row=1,column=0)
###########################################################################################################################
#Frame 																												Dice
diceframe = Frame(root, bd=2, relief=GROOVE)
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
	#Var
numdies=IntVar()
numdies.set(1)
dietype=StringVar()
dietype.set("Pick")
rollresult=StringVar()
rollresult.set("Result")
	#Widgets
numberofdies=Entry(diceframe,textvar=numdies,width=3)
thedietype=OptionMenu(diceframe, dietype, "D4", "D6", "D8", "D12", "D10", "D20","D100")
rollbutton=Button(diceframe,text="Roll", command=roll)
rollresultlabel=Label(diceframe,textvar=rollresult)
numberofdies.bind("<Return>", roll)
numberofdies.bind("<Delete>", reset_roll)
	#Setup
numberofdies.grid(row=0,column=0)
thedietype.grid(row=0,column=1)
rollresultlabel.grid(row=1,column=0,columnspan=2)
###########################################################################################################################
#Frame 																												Health
healthframe = Frame(root, bd=2, relief=GROOVE)
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
	#Var
maxhp=remove_n(info[16])
currenthp=StringVar()
currenthp.set(remove_n(info[17]))
hpentery=StringVar()
hpentery.set("")
	#Widgets
hplabel=Label(healthframe,text="Max HP: %s \nCurrent HP: " % maxhp)
currenthplabelvar=Label(healthframe,textvariable=currenthp)
hpedit=Entry(healthframe,textvariable=hpentery,width=10)
hpedit.bind("<Return>",HP)
	#Setup
hplabel.grid(row=0,column=0)
currenthplabelvar.grid(row=0,column=1,sticky=SW)
hpedit.grid(row=1,column=0,columnspan=2)
###########################################################################################################################
#Frame 																											Experience
expframe = Frame(root, bd=2, relief=GROOVE)
def experiencesubmit(event=None):
	experiencevalue.set(int(experiencevalue.get()+int(experienceentery.get())))
	experienceentery.set("")
	writeinfo()
#Var
experienceentery=StringVar()
experienceentery.set("")
experiencevalue=IntVar()
experiencevalue.set(remove_n(info[4]))
	#Widgets
experiencelabel=Label(expframe,text="Experience:")
experiencevaluelabel=Label(expframe,textvariable=experiencevalue)
experiencefield=Entry(expframe,textvariable=experienceentery,width=8)
experiencesubmitbutton=Button(expframe,text="Submit",command=experiencesubmit)
experiencefield.bind("<Return>", experiencesubmit)
	#Setup
experiencelabel.grid(row=0,column=0,columnspan=2)
experiencefield.grid(row=1,column=0,columnspan=2)
experiencesubmitbutton.grid(row=1,column=2)
experiencevaluelabel.grid(row=0,column=2,sticky=W)
###########################################################################################################################
#Frames																											Inventory
inventoryframe = Frame(root, bd=2, relief=GROOVE)
def writenewitem(event=None):
	file=open("Back/Inventory.txt","a")
	file.write(str(inventry.get()) + "\n")
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
	inventry.set("")
def deleteitem(event=None):
	global items
	todelete=items[int(str(inventorybox.curselection())[1:len(str(inventorybox.curselection()))-2])]
	ctr=0
	old=items
	items=[]
	found=False
	while(ctr<len(old)):
		temp=old[ctr]
		if (temp==str(todelete)) and (found == False):
			found=True
		else:
			items.append(temp)
		ctr+=1
	ctr=0
	file=open("Back/Inventory.txt","w")
	while(ctr<len(items)):
		file.write(str(items[ctr])+"\n")
		ctr+=1
	file.close()
	updateinventory()
def edit(event=None):
	selected=items[int(str(inventorybox.curselection())[1:len(str(inventorybox.curselection()))-2])]
	inventry.set(selected)
#Var
inventry=StringVar()
inventry.set("")
#Widgets
inventorybox = Listbox(inventoryframe,width=20,height=boxheight)
inventorybox.bind("<Delete>",deleteitem)
invscroll = Scrollbar(inventoryframe)
invscroll.config(command=inventorybox.yview)
inventorybox.config(yscrollcommand=invscroll.set)
inventoryentry=Entry(inventoryframe,textvariable=inventry,width=20)
inventoryentry.bind("<Return>",writenewitem)
inventorybox.bind("<Double-Button-1>",edit)
inventoryentry.bind("<Escape>",inventry.set(""))
#Setup
invscroll.pack(side=RIGHT, fill=Y)
inventorybox.pack()
inventoryentry.pack()
###########################################################################################################################
#Frames																												Spells
spellframe = Frame(root, bd=2, relief=GROOVE)
def windowspell(event=None):
	file=open("Back\\Spellbook\\"+str(sortedlist[int(str(spellbox.curselection())[1:(len(str(spellbox.curselection()))-2)])])+".txt","r")
	rawspellinfo=file.readlines()
	file.close()
	ctr=0
	spellinfo=[]
	while(ctr<len(rawspellinfo)):
		spellinfo.append(remove_n(rawspellinfo[ctr]))
		ctr += 1
	if(spellinfo[1] == "0"):
		spellinfo[1] = "Cantrip"

	top=tk.Toplevel(root)
	top.title(spellinfo[0])

	namelabeltop=Label(top,text="Name:")
	levellabeltop=Label(top,text="Level:")
	timelabeltop=Label(top,text="Time:")
	rangelabeltop=Label(top,text="Range:")
	componentslabeltop=Label(top,text="Components:")
	durationlabeltop=Label(top,text="Duration:")
	descriptionlabeltop=Label(top,text="Description:")

	nametop=Label(top,text=spellinfo[0])
	leveltop=Label(top,text=spellinfo[1])
	timetop=Label(top,text=spellinfo[2])
	rangetop=Label(top,text=spellinfo[3])
	componentstop=Label(top,text=spellinfo[4])
	durationtop=Label(top,text=spellinfo[5])
	descriptiontop=Label(top,text=formatdescription(spellinfo[6]))

	namelabeltop.grid(column=0,row=1,sticky=W)
	levellabeltop.grid(column=0,row=2,sticky=W)
	timelabeltop.grid(column=0,row=3,sticky=W)
	rangelabeltop.grid(column=0,row=4,sticky=W)
	componentslabeltop.grid(column=0,row=5,sticky=W) 
	durationlabeltop.grid(column=0,row=6,sticky=W)
	descriptionlabeltop.grid(column=0,row=7,sticky=W)

	nametop.grid(column=1,row=1,sticky=W)
	leveltop.grid(column=1,row=2,sticky=W)
	timetop.grid(column=1,row=3,sticky=W)
	rangetop.grid(column=1,row=4,sticky=W)
	componentstop.grid(column=1,row=5,sticky=W) 
	durationtop.grid(column=1,row=6,sticky=W)
	descriptiontop.grid(column=1,row=7,sticky=W)
def formatdescription(rawdata):
	deslist=[]
	finaldes=""
	deslist=rawdata.split()
	leng = 0
	for x in deslist:
		leng += len(x)
		if (leng>60):
			finaldes += "\n"
			leng = 0
		else:
			finaldes += (x + " ")
	return (finaldes)

def newspell(event=None):
	top=tk.Toplevel(root)
	top.title("New Spell")

	def writenew(event=None):
		#Check if file exists
		file=open("Back\\Spellbook\\"+newname.get()+".txt","w")
		file.write(newname.get()+"\n")
		file.write(newlevel.get()+"\n")
		file.write(newtime.get()+"\n")
		file.write(newrange.get()+"\n")
		file.write(newcomponents.get()+"\n")
		file.write(newduration.get()+"\n")
		file.write(newdescription.get()+"\n")
		file.close()
		updatespells()
		top.destroy()

	newname=StringVar()
	newname.set("")
	newlevel=StringVar()
	newlevel.set("")
	newtime=StringVar()
	newtime.set("")
	newrange=StringVar()
	newrange.set("")
	newcomponents=StringVar()
	newcomponents.set("")
	newduration=StringVar()
	newduration.set("")
	newdescription=StringVar()
	newdescription.set("")

	namelabeltop=Label(top,text="Name:")
	levellabeltop=Label(top,text="Level:")
	timelabeltop=Label(top,text="Time:")
	rangelabeltop=Label(top,text="Range:")
	componentslabeltop=Label(top,text="Components:")
	durationlabeltop=Label(top,text="Duration:")
	descriptionlabeltop=Label(top,text="Description:")

	nameenttop=Entry(top,textvariable=newname)
	levelenttop=Entry(top,textvariable=newlevel)
	timeenttop=Entry(top,textvariable=newtime)
	rangeenttop=Entry(top,textvariable=newrange)
	componentsenttop=Entry(top,textvariable=newcomponents)
	durationenttop=Entry(top,textvariable=newduration)
	descriptionenttop=Entry(top,textvariable=newdescription)

	descriptionenttop.bind("<Return>",writenew)

	donebutton=Button(top,text="Submit",command=writenew)

	namelabeltop.grid(column=0,row=1,sticky=W)
	levellabeltop.grid(column=0,row=2,sticky=W)
	timelabeltop.grid(column=0,row=3,sticky=W)
	rangelabeltop.grid(column=0,row=4,sticky=W)
	componentslabeltop.grid(column=0,row=5,sticky=W) 
	durationlabeltop.grid(column=0,row=6,sticky=W)
	descriptionlabeltop.grid(column=0,row=7,sticky=W)

	nameenttop.grid(column=1,row=1,sticky=W)
	levelenttop.grid(column=1,row=2,sticky=W)
	timeenttop.grid(column=1,row=3,sticky=W)
	rangeenttop.grid(column=1,row=4,sticky=W)
	componentsenttop.grid(column=1,row=5,sticky=W) 
	durationenttop.grid(column=1,row=6,sticky=W)
	descriptionenttop.grid(column=1,row=7,sticky=W)

	donebutton.grid(columnspan=2,column=0,row=8)
def updatespells():
	global spelllist
	global sortedlist
	raw=sorted(os.listdir("Back\\Spellbook"))
	spelllist=[]

	#Get and format spellbook into a list
	ctr=0
	while(ctr<len(raw)):
		temp=raw[ctr]
		spelllist.append(temp[0:len(temp)-4])
		ctr += 1

	#Find Max spell level
	ctr=0
	maxlevel=0
	while(ctr<len(spelllist)):
		level=int(remove_n(open("back\\Spellbook\\" + spelllist[ctr] +".txt","r").readlines()[1]))
		if (level > maxlevel):
			maxlevel=level
		ctr +=1
	ctr=0
	sortedlist=[]
	#Sorts the list of spells into levels
	while(ctr<=maxlevel):
		if (ctr == 0):
			sortedlist.append("Cantrips:")
		else:
			sortedlist.append("\n")
			sortedlist.append("Level " + str(ctr)+ " Spells:")
		ctr2=0
		while(ctr2<len(spelllist)):
			temp=spelllist[ctr2]
			file=open("back\\Spellbook\\" + temp +".txt","r")
			level=file.readlines()
			level=remove_n(level[1])
			if (int(level) == ctr):
				sortedlist.append(spelllist[ctr2])
			ctr2 +=1
		ctr+=1
	spellbox.delete(0, END)
	ctr=0
	while(ctr<len(sortedlist)):
		spellbox.insert(END,sortedlist[ctr])
		ctr+=1
#Widgets
spellbox = Listbox(spellframe,width=20,height=boxheight)
spellbox.bind("<Double-Button-1>",windowspell)
newbutton=Button(spellframe,text="New Spell",command=newspell)
spellscroll = Scrollbar(spellframe)
spellscroll.config(command=spellbox.yview)
spellbox.config(yscrollcommand=spellscroll.set)
#Setup
spellscroll.pack(side=RIGHT, fill=Y)
spellbox.pack()
newbutton.pack()
###########################################################################################################################
#Frames 																											Money
moneyframe = Frame(root, bd=2, relief=GROOVE)
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
	#Var
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
	#Widgets
amount=Entry(moneyframe,textvariable=entery,width=10)
amount.bind("<Return>",inputmoney)
amount.bind("<Shift Return>",highestvalue)
typedrop=OptionMenu(moneyframe, moneytype, "Copper", "Silver", "Electrum", "Gold", "Platinum")
cpvaluelabel=Label(moneyframe,textvariable=str(cp))
cplabel=Label(moneyframe,text="Copper:")
spvaluelabel=Label(moneyframe,textvariable=str(sp))
splabel=Label(moneyframe,text="Silver:")
epvaluelabel=Label(moneyframe,textvariable=str(ep))
eplabel=Label(moneyframe,text="Electrum:")
gpvaluelabel=Label(moneyframe,textvariable=str(gp))
gplabel=Label(moneyframe,text="Gold:")
ppvaluelabel=Label(moneyframe,textvariable=str(pp))
pplabel=Label(moneyframe,text="Platinum:")
	#Setup
typedrop.grid(row=0,column=1)
amount.grid(row=0,column=0)
cpvaluelabel.grid(row=1,column=1,sticky=W)
cplabel.grid(row=1,column=0,sticky=E)
spvaluelabel.grid(row=2,column=1,sticky=W)
splabel.grid(row=2,column=0,sticky=E)
epvaluelabel.grid(row=3,column=1,sticky=W)
eplabel.grid(row=3,column=0,sticky=E)
gpvaluelabel.grid(row=4,column=1,sticky=W)
gplabel.grid(row=4,column=0,sticky=E)
ppvaluelabel.grid(row=5,column=1,sticky=W)
pplabel.grid(row=5,column=0,sticky=E)
###########################################################################################################################
#Frame 																											Initiative
initiativeframe = Frame(root, bd=2, relief=GROOVE)
#Widgets
armorlabel=Label(initiativeframe,text="Armor")
armor=Label(initiativeframe,text=str(remove_n(info[13])))
speedlabel=Label(initiativeframe,text="Speed")
speed=Label(initiativeframe,text=remove_n(info[15]))
initiativelabel=Label(initiativeframe,text="Initiative")
initiative=Label(initiativeframe,text=str(remove_n(info[14])))
perceptionlabel=Label(initiativeframe,text="Perception")
perception=Label(initiativeframe,text=str(remove_n(info[12])))
proficiencylabel=Label(initiativeframe,text="Proficiency")
proficiency=Label(initiativeframe,text=str(remove_n(info[11])))
inspirationlabel=Label(initiativeframe,text="Inspiration")
inspiration=Label(initiativeframe,text=str(remove_n(info[18])))
#Setup
armorlabel.grid(row=0,column=0)
armor.grid(row=1,column=0)
initiativelabel.grid(row=0,column=1)
initiative.grid(row=1,column=1)
speedlabel.grid(row=0,column=2)
speed.grid(row=1,column=2)
perceptionlabel.grid(row=2,column=0)
perception.grid(row=3,column=0)
proficiencylabel.grid(row=2,column=1)
proficiency.grid(row=3,column=1)
inspirationlabel.grid(row=2,column=2)
inspiration.grid(row=3,column=2)
###########################################################################################################################
#Frames 																											Traits
traitsframe = Frame(root, bd=2, relief=GROOVE)
#Widgets
strengthlabel=Label(traitsframe,text="Strength")
strengthvalue=Label(traitsframe,text=remove_n(info[5]))
dexteritylabel=Label(traitsframe,text="Dexterity")
dexterityvalue=Label(traitsframe,text=remove_n(info[6]))
constitutionlabel=Label(traitsframe,text="Constitution")
constitutionvalue=Label(traitsframe,text=remove_n(info[7]))
intelligencelabel=Label(traitsframe,text="Intelligence")
intelligencevalue=Label(traitsframe,text=remove_n(info[8]))
wisdomlabel=Label(traitsframe,text="Wisdom")
wisdomvalue=Label(traitsframe,text=remove_n(info[9]))
charismalabel=Label(traitsframe,text="Charisma")
charismavalue=Label(traitsframe,text=remove_n(info[10]))
#Setup
strengthlabel.pack()
strengthvalue.pack()
dexteritylabel.pack()
dexterityvalue.pack()
constitutionlabel.pack()
constitutionvalue.pack()
intelligencelabel.pack()
intelligencevalue.pack()
wisdomlabel.pack()
wisdomvalue.pack()
charismalabel.pack()
charismavalue.pack()
###########################################################################################################################
#Frame 																										Proficiencies
proficinciesframe = Frame(root, bd=2, relief=GROOVE)
#Functions
def newprof():
	top=tk.Toplevel(root)
	top.title("New Proficiency")
	def addfunc(event=None):
		allproficencies += newskill.get()
		quit()
	def quit(event=None):
		top.destroy()
	buttonframe=Frame(top,bd=2,relief=FLAT)
	newskill=StringVar()
	newskill.set("")
	lab=Label(top,text="New Skill: ")
	ent=Entry(top,textvariable=newskill)
	add=Button(buttonframe,text="Add Skill",command=addfunc)
	cancel=Button(buttonframe,text="Cancel",command=quit)
	ent.bind("<Return>",addfunc)
	ent.bind("<Escape>",quit)

	lab.grid(row=0,column=0)
	ent.grid(row=0,column=1)
	add.grid(row=0,column=1,padx=4)
	cancel.grid(row=0,column=0,padx=4)
	buttonframe.grid(row=1,column=0,columnspan=2)

#Var
allproficencies1=StringVar()
allproficencies1.set(allproficencies)
#Widgets
proflabel=Label(proficinciesframe, text="Proficencies:")
profvalues=Label(proficinciesframe, text=str(allproficencies1.get()))
newbutton=Button(proficinciesframe, text="New",command=newprof)
#Setup
proflabel.grid(row=0,column=0)
newbutton.grid(row=0,column=1,padx=8)
profvalues.grid(row=1,column=0,columnspan=2)
###########################################################################################################################
#																														Gap
#
#
#
#
#
#
#
#
#
#
#
###########################################################################################################################
#Row 1																									Displaying Frames
nameframe.grid(row=0,column=0, columnspan=2,sticky=NSEW)
diceframe.grid(row=0,column=2,sticky=NSEW)
healthframe.grid(row=0,column=3,sticky=NSEW)
expframe.grid(row=0,column=4,sticky=NSEW)
#Row 2
initiativeframe.grid(row=1,column=0,columnspan=2,sticky=NSEW)
inventoryframe.grid(row=1,column=2,rowspan=3,sticky=NSEW)
spellframe.grid(row=1,column=3,rowspan=3,sticky=NSEW)
moneyframe.grid(row=1,column=4,rowspan=2,sticky=NSEW)
#Row 3
traitsframe.grid(row=2,column=0,rowspan=3,sticky=NSEW)
proficinciesframe.grid(row=3,column=4,rowspan=2,sticky=NSEW)

updateinventory()
updatespells()
mainloop()