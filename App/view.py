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

    for i in range(1,4):
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

def printNewDisplay(lstExpo, area):

    firstDataLst = [result[0]['elements'][0], result[0]['elements'][1], result[0]['elements'][2]]
    LastDataLst = [result[0]['elements'][-1], result[0]['elements'][-2], result[0]['elements'][-3]]

    print('El area ocupada por la nueva exposicion es de: ')
    print(str(area) + str('m^2'))
    print('La nueva exposicion estara compuesta de: ' + str(lt.size(lstExpo)) + str(' obras'))
    print('Las primeras 3 obras de la nueva exposicion son : ')
    print(firstDataLst[0])
    print(firstDataLst[1])
    print(firstDataLst[2])
    print('Las ultimas 3 obras de la nueva exposicion son: ')
    print(LastDataLst[0])
    print(LastDataLst[1])
    print(LastDataLst[2])

def PrintArtistsSortedbyBirthdate(lista):
    for i in range (0,3):
        artistnamei = lista[-i]['name']
        birthdatei = lista[-i]['BeginDate']
        xi= lista[-i]['EndDate']
        if xi == 0:
            deathdatei = " "
        else:
            deathdatei = lista[-i]['EndDate']
        nacionalityi = lista[-i]['Nationality']
        genderi = lista[-i]['Gender']
        idict ={'Name': artistnamei, 'Birth Date': birthdatei, 'Death Date': deathdatei, 'Nationality': nacionalityi, 'Gender': genderi} 

        artistnamef = lista[i]['name']
        birthdatef = lista[i]['BeginDate']
        xf= int(lista[i]['EndDate'])
        if xf == 0:
            deathdatef = " "
        else:
            deathdatef = lista[i]['EndDate']
        nacionalityf = lista[i]['Nationality']
        genderf = lista[i]['Gender']
        fdict ={'Name': artistnamef, 'Birth Date': birthdatef, 'Death Date': deathdatef, 'Nationality': nacionalityf, 'Gender': genderf} 
        print (idict)
        print(fdict)


def printArtworksbyNationality(result):

    final_list = lt.subList(result[0], 1, 10)

    firstDatalst = [result[1]['elements'][0], result[1]['elements'][1], result[1]['elements'][2]]
    lastDatalst = [result[1]['elements'][-1], result[1]['elements'][-2], result[1]['elements'][-3]]

    print('En base al numero de obras en el MoMA por pais, ')
    print('Los TOP 10 paises en el MoMA son : ')
    print(final_list)
    print('Las primeras 3 obras de la lista del pais TOP 1 son: ')
    print(firstDatalst[0])
    print(firstDatalst[1])
    print(firstDatalst[2])
    print('Las ultimas 3 obras de la lista del pais TOP 1 son: ')
    print(lastDatalst[0])
    print(lastDatalst[1])
    print(lastDatalst[2])


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
        ainicial=int(input('Indique el año inicial de nacimiento de los artistas que desea consultar en formato YYYY:  '))
        afinal= int(input ('Indique el año final de nacimiento de los artistas que desea consultar en formato YYYY: '))
        result = controller.sortArtists(catalog, sizeArtists, ainicial,afinal)
        print('En total hay '+ str(result[2])+' artistas que nacieron entre '+str(ainicial)+' y ' + str(afinal))
        PrintArtistsSortedbyBirthdate(result[1])

        
                     
    elif int(inputs[0]) == 3:
        aninicial = input('Indique la fecha inicial de las obras que desea consultar en el formato AAAA-MM-DD (con los numeros menores a 10 como 01, 02, etc): ')
        afinal = input('Indique la fecha final de las obras que desea consultar en el formato AAAA-MM-DD (con los numeros menores a 10 como 01, 02, etc): ')

        result = controller.sortArtworks(catalog, sizeArtworks, aninicial, afinal)
        print('El moma adquirio en este periodo un total de ' + str(result[2])+ ' obras unicas')
        print('De estas obras 0' + str(result[3]) + ' fueron compradas.' )
        print('Los primeros y ultimas 3 obras de la lista ordenada en el periodo mencionado son: ')
        printSortedResults(result[1])

    elif int(inputs[0]) == 4:

        a = 1

    elif int(inputs[0]) == 5:

        result = controller.countArtworksNationality(catalog)

        printArtworksbyNationality(result)

    elif int(inputs[0]) == 6:

        a=1

    elif int(inputs[0]) == 7:

        a_inicial = input('Digite el año inicial de las obras que desea exponer: ')
        a_final = input('Digite el año final de las obras que desea exponer: ')
        area = float(input('Area disponible para la exposicion en m^2: '))

        result = controller.createNewDisplay(catalog, a_inicial, a_final, area)
        printNewDisplay(result[0], result[1])

    else:
        sys.exit(0)
sys.exit(0)
