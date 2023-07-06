import os
os.system("cls")
class electron_saylov:
    def __init__(self):
        self._passport=None
        self._password=None
        self._name=None
        self._surname=None
        self._brithday=None
        self._adress=None
        self._age=None
        self._saylovchilar=list()
        self._ovozlar={"Shavkat Miromonovich MIRZIYOYEV":0,"Ulug‘bek Ilyasovich INOYATOV":0,"Robaxon Anvarovna MAXMUDOVA":0,"Abdushukur Xudoyqulovich XAMZAYEV":0}

    def sign_up_admin(self):
        n=int(input("Saylovchilar sonini kiriting: "))
        x=0
        while x<n:
            print(f"{x+1}-saylovchining ma'lumotlarini kiriting")
            self._name=input("Saylovchining ismini kiriting: ")
            self._surname=input("Saylovchining familiyasini kiriting: ")
            self._age=int(input("Saylovchining yoshini kiriting: "))
            self._brithday=input("Saylovchining tug'ulgan kunini kiriting: ")
            self._passport=input("Saylovchining passport raqami va seriyasini kiriting: ")
            self._password=input("Saylovchining JSHSHIRni kiriting: ")
            self._adress=input("Saylovchining manzilini kiriting: ")
            self._saylovchilar.append([self._passport,self._password,self._name,self._surname,self._brithday,self._adress,self._age])
            x+=1
    def show_info(self):
        password=input("Saylovchining ma'limotlarini ko'rish uchun uning JSHSHIRni kiriting: ")
        for x in self._saylovchilar:
            if x[1]==password:
                print(f"""\t\t\tSaylovchining ma'lumotlari\n\t\tIsmi: {x[2]}\n\t\tFamiliyasi: {x[3]}\n\t\tYoshi: {x[6]}\n\t\tTug'ulgan sanasi: {x[4]}\n\t\tManzili: {x[5]}\n\t\tPassporti: {x[0]}""")
    def saylov(self):
        ovoz=int(input("Ovoz beruvchilar sonini kiriting: "))
        while ovoz:
            password=input("JSHSHIRni kiriting: ")
            passport=input("Passport seriyasini va raqamini kiriting: ")
            for x in self._saylovchilar:
                print(len(x))
                if x[0]==passport and x[1]==password and len(x)<8:
                    print("Nomzodlardan birini tanlang:\n\t\t1.Shavkat Miromonovich MIRZIYOYEV\n\t\t2.Ulug‘bek Ilyasovich INOYATOV\n\t\t3.Robaxon Anvarovna MAXMUDOVA\n\t\t4.Abdushukur Xudoyqulovich XAMZAYEV")
                    temp=int(input())
                    match(temp):
                        case 1:
                            self._ovozlar["Shavkat Miromonovich MIRZIYOYEV"]+=1
                            print("Siz Shavkat Miromonovich MIRZIYOYEV ovoz berdingiz")
                        case 2:
                            self._ovozlar["Ulug‘bek Ilyasovich INOYATOV"]+=1
                            print("Siz Ulug‘bek Ilyasovich INOYATOV ovoz berdingiz")
                        case 3:
                            self._ovozlar["Robaxon Anvarovna MAXMUDOVA"]+=1
                            print("Siz Robaxon Anvarovna MAXMUDOVA ovoz berdingiz")
                        case 4:
                            self._ovozlar["Abdushukur Xudoyqulovich XAMZAYEV"]+=1
                            print("Siz Abdushukur Xudoyqulovich XAMZAYEV ovoz berdingiz")
                        case _:
                            print("Bunday nomzod mavjud emas")
                    x.append(" ")
                    ovoz-=1
                else: 
                    print("Siz JSHSHIRni,passport raqamni yoki ovoz beib bo'lgansiz xato kiritdingiz")
    def saylov_natijasi(self):
        print("\t\t\tSaylov natijalari")
        for x in self._ovozlar:
            print(f"\t\t{x}: {self._ovozlar[x]}")

s=electron_saylov()
s.sign_up_admin()
os.system("cls")
s.saylov()
os.system("cls")
s.show_info()
s.saylov_natijasi()