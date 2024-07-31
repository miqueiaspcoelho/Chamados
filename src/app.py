import sys
from pathlib import Path
import PySimpleGUI as sg

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from views.addSetor import AddSetor
from views.pesquisa import Pesquisa
from views.update import Update
from views.deleteChamado import Delete

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


database = Database('DATABASEFILE.db') #criação do banco

cursor = DatabaseControler.conect_database(database.name)
DatabaseControler.create_table_chamados(cursor)
DatabaseControler.create_table_setores(cursor)

options= SetorControler.update_setor_list(database.name)
layout = Layout.show((Widget1.show(options)),
                Widget2.show(),
                Widget3.show(),
                Widget4.show(),
                Widget5.show()
                )
window = sg.Window('Gerenciador de chamados', layout ,resizable = True, element_justification='left')
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'exit'): # if user closes window or clicks exit
        break
        
    if event == 'insert':
        #formatação das datas
        data_completa = values['day'] + '/' + values['month'] + '/' + values['year']

        #checando radio buttons marcados e pegando o valor
        lista_radio_buttons = []
        for x in values.keys():
            if values[x] == True:
                lista_radio_buttons.append(x)
        item = lista_radio_buttons[0]
        status = lista_radio_buttons[1]
        
        if values['setor']!=[]:
            setor = values['setor'][0]
            
        else:
            setor = 'empty'
            
        descricao = values['description']
        check = ChamadoControler.verification_valid_options(setor, data_completa, item, status)
        
        if check == True:
            chamado = Chamado(setor=setor, data=data_completa, item=item, status=status, descricao=descricao)
            ChamadoControler.insert_into_chamados(database.name, chamado)
        if check == False:
            pass
        
    if event == 'add_setor':
        AddSetor.add_setor(database.name)
        option = SetorControler.update_setor_list(database.name)
        window['setor'].update(option)
    
    if event == 'search':
        Pesquisa.open_window_pesquisa('Pesquisar', database.name, ['Id','Setor','Data','Item','Status','Descricao','Todos'], 'field_name', 'filter', 'Buscar', 'buscar')
    
    
    if event == 'update_status':
        Update.open_window_update('Atualizar Status',database.name,['Resolvido','Pendente','Manutenção', 'Troca', 'RealJet Aberto','RealJet Resolvido'], 'status', 'filter', 'confirmar', 'update')
    
   
    if event == 'delete':
        Delete.open_window_delete('Excluir Chamado',database.name,'id', 'id', 'buscar', 'search','deletar','delete')
    
    if  event=='import':
        database_import = Database(values['file_import'])
        window['setor'].update(SetorControler.update_setor_list(database_import.name))
        database = database_import
        
        
        
window.close()
