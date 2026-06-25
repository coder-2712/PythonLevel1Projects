from pyfiglet import figlet_format
from colorama import Fore, Back, Style
hello = figlet_format("Hello", font = 'larry3d')
print(hello)
print("Do you really want to meet the famous fortune teller for a peek at your future?")
print("Well, wait in line!")
print("*You look at the line and it has hundreds of people*")
lineorwait = input("Are you just going to wait in line or will you try the secret line cut method? (w for wait, l for line cut) ")
if lineorwait == "w":
    print("Seriously? well, it's going to take  at least 5 hours till this line clears. It doesn't take a fortune teller to forsee you won't see the fortune teller anytime soon.")
    print('Good riddance!')
if lineorwait == "l":
    print("*sighs* I should have never told you about this and gotten you curious, but now I have to waste my time on you.")
    print("Well, you have to pass my quiz. I'ts so simple even stupid people like you should be able to pass it, but we'll see...")
    fortune = input("What is the deck of cards used by fortune tellers to read futures?")
    if fortune.lower() == "tarot" or "tarot cards" or "tarot deck":
        print("I'm surprised you had enough intellect to even get that right, but that was just a warmup.")
    else:
        print(Back.RED + "Are you telling me you can't even get that right? You're even stupider than I thought.")
        print(Style.RESET_ALL)
    word = input("🔮 The crystal ball seeks an 8-letter word with exactly 3 vowels.")
    if  not len(word) == 8:
        print(Fore.RED + "You are SUCH A DISASTER!!!")
        print("Your word isn't even 8 letters.")
        print(Style.RESET_ALL)
    else:
        print("Your word has 8 letters, but...")
        count_a = word.count("a")
        count_e = word.count("e")
        count_i = word.count("i")
        count_o = word.count("o")
        count_u = word.count("u")
        count_vowels = count_a + count_e + count_i + count_o + count_u 
        if count_vowels > 3:
            print("I only asked you for THREE vowels, you idiot! NOT MORE!!!")
        elif count_vowels == 3:
            print('Exactly 3 vowels and no more... where is the motivation?')
        elif count_vowels < 3:
            print("This word has LESS THAN 3 VOWELS! You're so lazy you couldnt even have 3??? Your chances of meeting the prof just plummeted.")
    wise = input("🌙 The stars demand a sentence whose final words are 'wise assistant'. Use punctuation but no questions!")
    if wise.endswith("wise assistant"):
        print("Don't you know what punctuation is? Go back to the first grade! (Even there, you'll probably have to take remedial claasses, you're such an idiot.)")
    elif wise.endswith("wise assistant."):
        print("Hmm... That looks ok... but...")
        len_first = wise.find(" ")
        if len_first < 8:
            print("The first word is too short.")
    else:
        print(Back.RED + "That doesn't end with WISE ASSISTANT! Can you  not even follow simple instructions? You're so slow.")
        print(Style.RESET_ALL)
    titanic = int(input('In what year did the titanic sink?' + '\n'))
    if titanic == 1912:
        print("At least you could get this right.")
    else:
        print(Back.RED + "WRONG! the titanic sank in 1912! You are really bad at this.")
        print(Style.RESET_ALL)
    islands = str(input('Which country has the most islands in the world?' + '\n'))
    if islands.lower() == "sweden":
        print("That's right, but it was the easiest question on the quiz.")
    else:
        print(Back.RED + 'Seriously? The answer is sweden. You really are stupid.')
        print(Style.RESET_ALL)
    print()
    print()
    print("Well, the fact that you attempted this quiz at all means you can access the line cut, because I have to make allowances for lesser minds like yours.")
    print()
    print()
    print("Well, now I have to give you an appointment slot. *sighs*")
    print('Pick a time tomorrow:')
    print("A. 3 minutes before sunrise      " + "B. 23 minutes after sunset", sep = "\t\t")
    print('C. 12 minutes after midnight     ' + "D. 45 minutes before noon", sep = '\t\t')
    print()
    slot = input('Please select your slot: (A/B/C/D)\n')
    if slot.upper() == 'A':
        print('Okay, but the fortune teller is known to go jogging then. You probably will not see him.')
    elif slot.upper() == 'B':
        print("Okay, but the fortune teller may be eating dinner then.You probably won't see him.")
    elif slot.upper() =='C':
        print("Okay, but the fortune teller may have fallen asleep. You probably won't see him.")
    else:
        print("Okay, but the fortune teller may be eating his breakfast. You probably won't see him.")
    print()
    print('No thanks for coming and wasting my time!')
    print("Have a horrible day!")
    bye = figlet_format("GOODBYE", font = "isometric2")
    print(bye)