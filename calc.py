print("calculadora con una sola variable\n")

print("menu de opciones\n")

print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. division entera")
print("6. exponente")
print("7. modulo o resto\n")

numero = int(input("introduce una opcion: "))

if numero == 1:
    print("Elegiste suma")
    numero = int(input("introduce el primer numero: "))
    numero += int(input("introduce el segundo numero: "))
    print("tu resultado es: ",numero)

elif numero == 2:
    print("elegiste resta")
    numero = int(input("intrduce el primer numero: "))
    numero -= int(input("introduce el segundo numero: "))
    print("tu resultado es: ", numero)

elif numero == 3:
    print("elegiste multiplicacion")
    numero = int(input("intrduce el primer numero: "))
    numero *= int(input("introduce el segundo numero: "))
    print("tu resultado es: ", numero)

elif numero == 4:
    print("elegiste division")
    numero = float(input("introduce el primer numero: "))
    numero /= float(input("introduce el segundo numero: "))
    print("tu resultado es: ", numero)

elif numero == 5:
    print("elegiste division entera")
    numero = int(input("introduce el primer numero: "))
    numero //= int(input("introduce el segundo numero: "))
    print("tu resultado es: ", numero)

elif numero == 6:
    print("elegiste exponente")
    numero = int(input("introduce el primer numero: "))
    numero **= int(input("introduce el segundo numero: "))
    print("tu resultado es: ", numero)

elif numero == 7:
    print("elegiste modulo o resto")
    numero = int(input("introduce el primer numero: "))
    numero %= int(input("introduce el segundo numero: "))
    print("tu resultado es: ", numero)

else:
    print("la opcion no existe")