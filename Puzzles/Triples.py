from math import gcd

limite = int(input())
m = 2
a,b,c = 0,0,0
triplas = set() 

while a<=limite:  #Enquanto o menor elemento nao passou do limite
    for n in range(1, m):
#Isso é equivalente a seu máximo divisor comum (mdc) sendo 1.
      #Retorna o resto da divisão de ambos operandos.
        if not (gcd(m,n) == 1 and not (m%2 != 0 and n%2 != 0)): 
            continue
        a = (m*m)-(n*n)
        b = 2*(m*n)
        c = (m*m)+(n*n)
      
       # Calculo a,b,c pela parametrizacao
       #tupla -> não é possível adicionar, alterar ou remover seus elementos
        a,b,c = tuple(sorted([a,b,c]))     #sorted pra criar uma nova lista # Ordeno eles
        if a>limite or b>limite or c>limite:     # Se algum deles passa do limite, posso parar aqui, aumentar o n nao vai diminuir eles, vamos pro proximo m
            break
        triplas.add(tuple([a,b,c])) # Adiciono eles num set(), que e um conjunto sem elementos repetidos
    m = m + 1
print(len(triplas))    #Imprimo o tamanho desse set