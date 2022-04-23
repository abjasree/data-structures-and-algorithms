items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(stuff):
    number = 0
    print('Inventory:')
    for i,j in stuff.items():
          print(str(j)+' ' + i)
          number = number + j
    print('Total number of items: '+ str(number))

displayInventory(items)
            
