#!/usr/bin/env python

from noSimples import NoSimples

# classe da lista encadeada simples
class listaEncadeadaSimples:
    #
    def __init__(self):
        self.cabeca = None
    
    #
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
