#funciones
import numpy
import os
import time
import msvcrt
asientos=numpy.zeros((10,10), int)
lista_filas=[]
lista_columna=[]
lista_ruts=[]
lista_asist=[]
contador_platinum=0
contador_gold=0
contador_silver=0
acumulador_p=0
acumulador_g=0
acumulador_s=0
precio_p=120000
precio_g=80000
precio_s=50000
def ver_menu():
    print(""" 
    bienvenido a Creativos.cl
    menu del concierto de michael jam
    1. comprar entradas
    2. mostrar ubicaciones disponibles
    3. ver listado de asistentes
    4. mostrar ganancias totales
    5. salir""" )

def validar_opcion():
        while True:
            try:
                opcion=int(input("ingrese una opcion: "))
                if opcion in(1,2,3,4,5):
                    return opcion
                else:
                    print( "error, ingrese una opcion valida")
                    time.sleep(3)
            except:
                print("error, ingrese un numero entero")
                time.sleep(3)

def salir():
    print("""
    gracias por su preferencia, vuelva pronto
    atten: rodrigo riquelme
    06/07/2023""")
    return
def validar_rut():
    while True:
        try:
            rut=int(input("ingrese su rut sin guion, puntos ni digito verificador: "))
            if rut>1000000 and rut< 99999999:
                return rut
            else:
                print("error, ingrese el rut correcto nuevamente")
                time.sleep(3)
        except:
            print("ERROR ingrese un numero entero")
            time.sleep(3)

def cant_entradas():
    while True:
        try:
            entradas=int(input("ingrese la cantidad de entradas: "))
            if entradas>=1 and entradas<=3:
                return entradas
            else:
                print("error, cantidad no especificada correctamente")
                time.sleep(3)
        except:
            print("error, ingrese un numero entero")
            time.sleep(3)

def ver_asientos():
    for x in range(10):
        print(f"fila{x+1}",end="  ")
        for y in range(10):
            print(asientos[x][y], end=" ")
        print()  
    print("columna 1 2 3 4 5 6 7 8 9 10")  
        
def comprar_entradas():
    contador_platinum=0
    contador_gold=0
    contador_silver=0
    acumulador_p=0
    acumulador_g=0
    acumulador_s=0
    precio_p=120000
    precio_g=80000
    precio_s=50000
    entrada=cant_entradas()
    rut=validar_rut()
    cedula=validar_carnet()
    ver_asientos()
    ver_precios()
    fila=validar_fila()
    columna=validar_columna()
        
    if fila>=1 and fila<=2:
        print("precio a pagar es: ",precio_p) 
        contador_platinum=contador_platinum+entrada
        acumulador_p=acumulador_p+precio_p
        time.sleep(3)
        
    elif fila>=3 and fila<=5:
        print("precio a pagar es: ",precio_g)
        
        contador_gold=contador_gold+entrada
        acumulador_g=acumulador_g+precio_g
    else:
        print("precio a pagar es: ",precio_s)  
        acumulador_s=acumulador_s+precio_s
        contador_silver=contador_silver+entrada   
    
    if asientos[fila-1][columna-1]==0:
        asientos[fila-1][columna-1]=="x"
        lista_ruts.append(rut)
        lista_asist.append(cedula)
        lista_filas.append(fila-1)
        lista_columna.append(columna-1)
        print("compra finalizada")
        time.sleep(3)
        return   
    else:
        print("error, asiento no disponible")
        time.sleep(3)
    
        

def ver_precios():
    print(f"""
    Platinum, ${precio_p}. (Asientos del 1 al 20)
    Gold      ${precio_g}. (Asientos del 21 al 50)
    Silver    ${precio_s}.  (Asientos del 51 al 100)""")



def buscar():
    print(lista_ruts.sort())
    print(lista_asist.sort())
    rut=validar_rut()
    if rut in lista_ruts:
        posicion=lista_ruts(rut)
        print("el asistente que busca es: ",lista_asist(posicion))
    else:
        print("el asistente no existe")    
def validar_fila():
    while True:
        try:
            fila=int(input("ingrese la fila de su preferencia: "))
            if fila<=10 and fila>=1:
                return fila
            else:
                print("error, fila inexistente")
        except:
            print("error, ingrese nu numero entero")  

def validar_carnet():
    while True:
        try:
            carnet=int(input("ingrese su cedula de identidad(sin puntos ni guion): "))
            if carnet<999999999 and carnet>100000000:
              return
            else:
                print("error, cedula no valida")
        except:
            print("error, ingrese un numero entero")

def valor_total():
   print(f"""
   _________________________________________________________
   |   tipo entrada  |      cantidad       |      total    |
   | platinum $120000|{contador_platinum}                            {acumulador_p}
   | gold     $80000 |{contador_gold}                            {acumulador_g}
   | silver   $50000 |{contador_silver}                            {acumulador_s}
   |_________________|_____________________|_______________|""")
   time.sleep(10)
   
def validar_columna():
    while True:
        try:
            columna=int(input("ingrese la columna de su preferencia: "))
            if columna<=20 and columna>=1:
                return columna
            else:
                print("error, columna inexistente")
        except:
            print("error, ingrese nu numero entero")   

   