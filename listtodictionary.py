def addToInventory(inventory, addedItems):
  total = 0
  for i in addedItems:
      if i not in inventory.keys():
        inventory.setdefault(i,0)
        inventory[i] = inventory[i]+1
      else:
          inventory[i] = inventory[i]+1
  print('Inventory:')
  for l,m in inventory.items():
      total += m
      print(str(m)+' '+l)
  print('total number of items: '  + str(total))
        
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
   
