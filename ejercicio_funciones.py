# Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
# como parámetro.

# Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.

def mostrar_numero(numero:int):
    print(numero)

# def pedir_numero():
#     numero = int(input("Ingrese un número: "))
#     return numero

# num = pedir_numero()
# mostrar_numero(num)

# Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La
# función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
# programa principal realizando la invocación o llamada.

def encontrar_par(numero:int)->bool:
    if numero % 2 == 0:
        return True
    else:
        return False

# num = int(input("Ingrese un número: "))

# resultado = encontrar_par(num)

# print(resultado)


# Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en
# un rango determinado pasado por parámetro “desde”-“hasta”.


def pedir_numero(min:int, max:int):
    numero = int(input(f"Ingrese un número entre {min} y {max}: "))

    while validar_numero(numero, min, max) == False:
        numero = int(input(f"Error!! Ingrese un número entre {min} y {max}: "))

    return numero

# num = pedir_numero(1, 10)
# print(num)

def mostrar_numero(numero:int, min:int, max:int):
    if min <= numero <= max:
        print(numero)
    else:
        print("Número fuera de rango")

# mostrar_numero(50, 1, 100)

# Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la
# función Restar en sus 4 combinaciones.
#  Restar1(int, int)->int:
#  Restar2()->int:
#  Restar3(int, int):
#  Restar4():

def restar_numeros_1(numero_1:int, numero_2:int) -> int:
    return numero_1 - numero_2


def restar_numeros_2() -> int:
    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))
    return numero_1 - numero_2


def restar_numeros_3(numero_1:int, numero_2:int):
    resultado = numero_1 - numero_2
    print(f"El resultado es: {resultado}")


def restar_numeros_4():
    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))
    resultado = numero_1 - numero_2
    print(f"El resultado es: {resultado}")



# resultado = restar_numeros_1(10, 5)
# print(f"Restar1: {resultado}")


# resultado = restar_numeros_2()
# print(f"Restar2: {resultado}")


# restar_numeros_3(20, 8)


# restar_numeros_4()

# Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
# solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
# dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
# por pantalla. Atención: pueden reutilizarse funciones ya creadas.

def validar_numero(numero:int, min:int, max:int) -> bool:
    return min <= numero <= max


def calcular_descuento(numero:float) -> float:
    descuento = numero * 0.05
    return numero - descuento


# numero_1 = int(input("Ingrese un número entre 10 y 100: "))

# while validar_numero(numero_1, 10, 100) == False:
#     print("Error. El número debe estar entre 10 y 100.")
#     numero_1 = int(input("Ingrese un número entre 10 y 100: "))

# resultado = calcular_descuento(numero_1)

# print(f"Valor original: {numero_1}")
# print(f"Valor con descuento del 5%: {resultado}")

# Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2
# los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
# variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
# la operación de dichos valores a través de una función. Mostrar el resultado por
# pantalla.

def sumar(numero_1:int, numero_2:int) -> int:
    return numero_1 + numero_2


def validar_operacion(operacion:str) -> bool:
    return operacion == "s" or operacion == "r"


def realizar_operacion(numero_1:int, numero_2:int, operacion:str):
    if operacion == "s":
        return sumar(numero_1, numero_2)
    else:
        return restar_numeros_1(numero_1, numero_2)
    



numero_1 = pedir_numero(1, 100)
numero_2 = pedir_numero(1, 100)

operacion = input("Ingrese 's' para sumar o 'r' para restar: ")

while validar_operacion(operacion) == False:
    operacion = input("Error. Ingrese 's' para sumar o 'r' para restar: ")

resultado = realizar_operacion(numero_1, numero_2, operacion)

print(f"El resultado es: {resultado}")

