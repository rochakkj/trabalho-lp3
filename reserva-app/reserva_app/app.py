from flask import Flask, render_template, request
from criar_sala import criar_sala, salvar_dicionario_em_arquivo



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


salvar_dicionario_em_arquivo(criar_sala(1, 25, True, "lab", "é um lab"))



# (codigo, capacidade, ativa, tipo, descricao)

app.run()