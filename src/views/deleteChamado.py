import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import PySimpleGUI as sg #aqui nesse ambiente não aceita algo instalado no venv
#import FreeSimpleGUI as sg

from models.setor import Setor
from models.widget7 import Widget7

from controlers.chamadoControler import ChamadoControler


class Delete:
    
    @staticmethod
    def open_window_delete(title:str, database_name: str, input_label:str, input_key:str, button_name1:str, button_name_key1:str,button_name2:str, button_name_key2:str) -> None:
        """
        Não recebe nenhum parâmetro de entrada. Renderiza uma janela onde fornece
        ao usuário o campo Id, com a finalidade de após isso fazer a exclusão do
        dado por meio do Id informado, dessa forma os erros ao excluir um chamado
        são minimizados

        :param None
        :return void
        """
        widget7 = Widget7.show(input_label, input_key, button_name1,button_name_key1,button_name2,button_name_key2)
        window = sg.Window(title, widget7, modal=True,element_justification='left')
        
        id_input=''
        rows=''
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
                
            if event == 'search':
                id_input = values[input_key]
                rows = ChamadoControler.search_in_chamados(database_name, 'Id', id_input)
                ChamadoControler.show_results(rows)
            
            if event == 'delete':
                ChamadoControler.delete_chamado(database_name, id_input)

        window.close()

        