# Uma classe é um modelo para um objeto. 
# Segundo a Python Software Fundation (PSF, 2020a), podemos considerar uma classe como uma forma de organizar 
# os dados (de um objeto) e seus comportamentos.



class PrimeiraClasse:
    def __init__(self):  # Método especial para inicialização de objetos
        self.nome = None  # Inicializa o atributo 'nome' como None ao criar um objeto

    def imprimir_mensagem(self):
        print("Olá, seja bem-vindo!")

# Criando uma instância da classe PrimeiraClasse
objeto1 = PrimeiraClasse()

# Definindo o atributo 'nome' do objeto
objeto1.nome = "Diego"

# Imprimindo o atributo 'nome'
print(objeto1.nome)

# Chamando o método 'imprimir_mensagem' da instância objeto1
objeto1.imprimir_mensagem()

#-----------------------------------------

class FuncionarioTecnico:
    nivel = 'Técnico'  # Atributo de classe para armazenar o nível

    def __init__(self, status):
        self.status = status  # Atributo de instância para armazenar o status do funcionário

# Criando instâncias da classe FuncionarioTecnico
func1 = FuncionarioTecnico('Ativo')
func2 = FuncionarioTecnico('Licença Mestrado')

# Imprimindo os atributos das instâncias
print(func1.nivel)  # Imprime o nível do funcionário 1
print(func2.nivel)  # Imprime o nível do funcionário 2
print(func1.status)  # Imprime o status do funcionário 1
print(func2.status)  # Imprime o status do funcionário 2

# ----------------------------------------------------------------

# import sqlite3


#  Conectando ao banco de dados
# conn = sqlite3.connect('aulaDB.db')

# # Criando um cursor para executar comandos SQL
# cursor = conn.cursor()

## como fazer um create table 
# # Criando a tabela fornecedor, se ela ainda não existir
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS fornecedor (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome_fornecedor TEXT,
#     cnpj TEXT,
#     cidade TEXT,
#     estado TEXT,
#     cep TEXT,
#     data_cadastro DATE
# )
# ''')

## Commit para confirmar as alterações no banco de dados
# conn.commit()

# # Fechando a conexão com o banco de dados
# conn.close()



# como executar um insert
# cursor = conn.cursor()
# cursor.execute("""
# INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
# VALUES ('Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
# """)
# conn.commit()