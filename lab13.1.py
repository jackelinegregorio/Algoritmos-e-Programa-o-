###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Super Trunfo
# Nome: Jackeline Leme Gregório 
# RA: 173678
###################################################

# Leitura das cartas

qtde_cartas = int(input())
campos = input()
campos = campos.split()
cartas = [0]*qtde_cartas
for i in range(qtde_cartas):
    carta_sem_lista = input()
    carta_lista = carta_sem_lista.split()
    for j in range(1, len(carta_lista)):
        carta_lista[j] = int(carta_lista[j])
    cartas[i] = carta_lista
ordenacao = input()
ordenacao = ordenacao.split()
# Ordenação das cartas

contador_de_insercoes = 0
for i in reversed(ordenacao):
    for j in range(1, len(campos)):
            if i == campos[j]:
                for indice in range(1, len(cartas)):
                    fez_mudanca = 0
                    valor_atributo = int(cartas[indice][j])
                    carta_atual = cartas[indice]
                    pos = indice
                    while pos > 0 and int(cartas[pos-1][j]) < valor_atributo:
                        cartas[pos] = cartas[pos-1]
                        pos = pos - 1
                        if fez_mudanca == 0:
                            contador_de_insercoes = contador_de_insercoes + 1
                            fez_mudanca = 1
                    cartas[pos] = carta_atual

# Impressão dos dados

print('{:15s}'.format(campos[0]), ''.join('{:>10}'.format(campo) for campo in campos[1:]))

for carta in cartas:
  print('{:15s}'.format(carta[0]), ''.join('{:>10}'.format(atributo) for atributo in carta[1:]))
print('Insercoes realizadas:', contador_de_insercoes)