import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar_productos(precios, umbral, operacion="mayor"):
    """
    Filtra los productos según el umbral y la operación especificada.

    :param precios: Diccionario con los productos y sus precios.
    :param umbral: Valor de referencia para filtrar los productos.
    :param operacion: Operación a realizar, puede ser "mayor" o "menor".
    :return: Lista de productos que cumplen con la condición.
    """
    productos_filtrados = []

    if operacion == "mayor":
        productos_filtrados = [producto for producto, precio in precios.items() if precio > umbral]
    elif operacion == "menor":
        productos_filtrados = [producto for producto, precio in precios.items() if precio < umbral]
    else:
        return "Lo sentimos, no es una operación válida"

    return productos_filtrados

if __name__ == "__main__":
    import sys

    # Definir operacion fuera de las condiciones del if
    operacion = "mayor"

    # Verificar el número de argumentos proporcionados
    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        resultado = filtrar_productos(precios, umbral)
    elif len(sys.argv) == 3 and sys.argv[2] in ["mayor", "menor"]:
        umbral = int(sys.argv[1])
        operacion = sys.argv[2]
        resultado = filtrar_productos(precios, umbral, operacion)
    else:
        resultado = "Lo sentimos, no es una operación válida"

    # Imprimir el resultado
    if isinstance(resultado, list):
        print(f"Los productos {operacion} al umbral son: {', '.join(resultado)}")
    else:
        print(resultado)