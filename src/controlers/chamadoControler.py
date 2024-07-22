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
    def search_in_chamados(database_name: str, field_name:str,  filter: str) -> list:
        """
        Faz uma pesquisa na tabela de chamados de acordo o id único do chamado
        retornando todos os chamados referentes ao id informado.

        :param name_db: string
        :filter: string
        :return rows: list
        """
        if field_name=="Todos":
            rows = ChamadoControler.search_in_chamados_all(database_name)
            return rows
        
        else:
            try:
                if field_name=="Descricao":
                    filter = '%'+filter+'%'
                    conn = DatabaseControler.conect_database(database_name)
                    cursor = conn.cursor()
                    cursor.execute(f'''
                    SELECT Id, Descricao, Data, Item, Status, Descricao FROM Chamados WHERE {field_name} LIKE ?;
                    ''',(filter,))
                    rows = cursor.fetchall()
                    if rows == '' or rows is None or len(rows)==0:
                        sg.PopupTimed(f'Não há dados para o(a): {field_name.upper()} informado (a)')
                    return(rows)

                    
                    
                conn = DatabaseControler.conect_database(database_name)
                cursor = conn.cursor()
                cursor.execute(f'''
                SELECT * FROM Chamados WHERE {field_name} = ?;
                ''',(filter,))
                rows = cursor.fetchall()
                if rows == '' or rows is None or len(rows)==0:
                    sg.PopupTimed(f'Não há dados para o(a): {field_name.upper()} informado (a)')
                return(rows)

            except Error as e:
                print(e)
            conn.close()
    
    @staticmethod
    def update_status_chamado (database_name: str, status:str, id: int) -> None:
        """
        Com base em id informado é feita a atualização do status
        (Resolvido, Pendente, Manutenção,
        RealJet Pendente, RealJet Resolvido).
        Como retorno há um popup que informa o sucesso ou falha na operaçao

        :param name_db: string
        :status: string
        :return void
        """
        id_list = DatabaseControler.select_all_id_from_chamados(database_name)
        
        try:
            if id in id_list:
                conn = DatabaseControler.conect_database(database_name)
                cursor = conn.cursor()
                cursor.execute('''
                UPDATE Chamados SET Status = ? WHERE Id = ?;
                ''',(status.lower(), id))
                sg.PopupTimed(f'Chamado {id} atualizado status para {status}')
                conn.commit()
                conn.close()
            else:
                sg.PopupTimed(f'Não há chamados para o id {id}')

        except Error as e:
            print(e)
            sg.PopupTimed('Erro na operação')
            
        
        
    @staticmethod
    def show_results(rows: list) -> None:
        """
        Recebe os dados já do banco de dados para serem exibidos em tela.
        Renderiza uma tela que faz a exibição de todos os itens que foram fornecidos
        dentro do vetor dado como parâmetro

        :param dados: list
        :return void
        """
        
        number = str(len(rows))
        if number == None:
            number = '0'
        headings=[' Id ', 'Setor','Data', 'Item','Status','Descrição']
        col_widths = list(map(lambda x:len(x)+4, headings))
        layout = [
            [sg.Text('Chamados', pad=(5, 10))],
            [sg.Table(values=rows,headings=headings,col_widths=col_widths, row_height=35, auto_size_columns=True, justification='left')],
            [sg.Text('Total: '),sg.Text(number)],
        ]
        window = sg.Window('Chamados', layout,modal=True,resizable = True)
        event, values = window.read()
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break

        window.close()
        
        
    def delete_chamado(database_name: str, id: str) -> None:
        """
        Com base em id informado um chamado é deletado do banco de dados
        Como retorno há um popup que informa o sucesso ou falha na operação.

        :param name_db: string
        :status: string
        :return void
        """
        try:
            conn = DatabaseControler.conect_database(database_name)
            cursor = conn.cursor()
            cursor.execute('''
            DELETE FROM Chamados WHERE Id = ?;
            ''',(id,))
            sg.PopupTimed('Registro deletado com sucesso')
            conn.commit()
            

        except Error as e:
            print(e)
            sg.PopupTimed('Erro na operação')
        conn.close()