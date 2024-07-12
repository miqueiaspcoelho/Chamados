import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import sqlite3
from sqlite3 import Error
from models.setor import Setor
from typing import List
import PySimpleGUI as sg

from controlers.databaseControler import DatabaseControler

class SetorControler:

    #insere dados na tabela de setores
    @classmethod
    def insert_into_setores(cls, database_name: str, data: list) -> None:
        """
        Adiciona um setor a tabela de setores

        :param database_name: string
        :param data: list
        :return void
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
    @classmethod
    def get_setores(cls, database_name: str) -> object:
        """
        Faz uma busca na tabela setores e retorna uma lista com todos os setores cadastrados

        :param name_db: string
        :return rows: list
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
            
    @classmethod
    def update_setor_list(cls, database_name):
        """
        Responsável por fazer a atualização da lista de setores sempre que um novo setor é inserido.
        Não recebe parâmetros de entrada.

        :param None
        :return options: list
        """
        setor_list = SetorControler.get_setores(database_name)
        setor_list.sort()
        options =[]
        aux=''
        for x in setor_list:
            aux = str(x[0])+ '  -  ' + x[1]
            options.append(aux)
        return options
        