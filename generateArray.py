import random

#Usado para gerar arrays grandes e variados para testar os algoritmos de ordenação, com tamanho e distruibuições personalizáveis.
def gerateArray(size, distribution):

    if distribution == "aleatorio":
        # Gera 'size' números aleatórios entre 0 e 'size'
        return [random.randint(0, size) for _ in range(size)]
        
    elif distribution == "ordenado":
        # Retorna uma lista crescente
        return list(range(size))
        
    elif distribution == "inverso":
        # Retorna uma lista em ordem decrescente
        return list(range(size, 0, -1))
        
    elif distribution == "repetidos":
        # Escolhe números de um universo muito pequeno
        # para garantir uma alta taxa de repetição no array gerado
        universo_pequeno = [1, 2, 3, 4, 5]
        return [random.choice(universo_pequeno) for _ in range(size)]
        
    else:
        raise ValueError("Distribuição inválida.")