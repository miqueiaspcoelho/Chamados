import FreeSimpleGUI as sg

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.widget1 import Widget1
from models.widget2 import Widget2
from models.widget3 import Widget3
from models.widget4 import Widget4
from models.widget5 import Widget5


#LAYOUT PRINCIPAL
class Layout:
    
    @staticmethod
    def show(w1: object,w2: object,w3: object,w4: object,w5: object) -> object:
        """
        Recebe vários layouts e é reponsável por fazer a junção entre eles.
        Assim retorna um único objeto layout contendo uma série de elementos
        passados por parâmetro.
        Dessa forma alterar a posição dos itens, acrescentar mais itens,
        trocar itens na tela principal, fica mais prática e evita erros de 
        formatação.
        
        :param w1: object
        :param w2: object
        :param w3: object
        :param w4: object
        :param w5: object
        
        :return layout: object
        """
        layout = [
            [sg.Column(w1),
            sg.VerticalSeparator(pad=0),
            sg.Column(w2)],
            w5,
            w3,
            w4
            ]
        return layout