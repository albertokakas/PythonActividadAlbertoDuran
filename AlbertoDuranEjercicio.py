# AlbertoDuranEjercicio 1

print("Hola mundo")


# AlbertoDuranEjercicio 2

a = input("cual es tu nombre ")
print(a)


# AlbertoDuranEjercicio 3

a = int(input("Digite un numero 1 "))
b = int(input("Digite un numero 2 "))
print(a+b)


# AlbertoDuranEjercicio 4

a = int(input("Digite la base del triangulo "))
b = int(input("Digite la altura del triangulo "))
c = 0.5
print(c*a*b)


# AlbertoDuranEjercicio 5

a = int(input("Digite el valor de los grados celsius que desea convertir "))
b = 1.8
c = 32
print((a*b)+c," grados celcius")


# AlbertoDuranEjercicio 6

num = int(input("Digite un numero "))
if num % 2 == 0:
    print("El numero es par ")
else:
    print("El numero es impar")


# AlbertoDuranEjercicio 7

a = int(input("Digite el primer numero "))
b = int(input("Digite el segundo numero "))
c = int(input("Digite el tercero numero "))
if a > b and  a > c:
    print (f"{a} Es el mayor")
elif b > a and b > c:
    print(f"{b} Es el mayor")
elif c > a and c > b:
    print(f"{c} Es el mayor")
else:
    print("Hay numeros iguales")


# AlbertoDuranEjercicio 8

n = int(input("Digite un numero"))
print(n**2)


# AlbertoDuranEjercicio 9

n = int(input("Digite un numero "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")


# AlbertoDuranEjercicio 10

a = "Hola mundo"
print(a[::-1])


# AlbertoDuranEjercicio 11

edad = int(input("Cual es tu edad? "))
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")


# AlbertoDuranEjercicio 12

import math
n = int(input("Digite un numero "))
print(f"El factorial de{n} es: {math.factorial(n)}")


# AlbertoDuranEjercicio 13

import statistics
a = int(input("Digite el primer numero "))
b = int(input("Digite el segundo numero "))
c = int(input("Digite el tercero numero "))
d = int(input("Digite el cuarto numero "))
e = int(input("Digite el quinto numero "))
n = [a, b, c, d, e]
promedio = statistics.mean(n)
print(f"El promedio es:{promedio}")


# AlbertoDuranEjercicio 14

n = int(input("Digite un número: "))
print(f"Números pares desde 1 hasta {n}:")
for i in range(1, n + 1):
    if i % 2 == 0:  
        print(i)


# AlbertoDuranEjercicio 15

letra = input("Digite una letra: ")
if letra in "aeiouAEIOU":
    print("Es una vocal")
else:
    print("Es una consonante")


# AlbertoDuranEjercicio 16

a, b = 0, 1
for i in range(20):
    print(a)
    a, b = b, a + b 


# AlbertoDuranEjercicio 17

num = int(input("piensa en un numero: "))
primo = True
if num <= 1:
    primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
print(f"El numero:" , num , "si es primo" if primo else "no es primo")


# AlbertoDuranEjercicio 18

lista = list(range(1, 100))
for a in lista:
    if a % 5 == 0:
        print(a)


# AlbertoDuranEjercicio 19

p = input("Escribe cualquier palabra: ").lower()
vocal = "aeiou"
cont = 0
for letra in p:
    if letra in vocal:
        cont += 1
print("la cantidad de vocales en la palabra", p , "es de:", cont)


# AlbertoDuranEjercicio 20

a = float(input("Dime el primer numero: "))
b = float(input("Dime el segundo numero: "))
op = input("Que operacion quieres realizar? +, -, *, / : ")
if op == "+":
    print("El resultado de la suma es:", a + b)
elif op == "-":
    print("El resultado de la resta es:", a - b)
elif op == "*":
    print("El resultado de la multiplicacion es:", a * b)
elif op == "/":
    if b != 0:
        print("El resultado al hacer la division es:", a / b)
    else:
        print("Disculpa, no es posible dividir entre 0")
else:
    print("la operación no es valida")


# AlbertoDuranEjercicio 21

num = [1, 10, 8, 16, 12, 4, 7, 11, 6, 9]
may = num[0]
for n in num:
    if n > may:
        may = n
print("El numero mayor de la lista", num , "es:", may)


# AlbertoDuranEjercicio 22

numeros = [5, 2, 9, 1, 7]
ordenados = sorted(numeros)
print(ordenados)


# AlbertoDuranEjercicio 23

datos = [1, 2, 2, 3, 4, 4, 5]
limpios = list(set(datos))
print(limpios)


# AlbertoDuranEjercicio 24

personas = ["Alberto", "Valeria", "Yell", "Sharol"]
ordenados = sorted(personas)
print(ordenados)


# AlbertoDuranEjercicio 25

valores = [1, 2, 3, 4, 5]
total = sum(valores)
print(total)


# AlbertoDuranEjercicio 26

grupo1 = [1, 2, 3]
grupo2 = [4, 5, 6]
completo = grupo1 + grupo2
print(completo)


# AlbertoDuranEjercicio 27

F= input("split sirve para dividir una cadena de texto en una lista de subcadenas")
p=F.split()
print(len(p))


# AlbertoDuranEjercicio 28

p=input("Check de palindromo")
if p==p[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")


# AlbertoDuranEjercicio 29

C=[]
for i in range(1, 11):
    C.append(i**2)
print(C)


# AlbertoDuranEjercicio 30

N=[10, 1, 5, 8, 6, 18, 14]
N_U=list(set(N))
N_U.sort()
print(N_U[-2])


