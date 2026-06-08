import sys
import time
from colorama import Fore, Back, Style
from pyfiglet import figlet_format
print(figlet_format("H E L L O", font = "3-d"))

print("there!")
print("This is a job interview form which all candidates must fill to see if they are right for the position.")
print("You are competing for the job of a professional dog surfing teacher in California.")
player = input('What is your name?')
print("Welcome , " + player + "! We are so glad to have you here today! I hope you will be a great fit for the job!")
age = int(input("What is your age?"))
if age < 18:
    print("Sorry, you are not old enough to work here.")
    print("Come back when you are older!")
    sys.exit("Application rejected. Have a nice day!");
elif age > 70:
    print("Sorry, you are too old to work here.")
    print("You need to retire already!")
    sys.exit("Application rejected. Have a nice day!")
else:
    print("Great! You are old enough to work here!")
    print("Let's move on to the next question.")

phonenumber = input("What is your phone number? (please enter 10 digits) ")
if not(len(phonenumber) == 10):
    print("Sorry, that is not a valid phone number. Please enter 10 digits.")
    print("If you can't even enter a valid phone number, I don't think this job will work for you. Bye!")
    sys.exit("Application rejected. Have a nice day!")

height = int(input("What is your height in cm? "))
if height < 140:
    print("Sorry, you are not tall enough to work here.")
    print("You need to be at least 140 cm to work here. Bye!")
    sys.exit("Application rejected. Have a nice day!")
elif height > 200:
    print("Sorry, you are too tall to work here. You need to be shorter to operate surfboards our size.")
    print("Maybe come back after growing shorter? Bye!!!")
    sys.exit("Application rejected. Have a nice day!")
else:
    print("You are just the right height! Let's move on...")

experience = input("Are you comfortable around dogs? (yes or no) ")
if experience == "yes":
    print("You have relevant job experience.That is wonderful. Let's move on...")
else:
    print("Unfortunately, that is a mandatory requiremement. You are not fit for the job. Thank you for your time!")
    sys.exit("Application rejected. Have a nice day!")

swim = input("Can you swim? (yes or no) ")
if swim == "yes":
    print("Great! That is required for this position. Let's move on...")
else:
    print("Unfortunately, that is a mandatory requirement. You are not fit for the job. Thank you for your time!")
    sys.exit("Application rejected. Have a nice day!")

hat = input("Would you be willing to wear a ridiculous hat if it helped a dog feel comfortable? (yes or no) ")
if hat == "yes":
    print("Great! That is actually a case that comes up a lot for this position. Let's move on...")
else:
    print("Unfortunately, that means you are not fit for the job.")
    sys.exit("Application rejected. Have a nice day!")

dog = input("Will you look at this dog? (yes or no) ")
if dog == "yes":
    print("Great! That is a mandatory requirement for this position. Let's move on...")
    print()
    print()
    print()
    print("/^-----^\ ")
    print("V  o o  V")
    print(" |  Y  |")
    print("  \ Q /")
    print("  / - \ ")
    print("  |    \ ")
    print("  |     \    )")
    print("  || (___\====")
               
else:
    print("This may reflect badly on your application because you must be willing to spend as much time with dogs as possible.")
print("Congratulations! You are a great fit for the job! I would just like to clarify your details...")
print("Your name is " + player + ".")
print("Your age is " + str(age) + ".")
print("Your phone number is " + phonenumber + ".")
print("Your height is " + str(height) + " cm.")
print("You are comfortable around dogs.")
print("You can swim.")
print("You are willing to wear a ridiculous hat if it helps a dog feel comfortable.")
print()
print()
print(figlet_format("WOOF!", font = "nvscript"))

print("We have some more questions for you. This is a test to see if you are smart enough about dogs to work here.")
print("You need to get at least half of the questions right if you want to work here.")

accuracy = 0

answer = input("What is the name of the dog in the movie 'Up'? ")
if answer.lower() == "dug":
    print("Correct! Let's continue...")
    accuracy+=1
else:
    print("Wrong! The correct answer is Dug. You need to know your dog movies if you want to work here.")

scoobydoo = input("Which famous dog was known for solving mysteries with friends?")
if scoobydoo.lower() == "scooby doo" or scoobydoo.lower() == "scooby":
    print("Correct! Let's continue...")
    accuracy+=1
else:
    print("Wrong! The correct answer is Scooby Doo. You need to know your dog cartoons if you want to work here.")

