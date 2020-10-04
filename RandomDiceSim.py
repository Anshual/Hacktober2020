#Rolling Dice Simulator!
#By Itachi
import random
import time
print("Hello! Im Itachi Uchiha!")
time.sleep(1)
print("What's Your Name?")
name=input()
print(f"Hello \b {name}")
time.sleep(1)
print("Let's roll your Dice!")
time.sleep(1)
print("Enter \"Kamui\" To Exit My Genjutsu Game!")
time.sleep(1)
print("KOTOAMATSUKAMI!")
while ("true"):
	temp=random.randint(1,7)
	print(f"It's A {temp} ")
	print("Continue?")
	choice = input()
	if choice.casefold() == "kamui":
		print("IZANAMI!")
		break
	else:
		print("Infinite Tsukoyomi!")	