import csv
from random import randint

def gerar_codigo_unico(lista_eventos):
  if not lista_eventos:  # Se a lista estiver vazia
      return randint(1000, 9999)
  while True:
    codigo_aleatorio = randint(1000, 9999)
    codigos_existentes = {evento['codigo'] for evento in lista_eventos}
    if codigo_aleatorio not in codigos_existentes:
      return codigo_aleatorio
    
def dividir_lista(lista):


  nova_lista = []
  for item in lista:
    chave, valor = item.split(':')
    nova_lista.extend([chave, valor])
  return nova_lista

def dividir_lista_reserva(lista):
  """
  Divide uma lista de strings no formato "chave:valor" em uma lista única
  contendo alternadamente as chaves e os valores.
  """

  nova_lista = []
  for item in lista:
      if item.startswith('data_e_hora_de_inicio:'):
        chave, valor = item.split(':', 1)  # Divide apenas na primeira ocorrência de ':'
        nova_lista.extend([chave, valor])
      elif item.startswith('data_e_hora_do_fim:'):
        chave, valor = item.split(':', 1)  # Divide apenas na primeira ocorrência de ':'
        nova_lista.extend([chave, valor])
      else:
          chave, valor = item.split(':')
          nova_lista.extend([chave, valor])
  return nova_lista



def adicionar_dicionario_sala(dic: dict):

   with open("salas.csv", "a") as arquivo:
            lista: list[str] = []
                    
            for i in dic:
                a = dic[i]
                
                if type(a) == str:
                    a = a.replace(',', ';')
                    
                lista.append(fr'"{i}:{a}"')
                
            linha = ','.join(lista) + '\n'
            
            arquivo.write(linha)
        

def adicionar_dicionario_reserva(dic: dict):

    with open("reservas.csv", "a") as arquivo:
            lista: list[str] = []
                    
            for i in dic:
                a = dic[i]
                
                if type(a) == str:
                    a = a.replace(',', ';')
                    
                lista.append(fr'"{i}:{a}"')
                
            linha = ','.join(lista) + '\n'
            
            arquivo.write(linha)


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

def exibe_dicionario_reserva():
    lista_dicts: list[dict] = []
        
    with open("reservas.csv", "r") as arquivo:

        csv_reader = csv.reader(arquivo)

        for row in csv_reader:
            a = dividir_lista_reserva(row)
            dic = {chave.strip(': '): int(valor) if valor.isdigit() else valor for chave, valor in zip(a[::2], a[1::2])}
            dic['ativa'] = dic['ativa'].lower() == 'true'
            lista_dicts.append(dic)
            
    return lista_dicts
        

def exibe_sala(id: int):

    return adicionar_dicionario_sala()

# def criar_sala(codigo, capacidade, ativa, tipo, descricao):
#     sala = sala_modelo(codigo, capacidade, ativa, tipo, descricao)
#     return sala