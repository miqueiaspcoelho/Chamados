import PySimpleGUI as sg

class Widget1:
    
    @staticmethod
    def show(options):
        default_selected=['empty']
        if len(options)==0:
            options = default_selected
        widget1 = [
                [sg.Text('Data do atendimento: '),sg.Input(key='day', size=(3,1),do_not_clear=False),sg.Text('/'),sg.Input(key='month',size=(3,1),do_not_clear=False),sg.Text('/'),sg.Input(key='year',size=(5,1),do_not_clear=False)],
                [sg.HorizontalSeparator(color='gray')],
                [sg.Text('Selecione o Setor', tooltip='Setor de atendimento')],
                [sg.Listbox(options, default_values=options[0], key='setor',size=(30, 7))], 
                [sg.HorizontalSeparator(color='gray')]
                ]
        return widget1