# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_04-19.11.02 134264
# Run by Groth on Mon Mar 06 10:54:01 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=251.170288085938, 
    height=175.688873291016)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('C:/Users/Groth/Desktop/models_ml/tira_zero/tira_zero1.py', 
    __main__.__dict__)
#* IOError: (2, 'No such file or directory', 'tb1.csv')
#* File "C:/Users/Groth/Desktop/models_ml/tira_zero/tira_zero1.py", line 34, in 
#* <module>
#*     with open(csv_file_name) as f:
