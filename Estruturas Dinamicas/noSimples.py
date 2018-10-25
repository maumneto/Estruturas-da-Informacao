#!/usr/bin/env python

# classe Nó da lista encadeada simples
class NoSimples:
    # construtor da classe Nó
    def __init__(self, dado = 0, proximo_no = None):
        self.dado = dado
        self.proximo = proximo_no
        
    #
    def __repr__(self):
        return '%s --> %s' % (self.proximo, self.dado)