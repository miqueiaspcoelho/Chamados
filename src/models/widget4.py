import PySimpleGUI as sg
#WIDGET4 - botões de ok cancelar e pesquisar
'''são os responsáveis por gerar ações com base na interação do usuário com as janelas
o botão de ok cadastra um novo chamado, independente de termos campos vazios ou não
o botão de cancelar fecha a janela
o botão de pesquisar abre uma nova janela para realizar uma busca'''

class Widget4:
    def show():
        widget4 = [
            sg.Button('Cadastrar',key='Ok'), 
            sg.Button('Pesquisar',key='Pesquisar'),
            sg.Button('Excluir', key='delete'),
            sg.Button('Adicionar Setor', key='add_setor'),
            sg.Button('Atualizar Status', key='update'),
            sg.Button('Fechar', button_color='#8B0000', key='Cancel')
        ]
        return widget4
