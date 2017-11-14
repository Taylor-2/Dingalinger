from tkinter import *
import tkinter as tk
import os
import time
from random import *
import tkinter.messagebox as msg
###########################################################################################################################
root=Tk()
###########################################################################################################################
def save(event=None):
	print("Save")
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
	descriptiontop=Label(top,text=spellinfo[6])

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

	# descriptionenttop.bind("<Enter>",writenew)

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

def remove_n(value):
	return value[0:len(value)-1]
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

###########################################################################################################################

###########################################################################################################################
spellframe = Frame(root, bd=2, relief=GROOVE)

spellbox = Listbox(spellframe,width=20,height=8)
spellbox.bind("<Double-Button-1>",windowspell)

newbutton=Button(spellframe,text="New Spell",command=newspell)

spellscroll = Scrollbar(spellframe)
spellscroll.config(command=spellbox.yview)
spellbox.config(yscrollcommand=spellscroll.set)

###########################################################################################################################
spellscroll.pack(side=RIGHT, fill=Y)
spellbox.pack()
newbutton.pack()


spellframe.pack()

updatespells()
###########################################################################################################################
mainloop()