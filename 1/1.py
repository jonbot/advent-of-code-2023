import re

# Get the text input.
def getText():
    lines = []
    with open('input.txt') as fp:
        contents = fp.read()
        lines = contents.split('\n')
    return lines

# Get the first digit in a string.
def getDigit(txt):
    match = re.search('[0-9]', txt)
    return match.group()

# Do the stuff.
txt = getText()

total = 0
for line in txt:
    combinedNumber = getDigit(line) + getDigit(line[::-1])
    total += int(combinedNumber)

print(total)


