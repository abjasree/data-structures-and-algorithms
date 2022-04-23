import re
phonenumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumber.search('my number is 444-454-5343')
print('Phone number found: '+ mo.group())
