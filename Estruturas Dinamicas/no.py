#!/usr/bin/env python

# classe Nó da lista encadeada simples
class No:
    # construtor da classe Nó
    def __init__(self, proximo = None, dado = 0):
        self.proximo = proximo
        self.dado = dado
    #
    def __repr__(self):
        return '%s --> %s' % (self.dado, self.proximo)