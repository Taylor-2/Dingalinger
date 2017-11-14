ctr=0
level="0"
while(ctr<3):
	file=open("Spellbook\\Spell " + str(ctr+1) + ".txt","w")
	file.write("Spell " + str(ctr+1) + "\n")
	file.write(level + "\n")
	file.write("time\nrange\ncomp\nduration\ndescription\n")
	file.close()
	ctr += 1
level="1"
while(ctr<11):
	file=open("Spellbook\\Spell " + str(ctr+1) + ".txt","w")
	file.write("Spell " + str(ctr+1) + "\n")
	file.write(level + "\n")
	file.write("time\nrange\ncomp\nduration\ndescription\n")
	file.close()
	ctr += 1
level="2"
while(ctr<13):
	file=open("Spellbook\\Spell " + str(ctr+1) + ".txt","w")
	file.write("Spell " + str(ctr+1) + "\n")
	file.write(level + "\n")
	file.write("time\nrange\ncomp\nduration\ndescription\n")
	file.close()
	ctr += 1

