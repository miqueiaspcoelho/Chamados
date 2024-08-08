import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import FreeSimpleGUI as sg #aqui nesse ambiente não aceita algo instalado no venv
#import FreeSimpleGUI as sg

from models.setor import Setor
from models.widget6 import Widget6

from controlers.chamadoControler import ChamadoControler

class Update:
    
    @staticmethod
    def open_window_update(title:str, database_name: str, values: list[str], values_key:str, input_key:str, button_name:str, button_name_key:str) -> None:
        """
        Renderiza uma janela, que permite ao usuário informar o Id de qual chamado deseja atualizar
        o campo status, campo este que pode receber os seguintes valores:
        'Resolvido','Pendente','Manutenção', 'Troca', 'RealJet Aberto','RealJet Resolvido'.
        A seleção de tais valores funciona por meio de um menu de opções.
        Não recebe parâmetros de entrada

        :param None
        :return void
        """
        
        
        widget6 = Widget6.show(values, values_key, input_key, button_name,button_name_key)
        window = sg.Window(title, widget6, modal=True,element_justification='left')
        id=''
        status=''
        rows=''
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "update":
                ChamadoControler.update_status_chamado(database_name, values[values_key], values[input_key])
        window.close()
        