class tabela:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def insert(self): #subjetivo
        raise NotImplementedError("Método 'insert' deve ser implementado nas subclasses")
    
    def update(self): #subjetivo
        raise NotImplementedError("Método 'update' deve ser implementado nas subclasses")
    
    def delete(self): #subjetivo
        raise NotImplementedError("Método 'update' deve ser implementado nas subclasses")
    
    def select(self): #subjetivo
        raise NotImplementedError("Método 'update' deve ser implementado nas subclasses")
    

