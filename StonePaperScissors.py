import random
import time
print("Hello!")
time.sleep(1)
print("What's Your Name?")
name=input()
print("Welcome! ", name)
time.sleep(2)
print("Let's Play Stone Paper scissor!")
time.sleep(2)
print("There Will Be 10 Rounds!")
time.sleep(2)
print("If You Win More Times Than Me, You Win!")
time.sleep(2)
print("Ready?")
time.sleep(2)
print("Let's Go!")
list = [ "Stone" , "Paper" , "scissor"]
def result(a,b):
	if(a.casefold()=="stone" and b.casefold()=="paper" ):
		print("I Win!")
		return 0
	elif(a.casefold()=="stone" and b.casefold()=="scissor" ):
			print("You Win!")
			return 1
	elif(a.casefold()=="paper" and b.casefold()=="stone" ):
			print("You Win!")
			return 1
	elif(a.casefold()=="scissor" and b.casefold()=="paper" ):
	   	print("You Win!")
	   	return 1
	elif(a.casefold() == b.casefold()):
		print("It's A Draw!")
	else:
		print("I Win!")
		return 0
i=0
sp = 0
sc = 0
for i in range(0,10):
	print("Round ", i+1)
	print("Enter Your Choice!")
	chp=input()
	chc=random.choice(list)
	print(chc)
	r=result(chp,chc)
	if(r==1):
		sp+=1
		print("Congrats Let's See The Other Round!")
	else:
		sc+=1
		print("Yeei! Best Of Luck For The Next Round!")
if(sp>sc):
	print("Wah Re Party Dude You Won!")
	print("Your Score Was ",sp)
elif(sc>sp):
	print("Har Ke Jeetne Wale Ko Bazigaar Kehte h!")
	print("Your Score Was ",sp)
	print("Best Of Luck Next Time! I Won!!!")
else:
	print("Arre Bhai Bhai Bhai It's A Draw!")