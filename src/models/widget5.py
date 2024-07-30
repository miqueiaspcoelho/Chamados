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
        widget5 = [
            [sg.Text('Status', tooltip='Marque a atual condição da questão')],
            [sg.Radio('Resolvido', group_id='status',key='Resolvido',default=True),sg.Radio('Pendente',group_id='status',key='Pendente'), sg.Radio('Manutenção',group_id='status',key='Manutenção'),sg.Radio('Troca',group_id='status',key='Troca') ],
            [sg.Radio('RealJet Aberto', group_id='status',key='RealJet Aberto'),sg.Radio('RealJet Resolvido', group_id='status',key='RealJet Resolvido')],
            [sg.HorizontalSeparator(color='gray')]
            ]
        return widget5
