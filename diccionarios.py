def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # Ver diccionario
    # print(mi_diccionario)
    # Ver llave especifica
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brazil': 210147125,
        'Colombia': 50372424,
    }
    # Población de cada pais con llave
    print(poblacion_paises['Argentina'])
    
    # Recorrer con ciclo for metodo que devuelve llaves
    for pais in poblacion_paises.keys():
        print(pais)
    # Recorrer con ciclo for metodo que devuelve los valores del diccionario
    for pais in poblacion_paises.values():
        print(pais)
    # Recorrer con ciclo for metodo que devuelve los 2 valores del diccionario
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')



if __name__ == "__main__":
    run()