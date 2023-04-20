#main.py

names = ["George Washington", "Thomas Jefferson", "John Adams", "John Kennedy", "Herbert Hoover", "Ronald Reagan"]
print(len(names))
print(names[0:2]) #what ? the zeroth and first elements
nameSplit = [(name.upper()).split(" ") for name in names] #splits on the space #creates sub-lists or nested lists
print(nameSplit)

# Use a brute-force loop to replicate the results of the above List Comprehension
finalList = [] #creates empty list
for name in names:
    #Split on the space into a new 2-element list
    newList = name.split(" ")
    #print(newList)
    finalList.append(newList)
print(finalList)

#    A new list of lists such that last name precedes first name
lastFirst = [name.split()[::-1] for name in names]
print(lastFirst)