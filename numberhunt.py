import random
done = False
number = random.randint(0,100)
print("I'm thinking of a number between 0 and 100. Can you guess it?")
while not done:
  timesGuessed = 0
  answer = int(input("Enter your guess: "))
  while not(answer == number):
    if answer > number:
      print("My number is smaller than that")
      timesGuessed = timesGuessed + 1
    elif answer < number:
        print("My number is larger than that! !")
        timesGuessed = timesGuessed + 1
    answer = int(input("Enter your guess: "))
    if answer == number:
      print("That's correct! You win!")
      print("It took you " + str(timesGuessed) + " guesses.")
      done = True

# user inputs number and computer guesses it
print()
print()
print("Now your turn to pick a number!")
print("click ENTER when ready.")
input()
done = False
attempts = 0
guess = random.randint(0 , 100)
while not done:
  print("Is your number " + str(guess) + "?" + "\n")
  answer = input("Y is yes, L is larger than that, S is smaller than that:"+ "\n")
  if answer == "Y":
      print("I guessed it in " + str(attempts) + " attempts.")
      done = True
  elif  answer == "L":
    if guess > 1:
      guess = guess + 1
      attempts = attempts + 1
  elif answer == "S":
    if guess < 1:
      guess = guess - 1
      attempts = attempts + 1
  elif answer == "Y":
    done = True
    print('I finally guessed it!')
    print("It took me " + str(attempts) + " tries.")



# user inputs number and computer guesses it using binary search
print()
print()
print("Now pick another number between 0 and 100, but this time I will guess it using binary search!")
print("click ENTER when ready.")
input()
done = False
attempts = 0
guess = 50
low = 0
high = 100
while not done:
  guess = round((low + high) / 2)
  print("Is your number " + str(guess) + "?" + "\n")
  answer = input("Y is yes, L is larger than that, S is smaller than that:"+ "\n")
  attempts = attempts + 1
  if answer.lower() == "y":
      print("I guessed it in " + str(attempts) + " attempts.")
      done = True
  elif  answer.lower() == "l":
    low = guess
  elif answer.lower() == "s":
    high = guess