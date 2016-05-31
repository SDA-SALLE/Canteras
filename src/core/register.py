# -*- coding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

#------------ Fuction list archives CSV in directory ---------#
import os


def listaCSV(direccion):
	path = os.path.join(direccion,'')

	lstFilesEmissions = []

	lstDir = os.walk(path)  
	for root, dirs, files in lstDir:
	    for fichero in files:
	        (nombreFichero, extension) = os.path.splitext(fichero)
	        if(extension == '.csv'):
	        	lstFilesEmissions.append(nombreFichero+extension)

	return lstFilesEmissions