import random

lanzar_dados=input("Deseas lanzar los dados (si/no): ")

if lanzar_dados.lower()=="si":
    lanzar_dados=True
else:
    lanzar_dados=False


def funcion():

    lista=[1,2,3,4,5,6]

    numero_1 = random.choice(lista)
    frase_1 = f" El resultado del dado 1 es: {numero_1}\n"

    numero_2=random.choice(lista)
    frase_2=f"El resultado del dado 2 es: {numero_2}\n"

    frase_total=f"La suma de los resultados de los dados es: {numero_1+numero_2}\n"

    return print(frase_1,frase_2,frase_total)

funcion()

while lanzar_dados==True:

    lanzar_dados=input("Deseas lanzar los dados otra vez(si/no): ")

    if lanzar_dados.lower()=="si":
        lanzar_dados=True
        funcion()
    else:
        print("has dejado de lanzar dados.")
        lanzar_dados=False
