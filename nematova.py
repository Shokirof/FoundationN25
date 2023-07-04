import os
os.system("cls")


class telefon:
    def __init__(self):
        self.model = ""
        self.color = ""
        self.memory = 0

    def input_data(self):
        self.model = input("Telefon modelini kiriting: ")
        self.color = int(input("Telefon narxini kiriting: "))
        self.memory = int(input("Telefon xotira hajmini kiriting: "))

    def show(self):
        print("Rangi: ", self.color)
        print("Modeli: ", self.model)
        print("Xotirasi: ",self.memory)


t = telefon()
t.input_data()
t.show()
