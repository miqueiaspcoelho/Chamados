import PySimpleGUI as sg


class Widget6:
    @staticmethod
    def show(values: list[str], values_key:str, input_key:str, button_name:str, button_name_key:str ) -> object:
        widget6 = [
                    [sg.Text('Filtro: ', pad=(10,10)),sg.OptionMenu(values=values, key=values_key)],
                    [sg.Text('Digite:', pad=(10,10)),sg.Input(tooltip='Digite corretamente de acordo com o filtro marcado',key=input_key)],
                    [sg.Button(button_name, key=button_name_key)],
                ]
        return widget6