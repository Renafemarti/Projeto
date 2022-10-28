import os

#Classe Evento
class eventos():
  #Construtor
  def __init__(self, indice, evento, ano, mes, dia, hora, minuto):
    #Atributos da nossa classe
    self.__indice = indice
    self.__evento = evento
    self.__ano = ano
    self.__mes = mes
    self.__dia = dia
    self.__hora = hora
    self.__minuto = minuto

  #Métodos acessores (get)
  def getIndice(self):
    return self.__indice
  def getEvento(self):
    return self.__evento
  def getAno(self):
    return self.__ano
  def getMes(self):
    return self.__mes
  def getDia(self):
    return self.__dia
  def getHora(self):
    return self.__hora
  def getMinuto(self):
    return self.__minuto
    
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
        agendarevento = input('\n\033[0;92m Digite seu evento: ')
        ano = input('033[0;92m Digite o ano do seu evento: ')
        mes = input('033[0;92m Digite o mês do seu evento: ')
        dia = input('033[0;92m Digite o dia do seu evento: ')
        hora = input('033[0;92m Digite o hora do seu evento: ')
        minuto = input('033[0;92m Digite o minuto do seu evento: ')
        evento[agendarevento] =(f'{hora}:{minuto}')
        Eventos.append(eventos(k, agendarevento, ano, mes, dia, hora, minuto))
        print('Evento Adicionado com sucesso!!!')

  #Editar evento
  def editarevento(self):
    ede=input('Você deseja excluir um evento? (S)-Sim e (N)-Não: ')
    if ede == 's' or 'S':
      print(evento)
      qede = ('Digite a "Palavra chave" do seu evento: ')
      if evento.get(qede):
        agendarevento = input('Digite seu nova palava chave do seu evento: ')
        descricao = input('\033[0;92m Descrição do evento: ')
        ano = int(input('\033[0;92m Dia do evento: '))
        mes = int(input('\033[0;92m Mês do evento: '))
        dia = int(input('\033[0;92m Ano do evento: '))
        horario = int(input('\033[0;92m Horário do evento: '))
        while horario >= 24:
          print('\033[0;92m Digite o horário do evento até 24 horas!')
          horario = int(input('\033[0;92m Digite o horário do evento: '))
        minuto = int(input('\033[0;92m Digite os minutos do evento: '))
        local = input('\033[0;92m Local do evento: ')
        arq = open('Evento.txt', 'a')
        arq.write(f'{evento};{descricao};{ano};{mes};{dia};{horario}-horas;{local};\n')
        evento[agendarevento] =(f'{horario}:{minuto}')
        if evento in horas.keys():
          evento[agendarevento]=(f'{horario}:{minuto}')
        else:
          print('Palavra chave indisponivel!!!')

  #Deletar evento
  def deletarevento(self):
    dele=input('Você deseja deletar algum evento? (S)-Sim e (N)-Não')
    if dele == 's' or 'S':
      pl=input('Digite a "Palavra Chave" o evento que você deseja deletar: ')
      if pl in evento.keys():
        evento.pop(pl)
      else:
        print('Palavra chave inexitente!!!')

  def acessarevento(self):
    for i, (j,k) in enumerate(evento.items()):
      print(i,j,k)
