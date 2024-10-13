special_methods = ["__getattribute__","__getattr__","__delattr__","__delitem__","__delslice__","__setattr__","__setitem__","__setslice__","__missing__","__getitem__","__getslice__","__eq__","__ge__","__gt__","__le__","__ne__","__lt__","__hash__","__add__","__and__","__divmod__","__floordiv__","__lshift__","__matmul__","__mod__","__mul__","__or__","__pow__","__rshift__","__sub__","__truediv__","__xor__","__radd__","__rand__","__rdiv__","__rdivmod__","__rfloordiv__","__rlshift__","__rmatmul__","__rmod__","__rmul__","__ror__","__rpow__","__rrshift__","__rsub__","__rtruediv__","__rxor__","__iadd__","__iand__","__ifloordiv__","__ilshift__","__imatmul__","__imod__","__imul__","__ior__","__ipow__","__irshift__","__isub__","__itruediv__","__ixor__","__abs__","__neg__","__pos__","__invert__","__index__","__trunc__","__floor__","__ceil__","__round__","__iter__","__len__","__reversed__","__contains__","__next__","__int__","__bool__","__nonzero__","__complex__","__float__","__format__","__cmp__","__enter__","__exit__","__get__","__set__","__delete__","__set_name__","__aenter__","__aexit__","__aiter__","__anext__","__await__","__call__","__class__","__dir__","__init__","__init_subclass__","__prepare__","__new__","__subclasses__","__instancecheck__","__subclasscheck__","__class_getitem__","__str__","__repr__","__import__","__bytes__","__fspath__","__getnewargs__","__reduce__","__reduce_ex__","__sizeof__","__length_hint__"]

