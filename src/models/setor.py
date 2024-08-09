#classe setor
class Setor:
    
    def __init__(self, name: str) -> None:
        """
        Modelo do objeto setor, possuindo o atributo nome
        
        :param name: string
        
        :return None
        """
        self.name = name.lower()