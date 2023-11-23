#1

thisdict = {
'CoD': 'Activision',

'Skyrim': 'Bethesda',

'Overwatch': 'Blizzard',

'GTA': 'RockStar',

'Castlevania': 'Konami',

'Resident Evil': 'Capcom',

'HALO 3': 'Bungie',

'Battlefield': 'DICE',

'Gears of War': 'Epic Games',

'FallOut': 'Interplay Entertainment'
}



for keys, value in thisdict.items():
   print(keys)

#2

gameList = ['Call of Duty', 'Skyrim', 'Overwatch', 'GTA', 'Castlevania', 'Resident Evil', 'HALO', 'Battlefield', 'Gears of War', 'FallOut']
gameList.sort()

uppercase_gamelist = [x.upper for x in gameList]

def igen():
    again = input("Vill du söka på ett spel?")
    if again.lower() == "ja":
        print("Sure!")
    if again.lower() == "nej":
        print("okej!")
        return
      
def addGame(addNew):
    add = input("Vill du lägga till spelet?")
    if add.lower() == "ja":
        gameList.append(addNew.title())
        gameList.sort()
        print(gameList)
        igen()
    else:
        print("Lägger inte till den :I")
    igen()

def searchGame(newGame):
    if newGame.upper() in uppercase_gamelist:
        print("Det finns i listan!")
        return True
    else:
        print("Det finns inte i listan...")
        return False
      
def start():
    search = input("Vilket spel söker du?")
    if searchGame(search) == False:
        addGame(search)

start()
