lista_usuarios=[]

#Classe Usuario
class Usuario:
  #Construtor
  def __init__(self, nome, data_nascimento, telefone, email, senha, endereco, curso, ie):
      #Atributos da nossa classe
    self.__nome = nome
    self.__data_nascimento = data_nascimento
    self.__telefone = telefone
    self.__email = email
    self.__senha = senha
    self.__endereco = endereco
    self.__curso = curso
    self.__ie = ie

  #Métodos acessores (get)
  def getNome(self):
    return self.__nome
  def getData_nascimento(self):
    return self.__data_nascimento
  def getTelefone(self):
    return self.__telefone
  def getEmail(self):
    return self.__email
  def getSenha(self):
    return self.__senha
  def getEndereco(self):
    return self.__endereco
  def getCurso(self):
    return self.__curso
  def getIe(self):
    return self.__ie

  #Métodos modificadores (set)
  def setNome(self, nome):
    self.__nome = nome
  def setData_nascimento(self, data_nascimento):
    self.__data_nascimento = data_nascimento
  def setTelefone(self, telefone):
    self.__telefone = telefone
  def setEmail(self, email):
    self.__email = email
  def setSenha(self, senha):
    self.__senha = senha
  def setEndereco(self, endereco):
    self.__endereco = endereco
  def setCurso(self, curso):
    self.__curso= curso
  def setIe(self, ie):
    self.__ie = ie

  def redenfinirlogin():
    import os
    import time
    global j
    os.system('clear')
    print('\033[1;49;34m --- Planner TIGR --- \033[m')
    print('\n\033[1;49;92m REDEFINIR LOGIN \033[m')
    loginsenha = input('\033[0;92m Digite sua Senha: ')
    while loginsenha != lista_usuarios.__getitem__(x).getSenha():
      import time
      os.system('clear')
      print('\033[1;49;34m --- Planner TIGR --- \033[m')
      print('\n\033[1;49;92m LOGIN \033[m')
      print('\n\033[1;49;92m Salvando alterações... \033[m')
      time.sleep(1)
      print('\n\033[0;31m  ERRO!!!')
      print('\n\033[1;49;92mSua senha está incorreta!')
      print('\033[1;49;92m Efetue o login novamente')
      loginsenha = input('\033[0;92m Digite sua Senha: ')
      os.system('clear')
      if loginsenha == (lista_usuarios.__getitem__(x).getSenha()):
          menusecundario(j)