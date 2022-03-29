def imp(int1, int2):
  for a in range (int1, int2+1):
    print(a)
    for int2 in range (int2, int1-1, -1):
      print(int2)

int1=int(input("Informe o primeiro valor: "))
int2=int(input("Informe o segundo valor: "))
imp(int1, int2)

      