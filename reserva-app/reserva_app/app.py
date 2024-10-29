from flask import Flask, render_template, request, redirect, url_for
from reserva_app.conexao_bd import conexao_abrir, conexao_fechar
from reserva_app.funcs import *


app = Flask("My App")



@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=['POST'])
def cadastro_post():
    con = conexao_abrir("localhost", "estudante1", "123", "reserva_app")
    usuarioInserir(con, request.form['nome'], request.form['email'], request.form['password'])

    return render_template("cadastro.html")

@app.route("/cadastrar-sala")
def cadastrar_sala():
    
    return render_template("cadastrar-sala.html")

@app.route("/cadastrar-sala", methods=['POST'])
def cadastrar_sala_post():
    
    con = conexao_abrir("localhost", "estudante1", "123", "reserva_app")
    tipo = int(request.form['tipo'])
    if (tipo == 1):
        tipoString = "Laboratório de Informática"
    elif (tipo == 2):
        tipoString = "Laboratório de Química"
    elif (tipo == 3):
        tipoString = "Sala de Aula"
    else:
        tipoString = "Sem tipo"
    salaInserir(con, request.form['capacidade'], tipoString, request.form['descricao'])
    return render_template("cadastrar-sala.html")


@app.route("/reservar-sala")
def reservar_sala():    
    con = conexao_abrir("localhost", "estudante1", "123", "reserva_app")
    return render_template("reservar-sala.html", salas = salaListar(con), usuarios = usuarioListar(con))


@app.route("/reservar-sala", methods=['POST'])
def reservar_sala_post():
    con = conexao_abrir("localhost", "estudante1", "123", "reserva_app")
    dataI = request.form['inicio'].replace('T', ' ')
    dataF = request.form['fim'].replace('T', ' ')
    
    reservaInserir(con, dataI, dataF, request.form['usuario'], request.form['sala'])
    return render_template("reservar-sala.html")


@app.route("/reservas")
def reservas():
    con = conexao_abrir("localhost", "estudante1", "123", "reserva_app")
    return render_template("reservas.html", reservas = reservaListar(con))

@app.route("/")
def listar_salas():
    
    con = conexao_abrir("localhost", "estudante1", "123", "reserva_app")
    return render_template("listar-salas.html", salas = salaListar(con))

@app.route("/detalhe-reserva")
def detalhe_reserva():
    return render_template("reserva/detalhe-reserva.html")

    


app.run()