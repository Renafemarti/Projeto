import Usuario
import Evento

#Classe Agendamento
class Agendamento:
  #Construtor
  def __init__(self, data_agendamento, hora_agendamento, nome, data_nascimento, telefone, email, senha, endereco, curso, ie, indice, evento, data, horario, local, descricao):
    #Atributos da nossa classe
    self.__data_agendamento = data_agendamento
    self.__hora_agendamento = hora_agendamento
    self.usuario = Usuario(nome, data_nascimento, telefone, email, senha, endereco, curso, ie)
    self.evento = Evento(indice, evento, data, horario, local, descricao)

  #Métodos acessores (get)
  def getData_agendamento(self):
    return self.__data_agendamento
  def getHora_agendamento(self):
    return self.__hora_agendamento

   #Métodos modificadores (set)
  def setData_agendamento(self, data_agendamento):
    self.__data_agendamento = data_agendamento 
  def setHora_agendamento(self, hora_agendamento):
    self.__hora_agendamento = hora_agendamento
    