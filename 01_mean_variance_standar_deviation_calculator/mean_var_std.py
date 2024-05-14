import numpy as np


def calculate(numbers):

    # Verificar si la lista contiene exactamente 9 elementos
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Crear una matriz 3x3 a partir de la lista de entrada
    matrix = np.array(numbers).reshape(3, 3)

    # Calcular las estadísticas requeridas
    mean = [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()]
    variance = [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()]
    std_deviation = [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()]
    max_value = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()]
    min_value = [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()]
    sum_value = [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]

    # Crear el diccionario de resultados
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_deviation,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }

    return calculations