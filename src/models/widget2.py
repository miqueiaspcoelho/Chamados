import FreeSimpleGUI as sg
#WIDGET2 - checkbox para marcar onde foi o problema
''''''

class Widget2:
    
    @staticmethod
    def show() -> object:
        """
        Responsável por organizar as opções de item disponíveis para serem selecionados
        a depender de onde foi efetuado o chamado.
        Caso a demanda tenha sido de computador, selecionar a opções correspondente
        e assim segue.
        Por padrão, a opção computador vem selecionada.
        Como os radios buttons pertencem a um mesmo group_id só é permitida a seleção
        de um único elemento, contornando erro de seleção dupla de uma maneira simples 
        e eficaz.
        A única função retorna o widget2 com as opções organizadas em colunas.
        
        :return widget2: object
        """
    
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