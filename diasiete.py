#creammos un archivo nuevo
#guardaos en larpeta del repositorio
#con la extension .py
#uso de numeros aleatorios
from random import randint   
aleatorio=randint(0,20)     #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio)   #imprimios el numero generado


#eercicio
#escribir una funsion sorteo() que reciba una lisa de participantes, y elegit
#a uno de los participantes aleatoriomente, y retornar esa persona elegida
#desafio: no volver a retornar una persona ya sorteada

from random import randint

def sorteo(listas):   #definimos una funcion
#utilizamos len() para saber la cantidad de personas 
#que hay en la lista y guardamos en cant
#y guardamos en la variable ganador 
    cant=len(listas)-1
    indice=randint(0,cant)
    ganador=listas[indice]
    return ganador    #retornamos ganador



participantes=["jaz","mauri","maria","fran","pau"]  #creamos la lista de los participantes
ganar=sorteo(participantes)   #llamamos a la funcion y guardampos en la variable el resultadoentornado por la funsion 
print(ganar) #imprimimmos el ganador
