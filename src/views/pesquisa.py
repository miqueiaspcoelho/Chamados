import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import FreeSimpleGUI as sg #aqui nesse ambiente não aceita algo instalado no venv
#import FreeSimpleGUI as sg
from controlers.setorControler import SetorControler
from controlers.chamadoControler import ChamadoControler
from models.setor import Setor
from models.widget6 import Widget6

class Pesquisa:

    @staticmethod
    def open_window_pesquisa(title: str, database_name: str, values: list[str], values_key:str, input_key:str, button_name:str, button_name_key:str) -> None:
        """
        Renderiza uma janela que dá a opção de pesquisa ao usuário.
        A pesquisa ocorre por meio da seleção de um filtro e em seguida a correta escrita
        do valor desejado, de acordo com o filtro escolhido.
        Os parâmetros recebidos são de configuração para a renderização da janela.
        Apenas o database_name é utilizado para conexão com o banco de dados.

        :param title: string
        :param database_name: string
        :param values: list
        :param values_key: string
        :param input_key: string
        :param button_name: string
        :param button_name_key: string
        
        :return None
        """
        widget6 = Widget6.show(values, values_key, input_key, button_name,button_name_key)

        window = sg.Window(title, widget6, modal=True,element_justification='left')
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
    
    