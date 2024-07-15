import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import PySimpleGUI as sg #aqui nesse ambiente não aceita algo instalado no venv
#import FreeSimpleGUI as sg
from controlers.setorControler import SetorControler
from controlers.chamadoControler import ChamadoControler
from models.setor import Setor
from models.widget6 import Widget6

class Pesquisa:

    @staticmethod
    def open_window_pesquisa(database_name: str, title: str,values: list[str], values_key:str, input_key:str, button_name:str, button_name_key:str):
        """
        Renderiza uma janela que dá a opção de pesquisa ao usuário.
        A pesquisa ocorre por meio da seleção de um filtro e em seguida a correta escrita
        do valor desejado, de acordo com o filtro escolhido.
        Não recebe parâmetros de entrada

        :param None
        :return void
        """
        widget6 = Widget6.show(values, values_key, input_key, button_name,button_name_key)

        window = sg.Window(f'{title}', widget6, modal=True,element_justification='left')
        option=''
        filter=''
        rows=''
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == 'buscar':
                field_name = values['field_name']
                filter = values['filter']
                rows = ChamadoControler.search_in_chamados(database_name, field_name, filter)
                ChamadoControler.show_results(rows)
                

        window.close()
    
    