from tkinter import *
import os
import time
from random import *
import tkinter.messagebox as msg

items=[]
root=Tk()
def writenewitem(event=None):
	file=open("C:\\Users\\Dexter Hubbard\\Documents\\GitHub\\Dingalinger\\Back\\Inventory.txt","a")
	file.write(str(inventoryentery.get()) + "\n")
	file.close()
	updateinventory()
def updateinventory():
	global items
	file=open("C:\\Users\\Dexter Hubbard\\Documents\\GitHub\\Dingalinger\\Back\\Inventory.txt","r")
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
def remove_n(value):
	return value[0:len(value)-1]
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
	file=open("C:\\Users\\Dexter Hubbard\\Documents\\GitHub\\Dingalinger\\Back\\Inventory.txt","w")
	while(ctr<len(items)):
		file.write(str(items[ctr])+"\n")
		ctr+=1
	file.close()
	updateinventory()
def edit(event=None):
	selected=items[int(str(inventorybox.curselection())[1:len(str(inventorybox.curselection()))-2])]
	inventoryentery.set(selected)

inventoryentery=StringVar()
inventoryentery.set("")

invframe=Frame(root, bd=2, relief=GROOVE)

inventorybox = Listbox(invframe,width=30)
inventorybox.bind("<Delete>",deleteitem)

invscroll = Scrollbar(invframe)
invscroll.config(command=inventorybox.yview)
inventorybox.config(yscrollcommand=invscroll.set)
inventery=Entry(invframe,textvariable=inventoryentery,width=30)
inventorybox.bind("<Return>",writenewitem)
inventery.bind("<Return>",writenewitem)
inventorybox.bind("<Double-Button-1>",edit)

invscroll.pack(side=RIGHT, fill=Y)
inventorybox.pack()
inventery.pack()

invframe.grid(row=1,column=1)

updateinventory()

mainloop()

