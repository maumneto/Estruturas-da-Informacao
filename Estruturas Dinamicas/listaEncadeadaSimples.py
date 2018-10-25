#!/usr/bin/env python

from noSimples import NoSimples

# classe da lista encadeada simples
class listaEncadeadaSimples:
    
    # construtor da classe
    def __init__(self):
        self.cabeca = None
    
    # funcao para representar a lista encadeada simples
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    # insercao de um elemento na lista
    def inserir_elemento(self, lista, novo_dado):
        novo_no = NoSimples(novo_dado)
        novo_no.proximo = lista.cabeca
        lista.cabeca = novo_no

    # remocao de um elemento na lista encadeada simples
    def remover_elemento(self, valor):
        if self.cabeca == None:
            print("Impossivel remover de lista vazia! \n")
        else:
            if self.cabeca.dado == valor:
                self.cabeca = self.cabeca.proximo
            else:
                anterior = None
                corrente = self.cabeca
                while corrente and corrente.dado != valor:
                    anterior = corrente
                    corrente = corrente.proximo
                if corrente is True:
                    anterior.proximo = corrente.proximo
                else:
                    anterior.proximo = None

    # buscando um elemento na lista encadeada simples
    def buscar_elemento(self, lista, valor):
        corrente = lista.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        return corrente

    # verificando se a lista esta vazia ou nao
    def esta_vazia_lista_encadeada_simples(self):
        if self.cabeca == None:
            print("A lista está vazia \n")
        else:
            print("A lista NÃO está vazia \n")
