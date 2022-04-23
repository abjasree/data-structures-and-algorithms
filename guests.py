name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have')
numofguests = int(input())
if numofguests: #if numofguest is not 0 then the condition is true
    print('Be sure to have enough rooms for all your guests')
else :
    print('please enter a valid number')
print('Done')
