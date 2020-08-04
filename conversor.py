def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " +tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + " dólares")    


menu = """ 
Bienvenido al conversor de monedas $
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción : 
"""

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('ingresa una opción correcta')

"""
if opcion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + " dólares")

elif opcion == 2:
    pesos = input("¿Cuántos pesos argentinas tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + " dólares")

elif opcion == 3:
    pesos = input("¿Cuántos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + " dólares")

else:
    print('Por favor ingresa una opción correcta')

"""