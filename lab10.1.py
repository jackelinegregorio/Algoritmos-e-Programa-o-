###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

# Recebendo as entradas
campo = []
for i in range(8):
  campo.append(input().split())

num_sensores = int(input())
alcance = int(input())

sensores = []

for i in range(num_sensores):
  linha, coluna = [int(i) for i in input().split()]
  sensores.append((linha, coluna))

# Fazendo os cálculos
baus_encontrados = 0
locais = []  # locais onde encontramos os baús
for sensor in sensores:  # percorro cada sensor
    linha, coluna = sensor
    if campo[linha][coluna] == 'o':  # se eles já caem em uma zona morta eu não continuo processando
        break
    else:
        if campo[linha][coluna] == 'x' and (linha, coluna) not in locais:  # se caí em um baú achei um baú
            locais.append((linha, coluna))
            baus_encontrados += 1
        # Norte
        for zona in range(1, alcance+1):
            norte = linha - zona
            if norte < 0:
                break
            elif campo[norte][coluna] == 'x' and (norte, coluna) not in locais:
                baus_encontrados += 1
                locais.append((norte, coluna))
            elif campo[norte][coluna] == 'o':
                break
        
        # Sul
        for zona in range(1, alcance+1):
            sul = linha + zona
            if sul >= 8:
                break
            elif campo[sul][coluna] == 'x' and (sul, coluna) not in locais:
                baus_encontrados += 1
                locais.append((sul, coluna))
            elif campo[sul][coluna] == 'o':
                break

        # Leste
        for zona in range(1, alcance+1):
            leste = coluna + zona
            if leste >= 8:
                break
            elif campo[linha][leste] == 'x' and (linha, leste) not in locais:
                baus_encontrados += 1
                locais.append((linha, leste))
            elif campo[linha][leste] == 'o':
                break
        
        # Oeste
        for zona in range(1, alcance+1):
            oeste = coluna - zona
            if oeste < 0:
                break
            elif campo[linha][oeste] == 'x' and (linha, oeste) not in locais:
                baus_encontrados += 1
                locais.append((linha, oeste))
            elif campo[linha][oeste] == 'o':
                break


msg = ''
if baus_encontrados:
    msg = '{} bau(s) encontrado(s).'.format(baus_encontrados)
else:
    msg = 'Nenhum bau encontrado.'

print(msg)
    
