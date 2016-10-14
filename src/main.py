# -*- coding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
sys.path.append('core')
from clear import *
from emisions import *
from desagregation import *
from register import *
from speciation import *
from unions import *
folder = os.path.join('..', 'data', 'out', '')
clear(folder)

year = raw_input('Insert year running: ')

#Archive quarry in folder /data/in/
archive = os.path.join('..', 'data', 'in', 'database_' + year +'.xlsx')
emisionsquarry(archive, year)

#T/Year
archive = os.path.join('..', 'data', 'out', 'emisions', 'Emisions_' + year +'.csv')
emisionsTYear(archive, year)

#desagregation Hour
archive = os.path.join('..', 'data', 'out', 'emisions', 'Emisions_'+ year +'.csv')
desagregation(archive, year)

#unions
folderDesagregation = os.path.join('..', 'data', 'out', 'desagregation', '')
archives = listaCSV(folderDesagregation)
#print archives
for archive in archives:
    #print archive
    archive = folderDesagregation + archive
    final(archive)

#Speciation
print 'Start Speciation Canteras'

#Speciation
archivespeciation = os.path.join ('..', 'data', 'in', 'speciation', 'CANT_SCP_PROF_PM25_'+ year +'.xlsx')
folderCant = os.path.join('..', 'data', 'out', 'desagregation', '')
speciation(archivespeciation, folderCant)

#UNIONS
folder = os.path.join('..', 'data', 'out', 'speciation', '')
UNIONS(folder, year)