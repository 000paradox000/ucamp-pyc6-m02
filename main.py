# UCAMP Bootcamp Python C6
# Proyecto Módulo 2

palabra = input("Ingresa una palabra entre 4 a 8 caracteres: ")
longitud = len(palabra)

# validar que la longitud esté entre 4 y 8
# if 8 >= longitud >= 4:
if longitud >= 4 and longitud <= 8:
    print("La palabra es correcta y tiene la longitud correcta")

# Si la palabra tiene menos de 4 letras debe indicar un 
# mensaje que diga: Hacen falta letras. Solo tiene N letras   
if longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras")

# Si la palabra tiene más de 8 letras debe indicar un mensaje que 
# diga: Sobran letras. Tiene N letras ((siendo N el número de 
# letras de la palabra))
if longitud > 8:
    print(f"Sobran letras. Tiene {longitud} letras.")
