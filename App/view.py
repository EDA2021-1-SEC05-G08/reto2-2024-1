"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


def new_controller():
    """
        Se crea una instancia del controlador
    """
    return controller.new_controller()


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    
    data, jobs_quantity, table = controller.load_data(control, 'small-jobs.csv', 'small-skills.csv', 'small-employments_types.csv', 'small-multilocations.csv')

    print("El total de ofertas de trabajo pulicadas cargadas es: " + str(jobs_quantity) + "\n")  
    
    print("Las tres primeras y tres últimas ofertas de trabajo publicadas ordenadas por la fecha de publicación son:")
    print (table)
    print()

    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    
    pais = input("Ingrese el codigo del pais de interes: ")
    fecha_inicial = input("Ingrese la fecha inicial de interes en formato YYYY-MM-DD: ")
    fecha_final = input("Ingrese la fecha final de interes en formato YYYY-MM-DD: ")
    
    total_ofertas, total_empresas, total_ciudades, ciudad_menor, cantidad_menor, ciudad_mayor, cantidad_mayor, tabla = controller.req_4(control, pais, fecha_inicial, fecha_final)
    
    print("El total de ofertas de trabajo publicadas en el país " + pais + " entre " + fecha_inicial + " y " + fecha_final + " es: " + str(total_ofertas))
    print("El total de empresas que publicaron ofertas de trabajo en el país " + pais + " entre " + fecha_inicial + " y " + fecha_final + " es: " + str(total_empresas))
    print("El total de ciudades en las que se publicaron ofertas de trabajo en el país " + pais + " entre " + fecha_inicial + " y " + fecha_final + " es: " + str(total_ciudades))
    print("La ciudad con menor cantidad de ofertas de trabajo publicadas en el país " + pais + " entre " + fecha_inicial + " y " + fecha_final + " es: " + ciudad_menor + " con " + str(cantidad_menor) + " ofertas")
    print("La ciudad con mayor cantidad de ofertas de trabajo publicadas en el país " + pais + " entre " + fecha_inicial + " y " + fecha_final + " es: " + ciudad_mayor + " con " + str(cantidad_mayor) + " ofertas")
    print("Listado de ofertas en orden cronológico:")
    print(tabla)


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()
data = None

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(data)
        elif int(inputs) == 3:
            print_req_2(data)

        elif int(inputs) == 4:
            print_req_3(data)

        elif int(inputs) == 5:
            print_req_4(data)

        elif int(inputs) == 6:
            print_req_5(data)

        elif int(inputs) == 7:
            print_req_6(data)

        elif int(inputs) == 8:
            print_req_7(data)

        elif int(inputs) == 9:
            print_req_8(data)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
