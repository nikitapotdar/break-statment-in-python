'''Game : Guess the number between 1 to 20 in 5 attempts

User to input any number between 1 to 20 and
if the number is equal to the number generated
by computer then user wins within 5 attempts.
If he does not input any number or consumes 5 tries
then he loses and the program ends.
'''
#Below is the code of the program
import random #random module to generate random number
print('Game to guess the number from 1 to 20 in 5 attempts')
tries = 5
CompNum = random.randint(1, 20)#randint(<start>, <end>) generates random number in given range
GuessNum = 0
cnt = 1 #counter for user tries
while GuessNum != CompNum and cnt <= tries:
      cnt += 1
      GuessNum = int(input("Try number 1 to 20 to play or 0 to quit: ") or 0)
      if GuessNum < 0 or GuessNum > 20:
            print('Sorry, out of range 1-20')
      elif GuessNum == CompNum or GuessNum == 0:
            break #here is the break statement, watch the condition
if GuessNum == CompNum:
      print('Congrats, you win')
elif GuessNum == 0:
      print('You have quit the game')
else:
      print('You tried your best, keep spirit up!')
print('Thanks for playing')
