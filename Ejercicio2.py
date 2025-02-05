def Fibonacci(numero):
    if numero==0:
        return 0
    
    if numero==1:
        return 1
    
    else:
        return Fibonacci(numero-1) + Fibonacci(numero-2)

numero=int(input("Ingrese un numero: "))
resultado=Fibonacci(numero)
print(resultado)