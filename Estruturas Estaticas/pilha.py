#!/usr/bin/env python

class pilhaEstatica:
    # contrutor da classe pilhaEstatica
    def __init__(self):
        self.pilha = []
    # inserindo um elemento na pilha
    def inserir_elemento(self, dado):
        return self.pilha.append(dado)
    # removendo um elemento na pilha (remoção pelo topo)
    def remover_elemento(self):
        self.pilha.pop()
    # verificando se a pilha está vazia
    def esta_vazia(self):
        if self.pilha == []:
            print("A pilha está vazia")
        else:
            print("A pilha não está vazia")
    # mostrando os elementos da pilha
    def mostrar_pilha(self):
        print(self.pilha)