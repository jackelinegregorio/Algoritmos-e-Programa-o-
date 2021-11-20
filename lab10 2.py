###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

# Leitura da matriz

campo = []
for i in range(8):
  campo.append(input().split())

# Leitura e processamento dos sensores
num_sensores = int(input())
alcance = int(input())

sensores = []

for i in range(num_sensores):
  linha, coluna = [int(i) for i in input().split()]
  sensores.append((linha, coluna))

# Fazendo os cálculos
baus_encontrados = 0

for sensor in sensores:  # percorro cada sensor
    linha, coluna = sensor
    if campo[linha][coluna] == 'o':  # se eles já caem em uma zona morta eu não continuo processando
        break
    else:
        if campo[linha][coluna] == 'x':  # se caí em um baú achei um baú
            baus_encontrados += 1
        # Norte
        for zona in range(1, alcance+1):
            norte = linha - zona
            if norte < 0:
                break
            elif campo[norte][coluna] == 'x':
                baus_encontrados += 1
            elif campo[norte][coluna] == 'o':
                break
        
        # Sul
        for zona in range(1, alcance+1):
            sul = linha + zona
            if sul >= 8:
                break
            elif campo[sul][coluna] == 'x':
                baus_encontrados += 1
            elif campo[sul][coluna] == 'o':
                break

        # Leste
        for zona in range(1, alcance+1):
            leste = coluna + zona
            if leste >= 8:
                break
            elif campo[linha][leste] == 'x':
                baus_encontrados += 1
            elif campo[linha][leste] == 'o':
                break
        
        # Oeste
        for zona in range(1, alcance+1):
            oeste = coluna - zona
            if oeste < 0:
                break
            elif campo[linha][oeste] == 'x':
                baus_encontrados += 1
            elif campo[linha][oeste] == 'o':
                break

msg = ''
if baus_encontrados:
    msg = '{} bau(s) encontrado(s).'.format(baus_encontrados)
else:
    msg = 'Nenhum bau encontrado.'

print(msg)
    
