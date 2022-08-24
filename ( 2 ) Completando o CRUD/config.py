

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql',
        usuario = 'postgres',
        senha='Pyw8fk1jjkzfUDwd4EtH',
        servidor='localhost',
        database='postgres'
    )