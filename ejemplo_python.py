sentencia="Programación en Python - English School"
contador=0
indice=0

consonante="n"

while indice<len(sentencia):
    if consonante in sentencia[indice]:
        contador=contador+1
    indice=indice+1

print(f"Existen {contador} letras {consonante} en la frase {sentencia}")
