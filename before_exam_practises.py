#1
myList = ["apple", "bannana", "grape"]

print(myList)

print(myList[1])
print(myList[-2])

myList.append("grapefruit")
print(myList)

myList.insert(1, "melon")
print(myList)

#2
myListX = ["apple", "bannana", "grape", "orange", "pineapple"]

print(myListX[0:2])
print(myListX[:2])
print(myListX[2:])

#3
mySentence = "jag heter Theodor och är Theodor"

print(mySentence)
print(mySentence[10:17])

#4
myListY = ["apple", "bannana", "grape", "orange", "pineapple"]

for x in myListY:
    print(x)
    if x == "bannana":
        break

#5
list = [1, 1, 2,3,5,8,13]
print(list[list[4]])

#6
for x in range(10):
    print(x)

#7
i=1
while i<6:
    print(i)
    i += 1

#8
def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))

#9
def e():
    print("ahhhhh")
    print("ahhhhhh 2")
e()
