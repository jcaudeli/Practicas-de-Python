#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:06:20 2020

@author: jcaudeli
"""
from datetime import date

print ("BIENVENIDO A EMPAREJANDO.COM\n")

print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre = input("Escribe tu nombre: ")
ano = int(input("¿Año de nacimiento? "))
taburete = input("¿Te gusta Taburete? [Si/No] ")

#Obtengo el año para hacer el cálculo de la edad
ano_actual=date.today().year
edad = ano_actual-ano

print("Hola "+nombre+". Si no me equivoco tienes", edad,"años.")

#Guardo la variable taburete como un booleano porque es mucho más eficiente
if taburete in ('Si','Sí','S','s','si','sí'):
    tabu = True
else:
    tabu = False

if (tabu):
    print("OK boomer. Lo tuyo va a ser un caso difícil")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")

#Guardo la variable booleana en vez del texto: ocupa mucho menos y las comparaciones son mucho más
#rápidas
usuario=[nombre,edad,tabu]

for dato in usuario:
    print(dato)


