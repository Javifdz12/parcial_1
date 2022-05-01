from clases.libro import libro
from clases.cuenta_bancaria import cuenta_bancaria,cuenta_bancaria_vip,cuenta_bancaria_plazofijo

if __name__ == '__main__':
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

    libro1=libro(25,"novela aventuras","tu prima","sm","los cinco")
    libro1.descripcion()