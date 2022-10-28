#Caso o computador não tenha criado um arquivo, o sistema irá criar um

def arqExiste(arq):
  try:
    a = open(arq, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True

def CriarArquivo(arq):
  try:
    a = open(arq, 'wt+')
    a.close()
  except:
    print('Não deu pra Criar o arquivo!')
  else:
    print(f'Arquivo {arq} criado com sucesso!')