# -*- coding: utf-8 -*-
#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import sys
import json
sys.path.append('core')
from matriz import *
from wcsv import *




def emisionsquarry(archive): 
	
	archiveConstants = os.path.join('..', 'data', 'in', 'constants', 'FE.xlsx')
	Mconstants = convertXLSX(archiveConstants)
	constants = {}
	for i in range(1, Mconstants.shape[0]):
		if constants.get(Mconstants[i][0]) is None:
			constants[Mconstants[i][0]] = round(Mconstants[i][1], 6)
	Mconstants = None

	matriz = convertXLSX(archive)
	head = matriz[0,:]
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
		if 'ACANT' in value:
			colACANT = index
		if value == 'material' or value == 'Material':
			colMAT = index
		if value == 'FAE': 
			colFAE = index
		index += 1
	head = None

	data = {}
	for i in range(1, matriz.shape[0]): 
		key = int(float(matriz[i][colID]))
		if data.get(key) is None: 
			data[key] = {'General': {'COL': [], 'ROW': [], 'LAT': [], 'LON': [], 'FID_Grilla': [], 'ACANT': [], 'Material': [], 'FAE': []}, 'Emisions': {'AREA': [], 'PM25':[], 'PM10': []}}

		if data[key]['General']['COL'] == []:
			data[key]['General']['COL'].append(int(float(matriz[i][colCOL])))
			data[key]['General']['ROW'].append(int(float(matriz[i][colROW])))
			data[key]['General']['LAT'].append(matriz[i][colLAT])
			data[key]['General']['LON'].append(matriz[i][colLON])
			data[key]['General']['FID_Grilla'].append(int(float(matriz[i][colGrid])))
			data[key]['General']['ACANT'].append(matriz[i][colACANT])
			data[key]['General']['Material'].append(matriz[i][colMAT])
			data[key]['General']['FAE'].append(matriz[i][colFAE])

		data[key]['Emisions']['AREA'].append(float(data[key]['General']['ACANT'][0]) * float(data[key]['General']['FAE'][0]))

		names = constants.keys()
		for name in names: 
			if data[key]['General']['Material'][0] in name: 
				if 'PM25' in name:
					#print data[key]['Emisions']['AREA'][0], constants[name]
					data[key]['Emisions']['PM25'].append(float((data[key]['Emisions']['AREA'][0]*constants[name]*9*3600)))
				elif 'PM10' in name: 
					data[key]['Emisions']['PM10'].append(float((data[key]['Emisions']['AREA'][0]*constants[name]*9*3600)))

	folder = os.path.join('..', 'data', 'out', 'EMISIONS', '')
	writeEmisions(data, folder)

def emisionsTYear(archive):
	archiveDays = os.path.join('..', 'data', 'in', 'constants', 'DAYS.xlsx')
	Mdays = convertXLSX(archiveDays)
	DH = int(float(Mdays[0][1]))
	DNH = int(float(Mdays[1][1]))
	Saturday = int(float(Mdays[2][1]))
	#print DH, DNH, Saturday

	MEmisions = convertCSV(archive)
	head = MEmisions[0,:]
	index = 0
	for value in head: 
		if value == 'PM25': 
			colPM25 = index
		if value == 'PM10':
			colPM10 = index
		index += 1

	head = None
	EGDPM25 = 0 
	EGDPM10 = 0
	ETYearPM25 = 0
	ETYearPM10 = 0
	for i in range(1, MEmisions.shape[0]):
		EGDPM25 += float(MEmisions[i][colPM25])
		EGDPM10 += float(MEmisions[i][colPM10])

	ETYearPM25 = (EGDPM25/1000000)*DH + Saturday
	ETYearPM10 = (EGDPM10/1000000)*DH + Saturday

	folder = os.path.join('..', 'data', 'out', 'emisions', '')
	writeEmisionsTYear(EGDPM25, EGDPM10, ETYearPM25, ETYearPM10, folder)






