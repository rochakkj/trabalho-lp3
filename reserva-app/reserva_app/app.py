from flask import Flask, render_template, request
from funcs import criar_sala, criar_reserva, salvar_dicionario_em_arquivo_sala, salvar_dicionario_em_arquivo_reserva



app = Flask("My App")



@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar-sala")
def salvar_produto():

    return render_template("cadastrar-sala.html")



@app.route("/reservar-sala")
def reservar_sala():
    return render_template("reservar-sala.html")

@app.route("/reservas")
def reservas():
    return render_template("reservas.html")

@app.route("/")
def listar_salas():
    return render_template("listar-salas.html")

@app.route("/detalhe-reserva")
def detalhe_reserva():
    return render_template("detalhe-reserva.html")


salvar_dicionario_em_arquivo_sala(criar_sala(1, 25, True, "lab", "é um lab"))
salvar_dicionario_em_arquivo_sala(criar_sala(2, 30, True, "lab", "é um lab"))

salvar_dicionario_em_arquivo_reserva(criar_reserva(1, "01-05-2020 - 8:00", "10-05-2020 - 10:00", True))



# (codigo, capacidade, ativa, tipo, descricao)

app.run()