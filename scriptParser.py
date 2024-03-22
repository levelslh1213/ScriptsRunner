import os
import configparser as cp

module = 'Parser'

class Parser(object):
    def __init__(self):
        pass

    def getScripts(self, scriptsPath, sep):
        if scriptsPath == '':
            print( 'Execution error: ' + '\nModule: ' + module + '\nFunction: getScripts' + '\n Description: Caminho de script vazio!')
            return None
        
        if (not(os.path.exists(scriptsPath))):
            print( 'Execution error: ' + '\nModule: ' + module + '\nFunction: getScripts' + '\n Description: Caminho de script inválido!')
            return None
        
        fileContent = ''
        
        try:            
            with open(scriptsPath, encoding="utf8") as file:
                fileContent = file.read()
                finalScript  = fileContent.split(sep)
        except Exception as e:
            print('Execution error: ' + '\nModule: ' + module + '\nFunction: getScripts' + '\n Description: Erro ao realizar divisão de scripts!' + '\nException: ' + e)
            return None
        
        return finalScript