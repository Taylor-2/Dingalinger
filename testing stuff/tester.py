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
amount.bind("<Shift Return>",highestvalue)
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