class MiClase:
    def __init__(self, valor):
        self.valor = valor
    
    # Métodos de búsqueda de item/atributo/método:
    def __getattribute__(self, nombre):
        print(f'Obteniendo atributo {nombre}')
        return object.__getattribute__(self, nombre)
    
    def __getattr__(self, nombre):
        return f'Atributo {nombre} no encontrado'
    
    def __setattr__(self, nombre, valor):
        print(f'Estableciendo atributo {nombre} con valor {valor}')
        self.__dict__[nombre] = valor
    
    def __delattr__(self, nombre):
        print(f'Eliminando atributo {nombre}')
        del self.__dict__[nombre]
    
    def __getitem__(self, indice):
        return f'Elemento en el índice {indice}'
    
    def __setitem__(self, indice, valor):
        print(f'Estableciendo elemento en el índice {indice} con valor {valor}')
        self.__dict__[indice] = valor
    
    def __delitem__(self, indice):
        print(f'Eliminando elemento en el índice {indice}')
        del self.__dict__[indice]
    
    # Métodos de igualdad y hash:
    def __eq__(self, otro):
        return self.valor == otro.valor
    
    def __ge__(self, otro):
        return self.valor >= otro.valor
    
    def __gt__(self, otro):
        return self.valor > otro.valor
    
    def __le__(self, otro):
        return self.valor <= otro.valor
    
    def __ne__(self, otro):
        return self.valor != otro.valor
    
    def __lt__(self, otro):
        return self.valor < otro.valor
    
    def __hash__(self):
        return hash(self.valor)
    
    # Operadores binarios:
    def __add__(self, otro):
        return self.valor + otro.valor
    
    def __and__(self, otro):
        return self.valor & otro.valor
    
    def __divmod__(self, otro):
        return divmod(self.valor, otro.valor)
    
    def __floordiv__(self, otro):
        return self.valor // otro.valor
    
    def __lshift__(self, otro):
        return self.valor << otro.valor
    
    def __matmul__(self, otro):
        return self.valor @ otro.valor
    
    def __mod__(self, otro):
        return self.valor % otro.valor
    
    def __mul__(self, otro):
        return self.valor * otro.valor
    
    def __or__(self, otro):
        return self.valor | otro.valor
    
    def __pow__(self, otro):
        return self.valor ** otro.valor
    
    def __rshift__(self, otro):
        return self.valor >> otro.valor
    
    def __sub__(self, otro):
        return self.valor - otro.valor
    
    def __truediv__(self, otro):
        return self.valor / otro.valor
    
    def __xor__(self, otro):
        return self.valor ^ otro.valor
    
    # Métodos binarios invertidos:
    def __radd__(self, otro):
        return otro.valor + self.valor
    
    def __rand__(self, otro):
        return otro.valor & self.valor
    
    def __rdiv__(self, otro):
        return otro.valor / self.valor
    
    def __rdivmod__(self, otro):
        return divmod(otro.valor, self.valor)
    
    def __rfloordiv__(self, otro):
        return otro.valor // self.valor
    
    def __rlshift__(self, otro):
        return otro.valor << self.valor
    
    def __rmatmul__(self, otro):
        return otro.valor @ self.valor
    
    def __rmod__(self, otro):
        return otro.valor % self.valor
    
    def __rmul__(self, otro):
        return otro.valor * self.valor
    
    def __ror__(self, otro):
        return otro.valor | self.valor
    
    def __rpow__(self, otro):
        return otro.valor ** self.valor
    
    def __rrshift__(self, otro):
        return otro.valor >> self.valor
    
    def __rsub__(self, otro):
        return otro.valor - self.valor
    
    def __rtruediv__(self, otro):
        return otro.valor / self.valor
    
    def __rxor__(self, otro):
        return otro.valor ^ self.valor
    
    # Métodos de asignación aumentada:
    def __iadd__(self, otro):
        self.valor += otro.valor
        return self
    
    def __iand__(self, otro):
        self.valor &= otro.valor
        return self
    
    def __ifloordiv__(self, otro):
        self.valor //= otro.valor
        return self
    
    def __ilshift__(self, otro):
        self.valor <<= otro.valor
        return self
    
    def __imatmul__(self, otro):
        self.valor @= otro.valor
        return self
    
    def __imod__(self, otro):
        self.valor %= otro.valor
        return self
    
    def __imul__(self, otro):
        self.valor *= otro.valor
        return self
    
    def __ior__(self, otro):
        self.valor |= otro.valor
        return self
    
    def __ipow__(self, otro):
        self.valor **= otro.valor
        return self
    
    def __irshift__(self, otro):
        self.valor >>= otro.valor
        return self
    
    def __isub__(self, otro):
        self.valor -= otro.valor
        return self
    
    def __itruediv__(self, otro):
        self.valor /= otro.valor
        return self
    
    def __ixor__(self, otro):
        self.valor ^= otro.valor
        return self
    
    # Métodos unarios:
    def __abs__(self):
        return abs(self.valor)
    
    def __neg__(self):
        return -self.valor
    
    def __pos__(self):
        return +self.valor
    
    def __invert__(self):
        return ~self.valor
    
    # Métodos matemáticos:
    def __index__(self):
        return int(self.valor)
    
    def __trunc__(self):
        return int(self.valor)
    
    def __floor__(self):
        return int(self.valor)
    
    def __ceil__(self):
        return int(self.valor)
    
    def __round__(self):
        return round(self.valor)
    
    # Métodos de iterador:
    def __iter__(self):
        return iter(self.valor)
    
    def __len__(self):
        return len(self.valor)
    
    def __reversed__(self):
        return reversed(self.valor)
    
    def __contains__(self, item):
        return item in self.valor
    
    def __next__(self):
        return next(self.valor)
    
    # Conversión de tipos numéricos:
    def __int__(self):
        return int(self.valor)
    
    def __bool__(self):
        return bool(self.valor)
    
    def __nonzero__(self):
        return bool(self.valor)
    
    def __complex__(self):
        return complex(self.valor)
    
    def __float__(self):
        return float(self.valor)
    
    # Otros métodos:
    def __format__(self, formato):
        return format(self.valor, formato)
    
    def __cmp__(self, otro):
        if self.valor < otro.valor:
            return -1
        elif self.valor == otro.valor:
            return 0
        else:
            return 1
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def __get__(self, instancia, tipo):
        return self.valor
    
    def __set__(self, instancia, valor):
        self.valor = valor
    
    def __delete__(self, instancia):
        del self.valor
    
    def __set_name__(self, owner, name):
        pass
    
    def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        pass
    
    async def __aiter__(self):
        return self
    
    async def __anext__(self):
        return next(self.valor)
    
    async def __await__(self):
        return await self.valor
    
    def __call__(self, *args, **kwargs):
        return self.valor(*args, **kwargs)
    
    def __class__(self):
        return type(self.valor)
    
    def __dir__(self):
        return dir(self.valor)
    
    def __init__(self):
        pass
    
    def __init_subclass__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __prepare__(cls, *args, **kwargs):
        return {}
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __subclasses__(self):
        return self.valor.__subclasses__()
    
    def __instancecheck__(self, instance):
        return isinstance(self.valor, instance)
    
    def __subclasscheck__(self, subclass):
        return issubclass(self.valor, subclass)
    
    def __class_getitem__(self, item):
        return self.valor[item]
    
    def __str__(self):
        return str(self.valor)
    
    def __repr__(self):
        return repr(self.valor)
    
    def __import__(self):
        return __import__(self.valor)
    
    def __bytes__(self):
        return bytes(self.valor)
    
    def __fspath__(self):
        return None
        return fspath(self.valor)
    
    def __getnewargs__(self):
        return self.valor.__getnewargs__()
    
    def __reduce__(self):
        return self.valor.__reduce__()
    
    def __reduce_ex__(self, protocol):
        return self.valor.__reduce_ex__(protocol)
    
    def __sizeof__(self):
        return self.valor.__sizeof__()
    
    def __length_hint__(self):
        return len(self.valor)
    
