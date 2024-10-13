import asyncio
from typing import Any, AnyStr, AsyncGenerator, AsyncIterable, AsyncIterator, ByteString, Concatenate, Coroutine, Generator, Generic, Iterable, Iterator, Mapping, NamedTuple, NewType, NoReturn, Optional, Reversible, Sequence, Sized, Union, TypeVar, Callable, Protocol, ContextManager, IO, Match, Pattern, Text, Type, TypedDict, cast, get_args, get_origin, final, no_type_check, no_type_check_decorator, overload, runtime_checkable, AbstractSet, Deque, Dict, FrozenSet, List, MutableMapping, MutableSequence, MutableSet, OrderedDict, Set, Tuple
from collections import ChainMap, Counter, defaultdict, deque

# Any: puede ser cualquier tipo
def process(value: Any) -> None:
    print(f"Processing value of any type: {value}")

process(10)
process("text")
process([1, 2, 3])

# AnyStr: puede ser str o bytes
def concatenate(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

print(concatenate("Hello, ", "world!"))
print(concatenate(b"Hello, ", b"world!"))

# ByteString: secuencias inmutables de bytes
def process_bytes(data: ByteString) -> None:
    print(f"Processing ByteString: {data}")

process_bytes(b"byte data")

# Coroutine: una función corrutina
async def my_coroutine() -> Coroutine[None, None, int]:
    await asyncio.sleep(1)
    return 42

async def main():
    result = await my_coroutine()
    print(f"Coroutine result: {result}")

# Generic: creación de clases genéricas
T = TypeVar('T')
class Stack(Generic[T]):
    def __init__(self):
        self.items = []
    def push(self, item: T) -> None:
        self.items.append(item)
    def pop(self) -> T:
        return self.items.pop()

stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

# NewType: creación de un nuevo tipo
UserId = NewType('UserId', int)
def get_user_name(user_id: UserId) -> str:
    return f"User{user_id}"

user_id = UserId(12345)
print(get_user_name(user_id))

# NoReturn: una función que no retorna un valor
def stop_execution() -> NoReturn:
    raise SystemExit(1)

# Optional: puede ser un tipo especificado o None
def greet(name: Optional[str]) -> None:
    if name is not None:
        print(f"Hello, {name}")
    else:
        print("Hello, stranger")

greet("Alice")
greet(None)

# Union: puede ser uno de varios tipos especificados
def process_value(value: Union[int, str]) -> None:
    if isinstance(value, int):
        print(f"Processing an integer: {value}")
    else:
        print(f"Processing a string: {value}")

process_value(10)
process_value("ten")

# Tipado para colecciones y estructuras de datos

# AbstractSet: conjunto abstracto
def process_set(s: AbstractSet[int]) -> None:
    for item in s:
        print(f"Set item: {item}")

process_set({1, 2, 3})

# ChainMap: lista de mapeos
def process_chainmap(cm: ChainMap[str, int]) -> None:
    for key, value in cm.items():
        print(f"{key}: {value}")

chain_map = ChainMap({'a': 1, 'b': 2}, {'c': 3})
process_chainmap(chain_map)

# Deque: cola doble
def process_deque(d: Deque[int]) -> None:
    d.append(10)
    print(f"Deque after append: {d}")

deque_obj = deque([1, 2, 3])
process_deque(deque_obj)

# Dict: diccionario
def process_dict(d: Dict[str, int]) -> None:
    for key, value in d.items():
        print(f"{key}: {value}")

dict_obj = {'one': 1, 'two': 2}
process_dict(dict_obj)

# FrozenSet: conjunto inmutable
def process_frozenset(fs: FrozenSet[str]) -> None:
    for item in fs:
        print(f"FrozenSet item: {item}")

process_frozenset(frozenset(['a', 'b', 'c']))

# List: lista
def process_list(lst: List[str]) -> None:
    for item in lst:
        print(f"List item: {item}")

process_list(["apple", "banana", "cherry"])

# MutableMapping: mapeo mutable
def process_mutablemapping(mm: MutableMapping[str, int]) -> None:
    mm['key'] = 10
    print(f"MutableMapping after modification: {mm}")

mutable_mapping = {'a': 1, 'b': 2}
process_mutablemapping(mutable_mapping)

# MutableSequence: secuencia mutable
def process_mutablesequence(ms: MutableSequence[int]) -> None:
    ms.append(10)
    print(f"MutableSequence after append: {ms}")

mutable_sequence = [1, 2, 3]
process_mutablesequence(mutable_sequence)

# MutableSet: conjunto mutable
def process_mutableset(ms: MutableSet[str]) -> None:
    ms.add('item')
    print(f"MutableSet after add: {ms}")

mutable_set = set(['a', 'b'])
process_mutableset(mutable_set)

# OrderedDict: diccionario ordenado
def process_ordereddict(od: OrderedDict[str, int]) -> None:
    for key, value in od.items():
        print(f"{key}: {value}")

ordered_dict = OrderedDict([('one', 1), ('two', 2)])
process_ordereddict(ordered_dict)

# Set: conjunto
def process_set(s: Set[str]) -> None:
    s.add('item')
    print(f"Set after add: {s}")

simple_set = {'a', 'b'}
process_set(simple_set)

# Tuple: tupla
def process_tuple(t: Tuple[int, str]) -> None:
    print(f"Tuple content: {t}")

process_tuple((1, "one"))

# Tipos especializados

# Counter: contador para elementos hashables
def count_elements(lst: Counter[str]) -> None:
    print(f"Counter elements: {lst}")

counter = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
count_elements(counter)

# DefaultDict: diccionario con valor por defecto
def process_defaultdict(d: defaultdict[str, int]) -> None:
    d['missing'] += 1
    print(f"DefaultDict after access: {d}")

default_dict = defaultdict(int, {'a': 1, 'b': 2})
process_defaultdict(default_dict)

# NamedTuple: tupla con campos nombrados
class Point(NamedTuple):
    x: int
    y: int

def process_point(p: Point) -> None:
    print(f'Point(x={p.x}, y={p.y})')

point = Point(1, 2)
process_point(point)

# TypedDict: diccionario con tipos especificados para cada clave
class Person(TypedDict):
    name: str
    age: int

def process_person(p: Person) -> None:
    print(f'Name: {p["name"]}, Age: {p["age"]}')

person = Person(name="John", age=30)
process_person(person)

# Tipos de secuencia

# Concatenate: concatenación de tipos en funciones genéricas
T = TypeVar('T')
def concat_args(func: Callable[Concatenate[int, str, T, ...], None]) -> Callable[[int, str, T], None]:
    return func

# Sequence: secuencia inmutable
def process_sequence(seq: Sequence[int]) -> None:
    for item in seq:
        print(f"Sequence item: {item}")

sequence = [1, 2, 3]
process_sequence(sequence)

# MutableSequence: secuencia mutable
def process_mutablesequence(mseq: MutableSequence[int]) -> None:
    mseq.append(10)
    print(f"MutableSequence after append: {mseq}")

mutable_sequence = [1, 2, 3]
process_mutablesequence(mutable_sequence)

# Tipos de mapeo

# Mapping: mapeo inmutable de claves a valores
def process_mapping(map: Mapping[str, int]) -> None:
    for key, value in map.items():
        print(f"{key}: {value}")

mapping = {'a': 1, 'b': 2}
process_mapping(mapping)

# MutableMapping: mapeo mutable de claves a valores
def process_mutablemapping(mmap: MutableMapping[str, int]) -> None:
    mmap['new_key'] = 42
    print(f"MutableMapping after modification: {mmap}")

mutable_mapping = {'a': 1, 'b': 2}
process_mutablemapping(mutable_mapping)

# Tipos de iteradores y generadores

# AsyncGenerator: generador asíncrono
async def async_gen() -> AsyncGenerator[int, None]:
    for i in range(3):
        yield i
        await asyncio.sleep(1)

# AsyncIterable: objeto que puede ser iterado de forma asíncrona
class AsyncIter:
    async def __aiter__(self) -> AsyncIterator[int]:
        for i in range(3):
            yield i
            await asyncio.sleep(1)

async def process_asynciter(ai: AsyncIterable[int]) -> None:
    async for item in ai:
        print(f"AsyncIterable item: {item}")

# AsyncIterator: iterador asíncrono
async def async_iterator() -> AsyncIterator[int]:
    for i in range(3):
        yield i
        await asyncio.sleep(1)

# Generator: generador
def gen() -> Generator[int, None, None]:
    for i in range(3):
        yield i

# Iterator: iterador
def iterator() -> Iterator[int]:
    return iter([1, 2, 3])

# Iterable: objeto que puede ser iterado
def process_iterable(it: Iterable[int]) -> None:
    for item in it:
        print(f"Iterable item: {item}")

process_iterable([1, 2, 3])

# Protocolos y ABCs

# Protocol: definición de un protocolo
class Printable(Protocol):
    def __str__(self) -> str:
        ...

def print_item(item: Printable) -> None:
    print(item)

# Sized: objeto con tamaño definido
def process_sized(s: Sized) -> None:
    print(f"Size of the object: {len(s)}")

process_sized([1, 2, 3])

# Reversible: objeto que puede ser revertido
def process_reversible(r: Reversible[int]) -> None:
    for item in reversed(r):
        print(f"Reversed item: {item}")

process_reversible([1, 2, 3])

# Tipos de funciones y métodos

# Callable: cualquier tipo de función o método
def process_function(func: Callable[[int, str], None]) -> None:
    func(42, "hello")

def greet(name: str) -> None:
    print(f"Hello, {name}")

process_function(lambda x, y: print(f"Int: {x}, Str: {y}"))
process_function(greet)

# AnyCallable: cualquier tipo de función o método
def process_any_callable(func: Callable) -> None:
    func()

def example_callable():
    print("AnyCallable function")

process_any_callable(example_callable)

# Otros tipos y utilidades

# ContextManager: administrador de contexto
def process_contextmanager(cm: ContextManager[str]) -> None:
    with cm as file:
        print(file)

# IO: flujo de entrada/salida
def process_io(stream: IO[str]) -> None:
    print(stream.read())

# Match: objeto de coincidencia de patrones
def process_match(match: Match[str]) -> None:
    print(match.group(0))

# Pattern: objeto de patrón compilado
import re
def process_pattern(pattern: Pattern[str], text: str) -> None:
    match = pattern.match(text)
    if match:
        print("Match found:", match.group())
    else:
        print("No match")

pattern = re.compile(r'\d+')
process_pattern(pattern, "123abc")

# Text: cadena de texto
def process_text(text: Text) -> None:
    print(text)

process_text("Some text")

# Type: tipo
def process_type(t: Type[str]) -> None:
    print(t)

process_type(str)

# TypeVar: variable de tipo
T = TypeVar('T', int, float)
def process_typevar(t: T) -> None:
    print(t)

process_typevar(10)
process_typevar(3.14)

# GenericAlias: alias de tipo genérico
def process_generic_alias(ga) -> None:
    print(ga)

process_generic_alias(List[int])

# Funciones y utilidades

# cast: conversión de tipo
value = cast(str, 42)
print(f"Casted value: {value}")

# get_args: obtención de los argumentos de tipo de un tipo genérico
args = get_args(List[int])
print(f"Arguments of List[int]: {args}")

# get_origin: obtención del tipo original de un tipo genérico
origin = get_origin(List[int])
print(f"Origin of List[int]: {origin}")

# is_typeddict: verificación si un objeto es una instancia de TypedDict
class Person(TypedDict):
    name: str
    age: int

person_dict = {'name': 'John', 'age': 30}
print(f"Is 'person_dict' a TypedDict? {'Person' in globals() and isinstance(person_dict, TypedDict)}")

# reveal_type: muestra el tipo estático de una expresión
# reveal_type(42)  # Uncomment this line to see the type during static type checking
# reveal_type("hello")  # Uncomment this line to see the type during static type checking

# Decoradores y herramientas de comprobación de tipos

# final: marca una clase o método como final
@final
class Base:
    pass

# no_type_check: desactiva la comprobación de tipos para una función o un módulo
@no_type_check
def my_function() -> None:
    pass

# no_type_check_decorator: desactiva la comprobación de tipos para una función decorada
@no_type_check_decorator
def my_function2() -> None:
    pass

# overload: sobrecarga una función o método
@overload
def process(value: int) -> None:
    ...

@overload
def process(value: str) -> None:
    ...

def process(value: Union[int, str]) -> None:
    print(f"Processing value: {value}")

process(10)
process("ten")

# runtime_checkable: marca un protocolo como compatible con la comprobación de tipos en tiempo de ejecución
@runtime_checkable
class Printable(Protocol):
    def __str__(self) -> str:
        ...

def print_item(item: Printable) -> None:
    print(item)

class MyClass:
    def __str__(self) -> str:
        return "MyClass instance"

print_item(MyClass())
