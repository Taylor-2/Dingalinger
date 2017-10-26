from tkinter import *
import tkinter.messagebox as msg

root=Tk()

def inputfun(event=None):
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
def converter(event=None):
	amount=int(entery.get())
	total=money.get()

	if (moneytype.get() == "Copper"):
		total += amount
	elif(moneytype.get() == "Silver"):
		total += (amount*10)
	elif(moneytype.get() == "Gold"):
		total += (amount*100)
	elif(moneytype.get() == "Electrum"):
		total += (amount*500)
	elif(moneytype.get() == "Platinum"):
		total += (amount*1000)
	money.set(total)
	entery.set("")
	moneytype.set("Gold")
	allmoney1()
def highestconverter():
	final=""
	total=money.get()
	pp=0
	while(total>1000):
		pp+=1
		total-=1000
	ep=0
	while(total>1):
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
moneytype=StringVar()
moneytype.set("Gold")
allmoney=StringVar()
allmoney.set(str(money.get()))

cp=IntVar()
cp.set(0)
sp=IntVar()
sp.set(0)
ep=IntVar()
ep.set(0)
gp=IntVar()
gp.set(0)
pp=IntVar()
pp.set(0)

updatinglabel=Label(root,textvariable=allmoney)
amount=Entry(root,textvariable=entery)
amount.bind("<Return>",inputfun)
button=Button(root,text="Submit",command=inputfun)
typedrop=OptionMenu(root, moneytype, "Copper", "Silver", "Gold", "Electrum", "Platinum")
cpvaluelabel=Label(root,textvariable=str(cp))
cplabel=Label(root,text=" CP")
spvaluelabel=Label(root,textvariable=str(sp))
splabel=Label(root,text=" SP")
epvaluelabel=Label(root,textvariable=str(ep))
eplabel=Label(root,text=" EP")
gpvaluelabel=Label(root,textvariable=str(gp))
gplabel=Label(root,text=" GP")
ppvaluelabel=Label(root,textvariable=str(pp))
pplabel=Label(root,text=" PP")


typedrop.pack()
amount.pack()
cpvaluelabel.pack()
cplabel.pack()
spvaluelabel.pack()
splabel.pack()
epvaluelabel.pack()
eplabel.pack()
gpvaluelabel.pack()
gplabel.pack()
ppvaluelabel.pack()
pplabel.pack()

mainloop()