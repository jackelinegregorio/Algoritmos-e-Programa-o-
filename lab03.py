###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Imposto de Renda
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################

# Leitura de dados
rendimento_tributavel = float(input())
gasto_previdencia = float(input())
gasto_educacao = float(input())
imposto_retido = float(input())

base_simplificado = rendimento_tributavel - (20/100) * rendimento_tributavel
base_completo = 0

if gasto_educacao > 3_561.50:
    gasto_educacao = 3_561.50

if gasto_previdencia > (12/100) * rendimento_tributavel:
    base_completo = rendimento_tributavel - (12/100) * rendimento_tributavel - gasto_educacao
else:
    base_completo = rendimento_tributavel - gasto_previdencia - gasto_educacao

ir_simplificado = 0
ir_completo = 0

if base_simplificado >= 22_847.77 and base_simplificado <= 33_919.80:
  ir_simplificado = base_simplificado*(7.5/100) - 1_713.58
elif base_simplificado >= 33_919.81 and base_simplificado <= 45_012.60:
  ir_simplificado = base_simplificado*(15.0/100) - 4_257.57
elif base_simplificado >= 45_012.61 and base_simplificado <= 55_976.16:
  ir_simplificado = base_simplificado*(22.5/100) - 7_633.51
elif base_simplificado > 55_976.16:
  ir_simplificado = base_simplificado*(27.5/100)-10_432.32

if base_completo >= 22_847.77 and base_completo <= 33_919.80:
  ir_completo = base_completo*(7.5/100) - 1_713.58
elif base_completo >= 33_919.81 and base_completo <= 45_012.60:
  ir_completo = base_completo*(15.0/100) - 4_257.57
elif base_completo >= 45_012.61 and base_completo <= 55_976.16:
  ir_completo = base_completo*(22.5/100) - 7_633.51
elif base_completo > 55_976.16:
  ir_completo = base_completo*(27.5/100) - 10_432.32

ajuste_simplificado = ir_simplificado - imposto_retido
ajuste_completo = ir_completo - imposto_retido

print("Base de calculo (Simplificado):", format(base_simplificado, ".2f").replace(".", ","))
print("Base de calculo (Completo):", format(base_completo, ".2f").replace(".", ","))
print("Valor do IR (Simplificado):", format(ir_simplificado, ".2f").replace(".", ","))
print("Valor do IR (Completo):", format(ir_completo, ".2f").replace(".", ","))
print("Valor do ajuste (Simplificado):", format(ajuste_simplificado, ".2f").replace(".", ","))
print("Valor do ajuste (Completo):", format(ajuste_completo, ".2f").replace(".", ","))
