import PySimpleGUI as sg
#WIDGET4 - botões de ok cancelar e pesquisar
'''são os responsáveis por gerar ações com base na interação do usuário com as janelas
o botão de ok cadastra um novo chamado, independente de termos campos vazios ou não
o botão de cancelar fecha a janela
o botão de pesquisar abre uma nova janela para realizar uma busca'''

class Widget4:
    def show():
        widget4 = [sg.Button('Ok',key='Ok'), 
            sg.Button('Cancel', key='Cancel'),
            sg.Button('Pesquisar',key='Pesquisar'), 
            sg.Button('Adicionar Setor', key='add_setor')
        ]
        return widget4
