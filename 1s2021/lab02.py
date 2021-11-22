###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - O Grande Show
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################
#t_b_c=tempo de partida

# Leitura de dados
dist_a_b = int(input())
vel_t1 = float(input())
t_b_c = int(input())
dist_b_c = int(input())
vel_t2 = float(input())
t_show = int(input())

t_ab =(dist_a_b/vel_t1)*60
t_bc=(dist_b_c/vel_t2)*60

if t_ab>t_b_c:
  print("False")
elif t_bc+t_b_c<=t_show:
  print("True")
else:
  print("False")