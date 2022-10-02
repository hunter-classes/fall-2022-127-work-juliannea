myList = []
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList = myList + [True]
myList = myList + [4]
myList = myList + [76]

myList.append('apple')

myList.append(76)

myList[3:3] = ['cat']

myList[0:0] = [99]

index = myList.index("hello")
print(index)

print(myList.count(76))


print(myList)

myList[1:2] = []
print(myList)

myList.pop(4)
print(myList)
