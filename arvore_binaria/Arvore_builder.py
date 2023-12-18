from typing import List

from Arvore_binaria import ArvoreBinaria

def constroi_arvore(array: List[float], i: int = 0) -> [ArvoreBinaria]:
    """
    Constrói uma árvore binária a partir de uma lista.

    Args:
        array (List[float]): A array necessária para construir a árvore.
        i (int): Índice atual na lista.

    Returns:
        [ArvoreBinaria]: retorna o nó raiz construído.
    """
    # confere se deve parar (se i for >= significa que "acabaram os números")
    if i < len(array):
        valor = array[i]
        if (valor is not None):
            no_atual = ArvoreBinaria(valor)
            no_atual.esquerda = constroi_arvore(array, 2 * i + 1)
            no_atual.direita = constroi_arvore(array, 2 * i + 2)
            return no_atual
    return None
