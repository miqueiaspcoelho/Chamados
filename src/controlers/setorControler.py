import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import sqlite3
from sqlite3 import Error
from models.setor import Setor
from typing import List
import FreeSimpleGUI as sg

from controlers.databaseControler import DatabaseControler

class SetorControler:

    #insere dados na tabela de setores
    @staticmethod
    def insert_into_setores(database_name: str, data: list) -> None:
        """
        Adiciona um setor a tabela de setores
        try -> conecta ao banco de dados informado e caso o setor não tenha 
        sido cadastrado, cadastra na tabela de setores
        except -> informa o erro em caso de erro na operação anterior

        :param database_name: string
        :param data: list
        :return None
        """
        try:
            conn = DatabaseControler.conect_database(database_name)
            cursor = conn.cursor()
            for i in data:
                cursor.execute('''
                        INSERT OR IGNORE INTO Setores (Setor) VALUES (?);
                        ''', (i,))
                if cursor!= None:
                    sg.PopupTimed(f'Setor {i.upper()} cadastrado ou existente.')
            
        except Error as e:
            print(e)
            sg.PopupTimed('Erro ao inserir dados.')
        conn.commit()
        conn.close()
        
        
    #pegando todos os setores disponíveis no banco
    @staticmethod
    def get_setores(database_name: str) -> object:
        """
        Faz uma busca na tabela setores e retorna uma lista com todos os setores cadastrados
        try -> conecta ao banco de dados e seleciona todos os setores existentes da 
        tabela setores
        except -> informa o erro em caso de erro na operação anterior

        :param database_name: string
        :return rows: object
        """
        try:
            conn = DatabaseControler.conect_database(database_name)
            cursor = conn.cursor()
            cursor.execute('''
                    SELECT * FROM Setores;
                    ''')
            rows = cursor.fetchall()
            if rows == '' or rows is None or len(rows)==0:
                sg.PopupTimed('Não há dados cadastrados.')
                conn.close()
            return(rows)

        except Error as e:
            print(e)
            
            
    #atualiza a lista de setores
    @staticmethod
    def update_setor_list(database_name:str) -> list:
        """
        Responsável por fazer a atualização da lista de setores sempre que um novo setor é inserido.

        :param database_name:string
        :return options: list
        """
        setor_list = SetorControler.get_setores(database_name)
        options =[]
        if setor_list!= None or setor_list!="":
            aux=''
            for x in setor_list:
                aux = str(x[0])+ '  -  ' + x[1]
                options.append(aux)
            return options
        else:
            return options
        