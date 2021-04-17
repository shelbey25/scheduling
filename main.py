from treeSorting import *

listOfWatnedClasses = []
UXFriendlyList = []
listOfNeededClasses = []

userBreak = False

masterListM = returnMasterList()

while not userBreak:
    print("Enter wanted class name or STOP to stop")
    userInput = input()
    if userInput == "STOP":
        userBreak = True
    else:
        try:
            z = masterListM[userInput]
            UXFriendlyList.append(userInput)
            listOfWatnedClasses.append(z)
            print("CLASS ADDED")
        except KeyError:
            print("INVALID CLASS")

print("Your final list is:")
print(UXFriendlyList)

def fullSearchWithPres(className):
    l = initSearch(className)
    return findHighestPres(turnTreeLeaves(l))

for i in UXFriendlyList:
    y = fullSearchWithPres(i)
    for b in y:
        if b in listOfNeededClasses:
            pass
        else:
            listOfNeededClasses.append(b)

print(listOfNeededClasses)
