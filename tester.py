from tkinter import *
import tkinter.messagebox as msg

root=Tk()

def converter(event=None):
	amount=int(entery.get())
	selectedtype=typedropdown.get()
	total=money.get()

	if (selectedtype == "Copper"):
		total += amount
	elif(selectedtype == "Silver"):
		total += (amount*10)
	elif(selectedtype == "Gold"):
		total += (amount*100)
	elif(selectedtype == "Electrum"):
		total += (amount*500)
	elif(selectedtype == "Platinum"):
		total += (amount*1000)
	money.set(total)
	entery.set("")
	typedropdown.set("Gold")

def allmoney():
	total=money.get()
	while(((total/1000)%2)

money=IntVar()
money.set(1260)
entery=StringVar()
entery.set("")
typedropdown=StringVar()
typedropdown.set("Gold")
allmoney=StringVar()
allmoney.set("")


updatinglabel=Label(root,textvariable=allmoney)
#staticlabel=Label(root,textvariable=typedropdown)
amount=Entry(root,textvariable=entery)
amount.bind("<Return>",converter)
button=Button(root,text="Submit",command=converter)
typedrop=OptionMenu(root, typedropdown, "Copper", "Silver", "Gold", "Electrum", "Platinum")

typedrop.pack()
updatinglabel.pack()
#staticlabel.pack()
amount.pack()
button.pack()

mainloop()