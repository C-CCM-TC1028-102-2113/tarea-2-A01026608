def main():
    # Escribe el código adecuado para completar el programa
    n1= int(input('Ingresa el primer número:'))
    n2= int(input('Ingresa el segundo número:'))
    n3= int(input('Ingresa el tercer número:'))

    if ((n1<=n2) and (n1<=n3)):
        menor= n1
        if (n2<=n3):
            medio= n2
            mayor= n3
        else:
            medio=n3
            mayor= n2
    elif((n2<=n1) and (n2<n3)):
        menor= n2
        if (n1<=n3):
            medio= n1
            mayor= n3
        else:
            medio= n3
            mayor= n1
    else:
        menor= n3
        if(n1<=n2):
            medio= n1
            mayor= n2
        else:
            medio= n2
            mayor= n1
    
    print(menor)
    print(medio)
    print(mayor)

if __name__=='__main__':
    main()
