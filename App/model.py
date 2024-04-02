﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

from datetime import datetime
from tabulate import tabulate

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    
    data_structs = {
        
        "jobs": None,
        "skills": None,
        "employment_types": None,
        "multilocations": None,
        
        "jobs_sorted": None
        
    }
    
    data_structs['jobs'] = mp.newMap(
        250000,
        maptype='PROBING',
        loadfactor=0.5
    )
    
    data_structs['skills'] = mp.newMap(
        580000,
        maptype='PROBING',
        loadfactor=0.5
    )
    
    data_structs['employment_types'] = mp.newMap(
        260000,
        maptype='PROBING',
        loadfactor=0.5
    )
    
    data_structs['multilocations'] = mp.newMap(
        250000,
        maptype='PROBING',
        loadfactor=0.5
    )
    
    data_structs["jobs_sorted"] = lt.newList('ARRAY_LIST')
    
    return data_structs

# Funciones para agregar informacion al modelo

def add_job(jobs_map, job):
    
    job_dict = {
        "title": job[0],
        "street": None if job[1] == "NOT DEFINED" else job[1],
        "city": job[2],
        "country_code": job[3],
        "address_text": job[4],
        "maker_icon": job[5],
        "workplace_type": job[6],
        "company_name": job[7],
        "company_url": job[8],
        "company_size": None if job[9]=="Undefined" else int(job[9]),
        "experience_level": job[10],
        "published_at": datetime.strptime(job[11].split(".")[0], "%Y-%m-%dT%H:%M:%S"),
        "remote_interview": bool(job[12]),
        "open_to_hire_ukrainians": bool(job[13]),
        "display_offer": bool(job[15]),     
    }
    
    mp.put(jobs_map, job[14], job_dict)
    
    return jobs_map

def add_job_in_list(jobs_list, job):
    
    job_dict = {
        "title": job[0],
        "street": None if job[1] == "NOT DEFINED" else job[1],
        "city": job[2],
        "country_code": job[3],
        "address_text": job[4],
        "maker_icon": job[5],
        "workplace_type": job[6],
        "company_name": job[7],
        "company_url": job[8],
        "company_size": None if job[9]=="Undefined" else int(job[9]),
        "experience_level": job[10],
        "published_at": datetime.strptime(job[11].split(".")[0], "%Y-%m-%dT%H:%M:%S"),
        "remote_interview": bool(job[12]),
        "open_to_hire_ukrainians": bool(job[13]),
        "display_offer": bool(job[15]),     
    }
    
    
    lt.addLast(jobs_list, job_dict)

def add_skill(skills_map, skill):
    
    skill_dict = {
        "name": skill[0],
        "level": skill[1] 
    }

    if mp.contains(skills_map, skill[2]):
        current__values = me.getValue(mp.get(skills_map, skill[2]))
        lt.addLast(current__values, skill_dict)
        mp.put(skills_map, skill[2], current__values)
    else:
        value = lt.newList('ARRAY_LIST')
        lt.addLast(value, skill_dict)
        mp.put(skills_map, skill[2], value)
    
    return skills_map

def add_employment_type(employment_types_map, employment_type):
    
    employment_type_dict = {
        "type": employment_type[0],
        "currency_salary": employment_type[2],
        "salary_from": employment_type[3],
        "salary_to": employment_type[4],
    }
    
    if mp.contains(employment_types_map, employment_type[1]):
        current__values = me.getValue(mp.get(employment_types_map, employment_type[1]))
        lt.addLast(current__values, employment_type_dict)
        mp.put(employment_types_map, employment_type[1], current__values)
    else:
        value = lt.newList('ARRAY_LIST')
        lt.addLast(value, employment_type_dict)
        mp.put(employment_types_map, employment_type[1], value)
    
    return employment_types_map

def add_multilocation(multilocations_map, multilocation):

    multilocation_dict = {
        "city": multilocation[0],
        "street": multilocation[1] 
    }
    
    if mp.contains(multilocations_map, multilocation[2]):
        current__values = me.getValue(mp.get(multilocations_map, multilocation[2]))
        lt.addLast(current__values, multilocation_dict)
        mp.put(multilocations_map, multilocation[2], current__values)
    else:
        value = lt.newList('ARRAY_LIST')
        lt.addLast(value, multilocation_dict)
        mp.put(multilocations_map, multilocation[2], value)
    
    return multilocations_map

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(list):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(list)

def create_table(data):
    """
    Crea una tabla de datos
    """
    
    data_list = []
    
    for index in range(1,4):
        job = lt.getElement(data, index)
        formatted_job = {
            "Fecha de publicacion": job['published_at'],
            "Titulo de la oferta": job['title'],
            "Empresa": job['company_name'],
            "Nivel de experticia": job['experience_level'],
            "Pais de la oferta": job['country_code'],
            "Ciudad de la oferta": job['city']
        }
        data_list.append(formatted_job)
        
    for index in range(lt.size(data)-3, lt.size(data)):
        job = lt.getElement(data, index)
        formatted_job = {
            "Fecha de publicacion": job['published_at'],
            "Titulo de la oferta": job['title'],
            "Empresa": job['company_name'],
            "Nivel de experticia": job['experience_level'],
            "Pais de la oferta": job['country_code'],
            "Ciudad de la oferta": job['city']
        }
        data_list.append(formatted_job)
    
    return tabulate(data_list, headers='keys', tablefmt='grid')


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare_jobs_date(job_1, job_2):
    """
    Función encargada de comparar dos datos
    """
    return job_1['published_at'] > job_2['published_at']

# Funciones de ordenamiento

def sort_jobs(jobs_map):
    """
    Ordena los datos del modelo
    """
    return merg.sort(jobs_map, compare_jobs_date)
