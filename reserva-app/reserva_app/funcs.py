import csv


def salvar_dicionario_em_arquivo_sala(a: dict):

    with open("salas.csv", "a") as arquivo:
        lista_valores: list[str] = []
                    
        for key in a:
            value = a[key]
                    
            lista_valores.append(fr'"{key}:{value}"')
                
        sala = ','.join(lista_valores) + '\n'
            
        arquivo.write(sala)


def salvar_dicionario_em_arquivo_reserva(a: dict):

    with open("reservas.csv", "a") as arquivo:
        lista_valores: list[str] = []
                    
        for key in a:
            value = a[key]
                    
            lista_valores.append(fr'"{key}:{value}"')
                
        sala = ','.join(lista_valores) + '\n'
            
        arquivo.write(sala)

def criar_sala (codigo, capacidade, ativa, tipo, descricao):
    return{
        "codigo": codigo,
        "capacidade": capacidade,
        "ativa": ativa,
        "tipo": tipo,
        "descricao": descricao

    }


def criar_reserva(codigo, sala, data_hora_inicio, data_hora_fim):
    return {
        "codigo": codigo,
        "sala": criar_sala(1, 25, True, "lab", "é um lab"),
        "data_e_hora_de_inicio": data_hora_inicio,
        "data_e_hora_do_fim": data_hora_fim,
        "ativa": True
    }


# def criar_sala(codigo, capacidade, ativa, tipo, descricao):
#     sala = sala_modelo(codigo, capacidade, ativa, tipo, descricao)
#     return sala





