from datetime import datetime

class Venda:
    def __init__(self, produto_id, quantidade, data_venda=None, id=None):
        self.id = id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.data_venda = data_venda or datetime.now()