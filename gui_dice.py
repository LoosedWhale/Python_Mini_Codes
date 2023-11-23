import random
from tkinter import *

class DICE: 
    def __init__(self, result):
        self.num = [1, 2, 3, 4, 5, 6]
        self.result = result
        self.Draw()


    def Dice(self):
        self.result = random.choice(self.num)
        self.Update()

    def Draw(self):
        self.label = Label(root, text="Tärningen visar: " + str(self.result), bg="white")
        self.label.pack()

        self.button = Button(root, text="Kasta tärning", command=self.Dice, bg="white")
        self.button.pack()

    def Update(self):
        self.label.config(text="Tärningen visar: " + str(self.result), bg="white")



root = Tk()
root.config(bg="white")
root.geometry("200x200")

root.title("Tärning")
    
Tärning = DICE(random.choice([1, 2, 3, 4, 5, 6]))


mainloop()
