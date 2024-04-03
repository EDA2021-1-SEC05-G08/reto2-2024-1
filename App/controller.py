"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc

from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt


csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    return model.new_data_structs() 

# Funciones para la carga de datos

def load_data(control, jobs_filename, skills_filename, employment_types_filename, multilocations_filename):
    """
    Carga los datos del reto
    """
    
    control = load_jobs(control, jobs_filename)
    control = load_skills(control, skills_filename)
    control = load_employment_types(control, employment_types_filename)
    control = load_multilocations(control, multilocations_filename)
    
    return (control, model.data_size(control['jobs_sorted']), model.create_table(control['jobs_sorted'])) 

def load_jobs(control, jobs_filename):
    """
    Carga los datos de los trabajos
    """
    with open(cf.data_dir + "/Data/" + jobs_filename, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')

        next(lector_csv)

        for fila in lector_csv:
            control["jobs"] = model.add_job(control["jobs"], fila)
            model.add_job_in_list(control["jobs_sorted"], fila)
            
    control["jobs_sorted"] = model.sort_jobs(control["jobs_sorted"])
    
    return control

def load_skills(control, skills_filename):
    """
    Carga los datos de las habilidades
    """
    with open(cf.data_dir + "/Data/" + skills_filename, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')

        for fila in lector_csv:
            control["skills"] = model.add_skill(control["skills"], fila)
    
    return control

def load_employment_types(control, employment_types_filename):
    """
    Carga los datos de los tipos de empleo
    """
    with open(cf.data_dir + "/Data/" + employment_types_filename, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')

        for fila in lector_csv:
            control["employment_types"] = model.add_employment_type(control["employment_types"], fila)
    
    return control

def load_multilocations(control, multilocations_filename):
    """
    Carga los datos de las locaciones
    """
    with open(cf.data_dir + "/Data/" + multilocations_filename, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')

        for fila in lector_csv:
            control["multilocations"] = model.add_multilocation(control["multilocations"], fila)
    
    return control

"""
struct = load_data(new_controller(), 'small-jobs.csv', 'small-skills.csv', 'small-employments_types.csv', 'small-multilocations.csv')
jobs = (struct["jobs_sorted"])
for job in lt.iterator(jobs):
    print(job['published_at'].strftime("%Y-%m-%dT%H:%M:%S"))
"""

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control, pais, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    return model.req_4(control, pais, fecha_inicial, fecha_final)


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control, N, anio, mes):
    """
    Retorna el resultado del requerimiento 7
    """
    return model.req_7(control, N, anio, mes)


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
