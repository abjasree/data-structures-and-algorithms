import sys
import pyperclip
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
import sys, pyperclip
if len(sys.argv) < 2:
 print('Usage: py pw.py [account] - copy account password')
 sys.exit()
account = sys.argv[1] # first command line arg is the account name
if account in PASSWORDS:
 pyperclip.copy(PASSWORDS[account])
 print('Password for ' + account + ' copied to clipboard.')
else:
 print('There is no account named ' + account + '\n' +'If you want to save new enter: savenew ')
 enter = input()
 if enter == 'savenew':
     print('Enter the password to be saved for '+ account)
     password = input()
     PASSWORDS.setdefault(account,password)
     print('The password for the '+account+' is successfully saved')

