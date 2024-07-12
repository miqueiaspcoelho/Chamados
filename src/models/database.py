import sqlite3
from sqlite3 import Error
class Database:
    def __init__(self, name: str):
        self.name = name
        try:
            conn = sqlite3.connect(self.name) #já irá instanciar o banco
        except Error as e:
            print(e)
            print('Erro')
            
 