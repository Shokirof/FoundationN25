import os
class Saylov:
    def __init__(self, nomzodlar):
        self.nomzodlar = nomzodlar
        self.ovoz = {nomzod: 0 for nomzod in nomzodlar}
        self.ovoz_beruvchilar = {}

    def saylash(self, jshir, pasport_seriyasi, nomzod):
        if pasport_seriyasi in self.ovoz_beruvchilar:
            print("Siz ovoz bergansiz!")
        elif nomzod in self.nomzodlar:
            self.ovoz[nomzod] += 1
            self.ovoz_beruvchilar[jshir] = nomzod
            print(f"Jshir: {jshir} va Pasport seriyasi: {pasport_seriyasi} nomli saylovchi {nomzod} ga ovoz berdi!")
        else:
            print("Nomzod yo'q")

    def get_result(self):
        results = sorted(self.ovoz.items(), key=lambda x: x[1], reverse=True)
        for nomzod, ovoz in results:
            print(f"{nomzod}: {ovoz} ta ovoz")

electron = Saylov(["Shavkat Mirziyoyev", "Ulug'bek Inoyatov", "Robaxon Mahmudova"])
electron.saylash(14586984123457, "AC1486553", "Shavkat Mirziyoyev")
electron.saylash(23698142576322, "AA66987411", "Robaxon Mahmudova")
electron.saylash(142597836441121, "AD58963221", "Ulug'bek Inoyatov")
electron.get_result()