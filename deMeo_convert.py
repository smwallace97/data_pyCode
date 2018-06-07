# deMeo_convert.py
# Sydney Wallace
# Mount Holyoke College
# Mineral Spectroscopy Lab
# Professor M. Darby Dyar
# 07 jun 2018

import os, csv, glob

# initialize arrays
txtfiles = [] #holds all .txt files
dmfiles = [] #holds all DeMeo file names

# appends txtfiles into dmfiles array
for txtfile in glob.glob('X:\\asteroids_n_meteorites_2018\\Original_data\\DeMeo_asteroid_data\\DeMeo2009Data\\*'):
    txtfiles.append(txtfile)
    fileName = txtfile.split(".")
    dmfiles.append(txtfile)
    
print(txtfiles)
# open a csv file for each atxt file
# for atxt in txtfiles:
#     with open(atxt, 'r') as csvfile:
#         reader = csv.reader(csvfile)
