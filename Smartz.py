class Smartz:
    def __init__(self, 
                 titel1="Übermensch", 
                 titel2="Untermensch",
                 voornaam1="Jeffrey", 
                 voornaam2="Tim-mmyyy", 
                 voornaam3="Cowboy Wesley Speed-Guns", 
                 voornaam4="Dunne Dennis de Dikkop",  
                 mietje="Status: Gaaaaaaayyy", 
                 hetero="Status: Vrouwenverslinder"):

        self.titel1 = titel1
        self.titel2 = titel2
        self.voornaam1 = voornaam1
        self.voornaam2 = voornaam2
        self.voornaam3 = voornaam3
        self.voornaam4 = voornaam4 
        self.mietje = mietje
        self.hetero = hetero

    def gamen1(self):
        print(" is aan het winnen met gamen.")

    def gamen2(self):
        print (" is hopeloos aan het verliezen met gamen")

    def vechten1(self):
        print(" is aan het winnen met vechten.")

    def vechten2(self):
        print(" zet zichzelf verschut in een gevecht")

    def versieren1(self):
        print(" is succesvol aan het versieren.")

    def versieren2(self):
        print(" loopt bont en blauwtjes bij de vrouwtjes.")

    def mietje(self):
        print("Status: Gaaaaaaayyy")

    def hetero(self):
        print("Status: Vrouwenverslinder")
        
class Übermensch(Smartz):
    pass

jeffrey = Übermensch("")
print(jeffrey.voornaam1 + " " + jeffrey.titel1)
print(jeffrey.hetero)
jeffrey.gamen1()
jeffrey.vechten1()
jeffrey.versieren1()

class Untermensch(Smartz):
    pass

timmy = Untermensch("")
print(timmy.voornaam2 + " " + timmy.titel2)
print(timmy.mietje)
timmy.gamen2()
timmy.vechten2()
timmy.versieren2()

class Untermensch(Smartz):
    pass

wesley = Untermensch("")
print(wesley.voornaam3 + " " + wesley.titel2)
print(wesley.mietje)
wesley.gamen2()
wesley.vechten2()
wesley.versieren2()

class Untermensch(Smartz):
    pass

dennis = Untermensch("")
print(dennis.voornaam4 + " " + dennis.titel2)
print(dennis.mietje)
dennis.gamen2()
dennis.vechten2()
dennis.versieren2()



