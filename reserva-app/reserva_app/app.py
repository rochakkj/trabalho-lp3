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
    #Pegando valores do form, nome, descricao, etc
    #codigo, capacidade, tipo, descricao
    adicionar_dicionario_sala(criar_sala(request.form['tipo'], request.form['codigo'], request.form['capacidade'], request.form['descricao']))


    return render_template("cadastrar-sala.html")


@app.route("/reservar-sala")
def reservar_sala():
    #codigo, sala, data_hora_inicio, data_hora_fim
    #criar_reserva(request.form['codigo'], request.form['sala'], request.form['data_hora_inicio'], request.form['data_hora_fim'])
    return render_template("reservar-sala.html")

@app.route("/reservas")
def reservas():
    return render_template("reservas.html")

@app.route("/")
def listar_salas():
    return render_template("listar-salas.html")

@app.route("/detalhe-reserva")
def detalhe_reserva():
    return render_template("reserva/detalhe-reserva.html")


    



# (codigo, capacidade, ativa, tipo, descricao)

app.run()