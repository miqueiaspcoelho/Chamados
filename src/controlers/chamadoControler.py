import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.chamado import Chamado
from controlers.databaseControler import DatabaseControler


from typing import List
import FreeSimpleGUI as sg
import sqlite3
import sqlite3
from sqlite3 import Error

class ChamadoControler:
        
    
    #inserindo um chamado no banco de dados
    @staticmethod
    def insert_into_chamados(database_name: str, data: list) -> None:
        """
        Adiciona um chamado na tabela de chamados. 
        try -> conecta ao banco e executa a query para insetir os dados do chamado
        execpt -> mostra tela de erro e printa o erro ocorrido

        :param database_name: string
        :param data: list
        :return None
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
        retorna todos os chamados existentes.
        try -> conecta ao banco e executa a query para buscar todos os chamados
        execpt -> mostra tela de erro e printa o erro ocorrido

        :param database_name: string
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
 
    
    #pesquisando os dados por algum campo especifico do chamado
    @staticmethod
    def search_in_chamados(database_name: str, field_name:str,  filter: str) -> list:
        """
        Faz uma pesquisa na tabela de chamados de acordo uma categoria de filtro informado e o valor do mesmo.
        Retorna todos os resultados encontrados de acordo com o filtro informado.
        Possui algumas excessões.
        field_name == Todos -> search_in_chamados_all
        
        field_name == Descricao ou Setor -> a query é feita de forma a pesquisar por
        palavras chaves, se a descrição de um chamado tiver a palavra indica ele é retornado
        Também é utilizado bloco try execpt como nas funções acima

        :param database_name: string
        :param field_name: string
        :param filter: string
        :return rows: list
        """
        if field_name=="Todos":
            rows = ChamadoControler.search_in_chamados_all(database_name)
            return rows
        
        else:
            try:
                if field_name=="Descricao" or field_name=="Setor":
                    filter = '%'+filter+'%'
                    conn = DatabaseControler.conect_database(database_name)
                    cursor = conn.cursor()
                    cursor.execute(f'''
                    SELECT * FROM Chamados WHERE {field_name} LIKE ?;
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
    
    
    #atualizando o status de um chamado com base no id do chamado
    @staticmethod
    def update_status_chamado (database_name: str, status:str, id: str) -> None:
        """
        Com base em id informado é feita a atualização do status, dentro das opções setadas no view de update.
        Essa atualização em banco funciona por meio de querys, na tela é exibido pop up de sucesso ou falha
        Também é utilizado bloco try execpt como nas funções acima

        :param database_name: string
        :param status: string
        :return None
        """
        id_list = DatabaseControler.select_all_id_from_chamados(database_name)
        try:
            if int(id) in id_list:
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
            
        
    
    #exibe os chamados retornados de uma busca
    @staticmethod
    def show_results(rows: list) -> None:
        """
        Recebe os dados já do banco de dados para serem exibidos em tela.
        Renderiza uma tela que faz a exibição de todos os itens que foram fornecidos
        dentro do vetor dado como parâmetro.
        Utiliza mais elementos de view, porém, como não havia uma tela especifica e é 
        uma chamada de função para exibir os chamados, foi adicionada dentro do controler de chamados

        :param row: list
        :return None
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
        
        
    #faz a exclusão de um chamado com base no id informado
    def delete_chamado(database_name: str, id: str) -> None:
        """
        Com base em id informado um chamado é deletado do banco de dados
        Como retorno há um popup que informa o sucesso ou falha na operação.
        Também é utilizado bloco try execpt como nas funções acima

        :param database_name: string
        :param id: string
        
        :return None
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
    
    
    #verifica de um chamado pode não ser inserido, se é um chamado válido
    @staticmethod
    def verification_valid_options(setor: str, data:str, item: str, status=str) -> bool:
        """
        Verifica se é possível ou não o cadastro do chamado com base nas informações adicionadas em tela pelo usuário
        tem por objetivo minimizar erros de inserção, tornando obrigatório que todos os chamados tenham:
        setor válido, data, item, status, sendo facultativo a descrição

        :param setor: string
        :param data: string
        :param item: string
        :param: status: string
        
        :return boll
        """
        list_check = [setor, item, status]
        
        for option in list_check:
            if len(option)<1 or option=='empty' or len(data)<10:
                sg.PopupTimed(f'Preencha Corretamente as Informações')
                return False
            else:
                return True
