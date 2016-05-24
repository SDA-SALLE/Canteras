#created by @ceapalaciosal
#under code Creative Commons
# -*- encoding: utf-8 -*-

#! /usr/bin/env python
import csv
import os
import xlrd

def wcsv(data, name, folder):	
	csvsalida = open (folder + name, 'w')
	salida = csv.writer(csvsalida, delimiter=',')
	
	if 'combustion' in folder:
		FEmissions = os.path.join('..', 'data', 'FEmition', 'FactoresEmision.xlsx')
	if 'wear' in folder:
		FEmissions = os.path.join('..', 'data', 'FEmition', 'FEBrake.xlsx')
	
	workbook = xlrd.open_workbook(FEmissions)
	names = workbook.sheet_by_index(1)

	listpollutant = []
	for pos in range (1, names.nrows):
		listpollutant.append(str(names.cell_value(pos, 0)))
	salida.writerow(['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h'])
	ID_Grilla = data.keys()

	for ID in ID_Grilla:
		pollutant = data[ID]['pollutants'].keys()
		pollutant = pollutant[0]
		csvsalida.write(data[ID]['General']['ROW'][0])
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['COL'][0])
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['LAT'][0])
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['LON'][0])
		csvsalida.write(',')
		csvsalida.write(pollutant)
		csvsalida.write(',')
		if pollutant in listpollutant:
			csvsalida.write('mol/h')	
		else:
			csvsalida.write('g/h')
		csvsalida.write(',')
		hours = data[ID]['pollutants'][pollutant].keys()
		for hour in hours:
			csvsalida.write(str(data[ID]['pollutants'][pollutant][hour][0]))
			csvsalida.write(',')
		csvsalida.write(str(data[ID]['pollutants'][pollutant][0][0]))
		csvsalida.write('\n')

	data = None
	csvsalida.close()
	
def writeEmisions(data, folder): 
	
	csvsalida = open(folder + 'Emisions.csv', 'w')
	
	names = ['ID', 'FID_Grilla', 'ROW', 'COL', 'LAT', 'LON', 'Material', 'ACANT(m2)', 'FAE', 'AREA Dia(m2)', 'PM25', 'PM10']
	for name in names: 
		if name == 'ID':
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	
	csvsalida.write('\n')
	keys = data.keys()
	for key in keys: 
		csvsalida.write(str(key))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['FID_Grilla'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['ROW'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['COL'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['LAT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['LON'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['Material'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['ACANT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['FAE'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['AREA'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM25'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM10'][0]))
		csvsalida.write('\n')
	csvsalida.close()

def writeEmisionsTYear(EGDPM25, EGDPM10, ETYearPM25, ETYearPM10, folder):
	csvsalida = open(folder + 'EmisionsTYear.csv', 'w')
	names = ['EGDPM25', 'EGDPM10', 'ETYearPM25', 'ETYearPM10']
	for name in names: 
		if name == 'EGDPM25':
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')
	csvsalida.write(str(EGDPM25))
	csvsalida.write(',')
	csvsalida.write(str(EGDPM10))
	csvsalida.write(',')
	csvsalida.write(str(ETYearPM25))
	csvsalida.write(',')
	csvsalida.write(str(ETYearPM10))
	csvsalida.close()

def writeDesagregation(data): 
	folder = os.path.join('..', 'data', 'out', 'desagregation', '')
	archives = ['PM25DH', 'PM10DH', 'PM25DNH', 'PM10DNH']
	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	
	for archive in archives:
		csvsalida = open(folder + archive + '.csv', 'w')

		for name in names: 
			if name == 'ROW':
				csvsalida.write(name)
			else: 
				csvsalida.write(',')
				csvsalida.write(name)

		csvsalida.write('\n')
		keys = data.keys()
		for key in keys: 
			csvsalida.write(str(data[key]['General']['ROW'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['COL'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['LAT'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['LON'][0]))
			csvsalida.write(',')
			if 'PM25' in archive:
				csvsalida.write('PM25')
			elif 'PM10' in archive:
				csvsalida.write('PM10')
			csvsalida.write(',')
			csvsalida.write('g/h')
			hours = data[key][archive].keys()
			for hour in hours:
				csvsalida.write(',')
				csvsalida.write(str(data[key][archive][hour][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key][archive][0][0]))

			csvsalida.write('\n')

