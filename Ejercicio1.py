
def factorial_numero(numero):
    factorial=1

    for n in range(1,numero+1):
        factorial=factorial*n

    return factorial

numero=int(input("Introduce un número:"))
resultado=factorial_numero(numero)
print(resultado)