# Funciones recursivas

# function():
    # if condition:
        # function()
        
def cuenta_atras(num: int):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else: print("[!] Final")
    print(f"Orden de liberación {num}")
    
cuenta_atras(5)

# Función calculo de fibonacci hasta un número menor o igual al input
def fibonacci_hasta(n: int, fibo=[0,1]) -> list:
    # Expresión
    fibo.append(fibo[-1] + fibo[-2])
    
    # Comprobación
    if n > fibo[-1]: fibonacci_hasta(n, fibo) # Llamada recursiva
    else: print(fibo[:-1])

fibonacci_hasta(10)

def factorial(num: int) -> int:
    if num == 0: return 1
    # Verificación
    if num > 1: num = num * factorial(num - 1)
    return num 

print(factorial(6))