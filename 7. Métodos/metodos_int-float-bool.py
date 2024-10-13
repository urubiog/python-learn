# Integer methods
['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

# Definimos un número entero
integer = 42

# Devuelve la fracción asociada al número entero
fraccion = integer.as_integer_ratio() # Output: Fracción: (42, 1)

# Devuelve el número de bits establecidos en la representación binaria del entero
conteo_bits = integer.bit_count() # Output: Número de bits: 5

# Devuelve la longitud en bits necesaria para representar el entero en binario
longitud_bits = integer.bit_length() # Output: Longitud de bits: 6

# Devuelve el conjugado del número complejo (para enteros, es el mismo número)
conjugado = integer.conjugate() # Output: Conjugado: 42

# Devuelve el denominador del número (si es entero, el denominador es 1)
denominador = integer.denominator # Output: Denominador: 1

# Crea un número entero a partir de una secuencia de bytes
bytes_entero = integer.to_bytes(2, byteorder='big') # Output: 42

# Retorna la parte imaginaria del número (si es entero, es 0)
parte_imaginaria = integer.imag # Output: Parte imaginaria: 0 

# Devuelve True si el número es entero, False si no lo es
es_entero = integer.is_integer() # Output: ¿Es entero?: True

# Float mehtods
['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

flotante = 3.14

# Devuelve la fracción asociada al número de punto flotante
fraccion_flotante = flotante.as_integer_ratio() # Output: Fracción: (7070651414971679, 2251799813685248)

# Devuelve el conjugado del número complejo (para flotantes, es el mismo número)
conjugado_flotante = flotante.conjugate() # Output: Conjugado: 3.14

# Crea un número de punto flotante a partir de su representación hexadecimal
fromhex_flotante = float.fromhex('0x1.921fb54442d18p+1') # Output: 3.14

# Retorna la representación hexadecimal del número de punto flotante
hex_flotante = flotante.hex() # Output: 0x1.921fb54442d18p+1

# Retorna la parte imaginaria del número (si es un flotante, es 0)
parte_imaginaria_flotante = flotante.imag # Output: Parte imaginaria: 0.0

# is_integer(): Devuelve True si el número es un entero, False si no lo es
es_entero_flotante = flotante.is_integer() # Output: ¿Es entero?: False

# Bool methods
['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

booleano = True

# Devuelve la fracción asociada al valor booleano (1 para True, 0 para False)
fraccion_booleano = booleano.as_integer_ratio() # Output: Fracción: (1, 1)

# Devuelve el número de bits establecidos en la representación binaria del valor booleano
conteo_bits_booleano = booleano.bit_count() # Output: Número de bits: 1

# Devuelve la longitud en bits necesaria para representar el valor booleano en binario
longitud_bits_booleano = booleano.bit_length() # Output: Longitud de bits: 1

# Devuelve el conjugado del número complejo (para valores booleanos, es el mismo valor)
conjugado_booleano = booleano.conjugate() # Output: Conjugado: 1

# Devuelve el denominador del número (si es un booleano, el denominador es 1)
denominador_booleano = booleano.denominator # Output: Denominador: 1

# Crea un número entero a partir de una secuencia de bytes (1 para True, 0 para False)
bytes_booleano = booleano.to_bytes(1, byteorder='big') # Output: b'\x01'

# Retorna la parte imaginaria del número (si es un booleano, es 0)
parte_imaginaria_booleano = booleano.imag # Output: Parte imaginaria: 0

# is_integer(): Devuelve True si el número es un entero, False si no lo es (siempre devuelve True o False para valores booleanos)
es_entero_booleano = booleano.is_integer() # Output: ¿Es entero?: True