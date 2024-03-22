from configuration import getConnection, getScriptPath
from scriptParser import Parser
from runner import Runner

modulo = 'Principal'

connectionString, owner = getConnection()
print(connectionString)
if connectionString is None: 
    exit

scriptPath, sep = getScriptPath()
if scriptPath is None: 
    exit

parserer = Parser()
scripts = parserer.getScripts(scriptsPath=scriptPath, sep= sep)
print(scripts[0])

runner = Runner(connectionString)

# script = 'SELECT * FROM SISTEMA_VERSAO;'
# print(str(runner.runScript(script)))


