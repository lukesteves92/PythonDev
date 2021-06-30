nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()

if idade >= 65:
    print("O pacitente " + nome + "possui atendimento prioritário")

elif doenca_infectocontagiosa=="SIM":
    print("O paciente " + nome + "deve ser direcionado para sala de espera reservada")
else:
    print("O pacitente " + nome + "Não possui atendimento prioritário")