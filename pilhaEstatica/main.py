#!/usr/bin/env python

from pilha import pilhaEstatica
from fila import filaEstatica

# TESTE DA PILHA
p = pilhaEstatica()
p.esta_vazia()

for i in range(20):
    p.inserir_elemento(i)
p.mostrar_pilha()

for j in range(15):
    p.remover_elemento()
p.mostrar_pilha()

p.esta_vazia()

# TESTE DA FILA
f = filaEstatica()
f.esta_vazia()

for l in range(20):
    f.inserir_elemento(l)
f.mostrar_fila()

for k in range(15):
    f.remover_elemento()
f.mostrar_fila()

f.esta_vazia()