# Crear una instancia de MiClase
objeto = MiClase(5)

# Ejemplos de métodos de búsqueda de item/atributo/método:
print(objeto.atributo_existente)  # Salida: 'Obteniendo atributo atributo_existente'

print(objeto.atributo_inexistente)  # Salida: 'Atributo atributo_inexistente no encontrado'

# Establecimiento de atributo
objeto.nuevo_atributo = 'Nuevo valor'  # Salida: 'Estableciendo atributo nuevo_atributo con valor Nuevo valor'

# Eliminación de atributo
del objeto.nuevo_atributo  # Salida: 'Eliminando atributo nuevo_atributo'

# Acceso a elemento como diccionario
print(objeto['clave'])  # Salida: 'Elemento en el índice clave'

# Establecimiento de elemento como diccionario
objeto['clave'] = 'nuevo_valor'  # Salida: 'Estableciendo elemento en el índice clave con valor nuevo_valor'

# Eliminación de elemento como diccionario
del objeto['clave']  # Salida: 'Eliminando elemento en el índice clave'

# Ejemplos de métodos de igualdad y hash:
otro_objeto = MiClase(5)
print(objeto == otro_objeto)  # Salida: True

print(objeto != otro_objeto)  # Salida: False

print(hash(objeto))  # Salida: hash del valor del objeto

# Ejemplo de operador binario:
resultado = objeto + otro_objeto
print(resultado)  # Salida: suma de los valores de los objetos

# Ejemplo de método unario:
print(abs(objeto))  # Salida: valor absoluto del objeto

# Ejemplo de método matemático:
print(int(objeto))  # Salida: valor del objeto convertido a entero

# Ejemplos de métodos de iterador:
for elemento in objeto:
    print(elemento)  # Salida: iteración sobre los elementos del objeto

print(len(objeto))  # Salida: longitud del objeto

print(list(reversed(objeto)))  # Salida: lista de los elementos del objeto en orden inverso

print('clave' in objeto)  # Salida: verificación de si el objeto contiene la clave 'clave'

# Ejemplo de conversión de tipos numéricos:
print(float(objeto))  # Salida: valor del objeto convertido a flotante

# Ejemplos de otros métodos:
print(str(objeto))   # Salida: representación en cadena del objeto
print(repr(objeto))  # Salida: representación de cadena del objeto para su reproducción exacta