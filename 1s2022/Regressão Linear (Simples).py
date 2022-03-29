import numpy as np
from sklearn.linear_model import LinearRegression

qnt=int(input("Informe a quantidade de variáveis do modelo: "))
x=list(range(0,qnt))
y=list(range(0,qnt))
print("Informa as ", qnt, "variáveis dependentes: ")

for n in range(0, qnt):
    print("Informe o valor ", n+1)
    y[n]=int(input())

print("Informe as ", qnt, " variáveis independentes: ")
for n in range(0, qnt):
    print("Informe o valor ", n+1)
    x[n]=int(input())

print("Informe o valor que quer prever ")
prev=list(range(0,1))
prev[0]=int(input())

x=np.asarray(x)
x=x.reshape(-1,1)
y=np.asarray(y)

modelo=LinearRegression()
modelo.fit(x,y)

prev=np.asarray(prev)
prev=prev.reshape(-1,1)

answer=modelo.predict(prev.reshape(-1,1))
print("Resultado da previsão: ", answer)
