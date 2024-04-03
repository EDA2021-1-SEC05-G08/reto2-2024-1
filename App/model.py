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
        "id": job[14],
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


def req_4(control, pais, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 4
    """
    jobs = control['jobs']
    
    result_jobs = lt.newList('ARRAY_LIST')
    companies = lt.newList('ARRAY_LIST')
    cities_quantity = mp.newMap(
        250000,
        maptype='PROBING',
        loadfactor=0.5
    )
    
    for job_id in lt.iterator(mp.keySet(jobs)):
        job = me.getValue(mp.get(jobs, job_id))
        
        if job['country_code'] == pais and job['published_at'] >= datetime.strptime(fecha_inicial, "%Y-%m-%d") and job['published_at'] <= datetime.strptime(fecha_final, "%Y-%m-%d"):
            
            lt.addLast(result_jobs, job)
            
            if not lt.isPresent(companies, job['company_name']):
                lt.addLast(companies, job['company_name'])
                
            if not lt.isPresent(mp.keySet(cities_quantity), job['city']):
                mp.put(cities_quantity, job['city'], 1)
            else:
                current_value = me.getValue(mp.get(cities_quantity, job['city']))
                mp.put(cities_quantity, job['city'], current_value+1)
                
    ciudad_menor, cantidad_menor = None, float('inf')
    
    for city in lt.iterator(mp.keySet(cities_quantity)):
        current_value = me.getValue(mp.get(cities_quantity, city))
        if current_value < cantidad_menor:
            ciudad_menor, cantidad_menor = city, current_value
    
    ciudad_mayor, cantidad_mayor = None, 0
    
    for city in lt.iterator(mp.keySet(cities_quantity)):
        current_value = me.getValue(mp.get(cities_quantity, city))
        if current_value > cantidad_mayor:
            ciudad_mayor, cantidad_mayor = city, current_value
         
    result_jobs = sort_jobs(result_jobs)
    result_jobs = sort_jobs_by_company_name(result_jobs)
    
    table_data = []
    if lt.size(result_jobs) <= 10:
        for job in lt.iterator(result_jobs):
            table_data.append({
                "Fecha de publicacion": job['published_at'],
                "Titulo de la oferta": job['title'],
                "Experiencia requerida": job['experience_level'],
                "Empresa": job['company_name'],
                "Ciudad": job['city'],
                "Tipo de lugar de trabajo": job['workplace_type'],
                "Tipo trabajo": job['workplace_type'],
                "Contrata ucranianos": job['open_to_hire_ukrainians']
            })
    else:
        for index in range(5):
            job = lt.getElement(result_jobs, index)
            table_data.append({
                "Fecha de publicacion": job['published_at'],
                "Titulo de la oferta": job['title'],
                "Experiencia requerida": job['experience_level'],
                "Empresa": job['company_name'],
                "Ciudad": job['city'],
                "Tipo de lugar de trabajo": job['workplace_type'],
                "Tipo trabajo": job['workplace_type'],
                "Contrata ucranianos": job['open_to_hire_ukrainians']
            })
        for index in range(lt.size(result_jobs)-5, lt.size(result_jobs)):
            job = lt.getElement(result_jobs, index)
            table_data.append({
                "Fecha de publicacion": job['published_at'],
                "Titulo de la oferta": job['title'],
                "Experiencia requerida": job['experience_level'],
                "Empresa": job['company_name'],
                "Ciudad": job['city'],
                "Tipo de lugar de trabajo": job['workplace_type'],
                "Tipo trabajo": job['workplace_type'],
                "Contrata ucranianos": job['open_to_hire_ukrainians']
            })
        
        
    table = tabulate(table_data, headers='keys', tablefmt='grid') 
            
    return (lt.size(result_jobs), lt.size(companies), lt.size(mp.keySet(cities_quantity)), ciudad_menor, cantidad_menor, ciudad_mayor, cantidad_mayor, table)


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


def req_7(data_structs, N, anio, mes):
    """
    Función que soluciona el requerimiento 7
    """
    
    jobs = data_structs['jobs']
    contries_quantity = mp.newMap(
        250000,
        maptype='PROBING',
        loadfactor=0.5
    )
    
    for job in lt.iterator(mp.keySet(jobs)):
        job = me.getValue(mp.get(jobs, job))
        if job['published_at'].year == int(anio) and job['published_at'].month == int(mes):
            if not mp.contains(contries_quantity, job['country_code']):
                mp.put(contries_quantity, job['country_code'], {"country":job['country_code'], "jobs": [job], "quantity": 1, "cities": {job['city']: 1}})
            else:
                current_value = me.getValue(mp.get(contries_quantity, job['country_code']))
                current_value["quantity"] += 1
                current_value["jobs"].append(job)
                if job["city"] in current_value["cities"]:
                    current_value["cities"][job["city"]] += 1
                else:
                    current_value["cities"][job["city"]] = 1
                mp.put(contries_quantity, job['country_code'], current_value)
      
    countries_list = lt.newList('ARRAY_LIST')          
    total_ofertas = 0
    pais_mayor_ofertas, conteo_pais_mayor_ofertas = None, 0
    ciudad_mayor_ofertas, conteo_ciudad_mayor_ofertas = None, 0
    for country in lt.iterator(mp.keySet(contries_quantity)):
        current_value = me.getValue(mp.get(contries_quantity, country))
        lt.addLast(countries_list, current_value)
        total_ofertas += current_value["quantity"]
        if current_value["quantity"] > conteo_pais_mayor_ofertas:
            pais_mayor_ofertas, conteo_pais_mayor_ofertas = country, current_value["quantity"]
        for city in current_value["cities"]:
            if current_value["cities"][city] > conteo_ciudad_mayor_ofertas:
                ciudad_mayor_ofertas, conteo_ciudad_mayor_ofertas = city, current_value["cities"][city]
       
    countries_list = sort_by_jobs_quantity(countries_list)
    countries_list  = lt.subList(countries_list, 1, int(N))
    
    cantidad_ciudades = 0
    """
    cada seniority tiene:
    - una lista de las habilidades solicitadas donde cada elemento es un diccionario con el nombre de la habilidad, el numero de veces encontrada en las ofertas y el nivel de la habilidad
    - una lista de las empresas donde cada elemento es un diccionario con el nombre de la empresa, el numero de veces encontrada en las ofertas y un booleano que indica si la empresa tiene una o mas sedes (esto se mira en mapa de multilocations buscando por el id de la oferta)
    """
    seniority_info = mp.newMap(
        3,
        maptype='PROBING',
        loadfactor=0.5
    )
    for seniority in ["junior", "mid", "senior"]:
        mp.put(seniority_info, seniority, {"skills": {}, "companies": {}})
    
    for country in lt.iterator(countries_list):
        cantidad_ciudades += len(country["cities"])
        
        for job in country["jobs"]:
            
            seniority_level = job["experience_level"]
            job_id = job["id"]
            skills = me.getValue(mp.get(data_structs["skills"], job_id))
            for skill in lt.iterator(skills):
                if skill["name"] in me.getValue(mp.get(seniority_info, seniority_level))["skills"]:
                    current_skill_info = me.getValue(mp.get(seniority_info, seniority_level))["skills"][skill["name"]]
                    current_skill_info["quantity"] += 1
                else:
                    (me.getValue(mp.get(seniority_info, seniority_level))["skills"])[skill["name"]] = {
                        "quantity": 1,
                        "level": skill["level"]
                    }
                    
            company_name = job["company_name"]
            if company_name in me.getValue(mp.get(seniority_info, seniority_level))["companies"]:
                current_company_info = me.getValue(mp.get(seniority_info, seniority_level))["companies"][company_name]
                current_company_info["quantity"] += 1
            else:
                is_multilocation = False
                if mp.contains(data_structs["multilocations"], job_id):
                    is_multilocation = True
                (me.getValue(mp.get(seniority_info, seniority_level))["companies"])[company_name] = {
                    "quantity": 1,
                    "multilocation": is_multilocation
                }
    
    """
    junior_skills_count = len(me.getValue(mp.get(seniority_info, "junior"))["skills"])
    junior_skills = lt.newList('ARRAY_LIST')
    for skill in me.getValue(mp.get(seniority_info, "junior"))["skills"]:
        skill_info = me.getValue(mp.get(seniority_info, "junior"))["skills"][skill]
        skill_info["name"] = skill
        lt.addLast(junior_skills, skill_info)
    junior_skills_ordered = sort_by_jobs_quantity(junior_skills)
    junior_most_demanded_skill_name = lt.getElement(junior_skills_ordered, 1)["name"]
    junior_most_demanded_skill_quantity = lt.getElement(junior_skills_ordered, 1)["quantity"]
    junior_less_demanded_skill_name = lt.getElement(junior_skills_ordered, junior_skills_count)["name"]
    junior_less_demanded_skill_quantity = lt.getElement(junior_skills_ordered, junior_skills_count)["quantity"]
    junior_mean_level = 0
    for skill in lt.iterator(junior_skills):
        junior_mean_level += int(skill["level"])
    junior_mean_level /= junior_skills_count
    junior_companies_count = len(me.getValue(mp.get(seniority_info, "junior"))["companies"])
    junior_companies = lt.newList('ARRAY_LIST')
    junior_companies_whit_multilocation = 0
    for company in me.getValue(mp.get(seniority_info, "junior"))["companies"]:
        junior_companies_whit_multilocation += 1 if me.getValue(mp.get(seniority_info, "junior"))["companies"][company]["multilocation"] else 0
        company_info = me.getValue(mp.get(seniority_info, "junior"))["companies"][company]
        company_info["name"] = company
        lt.addLast(junior_companies, company_info)
    junior_companies_ordered = sort_by_jobs_quantity(junior_companies)
    junior_most_offered_company_name = lt.getElement(junior_companies_ordered, 1)["name"]
    junior_most_offered_company_quantity = lt.getElement(junior_companies_ordered, 1)["quantity"]
    junior_less_offered_company_name = lt.getElement(junior_companies_ordered, junior_companies_count)["name"]
    junior_less_offered_company_quantity = lt.getElement(junior_companies_ordered, junior_companies_count)["quantity"]
    """
    
    skills_companies_info = []
    for seniority in ["junior", "mid", "senior"]:
        info = {}
        junior_skills_count = len(me.getValue(mp.get(seniority_info, seniority))["skills"])
        info["skills_count"] = junior_skills_count
        junior_skills = lt.newList('ARRAY_LIST')
        for skill in me.getValue(mp.get(seniority_info, seniority))["skills"]:
            skill_info = me.getValue(mp.get(seniority_info, seniority))["skills"][skill]
            skill_info["name"] = skill
            lt.addLast(junior_skills, skill_info)
        junior_skills_ordered = sort_by_jobs_quantity(junior_skills)
        junior_most_demanded_skill_name = lt.getElement(junior_skills_ordered, 1)["name"]
        info["most_demanded_skill_name"] = junior_most_demanded_skill_name
        junior_most_demanded_skill_quantity = lt.getElement(junior_skills_ordered, 1)["quantity"]
        info["most_demanded_skill_quantity"] = junior_most_demanded_skill_quantity
        junior_less_demanded_skill_name = lt.getElement(junior_skills_ordered, junior_skills_count)["name"]
        info["less_demanded_skill_name"] = junior_less_demanded_skill_name
        junior_less_demanded_skill_quantity = lt.getElement(junior_skills_ordered, junior_skills_count)["quantity"]
        info["less_demanded_skill_quantity"] = junior_less_demanded_skill_quantity
        junior_mean_level = 0
        for skill in lt.iterator(junior_skills):
            junior_mean_level += int(skill["level"])
        junior_mean_level /= junior_skills_count
        info["mean_level"] = junior_mean_level
        junior_companies_count = len(me.getValue(mp.get(seniority_info, seniority))["companies"])
        info["companies_count"] = junior_companies_count
        junior_companies = lt.newList('ARRAY_LIST')
        junior_companies_whit_multilocation = 0
        for company in me.getValue(mp.get(seniority_info, seniority))["companies"]:
            junior_companies_whit_multilocation += 1 if me.getValue(mp.get(seniority_info, seniority))["companies"][company]["multilocation"] else 0
            company_info = me.getValue(mp.get(seniority_info, seniority))["companies"][company]
            company_info["name"] = company
            lt.addLast(junior_companies, company_info)
        info["companies_with_multilocation"] = junior_companies_whit_multilocation
        junior_companies_ordered = sort_by_jobs_quantity(junior_companies)
        junior_most_offered_company_name = lt.getElement(junior_companies_ordered, 1)["name"]
        info["most_offered_company_name"] = junior_most_offered_company_name
        junior_most_offered_company_quantity = lt.getElement(junior_companies_ordered, 1)["quantity"]
        info["most_offered_company_quantity"] = junior_most_offered_company_quantity
        junior_less_offered_company_name = lt.getElement(junior_companies_ordered, junior_companies_count)["name"]
        info["less_offered_company_name"] = junior_less_offered_company_name
        junior_less_offered_company_quantity = lt.getElement(junior_companies_ordered, junior_companies_count)["quantity"]
        info["less_offered_company_quantity"] = junior_less_offered_company_quantity        
        skills_companies_info.append(info)
        
    return total_ofertas, cantidad_ciudades, pais_mayor_ofertas, conteo_pais_mayor_ofertas, ciudad_mayor_ofertas, conteo_ciudad_mayor_ofertas, skills_companies_info


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

def compare_jobs_quantity(job_1, job_2):
    """
    Función encargada de comparar dos datos
    """
    return job_1['quantity'] > job_2['quantity']

def compare_jobs_company_name(job_1, job_2):
    """
    Función encargada de comparar dos datos
    """
    if job_1['published_at'] == job_2['published_at']:
        return job_1['company_name'] < job_2['company_name']

# Funciones de ordenamiento

def sort_jobs(jobs_map):
    """
    Ordena los datos del modelo
    """
    return merg.sort(jobs_map, compare_jobs_date)

def sort_by_jobs_quantity(jobs_map):
    """
    Ordena los datos del modelo
    """
    return merg.sort(jobs_map, compare_jobs_quantity)

def sort_jobs_by_company_name(jobs_map):
    """
    Ordena los datos del modelo
    """
    return merg.sort(jobs_map, compare_jobs_company_name)
