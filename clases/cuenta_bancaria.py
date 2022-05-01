import datetime
class cuenta_bancaria:

    def __init__(self, titular,fondos,fecha_apertura,ID,numero_cuenta):
        if isinstance(titular,str):
            self.titular=titular
        else:
            self.titular="nombre"
        if isinstance(fondos,float):
            self.fondos=fondos
        else:
            self.fondos=0
        if len(fecha_apertura)==8:
            fecha_apertura=datetime.datetime.strptime(fecha_apertura,"%d%m%Y")
            self.fecha_apertura=fecha_apertura
        else:
            print("fecha de apertura de cuenta no existe")
        if 999999999999>=numero_cuenta>=100000000000:
            self.numero_cuenta=numero_cuenta
        else:
            print("numero de cuenta incorrecto, debe tener 12 numeros")
        self.ID=ID

    def imprimir(self):
        print("el cliente",self.titular,"tiene",self.fondos)

    def ingresar(self,x):
        if x<0:
            print("cantidad erronea")
        else:
            self.fondos=x+self.fondos
            print("ahora tienes",self.fondos)

    def retirar(self,y):
        if y>self.fondos:
            print("retirada cancelada")
        elif y<0:
            print("cantidad erronea")
        else:
            self.fondos=self.fondos-y
            print("te quedan",self.fondos)

    def transferir(self,cantidad,cuenta):
        if cantidad>self.fondos:
            print("no es posible hacer la transferencia")
        else:
            cuenta.fondos=cuenta.fondos+cantidad
            self.fondos=self.fondos-cantidad
            print(f'has transferido {cantidad} a {cuenta.titular}')




class cuenta_bancaria_vip:

    def __init__(self, titular,fondos,fecha_apertura,ID,numero_cuenta):
        if isinstance(titular,str):
            self.titular=titular
        else:
            self.titular="nombre"
        if isinstance(fondos,float):
            self.fondos=fondos
        else:
            self.fondos=0
        if len(fecha_apertura)==8:
            fecha_apertura=datetime.datetime.strptime(fecha_apertura,"%d%m%Y")
            self.fecha_apertura=fecha_apertura
        else:
            print("fecha de apertura de cuenta no existe")
        if 999999999999>=numero_cuenta>=100000000000:
            self.numero_cuenta=numero_cuenta
        else:
            print("numero de cuenta incorrecto, debe tener 12 numeros")
        self.ID=ID

    def imprimir(self):
        print("el cliente",self.titular,"tiene",self.fondos)

    def ingresar(self,x):
        if x<0:
            print("cantidad erronea")
        else:
            self.fondos=x+self.fondos
            print("ahora tienes",self.fondos)

    def retirar(self,y):
        if y>(self.fondos+1000):
            print("retirada cancelada")
        elif y<0:
            print("cantidad erronea")
        else:
            self.fondos=self.fondos-y
            print("te quedan",self.fondos)

    def transferir(self,cantidad,cuenta):
        if cantidad>self.fondos:
            print("no es posible hacer la transferencia")
        else:
            cuenta.fondos=cuenta.fondos+cantidad
            self.fondos=self.fondos-cantidad
            print(f'has transferido {cantidad} a {cuenta.titular}')

class cuenta_bancaria_plazofijo:

    def __init__(self, titular,fondos,fecha_apertura,fecha_vencimiento,ID,numero_cuenta):
        if isinstance(titular,str):
            self.titular=titular
        else:
            self.titular="nombre"
        if isinstance(fondos,float):
            self.fondos=fondos
        else:
            self.fondos=0
        if len(fecha_apertura)==8 and len(fecha_vencimiento)==8:
            fecha_apertura=datetime.datetime.strptime(fecha_apertura,"%d%m%Y")
            self.fecha_apertura=fecha_apertura
            fecha_vencimiento=datetime.datetime.strptime(fecha_vencimiento,"%d%m%Y")
            if fecha_apertura<fecha_vencimiento:
                self.fecha_vencimiento=fecha_vencimiento
            else:
                print("fecha de vencimiento invalida")
        else:
            print("fecha no existe")

        if 999999999999>=numero_cuenta>=100000000000:
            self.numero_cuenta=numero_cuenta
        else:
            print("numero de cuenta incorrecto, debe tener 12 numeros")
        self.ID=ID

    def imprimir(self):
        print("el cliente",self.titular,"tiene",self.fondos)

    def ingresar(self,x):
        if x<0:
            print("cantidad erronea")
        else:
            self.fondos=x+self.fondos
            print("ahora tienes",self.fondos)

    def retirar(self,y,fecha_retiro):
        fecha_retiro=datetime.datetime.strptime(fecha_retiro,"%d%m%Y")
        if fecha_retiro<self.fecha_vencimiento:
            if y+(y*0.05)>self.fondos:
                print("retirada cancelada")
            elif y<0:
                print("cantidad erronea")
            else:
                self.fondos=self.fondos-(y+(y*0.05))
                print("te quedan",self.fondos)
        else:
            if y>(self.fondos+1000):
                print("retirada cancelada")
            elif y<0:
                print("cantidad erronea")
            else:
                self.fondos=self.fondos-y
                print("te quedan",self.fondos)

    def transferir(self,cantidad,cuenta):
        if cantidad>self.fondos:
            print("no es posible hacer la transferencia")
        else:
            cuenta.fondos=cuenta.fondos+cantidad
            self.fondos=self.fondos-cantidad
            print(f'has transferido {cantidad} a {cuenta.titular}')


cuenta_1=cuenta_bancaria("javi",10000.0,"02042022",1234,34567883632)
cuenta_2=cuenta_bancaria_vip("pepe",10000.0,"23102021",3456,678909876555)
cuenta_3=cuenta_bancaria_plazofijo("andres",10000.0,"12051975","24092002",3456,345267354898)
cuenta_1.imprimir()
cuenta_1.ingresar(575)
cuenta_1.retirar(78)
cuenta_1.imprimir()
cuenta_1.transferir(2000,cuenta_2)
cuenta_1.imprimir()
cuenta_2.retirar(78)
cuenta_2.imprimir()
cuenta_2.ingresar(575)
cuenta_2.imprimir()
cuenta_2.transferir(2000,cuenta_3)
cuenta_2.imprimir()
cuenta_3.imprimir()
cuenta_3.retirar(2000,"23092002")
cuenta_3.retirar(5000,"25092002")
