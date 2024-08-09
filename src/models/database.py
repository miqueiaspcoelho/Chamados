import sqlite3
from sqlite3 import Error
class Database:
    def __init__(self, name: str) -> None:
        """
        Criação do banco de dados, possui um único atributo nome.
        A estrutura do banco está em databaseControler
        try -> instancia o banco 
        except -> em caso de erro informa o erro
        
        :param name: string
        
        :return None
        """
        self.name = name
        try:
            conn = sqlite3.connect(self.name) #já irá instanciar o banco
        except Error as e:
            print(e)
            print('Erro')
            
 