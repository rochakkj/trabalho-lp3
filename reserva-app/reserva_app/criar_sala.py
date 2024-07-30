import csv


def salvar_dicionario_em_arquivo(a: dict):
    with open("produtos.csv", "a") as arquivos_produtos:
        b = csv.DictReader(a)
        salas =[]

        for linha in b: 
            salas.appendlist(list(linha.values()))
        arquivos_produtos.write(salas)

def criar_sala (codigo, capacidade, ativa, tipo, descricao):
    return{
        "codigo": codigo,
        "capacidade": capacidade,
        "ativa": ativa,
        "tipo": tipo,
        "descricao": descricao

    }


def reserva_modelo(codigo, sala, data_hora_inicio, data_hora_fim):
    return {
        "codigo": codigo,
        "sala": sala,
        "data_e_hora_de_inicio": data_hora_inicio,
        "data_e_hora_do_fim": data_hora_fim,
        "ativa": True
    }


# def criar_sala(codigo, capacidade, ativa, tipo, descricao):
#     sala = sala_modelo(codigo, capacidade, ativa, tipo, descricao)
#     return sala





