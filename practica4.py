#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:06:20 2020

@author: jcaudeli
"""

print ("BIENVENIDO A EMPAREJANDO.COM\n")

print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre = input("Escribe tu nombre: ")
ano = int(input("¿Año de nacimiento? "))
taburete = input("¿Te gusta Taburete? [Si/No] ")

edad = 2020-ano

print("Hola "+nombre+". Si no me equivoco tienes", edad,"años.")

if taburete in ('Si','Sí','S','s','si','sí'):
    print("OK boomer. Lo tuyo va a ser un caso difícil")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")

usuario=[nombre,edad,taburete]

for dato in usuario:
    print(dato)


