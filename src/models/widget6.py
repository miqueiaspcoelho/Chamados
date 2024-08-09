import FreeSimpleGUI as sg


class Widget6:
    @staticmethod
    def show(values: list[str], values_key:str, input_key:str, button_name:str, button_name_key:str ) -> object:
        """
        Widget resposável por organizar e retornar a janela que será usada na tela de pesquisar
        Cada valor da lista de valores será exibido dentro de um menu de opções,
        permitindo a seleção de um único valor.
        
        :param values: list
        :param values_key: string
        :param input_key: string
        :param button_name: string
        :param: button_name_key: string
        
        :return widget6: object
        """
        widget6 = [
                    [sg.Text('Filtro: ', pad=(10,10)),sg.OptionMenu(values=values, key=values_key)],
                    [sg.Text('Digite:', pad=(10,10)),sg.Input(tooltip='Digite corretamente de acordo com o filtro marcado',key=input_key)],
                    [sg.Button(button_name.capitalize(), key=button_name_key)],
                ]
        return widget6