import Agendamento
import calendar

#Classe Calendário
class Calendario():
  #Construtor
  def __init__(self, dia, mes, ano, data_agendamento, hora_agendamento):
    #Atributos da nossa classe
    self.__dia = dia
    self.__mes = mes
    self.__ano = ano
    self.agendamento = Agendamento(data_agendamento, hora_agendamento)
    
  #Métodos acessores (get)
  def getDia(self):
    return self.__dia
  def getMes(self):
    return self.__mes
  def getAno(self):
    return self.__ano

  #Função para exibir o calendário
  def calendario():
      print('\n\033[1;49;92m Calendário 2022 \033[m')
      print('\n\033[1;49;92m', calendar.calendar(2022))

  