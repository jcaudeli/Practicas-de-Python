#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:43:31 2020

@author: jcaudeli
"""

# Declaración de constantes necesarias para todo el programa
abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Declaración de funciones
def cifracesar(texto,key):
    
    texto_cifrado=""

    for letra in texto:
        
        nueva_posicion=(abecedario.index(letra)+key)
        
        #La lista tiene 27 letras, desde la posición 0 a la 26. Si al cifrar nos pasamos de largo
        #hay que restarle 26 para "volver a empezar"
        if (nueva_posicion>26):
            nueva_posicion=nueva_posicion-26    
            #Ahora restamos 1 porque la lista empieza en la posición 0, no la 1. Se podría haber restado 27 directamente,
            #lo he hecho así para que se entienda
            nueva_posicion=nueva_posicion-1

        letra_cifrada=abecedario[nueva_posicion]
        texto_cifrado+=letra_cifrada

    return texto_cifrado

   
#Comienza el programa
print("BIENVENIDO A MI CIFRADOR CÉSAR")

texto_claro=input("Escribe el texto a cifrar:")
clave=int(input("Escribe la clave de cifrado (un número del 1 al 27):"))


cifrado=cifracesar(texto_claro,clave)
print ("El texto cifrado es:",cifrado)

