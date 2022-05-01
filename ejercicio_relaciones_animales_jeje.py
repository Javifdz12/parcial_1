class animal:
    def __init__(self,tipo,reproduccion,sexo,especie,color):
        self.tipo=tipo
        self.reproduccion=reproduccion
        sexos=["masculino","femenino"]
        if sexo.lower() in sexos:
            self.sexo=sexo
        else:
            print("sexo incorrecto")
        self.especie=especie
        self.color=color
class mamifero(animal):
    def __init__(self,sexo,especie,color,reproduccion):
        animal.__init__(self,sexo,especie,color,reproduccion)
class ave(animal):
    def __init__(self,sexo,especie,color,reproduccion):
        animal.__init__(self,sexo,especie,color,reproduccion)
class oviparo(mamifero,ave):
    def __init__(self,sexo,especie,color):
        ave.__init__(self,sexo,especie,color)

class viviparo(mamifero):
    def __init__(self,sexo,especie,color):
        mamifero.__init__(self,sexo,especie,color)
class pato(oviparo):
    def __init__(self,especie,color,sexo,nombre):
        oviparo.__init__(self,especie,color,sexo)
        self.nombre = nombre

class gato(viviparo):
    def __init__(self,especie,color,sexo,nombre):
        viviparo.__init__(self,especie,color,sexo)
        self.nombre = nombre
class ornitorrinco(oviparo):
    def __init__(self,sexo,color,nombre):
        oviparo.__init__(self,color,sexo)
        self.nombre = nombre

