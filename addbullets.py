import pyperclip
text = pyperclip.paste()

# to do to the text
lines = text.split('.')
for i in range(len(lines)):
    lines[i] = '* '+lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)