snoopy = input("Which famous dog was known for being the pet of charlie brown?")
if snoopy.lower() == "snoopy":
    print("Correct! Let's continue...")
    accuracy+=1
else:
    print("Wrong! The correct answer is Snoopy. You need to know your dog cartoons if you want to work here.")

pluto = input("Which famous dog was known for being mickey mouse's pet?")
if pluto.lower() == "pluto":
    print("Correct! Let's continue...")
    accuracy+=1
else:
    print("Wrong! The correct answer is Pluto. You need to know your disney dogs if you want to work here.")

print(figlet_format("WOOF!", font = "isometric2"))
if accuracy > 2:
    print("You do not have enough accuracy to pass this test. I'm sorry, but you are not a good fit for the job. Bye!" )
    sys.exit("Application rejected. Have a nice day!")
print("HOORAY! You passed the dog trivia test with sufficient accuraacy so you are one step closer to getting the job!")
print("We just have one more task for you to attempt...")
print("Find out which breed of dog you are through this quiz!")
collie = 0
poodle =0
retriever = 0
sheepdog =0
task = input("1. Your teacher gives you a free afternoon. What do you do?" + "\n" +"A) Read, learn, or solve puzzles. " + "\n" + "B) Work on an art project or hobby." + "\n" +"C) Meet up with friends." + "\n" +"D) Get ahead on chores or assignments.")
if task.lower() == "a":
    collie +=1
elif task.lower() == "b":
    poodle += 1
elif task.lower() == "c":
    retriever += 1
else:
    sheepdog+= 1
compliment = input("2. What is your favorite compliment to receive?" + "\n" + "A) You're so smart!" + "\n" + "B) You're so creative!" + "\n" + "C) You're so nice!" + "\n" + "D) You're so responsible!")
if task.lower() == "a":
    collie +=1
elif task.lower() == "b":
    poodle += 1
elif task.lower() == "c":
    retriever += 1
else:
    sheepdog += 1
project = input("3. Your group has a big project due. You are most likely to:" + "\n" + "A) Come up with the strategy." + "\n" + "B) Make it look amazing." + "\n" + "C) Keep everyone motivated." + "\n" + "D) Make sure everything gets finished.")
if project.lower() == "a":
    collie +=1
elif project.lower() == "b":
    poodle += 1
elif project.lower() == "c":
    retriever += 1
else:
    sheepdog += 1
button = input("4. You find a giant red button labeled 'DO NOT PRESS.'\n" + "A) Wonder what it does and research it.\n" + "B) Bedazzle it.\n" + "C) Press it with friends for moral support.\n" + "D) Stand guard so nobody presses it.\n")
if button.lower() == "a":
    collie +=1
elif button.lower() == "b":
    poodle += 1
elif button.lower() == "c":
    retriever += 1
else:
    sheepdog += 1
squirrel = input("5. A council of squirrels arrives at your house and declares you their chosen one. What do you do?\n" + "A) Ask for the terms and conditions. (Collie)\n" + "B) Request a ceremonial crown. (Poodle)\n" + "C) Invite them inside for snacks. (Retriever)\n" + "D) Demand to see official squirrel documentation. (Sheepdog)\n")
if squirrel.lower() == "a":
    collie +=1
elif squirrel.lower() == "b":
    poodle += 1
elif squirrel.lower() == "c":
    retriever += 1
else:
    sheepdog += 1
print(figlet_format("FETCH!", font = "nvscript"))
if collie >= poodle and collie >= retriever and collie >= sheepdog:
    print("Y", end= "\r")
    time.sleep(0.1)
    print("Yo", end= "\r")
    time.sleep(0.1)
    print("You", end= "\r")
    time.sleep(0.1)
    print("You ", end= "\r")
    time.sleep(0.1)
    print("You a", end= "\r")
    time.sleep(0.1) 
    print("You ar", end= "\r")
    time.sleep(0.1)
    print("You are", end= "\r")
    time.sleep(0.1)
    print("You are ", end= "\r")
    time.sleep(0.1)
    print("You are a", end= "\r")
    time.sleep(0.1)
    print("You are a ", end= "\r")
    time.sleep(0.1)
    print("You are a C", end= "\r")
    time.sleep(0.1)
    print("You are a Co", end= "\r")
    time.sleep(0.1)
    print("You are a Col", end= "\r")
    time.sleep(0.1)
    print("You are a Coll", end= "\r")
    time.sleep(0.1)
    print("You are a Colli", end= "\r")
    time.sleep(0.1)
    print("You are a Collie", end= "\r")
    time.sleep(0.1)
    print("You are a Collie!",)
    time.sleep(0.1)
    
