import FreeSimpleGUI as sg

#WIDGET3 - descrição
'''O campo de descrição é um completo, para melhor entender a causa do chamado, como foi solucionado
o que fazer para evitar, melhores abordagens futuras com base em históricos passados'''

class Widget3:

    staticmethod
    def show():
        widget3 = [
            [sg.Text('Descrição do problema')],
            [sg.Multiline(key='description',size = (None, 5),no_scrollbar = True,do_not_clear=False)]
            ]
        return widget3
