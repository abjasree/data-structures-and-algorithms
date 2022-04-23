import sys
def collatz(number):
 if number % 2 == 0:
   x = number // 2
   print(x)
 else:
  x = 3*number+1
  print(x)
 if x == 1:
    sys.exit()
 else:
    number = x
    collatz(x)

print('Enter a number')
try:
 number = int(input())
 collatz(number)
except ValueError:
    print('Input Invalid')
 
 
    

