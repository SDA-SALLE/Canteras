#created by @ceapalaciosal
#under code Creative Commons
# -*- encoding: utf-8 -*-

#! /usr/bin/env python
import csv
import os
import xlrd

	
def writeEmisions(data, folder, year): 
	
	csvsalida = open(folder + 'Emisions_' + year + '.csv', 'w')
	
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

def writeEmisionsTYear(EGDPM25, EGDPM10, ETYearPM25, ETYearPM10, folder, year):
	csvsalida = open(folder + 'EmisionsTYear_'+year+'.csv', 'w')
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

def writeDesagregation(data, year): 
	folder = os.path.join('..', 'data', 'out', 'desagregation', '')
	archives = ['PM25DH', 'PM10DH', 'PM25DNH', 'PM10DNH']
	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	
	for archive in archives:
		csvsalida = open(folder + archive + '_' + year +'.csv', 'w')

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

