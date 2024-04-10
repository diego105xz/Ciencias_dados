# Aula 1

# Python possui 3 Tipos de variáveis: String, Inteiro e float

# Ordem para resolver problemas matemáticos:
# parêteses, exponenciação, multiplicação, divisão, soma e subtração

# Estruturas condicionais
codigo_compra = 1

if codigo_compra == 1:
    print("Compra à vista.")
elif codigo_compra == 2:
    print("Compra a prazo no boleto.")
elif codigo_compra == 3:
    print("Compra a prazo no cartão.")
else:
    print("Código não cadastrado")


login = input("Digite o seu login:")
senha = input("Digite sua senha: ")
if login == "diego" and senha == "123":
    print("Bem-vindo Diego")
elif login == "userpy02" and senha == "teste02":
    print("Bem-vindo userpy02")
elif login == "userpy03" and senha == "teste03":
    print("Bem-vindo userpy03")
elif login == "userpy04" and senha == "teste04":
    print("Bem-vindo userpy04")
else:
    print("Login falhou!")


contagem = 0
for contagem in range(1,10):
    print(contagem)


contagem = 0
while(contagem < 10):
    print(contagem)
    contagem = contagem + 1

#---------------------------------------------------

# Built-in em Python
# abs(): Retorna o valor absoluto de um número.
# delattr(): Exclui um atributo de um objeto.
# hash(): Retorna o valor de hash de um objeto.
# memoryview(): Cria uma visualização da memória de um objeto.
# set(): Cria um conjunto.
# all(): Retorna True se todos os elementos de um iterável forem verdadeiros.
# dict(): Cria um dicionário.
# help(): Fornece ajuda interativa.
# min(): Retorna o menor elemento de um iterável.
# setattr(): Define o valor de um atributo de um objeto.
# any(): Retorna True se qualquer elemento de um iterável for verdadeiro.
# dir(): Retorna uma lista de nomes de atributos de um objeto.
# hex(): Converte um número inteiro em uma representação hexadecimal.
# next(): Retorna o próximo item de um iterador.
# slice(): Cria um objeto de fatia para fatiar sequências.
# ascii(): Retorna uma representação ASCII de um objeto.
# divmod(): Retorna o quociente e o resto da divisão de dois números.
# id(): Retorna o identificador único de um objeto.
# object(): Cria um novo objeto base.
# sorted(): Retorna uma lista ordenada de elementos.
# bin(): Converte um número inteiro em uma representação binária.
# enumerate(): Retorna um iterador de tuplas indexadas.
# input(): Lê a entrada do usuário como uma string.
# oct(): Converte um número inteiro em uma representação octal.
# staticmethod(): Transforma um método em um método estático.
# bool(): Converte um valor em um booleano.
# eval(): Avalia uma expressão Python.
# int(): Converte um valor em um número inteiro.
# open(): Abre um arquivo.
# str(): Converte um valor em uma string.
# breakpoint(): Chama o depurador.
# exec(): Executa código Python dinamicamente.
# isinstance(): Verifica se um objeto é uma instância de uma classe.
# ord(): Retorna o valor ASCII de um caractere.
# sum(): Retorna a soma dos elementos de um iterável.
# bytearray(): Cria um objeto de array de bytes.
# filter(): Filtra elementos de um iterável usando uma função.
# issubclass(): Verifica se uma classe é uma subclasse de outra.
# pow(): Retorna a potência de um número.
# super(): Retorna um objeto proxy que delega chamadas de métodos a uma classe pai.
# bytes(): Cria um objeto de bytes.
# float(): Converte um valor em um número de ponto flutuante.
# iter(): Retorna um iterador.
# print(): Imprime valores na saída padrão.
# tuple(): Cria uma tupla.
# callable(): Verifica se um objeto é chamável.
# format(): Formata um valor usando uma especificação de formato.
# len(): Retorna o comprimento de um objeto.
# property(): Cria uma propriedade de classe.
# type(): Retorna o tipo de um objeto.
# chr(): Retorna o caractere representado pelo código Unicode.
# frozenset(): Cria um conjunto imutável.
# list(): Cria uma lista.
# range(): Cria uma sequência de números.
# vars(): Retorna o dicionário de atributos de um objeto.
# classmethod(): Transforma um método em um método de classe.
# getattr(): Retorna o valor de um atributo de um objeto.
# locals(): Retorna o dicionário de variáveis locais.
# repr(): Retorna a representação de string de um objeto.
# zip(): Combina iteráveis em uma lista de tuplas.
# compile(): Compila uma expressão Python.
# globals(): Retorna o dicionário de variáveis globais.
# map(): Aplica uma função a todos os itens em um iterável.
# reversed(): Retorna um iterador reverso.
# __import__(): Importa um módulo.
# complex(): Cria um número complexo.
# hasattr(): Verifica se um objeto tem um determinado atributo.
# max(): Retorna o maior elemento de um iterável.
# round(): Arredonda um número para uma quantidade específica de casas decimais.

#---------------------------------------------------

# A sintaxe de uma função em Python é feita com:

# A palavra reservada def.
# O nome da função.
# Os parênteses que indicam se existem ou não parâmetros para a função.
# E o comando return (que é opcional);



def meu_nome():
    return print("Diego")

meu_nome()

def soma(a, b):
    resultado = a + b
    return print(resultado)

soma(1, 3)