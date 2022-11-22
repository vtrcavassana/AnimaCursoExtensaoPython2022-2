# importar sqlite3
import sqlite3

# criar conexão dc_universe.db
conn = sqlite3.connect('dc_universe.db')

# criar cursor
c = conn.cursor()

# exibir todos os registros da tabela pessoas cada registro numa linha
c.execute("SELECT * FROM pessoas")
for linha in c.fetchall():
    print(linha)

# pedir ao usuário para inserir um nome de um nome de um personagem
nome = input("Digite o nome de um personagem: ")

# pedir ao usuário para inserir nome civil de um personagem
nome_civil = input("Digite o nome civil de um personagem: ")

# pedir ao usuário para inserir 1 para herói ou 2 para vilão
tipo = input("Digite 1 para herói ou 2 para vilão: ")
if tipo == '1':
    tipo = 'Herói(na)'
else:
    tipo = 'Vilã(o)'

# comando para inserir incremento automático em pessoa_id
c.execute("INSERT INTO pessoas (nome, nome_civil, tipo) VALUES (?, ?, ?)", (nome, nome_civil, tipo))

# comando para inserir os dados digitados pelo usuário na tabela pessoas
# c.execute("INSERT INTO pessoas VALUES ('{}', '{}', '{}', '{}')".format(pes, nome, nome_civil, tipo))

# exibir todos os registros da tabela pessoas cada registro numa linha
c.execute("SELECT * FROM pessoas")
for linha in c.fetchall():
    print(linha)

# pedir ao usuário para inserir em qual grupo o personagem pertence 1 para Sociedade da Justiça da América, 2 para Liga da Justiça, 3 para Tropa dos Lanternas Verdes, 4 para Esquadrão Suicida
grupo = input("Digite 1 para Sociedade da Justiça da América, 2 para Liga da Justiça, 3 para Tropa dos Lanternas Verdes, 4 para Esquadrão Suicida: ")
if grupo == '1':
    grupo = 1
elif grupo == '2':
    grupo = 2
elif grupo == '3':
    grupo = 3
else:
    grupo = 4

# comando para inserir o personagem no grupo escolhido, na tabela pessoas_grupo
c.execute("INSERT INTO pessoas_grupos (pessoa_id, grupo_id) VALUES (?, ?)", (c.lastrowid, grupo))


# exibir todos os registros da tabela grupos cada registro numa linha
c.execute("SELECT * FROM grupos")
for linha in c.fetchall():
    print(linha)

# exibir nome de cada personagem e seu grupo
c.execute("SELECT pessoas.nome, grupos.nome FROM pessoas INNER JOIN pessoas_grupos ON pessoas.pessoa_id = pessoas_grupos.pessoa_id INNER JOIN grupos ON pessoas_grupos.grupo_id = grupos.grupo_id")
for linha in c.fetchall():
    print(linha)

# salvar alterações
conn.commit()

# fechar conexão
conn.close()