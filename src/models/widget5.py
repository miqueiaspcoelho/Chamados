import FreeSimpleGUI as sg
#WIDGET5 - status
class Widget5:
    @staticmethod
    def show() -> object:
        """
        Possui um único método que irá organizar e retornar o elemento
        que contém as opções de status de um chamado.
        Por padrão o status resolvido vem selecionado.
        Como todos os elementos pertencem ao mesmo group_id, apenas um e somente um
        elemento pode ser selecionado.
        
        :return widget5:object
        """
        column1 = [
            [sg.Radio('Resolvido', group_id='status',key='Resolvido',default=True)],
            [sg.Radio('Aguardando',group_id='status',key='Aguardando')],
            [sg.Radio('Pendente',group_id='status',key='Pendente')]
        ]
        
        column2 = [
            [sg.Radio('Manutenção Preventiva',group_id='status',key='Manutenção Preventiva')],
            [sg.Radio('Manutenção Corretiva',group_id='status',key='Manutenção Corretiva')],
            [sg.Text('')]
        ]
        
        column3 = [
            [sg.Radio('Troca',group_id='status',key='Troca')],
            [sg.Radio('Reparo',group_id='status',key='Reparo')],
            [sg.Text('')]
        ]
        
        column4 = [
            [sg.Radio('Pedido Efetuado',group_id='status',key='Pedido Efetuado')],
            [sg.Radio('Pedido Recebido',group_id='status',key='Pedido Recebido')],
            [sg.Text('')]
        ]
        widget5 = [
            [sg.Text('Status', tooltip='Marque a atual condição da questão')],
            [
            sg.Column(column1),
            sg.Column(column2),
            sg.Column(column3),
            sg.Column(column4)
            ],
            [sg.HorizontalSeparator(color='gray')]
            ]
        return widget5
