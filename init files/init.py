## This file will run every time you open the program

print(
    '''
    =============================================================
    |                                                           | 
    |                                                           |
    |                                                           |
    |       Hello! Welcome to the Python Terminal Logger!       |
    |        Please choose one of below to get started:         |
    |                                                           |
    |                                                           |
    |                                                           |
    =============================================================
    '''
)


import importlib

moduleName = input('Enter module name:')
importlib.import_module(moduleName)