def mostrar_resultados(r1, r2, r3, r4):
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

def leer_entrada():
    with open("entrada.txt", "rt", encoding="utf-8") as archivo_entrada:
        return archivo_entrada.readline()

def es_numero(c):
    return "0" <= c <= "9"

def es_impar(n):
    return n % 2 == 1

def es_vocal(c):
    return c.lower() in "aeiou"

def es_letra(c):
    return "a" <= c <= "z" or "A" <= c <= "Z"

def es_consonante(c):
    # return c in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return es_letra(c) and not es_vocal(c)

def es_b(c):
    return c in "bB"

def es_m(c):
    return c in "mM"

def es_d(c):
    return c in "dD"

def calcular_promedio(suma, cantidad):
    promedio = 0
    if cantidad > 0:
        promedio = suma // cantidad
    
    return promedio


def principal():
    texto = leer_entrada()
    cont_caracteres = 0

    # Punto 1
    cont_impar_minusculas = 0
    empieza_con_numero_impar = False
    todas_minusculas = True

    # Punto 2
    mayor_longitud = 0
    empieza_con_vocal = False
    tiene_b = False

    # Punto 3
    cont_palabras_con_mas_consonantes = 0
    suma_letras_palabras_con_mas_consonantes = 0
    cont_vocales = 0
    cont_consonantes = 0
    tiene_m = False

    # Punto 4
    anterior = None
    cont_d_vocal = 0
    cont_palabras_d_vocal = 0

    for c in texto:

        if c == " " or c == ".": # Detecta el final de cada palabra
            # Evaluación de variables por palabra

            # Punto 1
            if empieza_con_numero_impar and todas_minusculas:
                cont_impar_minusculas += 1

            # Punto 2
            if empieza_con_vocal and tiene_b:
                if cont_caracteres > mayor_longitud:
                    mayor_longitud = cont_caracteres

            # Punto 3
            if cont_consonantes > cont_vocales and tiene_m:
                cont_palabras_con_mas_consonantes += 1
                suma_letras_palabras_con_mas_consonantes += cont_caracteres

            # Punto 4
            if cont_d_vocal >= 2 and es_vocal(anterior):
                cont_palabras_d_vocal += 1

            # Inicialización de variables por palabra

            cont_caracteres = 0
            # Punto 1
            empieza_con_numero_impar = False
            todas_minusculas = True

            # Punto 2
            empieza_con_vocal = False
            tiene_b = False

            # Punto 3
            cont_vocales = 0
            cont_consonantes = 0
            tiene_m = False

            # Punto 4
            anterior = None
            cont_d_vocal = 0

        else: # Evalúa cada caracter en la palabra
            cont_caracteres += 1

            # Punto 1
            if cont_caracteres == 1:
                if es_numero(c):
                    empieza_con_numero_impar = es_impar(int(c))
            else:
                if empieza_con_numero_impar:
                    if not c.islower():
                        todas_minusculas = False

            # Punto 2
            if cont_caracteres == 1:
                empieza_con_vocal = es_vocal(c)
            else:
                tiene_b = tiene_b or es_b(c)

            # Punto 3
            if es_consonante(c):
                cont_consonantes += 1
            elif es_vocal(c):
                cont_vocales += 1
            if es_m(c):
                tiene_m = True

            # Punto 4
            if es_vocal(c) and anterior is not None and es_d(anterior):
                cont_d_vocal += 1

            anterior = c

    promedio = calcular_promedio(suma_letras_palabras_con_mas_consonantes,
                                cont_palabras_con_mas_consonantes)

    mostrar_resultados(cont_impar_minusculas, mayor_longitud, 
        promedio, cont_palabras_d_vocal)


if __name__ == "__main__":
    principal()