elif poodle >= retriever and poodle >= sheepdog:
    print("Y", end= "\r")
    time.sleep(0.1)
    print("Yo", end= "\r")
    time.sleep(0.1)
    print("You", end= "\r")
    time.sleep(0.1)
    print("You ", end= "\r")
    time.sleep(0.1)
    print("You a", end= "\r")
    time.sleep(0.1) 
    print("You ar", end= "\r")
    time.sleep(0.1)
    print("You are", end= "\r")
    time.sleep(0.1)
    print("You are ", end= "\r")
    time.sleep(0.1)
    print("You are a", end= "\r")
    time.sleep(0.1)
    print("You are a ", end= "\r")
    time.sleep(0.1)
    print("You are a P", end= "\r")
    time.sleep(0.1)
    print("You are a Po", end= "\r")
    time.sleep(0.1)
    print("You are a Poo", end= "\r")
    time.sleep(0.1)
    print("You are a Pood", end= "\r")
    time.sleep(0.1)
    print("You are a Poodl", end= "\r")
    time.sleep(0.1)
    print("You are a Poodle", end= "\r")
    time.sleep(0.1)
    print("You are a Poodle!", )
    time.sleep(0.1)
elif retriever >= sheepdog:
    print("Y", end= "\r")
    time.sleep(0.1)
    print("Yo", end= "\r")
    time.sleep(0.1)
    print("You", end= "\r")
    time.sleep(0.1)
    print("You ", end= "\r")
    time.sleep(0.1)
    print("You a", end= "\r")
    time.sleep(0.1)
    print("You ar", end= "\r")
    time.sleep(0.1)
    print("You are", end= "\r")
    time.sleep(0.1)
    print("You are ", end= "\r")
    time.sleep(0.1)
    print("You are a", end= "\r")
    time.sleep(0.1)
    print("You are a ", end= "\r")
    time.sleep(0.1)
    print("You are a S", end= "\r")
    time.sleep(0.1)
    print("You are a Sh", end= "\r")
    time.sleep(0.1)
    print("You are a She", end= "\r")
    time.sleep(0.1)
    print("You are a Shee", end= "\r")
    time.sleep(0.1)
    print("You are a Sheep", end= "\r")
    time.sleep(0.1)
    print("You are a Sheepd", end= "\r")
    time.sleep(0.1)
    print("You are a Sheepdo", end= "\r")
    time.sleep(0.1)
    print("You are a Sheepdog", end= "\r")
    time.sleep(0.1)
    print("You are a Sheepdog!", )
    time.sleep(0.1)
else:
    print("Y", end= "\r")
    time.sleep(0.1)
    print("Yo", end= "\r")
    time.sleep(0.1)
    print("You", end= "\r")
    time.sleep(0.1)
    print("You ", end= "\r")
    time.sleep(0.1)
    print("You a", end= "\r")
    time.sleep(0.1)
    print("You ar", end= "\r")
    time.sleep(0.1)
    print("You are", end= "\r")
    time.sleep(0.1)
    print("You are ", end= "\r")
    time.sleep(0.1)
    print("You are a", end= "\r")
    time.sleep(0.1)
    print("You are a ", end= "\r")
    time.sleep(0.1)
    print("You are a R", end= "\r")
    time.sleep(0.1)
    print("You are a Re", end= "\r")
    time.sleep(0.1)
    print("You are a Ret", end= "\r")
    time.sleep(0.1)
    print("You are a Retr", end= "\r")
    time.sleep(0.1)
    print("You are a Retri", end= "\r")
    time.sleep(0.1)
    print("You are a Retrie", end= "\r")
    time.sleep(0.1)
    print("You are a Retriev", end= "\r")
    time.sleep(0.1)
    print("You are a Retrieve", end= "\r")
    time.sleep(0.1)
    print("You are a Retriever", end= "\r")
    time.sleep(0.1)
    print("You are a Retriever!")
    time.sleep(0.1)

print(figlet_format("WOOF", font = "larry3d"))
print("Good Job, " + player + "! You are a great fit for the position of a professional dog surfing teacher in California! We will contact you soon. Thank you for your time and have a nice day!")