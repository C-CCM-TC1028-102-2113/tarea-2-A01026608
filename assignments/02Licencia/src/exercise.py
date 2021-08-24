
def main():
    #Escribe tu código debajo de esta línea
    edad= int(input('Ingresa tu edad:'))
    id_o= str(input('¿Tienes identificación oficial? (s/n):'))
    
    if edad<0:
        print('Respuesta Incorrecta')
    elif edad>= 18 and id_o == 's':
        print('Trámite de licencia concedido')
    elif edad<18 and id_o == 's':
        print ('No cumples con los requisitos')
    elif edad>= 18 and id_o == 'n':
        print('No cumple con los requisitos')
    elif edad<18 and id_o == 'n':
        print('No cumple con los requisitos')
    elif id_o != 'n' or 's':
        print('Respuesta Incorrecta')
    
if __name__ == '__main__':
    main()
