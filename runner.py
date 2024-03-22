import cx_Oracle

class Runner(object): 
    def __init__(self):
        self.__connectionString = None
        self.__connection = None
        self.__cursor = None

    def runScript(self, script):
        self.__cursor.execute(script)

        return self.__cursor.fetchall()
    
    