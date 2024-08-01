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

def criar_sala (codigo, tipo, capacidade, descricao: dict):
    return  {
        "codigo": codigo,
        "tipo": tipo,
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
def dividir_lista(lista):
  """
  Divide uma lista de strings no formato "chave:valor" em uma lista única
  contendo alternadamente as chaves e os valores.

  Args:
    lista: A lista de strings a ser dividida.

  Returns:
    Uma nova lista com as chaves e valores separados.
  """

  nova_lista = []
  for item in lista:
    chave, valor = item.split(':')
    nova_lista.extend([chave, valor])
  return nova_lista

def exibe_dicionario_sala():
    lista_dicts: list[dict] = []
        
    with open("salas.csv", "r") as arquivo:

        csv_reader = csv.reader(arquivo)

        for row in csv_reader:
            a = dividir_lista(row)
            dic = {chave.strip(': '): int(valor) if valor.isdigit() else valor for chave, valor in zip(a[::2], a[1::2])}
            dic['ativa'] = dic['ativa'].lower() == 'true'
            lista_dicts.append(dic)
            
    return lista_dicts
        

def exibe_sala(id: int):

    return adicionar_dicionario_sala()

# def criar_sala(codigo, capacidade, ativa, tipo, descricao):
#     sala = sala_modelo(codigo, capacidade, ativa, tipo, descricao)
#     return sala