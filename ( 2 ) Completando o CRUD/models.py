from jogoteca import db

class Jogos(db.Model):
    id = db.column(db.Integer, primary_key=True, autoincremente=True)
    nome = db.column(db.String(50),nullable=False)
    categoria = db.column(db.String(40),nullable=False)
    console = db.column(db.String(20),nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nickname = db.column(db.String(8), primary_key=True)
    nome = db.column(db.String(20),nullable=False)
    senha = db.column(db.String(100),nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name