"""
*************Welcome To HealthiPY***************
Use This Python Script To Keep Yourself Healthy
while Coding ;-)
***************************************************
"""
from pygame import mixer #module to play audio
from datetime import datetime#modules for date
from time import time#and time

#Function to play and pause audio tracks!
def musiconloop(file, stopper):#takes two arguments one — Which audio track to play and other what to input to stop the track
    mixer.init() #initializing mixer module
    mixer.music.load(file) #loading the file to play
    mixer.music.play()#playing the file
    while True:
        input_of_user = input()#taking input to stop audio
        if input_of_user == stopper:#if given input equals the stopper code 
            mixer.music.stop()#audio is stopped
            break#and the loop breaks!

def log_now(msg):#function to record the time of various activities in a text file called MyLogs!
    with open("mylogs.txt", "a") as f: #opening the file in "Append Mode" so that previous data isn't deleted when new log are created
        f.write(f"{msg} {datetime.now()}\n")#Using F-String To log the data

if __name__ == '__main__':#if we use the above two functions in some other class this name==main condition will prevent the code under it to be executed thus making the two functions above available for any use!
    #Setting initial values of time
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    #converting the time duration between two concequtive alarms to seconds for calculative purpose
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60
    print("Enter Q To Stop The Program!")
    while True:
        quit=input()#Chance to stop the program
        if quit == "Q":
        	break
        if time() - init_water > watersecs:#when 40 minutes have passed ring the alarm to drink water and log the time
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:#when 30 minutes have passed raise an alarm to do eye exercise and log the time!
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:#when 45 minutes have passed raise an alarm for physical exercise and log the time!
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")
