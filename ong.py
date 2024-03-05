def calcular_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calcular_productoria(lista):
    result = 1
    for elemento in lista:
        result *= elemento
    return result

def calcular(**kwargs):
    for key, value in kwargs.items():
        if 'fact' in key:
            resultado = calcular_factorial(value)
            print(f"El factorial de {value} es {resultado}")
        elif 'prod' in key:
            resultado = calcular_productoria(value)
            print(f"La productoria de {value} es {resultado}")

if __name__ == "__main__":
    calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6)