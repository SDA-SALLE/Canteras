# -*- coding: utf-8 -*-
#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import sys
import json
sys.path.append('core')
from matriz import *
from wcsv import *

def desagregation(archive):
	MEmisions = convertCSV(archive)

	head = MEmisions[0,:]
	index = 0
	for value in head: 
		if value == 'ID':
			colID = index
		if value == 'FID_Grilla':
			colGrid = index
		if value == 'ROW': 
			colROW = index
		if value == 'COL':
			colCOL = index
		if value == 'LAT': 
			colLAT = index
		if value == 'LON': 
			colLON = index
		if value == 'PM25': 
			colPM25 = index
		if value == 'PM10':
			colPM10 = index
		index += 1
	head = None

	data = {}
	hoursHabil = [7,8,9,10,11,13,14,15,16]
	hoursNHabil = [7,8,9,10,11]

	for i in range(1, MEmisions.shape[0]): 
		key = int(float(MEmisions[i][colID]))
		
		if data.get(key) is None: 
			data[key] = {'General': {'COL': [], 'ROW': [], 'LAT': [], 'LON': [], 'FID_Grilla': [], 'PM25':[], 'PM10': []}, 'PM25DH':{}, 'PM10DH':{}, 'PM25DNH':{}, 'PM10DNH':{}}

		if data[key]['General']['COL'] == []:
			data[key]['General']['COL'].append(int(float(MEmisions[i][colCOL])))
			data[key]['General']['ROW'].append(int(float(MEmisions[i][colROW])))
			data[key]['General']['LAT'].append(MEmisions[i][colLAT])
			data[key]['General']['LON'].append(MEmisions[i][colLON])
			data[key]['General']['FID_Grilla'].append(int(float(MEmisions[i][colGrid])))
			data[key]['General']['PM25'].append(float(MEmisions[i][colPM25]))
			data[key]['General']['PM10'].append(float(MEmisions[i][colPM10]))

		Types = data[key].keys()
		for Type in Types:
			if Type != 'General':
				for hour in range(0, 24): 
					if data[key][Type].get(hour) is None:
						data[key][Type][hour] = []

					if Type == 'PM25DH':
						if hour in hoursHabil:

							data[key][Type][hour].append(data[key]['General']['PM25'][0]/len(hoursHabil))
						else:
							data[key][Type][hour].append(0)

					if Type == 'PM10DH':
						if hour in hoursHabil:
							data[key][Type][hour].append(data[key]['General']['PM10'][0]/len(hoursHabil))
						else:
							data[key][Type][hour].append(0)

					if Type == 'PM25DNH':
						if hour in hoursNHabil:
							data[key][Type][hour].append(data[key]['General']['PM25'][0]/len(hoursNHabil))
						else:
							data[key][Type][hour].append(0)

					if Type == 'PM10DNH':
						if hour in hoursNHabil:
							data[key][Type][hour].append(data[key]['General']['PM10'][0]/len(hoursNHabil))
						else:
							data[key][Type][hour].append(0)


	writeDesagregation(data)
	
def final(Archive):
	
	data = {}
	matriz = convertCSV(Archive)
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
		if value == 'POLNAME':
			colPollname = index
		if value == 'UNIT':
			colUnit = index
		index += 1


	for i in range(1, matriz.shape[0]):
		keys = matriz[i][colROW] + matriz[i][colCOL] + matriz[i][colPollname]
		
		if data.get(keys) is None:
			data[keys] = {}
			data[keys]['hours'] = {}
			data[keys]['GENERAL'] = {'ROW': [], 'COL': [], 'LAT': [], 'LON': [], 'POLNAME': [], 'UNIT':[]}

		
		for hour in range(0, 25):
			data[keys]['hours'][hour] = []

	
	for i in range(1, matriz.shape[0]):
		keys = matriz[i][colROW] + matriz[i][colCOL] + matriz[i][colPollname]
		if data[keys]['GENERAL']['ROW'] == []:
			data[keys]['GENERAL']['ROW'].append(matriz[i][colROW])
			data[keys]['GENERAL']['COL'].append(matriz[i][colCOL])
			data[keys]['GENERAL']['LAT'].append(matriz[i][colLAT])
			data[keys]['GENERAL']['LON'].append(matriz[i][colLON])
			data[keys]['GENERAL']['POLNAME'].append(matriz[i][colPollname])
			data[keys]['GENERAL']['UNIT'].append(matriz[i][colUnit])

		hour = 0
		for x in range(6, matriz.shape[1]):
			data[keys]['hours'][hour].append(matriz[i][x])
			hour += 1

	matriz = None
	keys = data.keys()
	for key in keys:
		hours = data[key]['hours'].keys()
		for hour in hours:
			if hour == 'GENERAL':
				pass
			else:
				suma = eval('+'.join(data[key]['hours'][hour]))
				data[key]['hours'][hour] = []
				data[key]['hours'][hour].append(suma)

	
	csvsalida = open(Archive, 'w')
	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names:
		if name == 'ROW':
			csvsalida.write(name)
		else:
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	names = data.keys()

	for key in names:
		csvsalida.write(data[key]['GENERAL']['ROW'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['COL'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['LAT'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['LON'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['POLNAME'][0])
		csvsalida.write(',')
		csvsalida.write(data[key]['GENERAL']['UNIT'][0])
		#csvsalida.write(',')
		hours = data[key]['hours'].keys()
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[key]['hours'][hour][0]))
		csvsalida.write('\n')
	csvsalida.close ()
		




