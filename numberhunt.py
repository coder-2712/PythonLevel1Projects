import random
gamemode = input('There are 4 modes of play: respond from 1 to 4 for game mode.' + '\n' + '1. is when the computer thinks of a number and you guess it, 2. is when you think of a number and the computer guesses it using binary and linear search, 3. is like 1. but with letters, 4. is number hunt with only perfect squares.')
if gamemode == 1:
  done = False
  number = random.randint(0,100)
  timesGuessed = 0
  print("I'm thinking of a number between 0 and 100. Can you guess it?")
  while not done:
    try:
      answer = int(input("Enter your guess: "))
      while not(answer == number):
      
        if answer > number:
            print("My number is smaller than that!")
            timesGuessed = timesGuessed + 1
        elif answer < number:
            print("My number is larger than that!")
            timesGuessed = timesGuessed + 1 
        answer = int(input("Enter your guess: "))
        if answer == number:
          print("That's correct! You win!")
          print("It took you " + str(timesGuessed) + " guesses.")
          done = True
    except:
      print('That is not a valid input.')

elif gamemode == 2:



# user inputs number and computer guesses it
  print()
  print()
  print("Now your turn to pick a number!")
  print("click ENTER when ready.")
  input()
  done = False
  attempts = 0
  guess = 1
  guess_step = 10
  prev_answer = ""


  while not done:
    print("Is your number " + str(guess) + "?" + "\n")
    answer = input("Y is yes, L is larger than that, S is smaller than that:"+ "\n")


    if attempts > 1:
      if prev_answer != answer:
        guess_step = guess_step - 1

    prev_answer = answer
    if  answer == "L":
      if guess >= 1:
        guess = guess + guess_step
        attempts = attempts + 1
    elif answer == "S":
      if guess < 100:
        guess = guess - guess_step
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
elif gamemode == 3:
  letters = "abcdefghijklmnopqrstuvwxyz"
  letterchoice = random.choice(letters)
  timesGuessed = 0
  print("I'm thinking of a letter between 0 and 100. Can you guess it?")
  while not done:
    try:
      answer = (input("Enter your guess: "))
      while not(answer == letterchoice):
      
        if answer > letterchoice:
            print("My letter comes before that!")
            timesGuessed = timesGuessed + 1
        elif answer < letterchoice:
            print("My letter comes after that!")
            timesGuessed = timesGuessed + 1 
        answer = (input("Enter your guess: "))
        if answer == letterchoice:
          print("That's correct! You win!")
          print("It took you " + str(timesGuessed) + " guesses.")
          done = True
    except:
      print('That is not a valid input.')
else:
  squarenumbers = [x**2 for x in range (1,101)]
  num = random.choice(squarenumbers)
  print('I have picked a random square of the first 100 numbers. Can you guess it?')
  done = False

  timesGuessed = 0
  while not done:
      try:
        while not(answer == num):
          
          answer = int(input("Enter your guess: "))
          if answer in squarenumbers:
            if answer > num:
                print("My number is smaller than that!")
                timesGuessed = timesGuessed + 1
            elif answer < num:
                print("My number is larger than that!")
                timesGuessed = timesGuessed + 1 
            answer = int(input("Enter your guess: "))
            if answer == num:
              print("That's correct! You win!")
              print("It took you " + str(timesGuessed) + " guesses.")
              done = True
          else:
            print('Your guess is not even a square number!')
      except:
        print('That is not a valid input.')
