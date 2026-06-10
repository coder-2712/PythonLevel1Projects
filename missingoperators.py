import random
RandomorNot = input("Would you like to play with random numbers? (y/n)\n")
if RandomorNot == 'n':
    done = False
    while not done:
    
        try:
            num1 = int(input("Enter first number:\n"))
            done = True
        except:
            print("That was an invalid input. Please try again.")
    done = False
    while not done:
        try:
            num2 = int(input("Enter another number:\n"))
            done = True
        except:
            print("That was an invalid input. Please try again.")
else:
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)

print("Now I will give you a math problem with a missing operator.\n")
op_list = ['+', '-', '*']
op = random.randint(0, 2)
if op == 0:
    rhs = num1 + num2
if op == 1:
    rhs = num1 - num2
if op == 2:
    rhs = num1 * num2
print("Tell me the missing operator in this equation\n")
print("It can be substraction, multiplication, or addition (+, -, or *):\n")
answer = input(str(num1) + ' __ ' + str(num2) + ' = ' + str(rhs) + '\n')
if len(answer)<= 1:
  if answer == op_list[op]:
    print("Correct!")
  else:
    print("Incorrect!")
else:
  answer = input("Please enter the correct nuber of operators.")
print()
print()
print("Level Up! Try this harder one with 3 numbers!")

num3 = random.randint(0, 100)
op1 = random.randint(0, 1)
op2 = random.randint(0, 1)
if op1 == 0:
    rhs = num1 + num2
if op1 == 1:
    rhs = num1 - num2
if op2 == 0:
    rhs = rhs + num3
if op2 == 1:
    rhs = rhs - num3
print("Tell me the missing operators in this equation (only addition and substraction)\n")
print("Input the two operators in order without spaces (++, --, -+)\n")
answer = input(str(num1) + ' __ ' + str(num2) + ' __ ' + str(num3) + ' = ' + str(rhs) + '\n')
if len(answer)<= 2:
  if answer[0] == op_list[op1] and answer[1] == op_list[op2]:
    print("Correct!")
  else:
    print("Incorrect!")
else:
  answer = input("That was an invalid input. Please try again.")


print("Level Up! Try this harder one with 4 numbers!")
n_numbers = 4
list_numbers = []
list_operators = []
for kk in range(n_numbers):
    list_numbers.append(random.randint(1, 100))
for kk in range(n_numbers - 1):
    list_operators.append(op_list[random.randint(0, 2)])

list_numbers_new = list(list_numbers)
list_operators_new = list(list_operators)

while '*' in list_operators_new:
    idx = list_operators_new.index('*')
    res = list_numbers_new[idx] * list_numbers_new[idx + 1]
    list_numbers_new[idx] = res
    del list_numbers_new[idx + 1]
    del list_operators_new[idx]

rhs = list_numbers_new[0]
for kk in range(len(list_operators_new)):
    if list_operators_new[kk] == '+':
        rhs = rhs + list_numbers_new[kk + 1]
    elif list_operators_new[kk] == '-':
        rhs = rhs - list_numbers_new[kk + 1]

qn = ''
for kk in range(n_numbers):
    if kk <= n_numbers - 2:
        qn = qn + str(list_numbers[kk]) + ' __ '
    else:
        qn = qn + str(list_numbers[kk]) + ' = ' + str(rhs) + "\n"
print("Tell me the missing operators in this equation (addition, substraction, or multiplication)\n")
print("Input the three operators in order without spaces (+++, ---, +-+)\n")
answer = input(qn)
if len(answer)<= 3:
  for kk in range(n_numbers - 1):
    if answer[kk] == list_operators[kk]:
      if kk == n_numbers - 2:
        print("Correct!")
    else:
      print("Incorrect!  ")
      print("The correct answer is: " + str(list_operators))
else:
  answer = input("That was an invalid input. Please try again.")

print()
print("Level Up! Try this harder one with 5 numbers!")
n_numbers = 5
list_numbers = []
list_operators = []
for kk in range(n_numbers):
    list_numbers.append(random.randint(1, 100))
for kk in range(n_numbers - 1):
    list_operators.append(op_list[random.randint(0, 2)])

list_numbers_new = list(list_numbers)
list_operators_new = list(list_operators)


while '*' in list_operators_new:
    idx = list_operators_new.index('*')
    res = list_numbers_new[idx] * list_numbers_new[idx + 1]
    list_numbers_new[idx] = res
    del list_numbers_new[idx + 1]
    del list_operators_new[idx]


rhs = list_numbers_new[0]
for kk in range(len(list_operators_new)):
    if list_operators_new[kk] == '+':
        rhs = rhs + list_numbers_new[kk + 1]
    elif list_operators_new[kk] == '-':
        rhs = rhs - list_numbers_new[kk + 1]

qn = ''
for kk in range(n_numbers):
    if kk <= n_numbers - 2:
        qn = qn + str(list_numbers[kk]) + ' __ '
    else:
        qn = qn + str(list_numbers[kk]) + ' = ' + str(rhs) + "\n"
print("Tell me the missing operators in this equation (addition, substraction, or multiplication)\n")
print("Input the four operators in order without spaces (++++, ----, +-+-)\n")
answer = input(qn)

if len(answer)<= 4:
  for kk in range(n_numbers - 1):
    if answer[kk] == list_operators[kk]:
      if kk == n_numbers - 2:
        print("Correct!")
    else:
      print("Incorrect!")
      print("The correct answer is: ".join(list_operators))
else:
  answer = input("That was an invalid input. Please try again.")
print()
print()
print("Game over. Thanks for playing!")