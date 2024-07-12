import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.chamado import Chamado
from controlers.databaseControler import DatabaseControler

from typing import List
import PySimpleGUI as sg
import sqlite3
import sqlite3
from sqlite3 import Error

class ChamadoControler:
    chamados = []
    setores = []
    
    @classmethod
    def save_chamado(cls, chamado: Chamado) -> None:
        cls.chamados.append(chamado)
    
    @classmethod
    def show_chamados(cls) -> List[Chamado]:
        return cls.chamados
    
    @classmethod
    def insert_into_setores(cls, setor: str) -> None:
        cls.setores.append(setor)
        
        
    
    #inserindo um chamado no banco de dados
    @staticmethod
    def insert_into_chamados(database_name: str, data: list) -> None:
        """
        Adiciona um chamado na tabela de chamados

        :param name_db: string
        :param data: list
        :return void
        """
        try:
            conn = DatabaseControler.conect_database(database_name)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Chamados (Setor, Data, Item, Status, Descricao) VALUES (?,?,?,?,?);
                ''', (data.setor,data.data,data.item,data.status,data.descricao))
            sg.PopupTimed(
              'Dados inseridos com sucesso.')
            

        except Error as e:
            print(e)
            sg.PopupTimed('Erro ao inserir dados.')
        conn.commit()
        conn.close()
 
 
    #buscando todos os chamados
    @staticmethod
    def search_in_chamados_all(database_name: str) -> list:
        """
        Faz uma busca geral, ou seja, lista todos os chamados existentes.
        retorna todos os chamados existentes

        :param name_db: string
        :filter: string
        :return rows: list
        """
        try:
            conn = DatabaseControler.conect_database(database_name)
            cursor = conn.cursor()
            cursor.execute('''
            SELECT * FROM Chamados;
            ''')
            rows = cursor.fetchall()
            if rows == '' or rows is None or len(rows)==0:
              sg.PopupTimed('Não há dados para esse filtro.')
            
            return(rows)

        except Error as e:
            print(e)
            sg.PopupTimed('Erro na operação')
        conn.close()
 
    #pesquisando os dados por Id
    @staticmethod
    def search_in_chamados_id(database_name: str,filter: int) -> list:
        """
        Faz uma pesquisa na tabela de chamados de acordo o id único do chamado
        retornando todos os chamados referentes ao id informado.

        :param name_db: string
        :filter: string
        :return rows: list
        """
        try:
            conn = DatabaseControler.conect_database(database_name)
            cursor = conn.cursor()
            cursor.execute('''
            SELECT * FROM Chamados WHERE Id = ?;
            ''',(filter,))
            rows = cursor.fetchall()
            if rows == '' or rows is None or len(rows)==0:
                sg.PopupTimed(f'Não há dados para ID: {filter}')
                
            return(rows)

        except Error as e:
            print(e)
        conn.close()