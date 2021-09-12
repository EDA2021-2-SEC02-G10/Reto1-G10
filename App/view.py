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
""""
from DISClib.DataStructures.arraylist import getElement
from controller import initCatalog, loadData
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
"""
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printSortResults(ord_artworks, sample):
    size = lt.size(ord_artworks)
    if size > sample:
        print("Las primeros ", sample, " obras ordenados son:")
        i = 1
        while i <= sample:
            artwork = lt.getElement(ord_artworks, i)
            print('Titulo: ' + artwork['Title'] + ', fecha de adquisicion: ' + artwork['DateAcquired'])
            i += 1


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- Clasificar cronologicamente los artistas")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una exposicion del museo")


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Digite el tipo de estructura de datos que desea manejar para la lista de artistas"
        + " (lista 1) o la lista de obreas (lista 2) en donde 1 es un ArrayList y 2 es una SingleLinkedList ")
        type1 = int(input("Tipo de estructura de datos lista 1 de artistas: "))
        type2 = int(input("Tipo de estructura de datos lista 2 de obras: "))

        if type1 == 1:
            type1 = 'ARRAY_LIST'
        elif type1 == 2:
            type1 = 'SINGLE_LINKED'

        if type2 == 1:
            type2 = 'ARRAY_LIST'
        elif type2 == 2:
            type2 = 'SINGLE_LINKED'

        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog(type1, type2)
        controller.loadData(catalog)
        sizeArtworks = lt.size(catalog['artworks'])
        sizeArtists = lt.size(catalog['artists'])
        print('Obras cargadas: ' + str(sizeArtworks))
        print('Artistas Cargados: ' + str(sizeArtists))
        print('Los ultimos 3 artistas cargados son: ' + str(lt.getElement(catalog['artists'], sizeArtists)) + ', '
        + str(lt.getElement(catalog['artists'], sizeArtists-1)) + ', '
        + str(lt.getElement(catalog['artists'], sizeArtists-2)))
        A1 = lt.getElement(catalog['artworks'], sizeArtworks)
        A2 = lt.getElement(catalog['artworks'], sizeArtworks-1)
        A3 = lt.getElement(catalog['artworks'], sizeArtworks-2)
        print('Las ultimos 3 obras cargadas son: ' + str(A1['Title']) + ', '
        + str(A2['Title']) + ', '
        + str(A3['Title']))

    elif int(inputs[0]) == 3:
        size = input('Indique el tamaño de la muestra: ')
        sortType = int(input('Indique el algoritmo de sorting que desea usar (1=InsertionSort, 2=ShellSort, 3=MergeSort, 4=QuickSort) : '))
        showsize = int(input('indique el tamaño de la lista ordenada que desea ver: '))
        result = controller.sortArtworks(catalog, int(size), sortType)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        sorted_list = result[1]
        printSortResults(result[1], showsize)

    else:
        sys.exit(0)
sys.exit(0)
