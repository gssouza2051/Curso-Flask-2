from unicodedata import name
from flask import Flask, render_template, request, redirect, session, flash, url_for
import flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'alura'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql',
        usuario = 'postgres',
        senha='Pyw8fk1jjkzfUDwd4EtH',
        servidor='localhost',
        database='postgres'
    )

db = SQLAlchemy(app)

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


@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    return redirect(url_for('index'))

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo já existente!!')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)