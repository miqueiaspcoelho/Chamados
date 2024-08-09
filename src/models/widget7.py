import FreeSimpleGUI as sg


class Widget7:
    @staticmethod
    def show(input_label:str, input_key:str, button_name1:str, button_name_key1:str, button_name2:str, button_name_key2:str) -> object:
        """
        Organizar e retorna o widget7, que é utilizado dentro da view deleteChamado.
        Possui um campo de texto e dois botões, um para busca de um chamado, exclusivamente pelo
        id informado, e outro para confirmar a exclusão do chamado.
        
        :param input_label: string
        :param input_key: string
        :param button_name1: string
        :param button_name_key1: string
        :param button_name2: string
        :param button_name_key2: string
        
        :return widget7: object
        """
        widget7 = [
                    [sg.Text(input_label.capitalize(), pad=(10,7)),sg.Input(tooltip='Digite corretamente de acordo com o filtro marcado',key=input_key)],
                    [sg.Button(button_name1.capitalize(), key=button_name_key1), sg.Button(button_name2.capitalize(), key=button_name_key2)],
                ]
        return widget7