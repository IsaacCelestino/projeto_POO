class ArvoreBinaria:
    def __init__(self, valor: float) -> None:
        """Método de inicialização da ArvoreBinaria

        Args:
            valor (str): valor do nó da raiz
        """
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def heapify(self) -> None:
        """Método para executar o heap

        """
        while True:
            maior = self.valor
            filho = None
            if self.esquerda and self.esquerda.valor > maior:
                maior = self.esquerda.valor
                filho = self.esquerda
            if self.direita and self.direita.valor > maior:
                maior = self.direita.valor
                filho = self.direita
            if maior == self.valor or filho is None:
                break
            # Troca de valores entre o nó atual e o filho
            self.valor, filho.valor = filho.valor, self.valor
            # Atualiza a referência para o nó atual
            self = filho

    def to_array(self) -> list:
        """Método para converter a árvore binária em array de volta

        Returns:
            list: array com os valores agora organizados
        """
        # Implementação básica: converter a árvore para array
        resultado = [self.valor]
        if self.esquerda:
            #método para estender uma lista adicionando elementos de outra luista 
            #Se ele possuir filho a esquerda , estende a lista resultado com o
            #restante da chamada recursiva
            resultado.extend(self.esquerda.to_array())
        if self.direita:
            resultado.extend(self.direita.to_array())
        return resultado

    def imprime_arvore(self, nivel: int = 0, prefixo: str = "") -> None:
        """
        Imprime na tela uma forma de representar a árvore binária.

        Args:
            nivel (int): Nível do nó na árvore.
            prefixo (str): Prefixo a ser exibido antes do valor do nó (esquerda, direita).
        """
        if(prefixo == ""):
            prefixo = "Raiz: "
        print(" " * (nivel * 4) + prefixo + str(self.valor))
        # Verifica onde possúi filhos para chamar o método recursivamente
        if self.esquerda:
            self.esquerda.imprime_arvore(nivel + 1, "Esquerda: ")
        if self.direita:
            self.direita.imprime_arvore(nivel + 1, "Direita: ")