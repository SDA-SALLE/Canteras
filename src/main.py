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

folder = os.path.join('..', 'data', 'out', '')
clear(folder)

#Archive quarry in folder /data/in/CANTERAS.xlsx
archive = os.path.join('..', 'data', 'in', 'CANTERAS.xlsx')
emisionsquarry(archive)

#T/Year
archive = os.path.join('..', 'data', 'out', 'emisions', 'Emisions.csv')
emisionsTYear(archive)

#desagregation Hour
archive = os.path.join('..', 'data', 'out', 'emisions', 'Emisions.csv')
desagregation(archive)

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
archivespeciation = os.path.join ('..', 'data', 'in', 'PE', 'CANT_SCP_PROF_PM25.xlsx')
folderCant = os.path.join('..', 'data', 'out', 'desagregation', '')
speciation(archivespeciation, folderCant)

