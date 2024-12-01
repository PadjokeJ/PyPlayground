import os


def ShowHangman(s):
    if s == 8:
        r = "_________\n|/      |\n|       0\n|      /|\ \n|      / \ \n|.,,.,..,..,..,.,..,,."
    if s == 7:
        r = "_________\n|/      |\n|       0\n|      /|\ \n|       / \n|.,,.,..,..,..,.,..,,."
    if s == 6:
        r = "_________\n|/      |\n|       0\n|      /|\ \n|       \n|.,,.,..,..,..,.,..,,."
    if s == 5:
        r = "_________\n|/      |\n|       0\n|      /| \n|        \n|.,,.,..,..,..,.,..,,."
    if s == 4:
        r = "_________\n|/      |\n|       0\n|       | \n|        \n|.,,.,..,..,..,.,..,,."
    if s == 3:
        r = "_________\n|/      |\n|       0\n|       \n|        \n|.,,.,..,..,..,.,..,,."
    if s == 2:
        r = "_________\n|/      |\n|       \n|       \n|        \n|.,,.,..,..,..,.,..,,."
    if s == 1:
        r = "\n|      \n|       \n|       \n|       \n|.,,.,..,..,..,.,..,,."
    if s == 0:
        r = "\n\n\n\n\n.,,.,..,..,..,.,..,,."
    print(r)
print("Enter a word")
word = input()
def Clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
Clear()
length = len(word)
w =[""]
for l in word:
    w.append(l)
field = [""]
for i in range(length):
    field.append("_")
def ShowField(f):
    d_field = ""
    for letter in f:
        d_field = d_field + letter + " "
    print("\n" + d_field)
game = True
hangStep = 0
tested = ""
while game:
    Clear()
    ShowHangman(hangStep)
    ShowField(field)
    testLetter = input(tested)
    i = 0
    hasFound = False
    for l in w:
        if l == testLetter:
            field.insert(i, testLetter)
            field.pop(i + 1)
            hasFound = True
        i += 1
    if hasFound != True:
        hangStep += 1
        tested = tested + testLetter
    if hangStep == 8:
        game = False
        Clear()
        ShowHangman(hangStep)
        ShowField(field)
        print ("correct word was " + word)
        print(">>>>YOU LOSE<<<<")
        break
    left = 0
    for l in field:
        if l == "_":
            left += 1
    if left == 0:
        game = False
        Clear()
        ShowHangman(hangStep)
        ShowField(field)
        print(">>>>YOU WIN<<<<")
        break
exit()