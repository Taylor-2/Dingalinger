from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack()

def submit(event=None):
	items.append(textvar.get())
	inventory=open("back\\Inventory.txt","w")
	ctr = 0
	while (ctr < len(items)):
		inventory.write(items[ctr])
		ctr += 1
	inventory.close()
	textvar.set("")
	read()

def read():
	inventory=open("back\\Inventory.txt","r")
	items = inventory.readlines()
	inventory.close()
	ctr = 0
	while (ctr < len(items)):
		listbox.insert(END,items[ctr])
		ctr += 1

read()

textvar=StringVar()
textvar.set("")


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=BOTH)




fiel=Entry(root,textvariable=textvar)
fiel.bind("<Return>", submit)
fiel.pack()

ctr = 0
while (ctr < len(items)):
	listbox.insert(END,items[ctr])
	ctr += 1

# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

mainloop()