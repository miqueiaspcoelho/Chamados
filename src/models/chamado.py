#classe chamado

class Chamado:
    
    def __init__(self, setor: str, 
                data:str,
                item: str, 
                status: str, 
                descricao: str):
        self.setor = setor.lower()
        self.data = data
        self.item = item.lower()
        self.status = status.lower()
        self.descricao = descricao.lower()
