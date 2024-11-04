# Estableciendo una condición
condition: bool = True

if condition: # Si ...
    print("El flujo del programa pasa por aquí")
else: # De lo contrario ...
    print("Si no se cumpliese, se redirige hacía la estructura else")

# --- Ejemplo de uso del condicional if ---
edad = 17

if edad >= 18:
    print("Puedes entrar.")
else:
    print("No puedes pasar.")    
# ------
    
# --- También existe otra condición que es else if ---
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18:
    print("Puedes pasar.")
elif edad >= 16:
    print("Aún te queda un tiempo para poder pasar.")
else:
    print("¡No puedes pasar!")

# Aplicación de condiciones
ingreso_mensual = 10000
gasto_mensual = 6000

if ingreso_mensual >= 10000:
    if ingreso_mensual - gasto_mensual < 0: # if anidado
        print("estas en negativo")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else:
        print("estas gastando mucho")
    
elif ingreso_mensual >= 7000:
    print("estas bien en paises de buena calidad")
    
elif ingreso_mensual >= 3000:
    print("estas bien en francia")
    
elif ingreso_mensual >= 2000:
    print("estas bien en españa")
    
elif ingreso_mensual >= 1000:
    print("estas bien en latinoamerica")
    
else:
    print("eres pobre")
# ------