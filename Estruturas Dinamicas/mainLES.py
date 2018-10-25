#!/usr/bin/env python

from listaEncadeadaSimples import listaEncadeadaSimples
from noSimples import NoSimples

# instanciando a classe listaEncadeadaSimples
les = listaEncadeadaSimples()
# verificando se, inicialmente, a lista esta vazia
les.esta_vazia_lista_encadeada_simples()

# inserindo elementos na lista 
for i in range(20):
    les.inserir_elemento(les, i)
print("Lista: ", les, "\n")

# busca um possível elemento na lista
elemento_busca = les.buscar_elemento(les,10)
if elemento_busca is None:
    print("Este elemento não possui a lista \n")
else:
    print(str(elemento_busca) + "\n")

# removendo os elementos na lista
for j in range(15):
    les.remover_elemento(j)
print("Lista", les, "\n")

# verificando novamente se lista esta vazia
les.esta_vazia_lista_encadeada_simples()


