import sys
import random
number = random.randint(1,20)

print('I am thinking of a number between 1 and 20')
print('Take a guess')

for i in range(1,6):
 x = int(input())
 if x < number:
    print('Your guess is too low, Take a guess')
 elif x > number:
    print('Your guess is too high, Take a guess')
 else:
     break
    
if x == number:
    print('good job!', 'You have guessed my number in '+ str(i)+'th time')
else:
    print('The number I have been guessing is '+ str(number))

sys.exit()
