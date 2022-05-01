class animal:
    def __init__(self,tipo,reproduccion):
        self.tipo=tipo
        self.reproduccion=reproduccion
class mamifero:
    print("soy mamifero")
class ave:
    print("soy un ave")
class oviparo:
    print("soy oviparo")
class viviparo:
    print("soy viviparo")
class pato(animal):
    def __init__(self,tipo,reproduccion,especie,color):
        animal.__init__(self,tipo,reproduccion)
        self.especie=especie
        self.color=color

class gato(animal):
    def __init__(self,tipo,reproduccion,especie,color):
        animal.__init__(self,tipo,reproduccion)
        self.especie=especie
        self.color=color
class ornitorrinco(animal):
    def __init__(self,tipo,reproduccion,color):
        animal.__init__(self,tipo,reproduccion)
        self.color=color

pato1=pato(ave(),oviparo(),"anatida","verde")
#gato1=gato(mamifero(),viviparo(),"egipcio","rosa")
#ornitorrinco1=ornitorrinco(mamifero(),oviparo(),"marron")