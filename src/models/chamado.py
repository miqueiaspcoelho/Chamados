#classe chamado
class Chamado:
    
    def __init__(self, setor: str, 
                data:str,
                item: str, 
                status: str, 
                descricao: str) -> None:
        """
        Modelo de objeto chamado
        
        :param setor: string
        :param data: string
        :param item: string
        :param status: string
        :param descricao: string
        
        return None
        """
        
        self.setor = setor.lower()
        self.data = data
        self.item = item.lower()
        self.status = status.lower()
        self.descricao = descricao.lower()
