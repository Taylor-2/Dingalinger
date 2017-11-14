from tkinter import *
import os
import time
from random import *
import tkinter.messagebox as msg
info=[]
money=[]
inventory=[]
proficiencies=[]
spells=[]

root=tk()

def writeinfo()
	file=open("Back\\Info.txt","w")
	ctr=0
	while(ctr<len(info)):
		file.write(info[ctr] + "\n")
		ctr += 1
	file.close()

def writemoney()
	money.append(cp.get())
	money.append(sp.get())
	money.append(ep.get())
	money.append(gp.get())
	money.append(pp.get())

	file=open("Back\\Wallet.txt","w")
	ctr=0
	while(ctr<len(money)):
		file.write(money[ctr] + "\n")
		ctr+=1
	file.close()

def inventory()
	file=open("Back\\Inventory.txt","w")
	ctr=0
	while(ctr<len(inventory)):
		file.write(inventory[ctr] + "\n")
		ctr += 1
	file.close()

def proficiencies()
	file=open("Back\\Proficiencies.txt","w")
	ctr=0
	while(ctr<len(proficiencies)):
		file.write(proficiencies[ctr] + "\n")
		ctr += 1
	file.close()



mainloop()