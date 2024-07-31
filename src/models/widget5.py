import PySimpleGUI as sg
#WIDGET5 - status
'''cada registro de chamado precisa possuir um status, ou seja, se já foi concluído,
se está pendente, se foi repassado para outra empresa e como está a situação.
foi utilizada a mesma estratégia de radio buttons, dessa forma cada chamado possui um único status.
em breve será necessário criar a função de update no banco, com base no Id ser possível atualizar o status
do chamado desejado, pois, é nomal que com o passar do tempo eles alteram seu status'''

class Widget5:
    @staticmethod
    def show():
    
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
