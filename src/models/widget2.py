import FreeSimpleGUI as sg
#WIDGET2 - checkbox para marcar onde foi o problema
'''cada radio button pertence ao mesmo grupo, dessa forma, cada chamado pode possuir
apenas uma categoria de item, uma maneira simples e eficaz de permitir uma seleção única'''

class Widget2:
    
    @staticmethod
    def show():
        column1 = [
            [sg.Radio('Computador', group_id='item', key='Computador', default=True)],
            [sg.Radio('Rede', group_id='item',key='Rede')],
            [sg.Radio('Mouse', group_id='item',key='Mouse')],
            [sg.Radio('Office', group_id='item', key='Office')]
        ]
        
        column2 = [
            [sg.Radio('Impressora', group_id='item', key='Impressora')],
            [sg.Radio('Telefone', group_id='item',key='Telefone')],
            [sg.Radio('Teclado', group_id='item',key='Teclado')],
            [sg.Radio('Outro', group_id='item', key='Outro')]
        ]
        widget2 = [
                [sg.Text('Selecione o tipo', tooltip='Marque em quais itens foi o problema')],
                [sg.Column(column1), sg.Column(column2)],
                [sg.HorizontalSeparator(color='gray')]
        ]
        return widget2