# Listas, tuplas, set, dicionário em Python

# array mutavel
frutas = ['abacaxi', 'uva', 'limao', 'laranja']

# capturando o primeiro elemento do array
print(frutas[0])

# capturando o ultimo elemento do array
print(frutas[-1])

# adicionando um novo elemento no array
frutas.append('morango')
print(frutas)

# fatiar o array em pedaço
print(frutas[2:])


# for item in sequencia:
# Faça algo com o item
material = ['lapis', 'borracha', 'caderno', 'caneta', 'mochila']
for numero in material:
    print(numero)

# imprimir string
string = "Python"
for caractere in string:
    print(caractere)

# imprimir range
for i in range(5):
    print(i)

# imprimir numeros pares de um range
pares = []
for i in range(10):
    if i % 2 == 0:
        pares.append(i)
print(pares)


# lista de tuplas
lista_tuplas = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]


# objeto
cadastro = {
    'nome': 'Diego',
            'idade': 30,
            'cidade': 'São Paulo'
}

print(cadastro['nome'])
# alterando objeto
cadastro['idade'] = 31

print(cadastro['idade'])


# Busca

def pesquisarFilmes(lista, filme):
    posicao = 0
    encontrado = False

# a regra do and not signfica: Isso significa que o loop continuará enquanto posicao for menor que o comprimento da lista e encontrado for False.
# Ou seja, ele continuará até que ou todas as posições na lista tenham sido verificadas ou até que o filme seja encontrado na lista.
# Assim que encontrado se tornar True, o loop será interrompido.
    while posicao < len(lista) and not encontrado:
        if lista[posicao] == filme:
            encontrado = True
        else:
            posicao = posicao + 1

    return encontrado


filmes = ["Star Wars", "O Senhor dos Anéis", "Matrix",
          "Star Trek", "Os Vingadores", "Harry Potter"]


print(pesquisarFilmes(filmes, "Matrix"))
print(pesquisarFilmes(filmes, "De Volta para o Futuro"))

# ---------------------------------------------------

# Busca sequencia = Vai verificar de 1 a 1 elemento até encontrar o resultado
def busca_sequencial(lista, elemento):
    pos = 0
    encontrado = False

    while pos < len(lista) and not encontrado:
        if lista[pos] == elemento:
            encontrado = True
        else:
            pos = pos+1

    return encontrado


testelista = [2, 10, 8, 15, 18, 20, 12, 1]
print(busca_sequencial(testelista, 5))
print(busca_sequencial(testelista, 15))


# Busca Sequencial ordenada = Vai verificar de 1 a 1 elemento até encontra-lo, porem pode demorar menos pois o vetor está ordenado
def busca_sequencial_ordenada(lista, elemento):
    pos = 0
    encontrado = False
    para = False
    while pos < len(lista) and not encontrado and not para:
            if lista[pos] == elemento:
                    encontrado = True
            else:
                if lista[pos] > elemento:
                    para = True
                else:
                    pos = pos+1

    return encontrado
    
testelista = [1, 2, 8, 10, 13, 15, 18, 20]
print(busca_sequencial_ordenada(testelista, 5))
print(busca_sequencial_ordenada(testelista, 15))



# Busca binária = ao encontrar o valor central de uma sequência, a divide em duas partes, reduzindo ainda mais o tempo de busca

def busca_binaria(lista, elemento):
        minimo = 0 
        maximo = len(lista)-1
        encontrado = False
    
        while minimo <= maximo and not encontrado:
            meio_lista = (minimo + maximo)//2
            if lista[meio_lista] == elemento:
                encontrado = True
            else:
                if elemento < lista[meio_lista]:
                    maximo = meio_lista-1
                else:
                    minimo = meio_lista+1
    
        return encontrado
    
testelista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(busca_binaria(testelista, 14))

