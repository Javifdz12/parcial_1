class libro:
    def __init__(self,num_paginas,genero,autor,editorial,titulo):
        generos=["NOVELA","NOVELA GRAFICA","NOVELA COMEDIA","NOVELA AVENTURAS","NOVELA CIENCIA FICCION","NOVELA ROMANTICA","NOVELA FANTASTICA"
        ,"CUENTO","MICRORELATO","ENSAYO","POESIA"]
        if isinstance(num_paginas,int):
            if num_paginas<0:
                num_paginas=input("numero de paginas incorrecto debe ser numero positivo: ")
                if isinstance(num_paginas,int):
                    if num_paginas<0:
                        self.num_paginas=0
                    else:
                        self.num_paginas=num_paginas
                else:
                    self.num_paginas=0
            else:
                self.num_paginas=num_paginas
        else:
            num_paginas=input(f"{num_paginas} no es un numero de paginas introduce entero positivo: ")
            if isinstance(num_paginas,int):
                    if num_paginas<0:
                        self.num_paginas=0
                    else:
                        self.num_paginas=num_paginas
            else:
                self.num_paginas=0
        if isinstance(genero,str) and genero.upper() in generos:
            self.genero=genero
        else:
            self.genero="genero"

        if isinstance(autor,str):
            self.autor=autor
        else:
            self.genero="autor"
        if isinstance(editorial,str):
            self.editorial=editorial
        else:
            self.editorial="autor"
        if isinstance(titulo,str):
            self.titulo=titulo
        else:
            self.titulo="titulo"
    def get_num_paginas(self):
        print(f"el numero de paginas es {self.num_paginas}")
    def get_genero(self):
        print(f"se trata de: {self.genero}")
    def get_autor(self):
        print(f"el autor es {self.autor}")
    def get_titulo(self):
        print(f"se titula: {self.titulo}")
    def get_editorial(self):
        print(f"la editorial es: {self.editorial}")
    def set_num_paginas(self):
        self.num_paginas=input("cuantas paginas tiene el libro: ")
    def set_genero(self):
        self.genero=input("cual es el genero del libro: ")
    def set_autor(self):
        self.autor=input("cual es el autor del libro: ")
    def set_titulo(self):
        self.titulo=input("cual es el titulo del libro: ")
    def set_editorial(self):
        self.editorial=input("cual es la editorial del libro: ")



libro1=libro(25,"novela aventuras","tu prima","sm","los cinco")
libro1.get_genero()
