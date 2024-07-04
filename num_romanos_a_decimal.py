import re

def romano_a_decimal(romano):
    
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    

    total = 0
    valor_anterior = 0
    
    for caracter in reversed(romano):
        valor_actual = valores[caracter]
        
        if valor_actual < valor_anterior:
            total -= valor_actual
        else:
            total += valor_actual
        
        valor_anterior = valor_actual
    
    return total

def es_romano_valido(romano):
    
    caracteres_validos = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    if not all(caracter in caracteres_validos for caracter in romano):
        return False
    
    if re.search(r'IIII|XXXX|CCCC|MMMM|VV|LL|DD', romano):
        return False
    
    if re.search(r'IL|IC|ID|IM|VX|VL|VC|VD|VM|XD|XM|LC|LD|LM|DM', romano):
        return False
    
    return True

# Ejemplo de uso
numeros_romanos = [
    "III",     # 3
    "IV",      # 4
    "IX",      # 9
    "LVIII",   # 58
    "MCMXCIV", # 1994  
    "IIII",    # Numero Romano erroneo no existe
    "IC",      # Numero Romano erroneo no existe
    "IIIIIIII",# Numero Romano erroneo no existe
    "XXX",     # 30
    "xxx"      # Numero Romano erroneo no existe
    
]

for romano in numeros_romanos:
    if es_romano_valido(romano):
        decimal = romano_a_decimal(romano)
        print(f"{romano} su conversión a decimal es {decimal}")
    else:
        print(f"{romano} no es un número romano válido.")