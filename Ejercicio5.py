def contar_digitos(numero):
    if numero==0:
        return 0
    
    else:
        return numero%10 + contar_digitos(int(numero/10))

numero=int(input("Introduce un número entero positivo para contar: "))
resultado=contar_digitos(numero)
print(resultado)