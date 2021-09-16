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
import sys 
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printSortedResults(ordlst):

    size = len(ordlst)

    for i in range(3):
        titlef = ordlst[i]['Title']
        nameArtistf = ordlst[i]['Artists']
        datef = ordlst[i]['DateAcquired']
        mediumf = ordlst[i]['Medium']
        dimensionsf = ordlst[i]['Dimensions']
        fdict = {'Title': titlef, 'Artists': nameArtistf, 'Date': datef, 'Medium': mediumf, 'Dimensions': dimensionsf}

        titlei = ordlst[-i]['Title']
        nameArtisti = ordlst[-i]['Artists']
        datei = ordlst[-i]['DateAcquired']
        mediumi = ordlst[-i]['Medium']
        dimensionsi = ordlst[-i]['Dimensions']
        idict = {'Title': titlei, 'Artists': nameArtisti, 'Date': datei, 'Medium': mediumi, 'Dimensions': dimensionsi}

        print(idict)
        print(fdict)


def printArtworksbyNationality(result):

    final_list = lt.subList(result[0], 1, 10)

    firstDatalst = [result[1]['elements'][1], result[1]['elements'][2], result[1]['elements'][3]]
    lastDatalst = [result[1]['elements'][-1], result[1]['elements'][-2], result[1]['elements'][-3]]

    print(final_list)
    print('Las primeras 3 obras de la lista del pais TOP 1 son: ')
    print(firstDatalst)
    print('Las ultimas 3 obras de la lista del pais TOP 1 son: ')
    print(lastDatalst)


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
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        controller.loadData(catalog)
        sizeArtworks = lt.size(catalog['artworks'])
        sizeArtists = lt.size(catalog['artists'])
        print('Obras cargadas: ' + str(sizeArtworks))
        print('Artistas Cargados: ' + str(sizeArtists))
        print(lt.getElement(catalog["artists"], 2))
        print(lt.getElement(catalog["artworks"], 2))

    elif int(inputs[0]) == 2:

        a=1
                     
    elif int(inputs[0]) == 3:
        ainicial = input('Indique la fecha inicial de las obras que desea consultar en el formato AAAA-MM-DD: ')
        afinal = input('Indique la fecha final de las obras que desea consultar en el formato AAAA-MM-DD: ')

        result = controller.sortArtworks(catalog, sizeArtworks, ainicial, afinal)
        print('El moma adquirio en este periodo un total de ' + str(result[2])+ ' obras unicas')
        print('De estas obras 0' + str(result[3]) + ' fueron compradas.' )
        print('Los primeros y ultimas 3 obras de la lista ordenada en el periodo mencionado son: ')
        printSortedResults(result[1])

    elif int(inputs[0]) == 4:

        a=1

    elif int(inputs[0]) == 5:

        result = controller.countArtworksNationality(catalog)

        print('En base al numero de obras en el MoMA por pais, ')
        print('Los TOP 10 paises en el MoMA son : ')
        print(printArtworksbyNationality(result))

    elif int(inputs[0]) == 6:

        a=1

    elif int(inputs[0]) == 7:

        a=1
        

    else:
        sys.exit(0)
sys.exit(0)
