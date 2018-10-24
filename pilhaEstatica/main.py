from pilha import pilhaEstatica

p = pilhaEstatica()
p.esta_vazia()

for i in range(20):
    p.inserir_elemento(i)
p.mostrar_pilha()

for j in range(15):
    p.remover_elemento()
p.mostrar_pilha()

p.esta_vazia()