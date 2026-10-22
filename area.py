"""Queremos calcular el área de un círculo.
Importamos el número pi de la biblioteca de math.
"""
import math
#Declaramos la función:
def area_circulo (radio):
    """
Función que devuelve el área de un cículo.
Params:
    - radio(con decimales, da igual la unidad)
Return
    - Devuelve el área en unidades^2
Variables
    Las variables que viven dentro de una función no salen de aquí
    #Sin return el valor por defecto sería None. Hay que poner return "nombrevariable"
"""
    area = math.pi * (radio**2)
    
    return area 

def area_cuadrado(lado):
    area = lado**2
    return area

lado = int(input("Introduce el lado (sin decimales porfi):"))
area_cuadrado = area_cuadrado(lado)
print(f"El área del cuadrado de lado {lado} es {round(area_cuadrado,2)}")

"""
El round se lo tienes que hacer a una variable, es como un int o float.
Como norma general se redondea a la hora de pintarlo y en la funcion mantener el valor puro. 

Seteamos la variable area porque FUERA de la función no está definida;
Si queremos usarla tenemos que definirla ahora ->
"""
radio = float(input("De qué radio quieres el círculo? Incluye decimales."))
area_circulo = round(area_circulo(radio),2)

print(f"El área de un círculo de radio {radio} es {area_circulo}")
