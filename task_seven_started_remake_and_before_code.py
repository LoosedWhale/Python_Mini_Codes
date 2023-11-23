#Before
WorkersFood = {
    "Emil": "Röd Pölse",
    "Andreas": "Köttbullar med mos",
    "Mikael": "Resturang mat",
    "Kenneth": "Resturang mat",
}

EmilEnergy = int(800 * (2.5*60))
AndreasEnergy = int(800 * (3.5*60))
MikealEnergy = int(600 * (0.5*60))
KennethEnergy = int(600 * (0.5*60))


EmilPrice = 0.8 * (2.5/60) * 1.89
AndreasPrice = 0.8 * (3.5/60) * 1.89
MikealPrice = 0.8 * (0.5/60) * 1.89
KennethPrice = 0.8 * (0.5/60) * 1.89

def checkWorkersForFood():
    worker = input("Vilken arbetare vill välja\n")
    if worker == "Emil":
        print(WorkersFood["Emil"])
    elif worker == "Andreas":
        print(WorkersFood["Andreas"])
    elif worker == "Mikeal":
        print((WorkersFood["Mikael"]))
    elif worker == "Kenneth":
        print((WorkersFood["Kenneth"]))
    else:
        print("Den här personen jobbar inte här och får då ingen mat (Endast personal).\nKolla så att du skrev in namnet rätt\n")


def foodToEnergy():
    print("Kollar energi det tar att tillaga maten")
    workerOrFood = input("\n 1. Är du arbetare? \n 2. Välj egen maträtt\n")
    if workerOrFood == "1":
        whichWorker = input("\n 1. Emil \n 2. Andreas \n 3. Mikeal \n 4. Kenneth \n")
        if whichWorker == "1":
            print(str(EmilEnergy) + "J")
        elif whichWorker == "2":
            print(str(AndreasEnergy) + "J")
        elif whichWorker == "3":
            print(str(MikealEnergy) + "J")
        elif whichWorker == "4":
            print(str(KennethEnergy) + "J")
        else:
            print("Felaktig inskrivet.. du måste skriva 1 eller 2 osv")
    elif workerOrFood == "2":
        choiceFood = input("\n 1. Röd pölse \n 2. Köttbullar med mos\n 3. Resturang mat \n")
        if choiceFood == "1":
            print(str(EmilEnergy) + "J")
        elif choiceFood == "2":
            print(str(AndreasEnergy) + "J")
        elif choiceFood == "3":
            print((str(MikealEnergy) + "J"))


def costOfMicrowaving():
    costOfFood = input("\n 1. Är du arbetare? \n 2. Välj egen maträtt\n")
    if costOfFood == "1":
        workerCost = input("\n 1. Emil \n 2. Andreas \n 3. Mikeal \n 4. Kenneth \n")
        if workerCost == "1":
            print(str(EmilPrice) + "Kr")
        elif workerCost == "2":
            print(str(AndreasPrice) + "Kr")
        elif workerCost == "3":
            print(str(MikealPrice) + "Kr")
        elif workerCost == "4":
            print(str(KennethPrice) + "Kr")
        else:
            print("Felaktig inskrivet.. du måste skriva 1 eller 2 osv")
    elif costOfFood == "2":
        foodChoiceCost = input("\n 1. Röd pölse \n 2. Köttbullar med mos\n 3. Resturang mat \n")
        if foodChoiceCost== "1":
            print(str(EmilPrice) + "Kr")
        elif foodChoiceCost == "2":
            print(str(AndreasPrice) + "Kr")
        elif foodChoiceCost == "3":
            print((str(MikealPrice) + "Kr"))


def meny():
    question = (input("\n 1. Kolla arbetares mat \n 2. Energi det tar att värma matten \n 3. Kostnad i kroner för mat uppvärmningen \n 4. Avsluta programmet\n"))
    if question == "1":
        checkWorkersForFood()
        meny()
    elif question == "2":
        foodToEnergy()
        meny()
    elif question == "3":
        costOfMicrowaving()
        meny()
    elif question == "4":
        print("Avslutar...")
        return
    else:
        print("\n HALLÅ? va håller du på med detta var inte med i valen du fick.\n Valen var 1 2 3 4 \n är är du och skriver in allt annat än det.. \n *Arg microwave noises* \n")
        meny()
meny()

#Started on after
class Worker:
    def __init__(self, name, food, watt, time):
        self.name = name
        self.food = food
        self. watt = watt
        self.time = time

class Microwave:
    def __init__(self, price):
        self.price = price

    def calculate(self, price):
        self.price = price


