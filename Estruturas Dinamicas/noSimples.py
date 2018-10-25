#!/usr/bin/env python

# classe Nó da lista encadeada simples
class NoSimples:
    # construtor da classe Nó
    def __init__(self, proximo_no = None, dado = 0):
        self.proximo = proximo_no
        self.dado = dado
    #
    def __repr__(self):
        return '%s --> %s' % (self.dado, self.proximo)