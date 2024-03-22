from configuration import getConnection, getScriptPath
from scriptParser import Parser

modulo = 'Principal'

connection = getConnection()
print(connection)
if connection is None: 
    exit

scriptPath, sep = getScriptPath()
print(sep)
print(scriptPath)
print(type(scriptPath))
if scriptPath is None: 
    exit

parserer = Parser(scriptPath, sep)
print(parserer.scripts)
print(parserer.scripts[0])