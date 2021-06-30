equipamentos = []
valores = []
seriais = []
departamentos = []
inventario=[]
resposta="S"
while resposta=="S":
    equipamentos.append(input("Equipamento:"))
    valores.append(float(input("Valor:")))
    seriais.append(int(input("Número Serial:")))
    departamentos.append(input("Departamento:"))
    resposta=input("Digite \"S\" para continuar: ").upper()

# for elemento in inventario:
#       print(elemento)

for indice in range (0, len(equipamentos)):

    print("\n Equipamento..:", (indice+1))
    print("Nome.............: ", equipamentos[indice])
    print("Valor.............: ", valores[indice])
    print("Serial.............: ", seriais[indice])
    print("Departamento.............: ", departamentos[indice])
