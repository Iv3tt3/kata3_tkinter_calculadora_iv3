'''from romannumbers import *

class RomanNumber:
    def __init__(self, input):
        if type(input) == int:
            #cuando pones _ delante es como una regla legible para todo el mundo
            self._numero = input
            self._simbolo = entero_a_romano(input)
        elif isinstance (input, str):
            self._numero = Romano_a_Entero(input)
            self._simbolo = input
        else:
            raise RomanNumberError("Se debe introducir un entero o romano valido")
    
    @property
    def num(self):
        return self._numero
    
    @num.setter
    def num(self, input):
        self._numero = input
        self._simbolo = entero_a_romano(input)

    @property
    def simbol(self):
        return self._simbolo
    
    @simbol.setter
    def simbol(self, input):
        self._numero = Romano_a_Entero(input)
        self._simbolo = input
    
''' 
from romannumbers import *

class RomanNumber:
    def __init__(self, entrada):
        if type(entrada) == int and entrada >0:
            #cuando pones un _ delante estas diciendo que no los usen
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif isinstance (entrada, str):
            self._numero = Romano_a_Entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumberError("Se debe introducir un entero mayor que cero o un romano valido")
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, entrada):
        self._numero = entrada
        self._simbolo = entero_a_romano(entrada)

    @property
    def simbolo(self):
        return self._simbolo
    
    @simbolo.setter
    def simbolo(self, entrada):
        self._numero = Romano_a_Entero(entrada)
        self._simbolo = entrada


    def __to_roman(self, otro):
        #Este metodo queremos que sea privado por lo que lo indicamos con __
        if type(otro) != RomanNumber:
            otro = RomanNumber(otro)
        return otro

    #Metodos magicos para la logica


    def __eq__(self, other):
        #Este metodo es necesario para comparar instancias, es decir, el resultado de numero * otro numero saca una instancia y se compara con otra instancia guardada en otro espacio de memoria. Aunque sea iguales, python no los ve iguales. Por eso es necesario este metodo.
        other = self.__to_roman(other)
        return self.numero == other.numero
    
    #def __req__(self, other):
        #reverse equal
       # other = self.__to_roman(other)
       # return self.__eq__(other)
    
    def __lt__(self, other):
        #less
        other = self.__to_roman(other)
        return self.numero < other.numero
    
    def __le__(self, other):
        #less and equal
        other = self.__to_roman(other)
        return self.numero <= other.numero
    
    def __gt__(self, other):
        #grater
        other = self.__to_roman(other)
        return self.numero > other.numero
    
    def __ge__(self, other):
        #grater and equal
        other = self.__to_roman(other)
        return self.numero >= other.numero

    def __ne__(self, other):
        #not equal
        other = self.__to_roman(other)
        return self.numero != other.numero
    
    
    #Metodos magicos para aritmetica

    #Sumar
    def __add__(self, otro):
        otro = self.__to_roman(otro)
        resultado = self.numero + otro.numero
        return RomanNumber(resultado)

    def __radd__(self, otro):
        return self.__add__(otro)

    #Restar

    def __sub__(self, otro):
        otro = self.__to_roman(otro)
        if self.numero <= otro.numero:
            raise RomanNumberError("Resta no permitida, el resultado no existe en numeros romanos porque da un valor negativo o cero")
        resultado = self.numero - otro.numero
        return RomanNumber(resultado)

    def __rsub__(self, otro):
        otro = self.__to_roman(otro)
        return otro.__sub__(self)

    #Multiplicar
    def __mul__(self, otro):
        if not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)
        resultado = self.numero * otro.numero
        return RomanNumber(resultado)
    
    def __rmul__(self, otro):
        #En self mete el romano1 y en otro el 5 aunque en el test linea 54 hemos puesto assert 5 * romano1 porque el rmult es el mult reverse
        return self.__mul__(otro)


    #Dividir
    def __truediv__(self, otro):
        otro = self.__to_roman(otro)
        resultado = int(self.numero / otro.numero)
        #Nunca dividira entre cero por el AND añadido en linia 38
        if self.numero % otro.numero != 0:
            raise RomanNumberError("Division no permitida. La division no es exacta o entera, el resultado es un numero decimal")
            #resultado = int(resultado)
            #decimales = (self.numero / otro.numero) - resultado
            #print("La division no es entera o exacta, los decimales son: ", decimales)
        return RomanNumber(resultado)

    def __rtruediv__(self, otro):
        otro = self.__to_roman(otro)
        return otro.__truediv__(self)

    #Metodos magicos representacion

    def __repr__(self):
        return f"{self.numero} [{self.simbolo}]"
    
    def __str__(self):
        return self.__repr__()



if __name__ == "__main__":
    pass

