from Arvore_binaria import ArvoreBinaria
from Arvore_builder import constroi_arvore

# array aleatória para teste
array = [4, 3, 6, 1, 2, 5, 7]
arvore_b = constroi_arvore(array)

# Imprimir a árvore inicial através da função imprime_arvore()
print("Árvore inicial:")
arvore_b.imprime_arvore()

# Aplicar heapify
arvore_b.heapify()

# árvore pós convertida em heap
print("\nÁrvore após heapify:")
arvore_b.imprime_arvore()

# array ordenada dos números
print("\nLista ordenada:")
print(arvore_b.to_array())
