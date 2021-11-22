###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras
# Nome: Jackeline Leme Gregório
# RA: 173678
###################################################


L = int(input())
texto = []
for i in range(L):
	frase = input()
	frase = frase.split()
	texto = frase + texto

N = int(input())
for i in range(N):
	ocorrencia= 0
	similares = 0
	palavra_buscada = input()
	print("Palavra buscada:", palavra_buscada)
	palavra_buscada = palavra_buscada.lower()
	for i in range(len(texto)):
		texto[i] = texto[i].lower()
		texto[i] = texto[i].replace("?","").replace("!","").replace(".","").replace(",","").replace(":","").replace(";","")
		if(palavra_buscada == texto[i]):
			ocorrencia = ocorrencia + 1
		elif(palavra_buscada in texto[i]):
			similares = similares + 1
	print("Ocorrencia:", ocorrencia)
	print("Palavras similares:", similares)