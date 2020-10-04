import random
import time
print("Hello! What's Your Name?")
g = input()
print("Sup! ",g," Let's Play A Game")
time.sleep(1)
print("You'll Guess A Number And I'll Help You Find It!")
time.sleep(2)
print("Let's Do It!")
n = random.randint(0,10)
time.sleep(2)
print("Choose A Number From 1 to 10")
time.sleep(3)
print("Ready?? Let's See Your Guessing!")
time.sleep(1)
print("Enter Your No.")
c = int(input())
while n!=c:
	if n<c:
		print("Thoda Neeche Ane Ka Re Baba!")
		time.sleep(1)
		print("Koi Nahi Re Baba Fir Se Try Karne Ka!")
		c=int(input())
	elif n>c:
		print("Thoda Upar Jane Ka Re Baba!")
		time.sleep(1)
		print("Koi Nahi Re Baba Fir Se Try Karne Ka!")
		c=int(input())
print("Ye Baba Tu Bhagwan Hai Re! Mast Khela Re!")