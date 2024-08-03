from flask import Flask, render_template, request, redirect, url_for
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

    adicionar_dicionario_user(criar_user(gerar_codigo_unico(exibe_dicionario_user()), request.form['nome'], request.form['email'], request.form['password']))

    return render_template("cadastro.html")

@app.route("/cadastrar-sala")
def cadastrar_sala():


    return render_template("cadastrar-sala.html")

@app.route("/cadastrar-sala", methods=['POST'])
def cadastrar_sala_post():
    #codigo, capacidade, tipo, descricao
    codigo_limpo = int(request.form['codigo'].strip())
    a = verificar_codigo_unico(exibe_dicionario_sala(), codigo_limpo)
    if a == True: 
        adicionar_dicionario_sala(criar_sala(request.form['codigo'], request.form['tipo'], request.form['capacidade'], request.form['descricao']))
    elif a == False:
        return redirect(url_for('cadastrar_sala', erro = "Código já existe!"))
    erro = request.args.get('erro')
    return render_template("cadastrar-sala.html", erro=erro)


@app.route("/reservar-sala")
def reservar_sala():    

    return render_template("reservar-sala.html", salas = exibe_dicionario_sala())


@app.route("/reservar-sala", methods=['POST'])
def reservar_sala_post():
    #codigo, sala, data_hora_inicio, data_hora_fim
    adicionar_dicionario_reserva(criar_reserva(gerar_codigo_unico(exibe_dicionario_reserva()), request.form['sala'], request.form['inicio'], request.form['fim'], "User 1"))
    return render_template("reservar-sala.html")


@app.route("/reservas")
def reservas():
    return render_template("reservas.html", reservas = exibe_dicionario_reserva())

@app.route("/")
def listar_salas():
    return render_template("listar-salas.html", salas = exibe_dicionario_sala())

@app.route("/detalhe-reserva")
def detalhe_reserva():
    return render_template("reserva/detalhe-reserva.html")

    

# (codigo, capacidade, ativa, tipo, descricao)

app.run()