pregunta = 0
puntos = 0
print('--------------------BIENVENIDO A LA TRIVIA DE OLAF----------------------')
while pregunta <= 4:
    pregunta1 = input('cual es el color favorito de olaf?')
    if pregunta1 == 'verde' :
        puntos = puntos + 1
        print('respuesta correcta')
    else   :
        print('respuesta incorrecta') 
    pregunta2 = input('como es el pelo de olaf?')
    if pregunta2 == 'rizado' :
        puntos == puntos + 1
        print('respuesta correcta')
    else :
        print('respuesta incorrecta')
    pregunta3 = input('olaf enseña bien?')
    if pregunta3 == 'si' :
        puntos == puntos + 1
        print('respuesta correcta')
    else :
        print('respuesta incorrecta')
    pregunta4 = input('olaf traba en penguin academy?')
    if pregunta4 == 'si':
        puntos == puntos + 1
        print('respuesta correcta')
    else :
        print('respuesta incorrecta')
    if puntos == 4: 
        print('EXCELENTE, HAS GANADO LA TRIIVIA')
    elif puntos == 3 and puntos == 2:
        print('muy buen trabajo')
    else:
        print('puedes mejorar, debes conocer mas de olaf')


