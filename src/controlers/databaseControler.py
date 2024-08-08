import sqlite3
from sqlite3 import Error
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.database import Database
import FreeSimpleGUI as sg

class DatabaseControler:
    #conectando/criando o banco, caso ele não exista
    
    @staticmethod
    def conect_database(database_name: str) -> object:
        """
        Responsável por criar uma conexão com o banco de dados

        :param database_name: string
        :return connection: obj

        """
        try:
            conn = sqlite3.connect(database_name)
            print("Database Sqlite3.db formed.")
            return conn
        except Error as e:
            print(e)
            print('Erro na conexão')

    #criando a tabela dos chamados, caso não exista
    @staticmethod
    def create_table_chamados(cursor: object) -> None:
        """
        Caso não exista, cria uma tabela de chamados em um banco de dados sqlite3

        :param cursor: obj
        :return void
        """
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Chamados (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Setor varchar(30),
                Data date(10),
                Item varchar(15),
                Status varchar(15),
                Descricao varchar(255)
                );
            ''')
            print('Tabela criada ou já existente')
        except Error as e:
            print(e)
            print('Erro ao criar a tabela')
    
    #criando a tabela dos setores, caso não exista
    @staticmethod
    def create_table_setores(cursor: object) -> None:
        """
        Caso não exista, cria uma tabela de setores em um banco de dados sqlite3

        :param cursor: obj
        :return void
        """
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Setores (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Setor varchar(30) NOT NULL,
                CONSTRAINT Setor_Unique UNIQUE (Setor)
                );
            ''')
            print('Tabela criada ou já existente')

        except Error as e:
            print(e)
            print('Erro ao criar a tabela')
    
    @staticmethod
    def select_all_id_from_chamados(database_name:str):
        id_elements_list=[]
        try:
            conn = DatabaseControler.conect_database(database_name)
            cursor = conn.cursor()
            rows = cursor.execute('''SELECT Id FROM Chamados''')
            if rows!= None or rows!='':
                for element in rows:
                    id_elements_list.append(element[0])
                
            return id_elements_list
            
        except Error as e:
            print(e)
        