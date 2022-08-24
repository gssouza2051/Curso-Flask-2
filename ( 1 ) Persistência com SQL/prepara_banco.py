import psycopg2

print("Conectando...")
def conecta_db():
  con = psycopg2.connect(host='localhost',
                         database='postgres',
                         user='postgres',
                         password='Pyw8fk1jjkzfUDwd4EtH')
  return con
conn = conecta_db()
cursor = conn.cursor()
# criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
      CREATE TABLE public.jogos (
      id SERIAL,
      nome varchar(50) NOT NULL,
      categoria varchar(40) NOT NULL,
      console varchar(20) NOT NULL,
      PRIMARY KEY (id)
      ) ''')
TABLES['Usuarios'] = ('''
      CREATE TABLE public.usuarios (
      nome varchar(20) NOT NULL,
      nickname varchar(8) NOT NULL,
      senha varchar(100) NOT NULL,
      PRIMARY KEY (nickname)
      )''')
for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except Exception as e:
            print(e)
# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("Bruno Divino", "BD", "alohomora"),
      ("Camila Ferreira", "Mila", "paozinho"),
      ("Guilherme Louro", "Cake", "python_eh_vida")
]
cursor.executemany(usuario_sql, usuarios)
cursor.execute('select * from public.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])
# inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
      ('Tetris', 'Puzzle', 'Atari'),
      ('God of War', 'Hack n Slash', 'PS2'),
      ('Mortal Kombat', 'Luta', 'PS2'),
      ('Valorant', 'FPS', 'PC'),
      ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
      ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(jogos_sql, jogos)
cursor.execute('select * from public.jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])
# commitando se não nada tem efeito
conn.commit()
cursor.close()
conn.close()