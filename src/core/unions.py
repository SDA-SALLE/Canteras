# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import os
import os
import sys
from matriz import *
from clear import *

def listaCSV(direccion):
   	#Variable para la ruta al directorio
	path = os.path.join(direccion,'')
	#print direccion

	#Lista vacia para incluir los ficheros
	lstFilesEmissions = []

	#Lista con todos los ficheros del directorio:
	lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
	datos = {}

	#Crea una lista de los ficheros que existen en el directorio y los incluye a la lista.
	for root, dirs, files in lstDir:
	    for fichero in files:
	        (nombreFichero, extension) = os.path.splitext(fichero)
	        if(extension == '.csv'):
	        	lstFilesEmissions.append(nombreFichero+extension)

	return lstFilesEmissions


def UNIONS(folder, year):

	listHabil = []
	listNHabil = []

	#folder = os.path.join('..', 'data', 'in', 'unions', '')
	listout = listaCSV(folder)
	
	for out in listout:

		if 'DNH' in out or 'NHABIL' in out or '_NHabil' in out:
			listNHabil.append(out)
		elif 'DH' in out or 'HABIL' in out or '_Habil' in out:
			listHabil.append(out)

	foldersave = os.path.join('..', 'data', 'out', 'UNIONS', '')
	
	csvsalida = open(foldersave + 'rpm_quarrying_weekday_'+ year +'.csv', 'w')

	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names:
		if name == 'ROW':
			csvsalida.write(name)
		else:
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')
	
	for lista in listNHabil:
		archive = folder + lista
		matriz = convertCSV(archive)
		for i in range(1, matriz.shape[0]):
			for x in range(0, matriz.shape[1]):
				if x == 0:
					csvsalida.write(matriz[i][x])
				else:
					csvsalida.write(',')
					csvsalida.write(matriz[i][x])
			csvsalida.write('\n')
		matriz = None
	csvsalida.close()

	csvsalida = open(foldersave + 'rpm_quarrying_sat_'+ year +'.csv', 'w')
	for name in names:
		if name == 'ROW':
			csvsalida.write(name)
		else:
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')
	for lista in listHabil:
		archive = folder + lista
		matriz = convertCSV(archive)
		for i in range(1, matriz.shape[0]):
			for x in range(0, matriz.shape[1]):
				if x == 0:
					csvsalida.write(matriz[i][x])
				else:
					csvsalida.write(',')
					csvsalida.write(matriz[i][x])
			csvsalida.write('\n')

		matriz = None
	csvsalida.close()