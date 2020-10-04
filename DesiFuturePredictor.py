import time
import random
print("Aagya Aagya")
time.sleep(2)
print("Baba Lamba L@nd A Gaya!")
time.sleep(2)
print("Sabka Bhavishya Bataiga Baba!!")
time.sleep(2)
bhavishya = ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","N","N","N","N","N","C","C","C","C","C"]
print("Darbaar Khul Gaya H!")
time.sleep(2)
print("MAAAAAL")
time.sleep(2)
print("BAWAALLLL")
time.sleep(2)
print("Matalb Sawaal Pucho Beta!")
time.sleep(2)
print("Ek bar me ek!")
print("Type \"Baba Lamba L@nd Ki Jay\" to exit!")
while("true"):
	print("Sawaal Batao!")
	sawaal=input()
	temp=random.choice(bhavishya)
	bh=" "
	if temp=="Y":
		bh="Kripa Barsegi!"
	elif temp=="N":
		bh="Jhaat Khujaao"
	else:
		bh="Bandar Lauki Le Gaya!!!!!!!!"
	print(f"Beta!....{bh}")
	print("You Want Exxxtra?")
	choice=input()
	if choice.casefold() == "baba lamba l@nd ki jay":
		break
	else:
		print("Aham Brahmasmi! Pucho Beta!")