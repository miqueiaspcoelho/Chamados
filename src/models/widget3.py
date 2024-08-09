import FreeSimpleGUI as sg

#WIDGET3 - descrição
class Widget3:

    @staticmethod
    def show() -> object:
        """
        Possui um único método que é responsável por organizar e retornar o widget3.
        Criação do campo para descrição de um chamado, é um elemento que é semelhante
        a um bloco de notas, ou seja, aceita a entrada de várias linhas de texto.
        O campo de descrição é importante para compreender melhor a causa do problema,
        bem como, foi resolvido.
        
        :return widget3: object
        """
        widget3 = [
            [sg.Text('Descrição do problema')],
            [sg.Multiline(key='description',size = (None, 5),no_scrollbar = True,do_not_clear=False)]
            ]
        return widget3
