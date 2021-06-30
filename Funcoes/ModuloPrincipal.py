from Funcoes.Funcoes import *

minhalista=[]

print("Preenchendo")

prencherInventario(minhalista)

print("Exibindo")

exibirInventario(minhalista)

print("Pesquisando")

localizarPorNome(minhalista)

print("Alterando")

depreciarPorNome(minhalista, 20)

print("Excluindo")

print(excluirPorSerial(minhalista))

print("Exibindo inventário")

exibirInventario(minhalista)

print("Excluindo")

resumirValores(minhalista)