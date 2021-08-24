def main():
    #escribe tu código abajo de esta línea
    n1= int(input('Ingresa el primer número:'))
    n2= int(input('Ingresa el segundo número:'))
    n3= int(input('Ingresa el tercer número:'))
    
    if n2<n1>n3:
        print(n1)
    elif n1<n2>n3:
        print(n2)
    elif n1<n3>n2:
        print(n3)
    
if __name__=='__main__':
    main()
