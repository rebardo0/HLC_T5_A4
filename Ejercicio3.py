def potencia_numero(a,b):
    potencia=a
    for i in range(1,b):
        potencia=potencia*a

    return potencia

numero=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese la potencia del numero:"))
resultado=potencia_numero(numero,numero2)
print(resultado)