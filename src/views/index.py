import sys
from pathlib import Path
import PySimpleGUI as sg

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from views.addSetor import AddSetor
from views.pesquisa import Pesquisa
from views.update import Update

from controlers.chamadoControler import ChamadoControler
from controlers.databaseControler import DatabaseControler
from controlers.setorControler import SetorControler

from models.chamado import Chamado
from models.database import Database
from models.setor import Setor
from models.widget1 import Widget1
from models.widget2 import Widget2
from models.widget3 import Widget3
from models.widget4 import Widget4
from models.widget5 import Widget5
from models.layout import Layout



'''
#verificando a junção                
data = str(input('Digite a data: '))
tipo = str(input('Digite o tipo: '))
status = str(input('Digite o status: '))
descricao = str(input('Digite a descricao: '))
setor = str(input('Digite o setor: '))

c1 = Chamado(data=data, tipo=tipo, status=status, descricao=descricao, setor=setor)
ChamadoControler.save_chamado(c1)
for i in ChamadoControler.show_chamados():
    print(i.data, i.descricao)
'''
#addSetor.add_setor() #tela setor
database = Database('Teste.db') #criação do banco, rodar uma vez


stest1 = Setor(name='stest7')
stest2 = Setor(name='stest6')
data_setores = [stest1.name]
cursor = DatabaseControler.conect_database(database.name)
DatabaseControler.create_table_chamados(cursor)
DatabaseControler.create_table_setores(cursor)

#SetorControler.insert_into_setores(database.name,data_setores)
#print(SetorControler.get_setores(database.name))

        
chamado_test = Chamado(setor='stest2', data='08/07/2024', item='pc',status='resolvido', descricao='teste 2 do refatoramento')
#ChamadoControler.insert_into_chamados(database.name, chamado_test)
#a= ChamadoControler.search_in_chamados_all(database.name)
#a = ChamadoControler.search_in_chamados_id(database.name, 2)


options= SetorControler.update_setor_list(database.name)
layout = Layout.show((Widget1.show(options)),
                Widget2.show(),
                Widget3.show(),
                Widget4.show(),
                Widget5.show()
                )
window = sg.Window('Gerenciador de chamados', layout ,resizable = True)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':

        #formatação das datas
        data_completa = values['day'] + '/' + values['month'] + '/' + values['year']

        #checando radio buttons marcados e pegando o valor
        lista_radio_buttons = []
        for x in values.keys():
            if values[x] == True:
                lista_radio_buttons.append(x)
        item = lista_radio_buttons[0]
        status = lista_radio_buttons[1]
        setor = values['setor'][0]
        descricao = values['description']
        
        chamado = Chamado(setor=setor, data=data_completa, item=item,status=status, descricao=descricao)
        ChamadoControler.insert_into_chamados(database.name, chamado)
    if event == 'add_setor':
        AddSetor.add_setor(database.name)
        option = SetorControler.update_setor_list(database.name)
        window['setor'].update(option)
    
    if event == 'Pesquisar':
        Pesquisa.open_window_pesquisa(database.name, 'Pesquisar', ['Id','Setor','Data','Item','Status','Descricao','Todos'], 'field_name', 'filter', 'Buscar', 'buscar')
    
    
    if event == 'update':
        Update.open_window_update(['Resolvido','Pendente','Manutenção', 'Troca', 'RealJet Aberto','RealJet Resolvido'], 'status', 'filter', 'confirmar', 'update')
        
        
window.close()
