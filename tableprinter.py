import copy

def printTable(list):
       columwidth = max(list,key = len)
       print(columwidth)
       word = max(columwidth,key = len)
       print(word)
       rightwidth = int(len(word))+5
       print(rightwidth)
       for i in range(len(list)):
            for j in list:
                print(j[i].rjust(rightwidth,' '), end=' ')
            print('\n')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)