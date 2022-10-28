#Instituto Federal de Rondônia
#Projeto Integrador
#GRUPO: Geovanna Batista dos Santos, Thalita Golçalves da Costa, Ítalo Eduardo Maciel, Renato Ferreira Martins

#Variável global, biblioteca para limpar, listas, dicionário e a importação dos modolos
global j
import os
import time
from Usuario import *
from Evento import *
from Calendario import *
from arquivos import *
lista_usuarios = []
Eventos = []
evento={}
j = 0
arqu = ('Usuario.txt')
arqe = ('Evento.txt')
if not arqExiste(arqu):
  CriarArquivo(arqu)

if not arqExiste(arqe):
  CriarArquivo(arqe)

#Função menu(), início da tela
def menu():
    print('\n\033[1;49;34m --- Planner TIGR --- \033[m')
    print('\n\033[1;49;92m 1° --> CADASTRO \033[m')
    print('\n\033[1;49;92m 2° --> LOGIN \033[m')
    print('\n\033[1;49;92m 3° --> ENCERRAR \033[m')
    r = input(
        '\n\033[1;49;34m Digite aqui sua opção: ')
    return r


#Função início(), específica somente para o CADASTRO
def cadastro():
  global j
  print('\033[1;49;34m --- Planner TIGR --- \033[m')
  print('\n\033[1;49;92m CADASTRO \033[m')
  print('\033[0;92m Faça seu cadastro: ')
  nome = input('\n\033[0;92m Nome: ')
  data_nascimento = input('\033[0;92m Idade: ')
  telefone = input('\033[0;92m Telefone: ')
  email = input('\033[0;92m E-mail: ')
  senha = input('\033[0;92m Senha: ')
  endereco = input('\033[0;92m Endereço: ')
  curso = input('\033[0;92m Curso: ')
  ie = input('\033[0;92m Instituição de Ensino: ')
  lista_usuarios.append(Usuario(nome, data_nascimento, telefone, email, senha, endereco, curso, ie))
  arq = open('Usuario.txt', 'a+')
  arq.write(f'{nome}; {data_nascimento}; {telefone}; {email}; {senha}; {endereco}; {curso}; {ie}\n')
  arq.close()
  login()


#Função login(), específica somente para o LOGIN
def login():
    import time
    global j
    os.system('clear')
    print('\033[1;49;34m --- Planner TIGR --- \033[m')
    print('\n\033[1;49;92m LOGIN \033[m')
    print("\033[0;92m Efetue o login ")
    login_email = input('\n\033[0;92m Digite seu E-mail: ')
    loginsenha = input('\033[0;92m Digite sua Senha: ')

    if (len(lista_usuarios) == 0):
        print('\n\033[1;31m Não há nenhum perfil cadastrado!')
        time.sleep(0.5)
        os.system('clear')

    else:
        for x in range(len(lista_usuarios)):
            if login_email == lista_usuarios.__getitem__(x).getEmail():
                j = x
                break

        while login_email != lista_usuarios.__getitem__(x).getEmail() or loginsenha != lista_usuarios.__getitem__(
                x).getSenha():
            import time
            os.system('clear')
            print('\033[1;49;34m --- Planner TIGR --- \033[m')
            print('\n\033[1;49;92m LOGIN \033[m')
            print('\n\033[1;49;92m Salvando alterações... \033[m')
            time.sleep(1)
            print('\n\033[0;31m  ERRO!!!')
            print('\n\033[1;49;92m Seu E-mail ou senha estão incorretos!')
            print('\033[1;49;92m Efetue o login novamente')
            login_email = input('\n\033[0;92m Digite seu E-mail: ')
            loginsenha = input('\033[0;92m Digite sua Senha: ')
            os.system('clear')
        if login_email == (lista_usuarios.__getitem__(x).getEmail()) and loginsenha == (
        lista_usuarios.__getitem__(x).getSenha()):
            adicionarevento(j)


