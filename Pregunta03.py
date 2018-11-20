print("Matriz...(3x3)")

while True:

    a = int(input("Ingrese un numero para la primera fila : "))
    x = int(input("Ingrese un numero para la primera fila : "))
    y = int(input("Ingrese un numero para la primera fila : "))

    z = int(input("Ingrese un numero para la segunda fila : "))
    b = int(input("Ingrese un numero para la segunda fila : "))
    t = int(input("Ingrese un numero para la segunda fila : "))

    u = int(input("Ingrese un numero para la tercera fila : "))
    v = int(input("Ingrese un numero para la tercera fila : "))
    c = int(input("Ingrese un numero para la tercera fila : "))

    diagonal = a + b + c

    print(a," ",x," ",y)
    print(z," ",b," ",t)
    print(u," ",v," ",c)

    print("La suma total de la diagonal es ",diagonal)

    salir = input("¿Desea continuar? S/N : ")
    if salir == "N":
        break
