def Par_o_Impar(n):
    if n%2 == 0 :
        return 1
    else:
        return 0

if __name__ == "__main__":
    n = int(input("Ingrese un numero: "))
    if Par_o_Impar(numero)==1 :
        print("El numero es par")
    else:
        print("Es numero impar")