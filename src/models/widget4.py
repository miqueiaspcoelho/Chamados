import FreeSimpleGUI as sg
#WIDGET4 - botões de ok cancelar e pesquisar
'''são os responsáveis por gerar ações com base na interação do usuário com as janelas
o botão de ok cadastra um novo chamado, independente de termos campos vazios ou não
o botão de cancelar fecha a janela
o botão de pesquisar abre uma nova janela para realizar uma busca'''

class Widget4:
    def show():
        widget4 = [[
            sg.Button('Cadastrar',key='insert', button_color="#2F4F4F"), 
            sg.Button('Pesquisar',key='search'),
            sg.Button('Excluir', key='delete'),
            sg.Button('Adicionar Setor', key='add_setor'),
            sg.Button('Atualizar Status', key='update_status'),
            sg.Button('Fechar', button_color='#8B0000', key='exit')],
            [sg.Input(key='file_import', visible=True, enable_events=True), sg.FileBrowse('Buscar Dados', button_color="#483D8B")],
            [sg.Button('Importar',key='import')],
            sg.Text('Desenvolvido por: Miquéias Coelho')
        ]
        return widget4
