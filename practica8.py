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
        
        if (nueva_posicion>26):
            nueva_posicion=nueva_posicion-27    
 
        letra_cifrada=abecedario[nueva_posicion]
        texto_cifrado+=letra_cifrada

    return texto_cifrado

def descifracesar(texto,key):
    
    texto_claro=""

    for letra in texto:
        nueva_posicion=(abecedario.index(letra)-key)
        
        if (nueva_posicion<0):
            nueva_posicion=27+nueva_posicion
        
        letra_descifrada=abecedario[nueva_posicion]
        texto_claro+=letra_descifrada

    return texto_claro
   
#Comienza el programa
print("BIENVENIDO A MI CIFRADOR CÉSAR")

texto_claro=input("Escribe el texto a cifrar:")
clave=int(input("Escribe la clave de cifrado (un número del 1 al 27):"))


cifrado=cifracesar(texto_claro,clave)
print ("El texto cifrado es:",cifrado)

descifrado=descifracesar(cifrado,clave)
print ("El texto descifrado es:",descifrado)

