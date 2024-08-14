import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import FreeSimpleGUI as sg #aqui nesse ambiente não aceita algo instalado no venv
#import FreeSimpleGUI as sg
from controlers.setorControler import SetorControler
from models.setor import Setor

class AddSetor:

    @staticmethod
    def add_setor(database_name: str) -> None:
        """
        Recebe o nome do banco de dados ao qual deve se conectar.
        Renderiza uma janela onde fornece ao usuário um input para adicionar o nome do novo setor 
        a ser adicionado na tabela de setores do banco.
        A adição do setor ao banco dados, só ocorre caso o setor
        em questão ainda não esteja cadastrado.

        :param database_name: string
        :return None
        """
        layout = [
                [sg.Text('Setor: ',pad=(10,15)), sg.Input(key='setor_name', size=(None,1),do_not_clear=False)],
                [sg.Button('confirmar',key='confirm')]
                ]
        window = sg.Window('Adicionar Setor', layout, modal=True,element_justification='left')
        setor_name=''
        setor_list=[]
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == 'confirm':
                setor_name = values['setor_name']
                setor_name = setor_name.lower()
                s1 = Setor(name=setor_name)
                setor_list.append(s1.name)
                if s1.name not in SetorControler.get_setores(database_name):
                    SetorControler.insert_into_setores(database_name, setor_list)
                    setor_list=[]
                    

        window.close()
