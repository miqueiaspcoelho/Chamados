import PySimpleGUI as sg

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
'''criação do layout da janela utilizando os widgets, mais fácil de dar manutenção e posicionar
cada widget é posicionado de maneira individual dentro do layout, dessa forma ele é a junção
de cada um dos pequenos elementos construídos anteriormente.'''

class Layout:
    
    @staticmethod
    def show(w1: object,w2: object,w3: object,w4: object,w5: object):
        layout = [
            [sg.Column(w1),
            sg.VerticalSeparator(pad=0),
            sg.Column(w2)],
            w5,
            w3,
            w4
            ]
        return layout