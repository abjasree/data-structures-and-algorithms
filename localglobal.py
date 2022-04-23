def spam():
 eggs = 'spam local'
 print(eggs)

def bacon():
 eggs = 'bacon local'
 print(eggs) # prints 'bacon local'
 spam()
 

 
eggs = 'global'
bacon()
spam()
print(eggs)
