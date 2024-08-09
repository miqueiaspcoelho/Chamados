import FreeSimpleGUI as sg

class Widget1:
    
    @staticmethod
    def show(options: list) -> object:
        """
        Elemento 1 que é usado no layout principal. 
        Possui um método show, responsável por retornar o elemento a ser exibido
        Consiste da Lista de setores presentes no banco de dados, porém, caso 
        não tenha ainda setores cadastrados atribui o valor 'empty' como elemento
        da lista de exibição e o seleciona por padrão
        Em caso de setores cadastrados, por padrão, a primeira opção da lista
        virá selecionada ao rodar o script app.py
        
        :param options: list
        
        :return widget1: object
        """
        default_selected=['empty']
        if len(options)==0:
            options = default_selected
        widget1 = [
                [sg.Text('Data do atendimento: '),sg.Input(key='day', size=(3,1),do_not_clear=False),sg.Text('/'),sg.Input(key='month',size=(3,1),do_not_clear=False),sg.Text('/'),sg.Input(key='year',size=(5,1),do_not_clear=False)],
                [sg.HorizontalSeparator(color='gray')],
                [sg.Text('Selecione o Setor', tooltip='Setor de atendimento')],
                [sg.Listbox(options, default_values=options[0], key='setor',size=(40, 7))], 
                [sg.HorizontalSeparator(color='gray')]
                ]
        return widget1