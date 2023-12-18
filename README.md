# Arvore_binaria

Programa que reorganiza uma array através de um função.

## Instalação

Para instalar execute:

```
python setup.py install
```

## Uso

Exemplo de uso do módulo `arvore_binaria`:

```py
from Arvore_binaria import ArvoreBinaria
from Arvore_builder import build_arvore_from_array

# array aleatória para teste
array = [4, 2, 6, 1, 3, 5, 7]
arvore_b = build_arvore_from_array(array)

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
```