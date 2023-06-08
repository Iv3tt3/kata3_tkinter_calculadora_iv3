unidades = {
    1 : "I",
    5 : "V",
    10: "X"
}
decenas = {
    1 : "X",
    5 : "L",
    10: "C"
}

centenas = {
    1: "C",
    5: "D",
    10: "M"
}

miles = {
    1: "M"
}

class RomanNumberError(Exception):
    pass

def listar_numero(num):
    n_mil = num // 1000 * 1000
    n_cent = (num % 1000) // 100 * 100
    n_dec = (num % 100) // 10 * 10
    n_uni = (num % 10)

    return n_mil, n_cent, n_dec, n_uni

def sacar_clave(num):
    if num >=1000:
        clave = miles
        num = num // 1000
    
    elif num >= 100:
        clave = centenas
        num = num // 100

    elif num >= 10:
        clave = decenas
        num = num // 10
    else: 
        clave = unidades
    return clave, num

def sacar_simbolo_digito(clau, digit):
    simbol_digit = ""
    if digit < 4:
        simbol_digit += digit * clau[1]
    elif digit == 4:
        simbol_digit += clau[1] + clau[5]
    elif digit < 9:
        num_unidades = digit - 5
        simbol_digit += clau[5] + num_unidades * clau[1]
    else:
        simbol_digit += clau[1] + clau[10]
    return simbol_digit 


def entero_a_romano(n_int):
    if n_int > 3999:
        raise RomanNumberError("RomanNumber must be less of 4000")
    
    digitos = listar_numero(n_int)

    resultado = ''

    for digito in digitos:
        if digito == 0:
            continue # te ignora el siguiente codigo del for y te coge el siguiente digito
        
        clave, digito = sacar_clave(digito)

        resultado += sacar_simbolo_digito(clave, digito)

    return resultado


num_romanos = {
    'I' : 1,
    'V' : 5,
    'X': 10,
    "L" : 50,
    "C": 100,
    "D" : 500,
    "M": 1000
}

def comprobar_excepciones(romano):
    for simbolo in num_romanos:
        if simbolo * 4 in romano:
            #Arregla ejemplo 'XXXX'
            raise RomanNumberError("No se admiten más de tres simbolos iguales")
        elif simbolo in ('VLD') and simbolo * 2 in romano:
            #Los simbolos VLD solo pueden salir 1 vez en la cadena
            raise RomanNumberError("No se pueden repetir V, L o D")


def Romano_a_Entero(letras):
    valor_total = 0
    ultimo_valor = 0
    valor_final = 0
    #ultimo_simbolo = ""

    comprobar_excepciones(letras) #No hace falta devolver resultado. Si la cosa va bien no se queja y si se queja hemos lanzado una excepcion.

    for numeral in reversed(letras):
        valor_actual = num_romanos[numeral]
        if valor_actual <= 5 and ultimo_valor >= 50:
            # Si es I V y el ultimo valor es L D C M
            raise RomanNumberError("Resta no permitida")
        if valor_actual <= 50 and ultimo_valor >= 500:
            # Si es I V X L y el ultimo valor es D M
            raise RomanNumberError("Resta no permitida")
        
        if valor_final == valor_actual and ultimo_valor > valor_actual:
            #Para solucionar IVIV
            raise RomanNumberError("No permitidas dos restas seguidas")
        if valor_actual < valor_final:
            raise RomanNumberError("No ordenado en ascendente")
            #Para solucionar VIX i IIX

        if valor_actual >= ultimo_valor:
            valor_total += valor_actual
        elif numeral not in 'VLD': 
            # VLD no pueden restar por lo que no pueden entrar en resta
            valor_total -= valor_actual
        else:
            raise RomanNumberError("Resta no permitida")
        valor_final = ultimo_valor
        ultimo_valor = valor_actual
        #ultimo_simbolo = numeral
    return valor_total 


if __name__ == "__main__": #Esto es para que solo ejecute el codigo que sigue cuando ejecutemos el programa desde romannumbers, pero en otros ficheros donde se importe no se va a ejecutar
    print(entero_a_romano(0))