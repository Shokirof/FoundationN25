from os import system
system("cls")


class Saylov:
    def __init__(self, nomzodlar):
        self.nomzodlar = nomzodlar
        self.ovozlar = {nomzod: 0 for nomzod in nomzodlar}
        self.saylovchilar = {}

    def ovoz_berish(self, passport_seriya, nomzod):
        if passport_seriya in self.saylovchilar:
            print("Siz allaqachon ovoz berib bo'lgansiz!")
        elif nomzod in self.nomzodlar:
            self.ovozlar[nomzod] += 1
            self.saylovchilar[passport_seriya] = nomzod
            print(f"{passport_seriya} passport seriya egasi {nomzod}ga ovoz berdi!")
        else:
            print("Bunday nomzod mavjud emas!")

    def saylov_yakunlandi(self):
        natija = sorted(self.ovozlar.items(), key=lambda x: x[1], reverse=True)
        for nomzod, ovoz in natija:
            print(f"{nomzod}: {ovoz} ta ovoz")
        Max = 0
        golib = ""
        for x, y in natija:
            if y > Max:
                Max = y
                golib = x
        print(f"{golib} 2023-yilgi saylovda {Max} ta ovoz bilan Prezidentlikka saylandi")


saylov = Saylov(["Shavkat Mirziyoyev", "Ulug'bek Inoyatov", "Robaxon Mahmudova", "Abdushukur Hamzayev"])
saylov.ovoz_berish("AC148653", "Shavkat Mirziyoyev")
saylov.ovoz_berish("AA669874", "Robaxon Mahmudova")
saylov.ovoz_berish("AD589632", "Ulug'bek Inoyatov")
saylov.ovoz_berish("AC865539", "Shavkat Mirziyoyev")
saylov.ovoz_berish("BC652655", "Shavkat Mirziyoyev")
saylov.ovoz_berish("AC148653", "Islom Karimov")
saylov.saylov_yakunlandi()
