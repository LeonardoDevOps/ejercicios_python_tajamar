
"""
    Función que valida si una contraseña cumple con los siguientes requisitos:
    - Al menos 12 caracteres de tamaño.
    - Al menos 1 letra mayúscula.
    - Al menos 1 letra minúscula.
    - Al menos 1 número.
    - Al menos 1 carácter especial.
"""

import re

def validar_contraseña(contraseña):

    condicion = []
    
    # Verificar longitud mínima
    if len(contraseña) < 12:
        condicion.append("Debe tener al menos 12 caracteres.")
    
    # Verificar al menos una mayúscula
    if not re.search(r'[A-Z]', contraseña):
        condicion.append("Debe tener al menos una letra mayúscula.")
    
    # Verificar al menos una minúscula
    if not re.search(r'[a-z]', contraseña):
        condicion.append("Debe tener al menos una letra minúscula.")
    
    # Verificar al menos un número
    if not re.search(r'[0-9]', contraseña):
        condicion.append("Debe tener al menos un número.")
    
    # Verificar al menos un carácter especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        condicion.append("Debe tener al menos un carácter especial.")
    
    if condicion:
        return False, condicion
    else:
        return True, "La contraseña es válida."

# Ejemplo de uso
contraseñas = [
    "Passw0rd!",
    "Password123!",
    "P@ssw0rd123456",
    "password123",
    "PASSWORD123!",
    "P@ssword"
]

for contraseña in contraseñas:
    es_valida, resultado = validar_contraseña(contraseña)
    if es_valida:
        print(f"Contraseña: {contraseña}\nResultado: {resultado}\n")
    else:
        print(f"Contraseña: {contraseña}\nLa contraseña no cumple:")
        for error in resultado:
            print(f"- {error}")
        print()