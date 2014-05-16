teststring = ""
searchchar = ""
charlist = []
lastposition = -1

while teststring == "":
    teststring = input("please enter some text to search :")

while len(searchchar)!=1:
    searchchar = input("enter a character to search for :")
    chosenchar = input("what would you like to change the character to")

for x in range (len(teststring)):
    if teststring[x] == searchchar:
        teststring = teststring[:x] + chosenchar + teststring[x+1:]

print()
print(teststring)


