#!/usr/bin/env python

class filaEstatica:
    # contrutor da classe filaEstatica
    def __init__(self):
        self.fila = []
    # inserindo um elemento na fila
    def inserir_elemento(self, dado):
        return self.fila.append(dado)
    # removendo um elemento na fila (remoção pelo topo)
    def remover_elemento(self):
        self.fila.pop(0)
    # verificando se a fila está vazia
    def esta_vazia(self):
        if self.fila == []:
            print("A fila está vazia")
        else:
            print("A fila não está vazia")
    # mostrando os elementos da fila
    def mostrar_fila(self):
        print(self.fila)