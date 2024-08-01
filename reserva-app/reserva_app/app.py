from flask import Flask, render_template, request
from reserva_app.funcs import *


app = Flask("My App")



@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar-sala")
def cadastrar_sala():


    return render_template("cadastrar-sala.html")

@app.route("/cadastrar-sala", methods=['POST'])
def cadastrar_sala_post():
    #codigo, capacidade, tipo, descricao
    adicionar_dicionario_sala(criar_sala(request.form['codigo'], request.form['tipo'], request.form['capacidade'], request.form['descricao']))


    return render_template("cadastrar-sala.html")


@app.route("/reservar-sala")
def reservar_sala():

    return render_template("reservar-sala.html", salas = exibe_dicionario_sala())


@app.route("/reservar-sala", methods=['POST'])
def reservar_sala_post():
    #codigo, sala, data_hora_inicio, data_hora_fim
    adicionar_dicionario_reserva(criar_reserva(gerar_codigo_unico(exibe_dicionario_reserva()), request.form['sala'], request.form['inicio'], request.form['fim']))
    return render_template("reservar-sala.html")


@app.route("/reservas")
def reservas():
    return render_template("reservas.html")

@app.route("/")
def listar_salas():
    return render_template("listar-salas.html", salas = exibe_dicionario_sala())

@app.route("/detalhe-reserva")
def detalhe_reserva():
    return render_template("reserva/detalhe-reserva.html")


    

# (codigo, capacidade, ativa, tipo, descricao)

app.run()