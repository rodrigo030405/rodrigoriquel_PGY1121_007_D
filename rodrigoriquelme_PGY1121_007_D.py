#examen transversal
import funciones as fn 
import numpy
import os
import time
import msvcrt
asientos=numpy.zeros((10,10), int)
lista_ruts=[]
lista_asist=[]
lista_filas=[]
lista_columna=[]

while True:
    os.system('cls')
    fn.ver_menu()
    opcion=fn.validar_opcion()

    if opcion==1:
        fn.comprar_entradas()
    elif opcion==2:
        fn.buscar()
        time.sleep(7)
    elif opcion==3:
        fn.ver_asientos()
        time.sleep(10)
    elif opcion==4:
        fn.valor_total()
    elif opcion==5:
        fn.salir()
        break