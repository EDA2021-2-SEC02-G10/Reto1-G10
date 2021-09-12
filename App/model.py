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

from DISClib.DataStructures.arraylist import size
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá 
dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(type1, type2):
    """

    """
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList(type1)
    catalog['artists'] = lt.newList(type2)

    return catalog


# Funciones para agregar informacion al catalogo

def addArtwork(catalog, title, dateAcquired):

    dictArtwork = newArtwork(title)
    dictArtwork['DateAcquired'] = dateAcquired
    lt.addLast(catalog['artworks'], dictArtwork)


def addArtist(catalog, artist):

    if artist not in catalog['artists']:
        lt.addLast(catalog['artists'], artist)
    else:
        pass


# Funciones para creacion de datos

def newArtist(name):  

    artist = {'name': "", "artworks": None}
    artist['name'] = name
    artist['artworks'] = lt.newList()

    return artist


def newArtwork(title):
    artwork = {'Title': "", 'DateAcquired': 0, 'Artists': None}
    artwork['Title'] = title
    artwork['Artists'] = lt.newList()

    return artwork


# Funciones de consulta

def sortArtworks(catalog, ltsize, sortType):
    sub_list = lt.subList(catalog['artworks'], 1, ltsize)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = None
    if sortType == 1:
        sorted_list = ins.sort(sub_list, cmpArtworkByDateAcquired)
    elif sortType == 2:
        sorted_list = sa.sort(sub_list, cmpArtworkByDateAcquired)
    elif sortType == 3:
        sorted_list = ms.sort(sub_list, cmpArtworkByDateAcquired)
    elif sortType == 4:
        sorted_list = qs.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """ Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
        Args:
            artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
            artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    date1 = artwork1['DateAcquired'].split("-")
    date2 = artwork2['DateAcquired'].split("-")
    r = None
    if (len(date1) > 1) and (len(date2) > 1):
        if int(date1[0]) < int(date2[0]):
            r = True
        elif int(date1[0]) > int(date2[0]):
            r = False
        elif int(date1[2]) < int(date2[2]):
            r = True
        elif int(date1[2]) > int(date2[2]):
            r = False
        elif int(date1[1]) < int(date2[1]):
            r = True
        elif int(date1[1]) > int(date2[1]):
            r = False

    return r



