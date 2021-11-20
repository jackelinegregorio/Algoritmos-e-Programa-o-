###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

def verifica_jogo(tabuleiro, ht, lt, p, hp, lp):
  for a in range(1+ht-hp):
    for i in range(1+lt-lp):
      verifica = False
      for j in range(hp):
        for b in range(lp):
          if not ((tabuleiro[a+j][i+b]=='.' and p[j][b]=='.')or(tabuleiro[a+j][i+b]=='*' and p[j][b]=='.')or(tabuleiro[a+j][i+b]=='.' and p[j][b]=='#')):
            verifica = True
            break
        if verifica:
          break
      if verifica:
        jogo='Fim de jogo'
      else:
        jogo='O jogo deve continuar'

        for r in range(hp):
          for s in range(lp):
            if (tabuleiro[a+r][i+s]=='.' and p[r][s]=='#'):
              tabuleiro[a+r][i+s] = '#'
        break
    if not verifica:
      break
  return tabuleiro, jogo

ht, lt = [int(x) for x in input().split()]

tabuleiro = []
for t in range(ht):
  tabuleiro.append(list(input()))

hp, lp = [int(x) for x in input().split()]

p=[]

for t in range(hp):
  p.append(list(input()))

tabuleiro, jogo = verifica_jogo(tabuleiro, ht, lt, p, hp, lp)

for linha in tabuleiro:
  print("".join(linha))

print(jogo)