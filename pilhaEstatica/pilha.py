class pilhaEstatica:
    
    def __init__(self):
        self.pilha = []
    
    def inserir_elemento(self, dado):
        return self.pilha.append(dado)
    
    def remover_elemento(self):
        self.pilha.pop()
    
    def mostrar(self):
        return