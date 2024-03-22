import configparser
import cryptocode

module = 'Connection'

def getConnection():
    passwordKey = "Comparer"
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')

    try:
        server = cfg.get('ConnectionString', 'serverOrigem')
        owner = cfg.get('ConnectionString', 'ownerOrigem')
        sid = cfg.get('ConnectionString', 'sidOrigem')
        username = cfg.get('ConnectionString', 'usernameOrigem')
        password = cfg.get('ConnectionString', 'passwordOrigem')
        password = cryptocode.decrypt(password, passwordKey)
        connectionString = f'{username}/{password}@{server}/{sid}'
    except configparser.Error as e:
        print('Execution error: ' + '\nModule: ' + module + '\nFunction: getScriptPath' + '\n Description: Erro ao buscar caminho do script!' + '\nExcetion: ' + e)
        return None, None, None, None  # Retorna como Nulo se existir erro ao ler o arquivo ini
    
    return connectionString, owner

def getScriptPath():
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')

    try: 
        path = cfg.get('Scripts', 'path')
        sep = cfg.get('Scripts', 'separator')
    except configparser.Error as e:
        print('Execution error: ' + '\nModule: ' + module + '\nFunction: getScriptPath' + '\n Description: Erro ao buscar caminho do script!' + '\nExcetion: ' + e)
        return None
    
    return path, sep