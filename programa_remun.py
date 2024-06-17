from os import system
lista_trabajador=[]
def menu_principal():
    opciones = {
        '1': ('registrar trabajador', reg_trabajador),
        '2': ('listar todos los trabajadores', listar_trabajador),
        '3': ('imprinir planilla de sueldos', imprimir_trabajador),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        #print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def reg_trabajador():
    print('Has elegido la opción 1')
    nombre_trabajador=(input("ingrese el nombre y apellido de l trabajador: "))
    cargo_trabajador=(input("ingrese cargo del trabajador: "))
    sueldo_trabajador=(int(input("ingrese el sueldo bruto del trabajador: ")))
    nombre_trabajador={"nombre":nombre_trabajador, "cargo":cargo_trabajador, "sueldo": sueldo_trabajador, "descuento tranajador": (sueldo_trabajador*7)/100, "liquido a pagar": sueldo_trabajador-((sueldo_trabajador*7)/100)}
    lista_trabajador.append(nombre_trabajador)
    

def listar_trabajador():
    print('Has elegido la opción 2')


def imprimir_trabajador():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')


menu_principal()



print(lista_trabajador)