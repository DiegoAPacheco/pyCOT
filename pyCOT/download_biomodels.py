#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:28:44 2023

@author: tveloz
"""

# main.py (or another script)

from pyCOT_constructor import *
from pyCOT_closure_structure import *
import networkx as nx
from File_manipulation import *
import matplotlib.pyplot as plt

path='/home/tveloz/Dropbox/Public/AcademicWork/Europe/CLEA/Postdocs/TempletonPostdoc/sftw/networks/biomodels_all'
link_address="https://www.ebi.ac.uk/biomodels/BIOMD0000001079"
url=link_address    
filename=path+"BIOMODEL_test"
download_webpage(url, filename)

# for i in range(0,2):
#     for j in range(0,10):
#         for z in range(0,10):
#             for w in range(0,10):
#                 number=str(i)+str(j)+str(z)+str(w)

