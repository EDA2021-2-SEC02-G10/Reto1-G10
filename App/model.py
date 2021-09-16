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

from DISClib.DataStructures.arraylist import getElement, iterator, size
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf
import time
from datetime import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá 
dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    """

    """
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtworks)
    catalog['artists'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtists)

    return catalog


# Funciones para agregar informacion al catalogo

def addArtwork(catalog, title, dateAcquired, lstmedium, dimensions, lstconstituentid, objectid, creditline, date):

    dictArtwork = newArtwork(title)
    dictArtwork['DateAcquired'] = dateAcquired
    dictArtwork['Dimensions'] = dimensions
    dictArtwork['Medium'] = lstmedium
    dictArtwork['ObjectID'] = objectid
    dictArtwork['ArtistsID'] = lstconstituentid
    dictArtwork['CreditLine'] = creditline
    dictArtwork['Date'] = date
    lt.addLast(catalog['artworks'], dictArtwork)

    for cID in lstconstituentid:
        addArtist(catalog, cID, dictArtwork)


def addArtist(catalog, constituentid, artwork):

    artists = catalog['artists']
    posartist = lt.isPresent(artists, constituentid)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else:
        artist = newArtist(constituentid)
        lt.addLast(catalog['artists'], artist)
    lt.addLast(artist['artworks'], artwork)


def addInfoArtist(catalog, name, constituentid, nationality):

    posartists = lt.isPresent(catalog['artists'], constituentid)
    if posartists > 0:
        artist = lt.getElement(catalog['artists'], posartists)
        artist['name'] = name
        artist['Nationality'] = nationality
    else:
        dictArtist = newArtist(constituentid)
        dictArtist['name'] = name
        dictArtist['Nationality'] = nationality

    posartwork = lt.isPresent(catalog['artworks'], constituentid)
    if posartwork > 0:
        artwork = lt.getElement(catalog['artworks'], posartwork)
        artwork['Artists'].append(name)


# Funciones para creacion de datos

def newArtist(constituentid):

    artist = {'name': "", 'ConstituentID': "", 'Nationality': "", "artworks": None,}
    artist['ConstituentID'] = constituentid
    artist['artworks'] = lt.newList('ARRAY_LIST')

    return artist


def newArtwork(title):
    artwork = {'Title': "", 'DateAcquired': 0, 'ArtistsID': None, 'Medium': None,
               'Dimensions': "", 'ObjectID': 0, "CreditLine": "", "Artists": [], 'Date': ""}
    artwork['Title'] = title

    return artwork


# Funciones de consulta

def sortArtworks(catalog, ltsize, a1, a2):

    dt_objectI1 = datetime.strptime(a1, '%Y-%m-%d').date()
    dt_objectI2 = datetime.strptime(a2, '%Y-%m-%d').date()
    sub_list = lt.subList(catalog['artworks'], 1, ltsize)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = None
    sorted_list = ms.sort(sub_list, cmpArtworkByDateAcquired)
    listFinal = []
    purchasedArtworks = 0
    totalArtworks = 0
    for value in lt.iterator(sorted_list):
        if len(value['DateAcquired']) > 1:
            dt_object1 = datetime.strptime(value['DateAcquired'], '%Y-%m-%d').date()
            if ((dt_object1 > dt_objectI1) and (dt_object1 < dt_objectI2)):
                listFinal.append(value)
                totalArtworks += 1
                if 'Purchase' in value['CreditLine']:
                    purchasedArtworks += 1
            else:
                pass

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg, listFinal, totalArtworks, purchasedArtworks


def countArtworksNationality(catalog):

    dictFinal = {}
    for artist in lt.iterator(catalog['artists']):
        if (len(artist['Nationality']) > 0 and (artist['Nationality'] != 'Nationality unknown')):
            if artist['Nationality'] not in dictFinal:
                dictFinal[artist['Nationality']] = lt.size(artist['artworks'])
            else:
                dictFinal[artist['Nationality']] += lt.size(artist['artworks'])

    lst = lt.newList('ARRAY_LIST')
    lstf= lt.newList('ARRAY_LIST')
    for key in dictFinal:
        dictT = {}
        dictT[key] = dictFinal[key]
        lt.addLast(lst, dictT[key])
    sorted_list = None
    sorted_list = ms.sort(lst, cmpCountriesbyArtworks)

    for value in lt.iterator(sorted_list):
        for key in dictFinal:
            dictTF = {}
            if value == dictFinal[key]:
                dictTF[key] = value
                lt.addLast(lstf, dictTF)

    # DATOS DE LAS OBRAS DEL TOP 1

    key_list = list(lstf['elements'][0])
    topCountry = key_list[0]

    lstTopCountryArtists = []
    for value in lt.iterator(catalog['artists']):
        if value['Nationality'] == topCountry:
            lstTopCountryArtists.append(value['name'])

    listData = lt.newList('ARRAY_LIST')
    for value in lt.iterator(catalog['artworks']):
        for i in range(len(value['Artists'])):
            dictData = {}
            if value['Artists'][i] in lstTopCountryArtists:
                dictData['Title'] = value['Title']
                dictData['Artists'] = value['Artists']
                dictData['Date'] = value['Date']
                dictData['Medium'] = value['Medium']
                dictData['Dimensions'] = value['Dimensions']
                lt.addLast(listData, dictData)
                break

    return lstf, listData


# Funciones utilizadas para comparar elementos dentro de una lista


def compareArtists(artistid1, artist):
    if artistid1 == artist['ConstituentID']:
        return 0
    return -1


def compareArtworks(artworkid, artwork):
    if artworkid in artwork['ArtistsID']:
        return 0
    return -1


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
    if (len(date1) < 2):
        date1 = [2021, 10, 20]
        artwork1['DateAcquired'] = '2021-10-02'
    if (len(date2)) < 2:
        date2 = [2021, 10, 20]
        artwork2['DateAcquired'] = '2021-10-02'

    if int(date1[0]) < int(date2[0]):
        r = True
    elif int(date1[0]) > int(date2[0]):
        r = False
    elif int(date1[1]) < int(date2[1]):
        r = True
    elif int(date1[1]) > int(date2[1]):
        r = False
    elif int(date1[2]) < int(date2[2]):
        r = True
    elif int(date1[2]) > int(date2[2]):
        r = False

    return r


    """
    date1 = artwork1['DateAcquired']
    date2 = artwork2['DateAcquired']
    date1l = artwork1['DateAcquired'].split("-")
    date2l = artwork2['DateAcquired'].split("-")
    r = None
    if (len(date1l) > 1) and (len(date2l) > 1):
        dt_object1 = datetime.strptime(date1, '%Y-%m-%d').date()
        dt_object2 = datetime.strptime(date2, '%Y-%m-%d').date()
        if dt_object1 < dt_object2:
            r = True
        else:
            r = False

    return r
    """

def cmpCountriesbyArtworks(country1, country2):

    r = None
    if country1 > country2:
        r = True
    else:
        r = False

    return r


