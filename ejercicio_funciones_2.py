# 1. Escribir una función que calcule el área de un rectángulo. La función recibe la base y
# la altura y retorna el área.

def calcular_area_rectangulo(base:float, altura:float)->float:
    area = base * altura
    return area



base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

resultado = calcular_area_rectangulo(base, altura)

print(f"El area del rectangulo es: {resultado}")

# 2. Escribe una función que calcule el área de un círculo. La función debe recibir el radio
# como parámetro y devolver el área.

def calcular_area_circulo(radio:float)->float:
    circulo = 3.1416 * radio ** 2
    return circulo

radio = float(input("Ingrese el radio: "))

resultado = calcular_area_circulo(radio)

print(f"El area del circulo es: {resultado}")

# 3. Crea una función que verifique si un número dado es par o impar. La función debe
# imprimir un mensaje indicando si el número es par o impar.

def verificar_par_impar(numero:int):
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


numero = int(input("Ingrese un numero: "))

verificar_par_impar(numero)


# 4. Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario

def verificar_par(numero:int):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = int(input("Ingrese un número: "))

resultado = verificar_par(numero)

print(resultado)

# 5. Define una función que encuentre el máximo de tres números. La función debe
# aceptar tres argumentos y devolver el número más grande

def maximo_tres(num_1:int, num_2:int, num_3:int):
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_2 >= num_1 and num_2 >= num_3:
        return num_2
    else:
        return num_3


numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))

numero_mayor = maximo_tres(numero_1, numero_2, numero_3)

print(f"El número mayor es: {numero_mayor}")


# 6. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def calcular_potencia(base:int, exponente:int):
    return base ** exponente


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = calcular_potencia(base, exponente)

print(f"El resultado es: {resultado}")

# 7. Crear una función que reciba un número y retorne True si el número es primo, False
# en caso contrario

def verificar_primo(numero:int):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


numero = int(input("Ingrese un numero para verificar si es primo: "))

print(verificar_primo(numero))

# 8. Crear una función que (utilizando la función del punto 11 de la guía de For),
# muestre todos los números primos comprendidos entre entre la unidad y un número
# ingresado como parámetro. La función retorna la cantidad de números primos
# encontrados.

def verificar_primo_2(numero:int):

    cont_divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            cont_divisores += 1

    return cont_divisores == 2


def mostrar_primos(numero:int):

    cont_primos = 0

    for i in range(2, numero + 1):
        if verificar_primo_2(i):
            print(i)
            cont_primos += 1

    return cont_primos


numerin = int(input("Ingrese un numero: "))

cantidad = mostrar_primos(numerin)

print(f"Cantidad de numeros primos: {cantidad}")

# 9. Crear una función que imprima la tabla de multiplicar de un número recibido como
# parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir
# el rango de multiplicación. Por defecto es del 1 al 10

def mostrar_tabla_multiplicar(numero:int, inicio:int=1, fin:int=10):
    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))

mostrar_tabla_multiplicar(numero)

# 10. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def pedir_entero():
    numero = int(input("Ingrese un número entero: "))
    return numero


num = pedir_entero()

print(f"El número ingresado es: {num}")

# 11. Crear una función que le solicite al usuario el ingreso de un número flotante y lo
# retorne.

def pedir_flotante():
    numero = float(input("Ingrese un número flotante: "))
    return numero


num = pedir_flotante()

print(f"El número ingresado es: {num}")

# 12. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne

def pedir_cadena():
    cadena = input("Ingrese una cadena: ")
    return cadena


string = pedir_cadena()

print(f"La cadena ingresada es: {string}")

# 13. Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar
# validaciones.

def pedir_entero(mensaje:str):

    while True:
        dato = input(mensaje)

        valido = True

        for i in dato:
            if i < "0" or i > "9":
                valido = False
                break

        if valido and dato != "":
            return int(dato)

        print("Error!!! Debe ingresar un número entero")

def pedir_flotante(mensaje:str):

    while True:

        dato = input(mensaje)

        valido = True
        contador_puntos = 0

        for i in dato:

            if i == ".":
                contador_puntos += 1

            elif i < "0" or i > "9":
                valido = False
                break

        if valido == True and contador_puntos <= 1 and dato != "":
            return float(dato)

        print("Error!!! Debe ingresar un número flotante")

def pedir_cadena(mensaje:str):

    while True:

        cadena = input(mensaje)

        if cadena != "":
            return cadena

        print("Error!!! Debe ingresar una cadena")

numero_entero = pedir_entero("Ingrese un numero entero: ")
numero_flotante = pedir_flotante("Ingrese un numero flotante: ")
string = pedir_cadena("Ingrese un string: ")

print("\n Datos ingresados: ")
print(f"Entero: {numero_entero}")
print(f"Flotante: {numero_flotante}")
print(f"Sting: {string}")