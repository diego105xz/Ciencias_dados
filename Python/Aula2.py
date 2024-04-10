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



#Algoritmo de Ordenação por inserção (Insertion Sort)
#nesse algoritmo ele faze comparação entre primeiro e segundo valor do vetor, depois segundo e terceiro valor do vetor...
def executar_insertion_sort(lista):
	n = len(lista)
	for i in range(1, n):
	    valor_inserir = lista[i] 
	    j = i - 1
	        
	    while j >= 0 and lista[j] > valor_inserir:
	        lista[j + 1] = lista[j]
	        j -= 1
	        lista[j + 1] = valor_inserir
	    
	return lista
	
	
lista = [10, 8, 7, 3, 2, 1]
executar_insertion_sort(lista)

#Algoritmo de ordenação por seleção (selection sort)
#percorre vetor ou lista múltiplas vezes, procuranod o menor valor e organizando do menor para o maior.
def executar_selection_sort(lista):
    n = len(lista)
    
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if lista[j] < lista[min]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista


lista = [10, 8, 7, 3, 2, 1]
executar_selection_sort(lista)


#Algoritmo de ordenação por bolha (bubble sort)
#percorre vetor ou lista múltiplas vezes. A cada passagem, os pares de elementos adjacentes do vetor são comparados e, depois disso, são trocados se não estiverem ordenados.
#não é indicado para uma grande quantidade de dados.

def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [10, 8, 7, 3, 2, 1]
executar_bubble_sort(lista)


#Algoritmo de ordenação merge sort
#O vetor é dividido em duas metades e, em seguida, novamente é dividido novamente em outras duas partes – ao repetir a divisão do vetor, em um determinado momento teremos vários vetores com apenas um elemento.
def executar_merge_sort(lista):
    if len(lista) <= 1: return lista
    else:
        meio = len(lista) // 2
        esquerda = executar_merge_sort(lista[:meio])
        direita = executar_merge_sort(lista[meio:])
        return executar_merge(esquerda, direita)

    
def executar_merge(esquerda, direita):
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    return sub_lista_ordenada


lista = [10, 8, 7, 8, 3, 2, 1]
executar_merge_sort(lista)


#Algoritmo de ordenação quick sort
#o pivô, que corresponde ao elemento do meio do vetor. Depois, nós trocamos os elementos no início do vetor com os elementos do final 