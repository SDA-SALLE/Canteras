# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
import json
import csv
sys.path.append('core')
from matriz import * 
from register import *

def writespeciation(data, namearchive, namespecie):

	folder = os.path.join('..', 'data', 'out', 'speciation', '')

	csvsalida = open(folder + namespecie + '_' + namearchive, 'w')
	salida = csv.writer(csvsalida, delimiter=',')

	salida.writerow(['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h'])

	keys = data.keys()
	for key in keys:
		csvsalida.write(str(data[key]['GENERAL']['ROW'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['COL'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['LAT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['LON'][0]))
		csvsalida.write(',')
		csvsalida.write(namespecie)
		csvsalida.write(',')
		csvsalida.write('g/s')
		csvsalida.write(',')
		hours = data[key]['hours'].keys()
		for hour in hours:
			csvsalida.write(data[key]['hours'][hour][0])
			if hour != 24:
				csvsalida.write(',')
		csvsalida.write('\n')
	csvsalida.close()

def speciation(archivespeciation, folder):
	print 'PM2.5 speciation taken from gsref*(EI SMOKE 2007 PM) for RPM from paved roads with PROFID = 92053'
	print 'Speciated emissions in g/s per SPCID per ROW,COL,H'

	lstFilesEmissions = listaCSV(folder)
	
	Files25 = []

	for File in lstFilesEmissions: 
		if 'PM25' in File: 
			Files25.append(File)
	
	
	Mspeciation = convertXLSX(archivespeciation)

	head = Mspeciation[0,:]
	index = 0
	for value in head: 
		if value == 'SPCID':
			colSPCID = index
		if value == 'MASSFRAC':
			colMASSFRAC = index
		index += 1 

	speciation = {}

	for i in range(1, Mspeciation.shape[0]):
		name = Mspeciation[i][colSPCID]
		val = Mspeciation[i][colMASSFRAC]

		if speciation.get(name) is None: 
			speciation[name] = val

	namesspecies = speciation.keys()
	
	for species in namesspecies:
		for File in Files25:
			data = {}
			archive = folder + File
			matriz = convertCSV(archive)

			head = matriz[0,:]
			index = 0
			for value in head:
				if value == 'ROW':
					colROW = index
				if value == 'COL':
					colCOL = index
				if value == 'LAT':
					colLAT = index
				if value == 'LON':
					colLON = index

				index += 1 
			
			for i in range(1, matriz.shape[0]):
				keys = int(matriz[i][0] + matriz[i][1])
				if data.get(keys) is None: 
					data[keys] = {}
					data[keys]['GENERAL'] = {'ROW': [] ,'COL': [],'LAT': [],'LON': []} 
					data[keys]['hours'] = {}

					if data[keys]['GENERAL']['ROW'] == []:
						data[keys]['GENERAL']['ROW'].append(int(matriz[i][colROW]))
						data[keys]['GENERAL']['COL'].append(int(matriz[i][colCOL]))
						data[keys]['GENERAL']['LAT'].append(matriz[i][colLAT])
						data[keys]['GENERAL']['LON'].append(matriz[i][colLON])

					entryhour = data[keys]['hours']
					
					for hour in range(0, 25):
						if entryhour.get(hour) is None:
							entryhour[hour] = []

					hour = 0
					for x in range(6, matriz.shape[1]):
						data[keys]['hours'][hour].append(str((float(matriz[i][x]) * float(speciation[species]))/3600))
						hour += 1			
			writespeciation(data, File, species)