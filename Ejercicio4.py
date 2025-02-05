def suma_digitos(numero):
    if numero==0:
        return 0
    
    else:
        return numero%10 + suma_digitos(int(numero/10))

numero=int(input("Introduce un número entero positivo para sumar: "))
resultado=suma_digitos(numero)
print(resultado)