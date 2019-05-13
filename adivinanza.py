#juego de adivinar el numero, todos juntos 
#adivinar un nuero enerado al aleatoriamente 
#ir introduciendo por teclado el dato a adivinar

from random import randint
generado=randint(0,10)
condicion=True
intento=10
numero=input("dame un numero del 0 al 10:")
while condicion:
    if intento>0:
        numero=input("dame un numero del 0 al 10: ")
        intento=intento-1 
        if generado==int(numero):
            print("ganaste una onvorgosa que lore paga")
            condicion=False
        else:
            print("el perdedor copra una pizza a lore")
            print("te quedan", intento, "intentos")
    else:
        condicion=False
        print("perdiste")

