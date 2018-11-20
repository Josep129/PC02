
a = int(input("Ingrese el primer numero : "))
b = int(input("Ingrese el segundo numero : "))
c = int(input("Ingrese el tercer numero : "))
d = int(input("Ingrese el cuarto numero : "))
e = int(input("Ingrese el quinto numero : "))

acd = [a,b,c,d,e]

print("Los numeros son : ",acd)

x = 0
y = 0
M = 0

def menor_en_arreglo():
    if a<b:
        a = x
    else:
        b = x

    if c<d:
        c = y
    else:
        d = y
    if x<y:
        x = M
    else:
        y = M
    if M<c:
        print(M)
    else:
        print(c)

print(menor_en_arreglo)