#Função evento(), específica para o usuário criar um evento
def adicionarevento(k):
    os.system('clear')
    print('\033[1;49;34m --- Planner TIGR --- \033[m')
    print('\n\033[1;49;92m EVENTO \033[m')
    nn = input('\n\033[0;92m Você deseja agendar um evento? (S)-Sim ou (N)-Não):  ')
    os.system('clear')
    if nn == 's' or nn == 'S':
      while True:
        os.system('clear')
        print('\033[1;49;34m --- Planner TIGR --- \033[m')
        print('\n\033[1;49;92m EVENTO \033[m')
        print('\n\033[1;49;92m !!!ATENÇÃO!!! \033[m')
        print('\033[1;49;92m !!!NUNCA DIGITE A MESMA PALAVRA CHAVE EM UM EVENTO!!! \033[m')
        agendarevento = input('\n\033[0;92m Digite a palavra chave seu evento: ')
        ano =input('\033[0;92m Digite o ano do seu evento: ')
        try:
          mes = int(input('\033[0;92m Digite o mês do seu evento: '))
          while mes > 12:
            print(' Digite numeros do meses até 12 !')
            mes = int(input('\033[0;92m Digite o mês do seu evento: ')) 
            if mes <= 12:
              pass
          dia = int(input('\033[0;92m Digite o dia do seu evento: '))
          while dia > 31:
            print('Digite os dias até 31 !')
            dia = int(input('\033[0;92m Digite o dia do seu evento: '))
            if dia <=31:
              pass
          hora = int(input('\033[0;92m Digite o hora do seu evento: '))
          while hora >= 24:
            print('Digite as horas até 23 !')
            hora = int(input('\033[0;92m Digite o hora do seu evento: '))
            if hora <=23 :
              pass
          minuto = int(input('\033[0;92m Digite o minuto do seu evento: '))
          while minuto > 59:
            print('Digite minuto no maximo até 59')
        except ValueError:
          print('Em datas e horarios digite números inteiros!')
        else:
          
          evento[agendarevento] =(f'{hora}:{minuto}')
          Eventos.append(eventos(k, agendarevento, ano, mes, dia, hora, minuto))
          arq = open('Evento.txt', 'a')
          arq.write(f'{agendarevento}; {ano}; {mes}; {dia}; {hora}; {minuto}\n')
          arq.close()

          print('\n\033[0;92m Evento adicionado com sucesso!!!')
          time.sleep(2)
          nn=input('\n\033[0;92m Você deseja agendar um novo evento? (S)-Sim ou (N)-Não: ')
          if nn == 'n' or nn == 'N':
            menusecundario()
            chamarmenusecudario()
            os.system('clear')
            break
  
#Condicional para o menu principal
while True:
    opcao = menu()
    if opcao == '1':
        os.system('clear')
        cadastro()
    if opcao == '2':
        os.system('clear')
        login()
    if opcao == '3':
      os.system('clear')
      print('\033[0;92m Obrigado(a) por acessar o planner TIGR!')
        

      
#Função menusecundario(), para mostrar o segundo menu após o cadastro
def menusecundario():
  print('\n\033[1;49;34m --- Planner TIGR --- \033[m')
  print('\n\033[1;49;92m 1° --> EVENTOS \033[m')
  print('\n\033[1;49;92m 2° --> PERFIL \033[m')
  print('\n\033[1;49;92m 3° --> REDEFINIR LOGIN \033[m')
  print('\n\033[1;49;92m 4° --> CALENDÁRIO \033[m')
  print('\n\033[1;49;92m 5° --> ENCERRAR SESSÃO \033[m')
  s=input('\n\033[1;49;34m Digite aqui sua opção: ')
  return s

  
#Função menuevento(), que vai mostrar somente o menu de eventos
def menuevento():
  print('\n\033[1;49;34m --- Planner TIGR --- \033[m')
  print('\n\033[1;49;92m 1° --> ACESSAR EVENTOS \033[m')
  print('\n\033[1;49;92m 2° --> EDITAR EVENTO \033[m')
  print('\n\033[1;49;92m 3° --> ADICIONAR EVENTO \033[m')
  print('\n\033[1;49;92m 4° --> DELETAR EVENTO \033[m')
  print('\n\033[1;49;92m 5° --> VOLTAR \033[m') 
  e=input('\n\033[1;49;34m Digite aqui sua opção: ')
  return e

  
#Condição para o menu
while True:
  opcao = menu() 
  if opcao == '1':
      os.system('clear')
      cadastro()
  if opcao == '2':
      os.system('clear')
      login()
  if opcao == '3':
      print('\033[0;92m Obrigado(a) por acessar o planner TIGR!')
      os.system('clear')

      
#Condição para o menu secundário
def chamarmenusecudario():
  while True:
    opcaos = menusecundario()
    if opcaos == '1':
      os.system('clear')
      menuevento()
    elif opcaos == '2':
      os.system('clear')
      infoatualizadas()
    elif opcaos == '3':
      os.system('clear')
      redefinirlogin()
    elif opcaos == '4':
      os.system('clear')
      calendario()
    elif opcaos == '5':
      os.system('clear')
      menu()
    else:
      print(' Digite uma opção valida!')