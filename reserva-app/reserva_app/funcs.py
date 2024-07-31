import csv


def adicionar_dicionario_sala(dic: dict):

   with open("salas.csv", "a") as arquivo:
            lista_valores: list[str] = []
                    
            for key in dic:
                value = dic[key]
                
                if type(value) == str:
                    value = value.replace(',', ';')
                    
                lista_valores.append(fr'"{key}:{value}"')
                
            linha_produto = ','.join(lista_valores) + '\n'
            
            arquivo.write(linha_produto)
        


def adicionar_dicionario_reserva(reserva: dict):

    with open("reservas.csv", "a") as arquivo:
        lista: list[str] = []
                    
        for key in reserva:
            value = reserva[key]
            
                    
            lista.append(fr'"{key}:{value}"')
                
        string = ','.join(lista) + '\n'
            
        arquivo.write(string)

def criar_sala (tipo, codigo, capacidade, descricao: dict):
    return  {
        "tipo": tipo,
        "codigo": codigo,
        "capacidade": capacidade,
        "descricao": descricao,
        "ativa": True

    }



def criar_reserva(codigo, sala, data_hora_inicio, data_hora_fim):
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