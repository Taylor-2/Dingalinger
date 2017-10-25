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
	allmoney1()

def allmoney1():
	final=""
	total=money.get()
	pp=total/1000
	pptot=0
	while(pp>1):
		pptot+=1
		pp-=1
	final+=str(pptot) + " PP, "
	ep=pp*2
	eptot=0
	while(ep>1):
		eptot+=1
		ep-=1
	final+=str(eptot) + " EP, "
	gp=ep*5
	gptot=0
	while(gp>1):
		gptot+=1
		gp-=1
	final+=str(gptot) + " GP, "
	sp=gp*10
	sptot=0
	while(sp>1):
		sptot+=1
		sp-=1
	final+=str(sptot) + " SP, "
	cp=sp*10
	cptot=0
	while(cp>1):
		cptot+=1
		cp-=1
	final+=str(cptot) + " CP, "
	print(final)
	allmoney.set(final)


money=IntVar()
money.set(1260)
entery=StringVar()
entery.set("")
typedropdown=StringVar()
typedropdown.set("Gold")
allmoney=StringVar()
allmoney.set(str(money.get()))


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