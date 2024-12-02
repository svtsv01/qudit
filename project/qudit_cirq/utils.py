import numpy as np
import cirq
# function to format the output

def format_out(matrix, output_type='float'):

    def format_element(elem):
        if np.isclose(elem.imag, 0):
            real_part = elem.real
            if output_type == 'float':
                return f"{real_part:.1f}"
            elif output_type == 'int':
                return f"{int(round(real_part))}"
            elif output_type == 'str':
                return str(real_part)
        return str(elem)

    if matrix.ndim == 1:
        matrix = matrix[np.newaxis, :]

    formatted_matrix = np.array([[format_element(elem) for elem in row] for row in matrix])
    return formatted_matrix

def printVector(final_state, dimensions, qudits=None, threshold=1e-6):

    if isinstance(dimensions, int):
        dimensions = [dimensions] * int(np.log(len(final_state)) / np.log(dimensions))
    elif isinstance(dimensions, list):
        if np.prod(dimensions) != len(final_state):
            raise ValueError("Product of dimensions does not match the length of the final state vector.")
    else:
        raise ValueError("Dimensions must be an integer or a list of integers.")

    n_qudits = len(dimensions)

    if qudits is not None:
        qudit_names = [str(q) for q in qudits]
    else:
        qudit_names = [f"q{i}" for i in range(n_qudits)]

    print("\nFinal state vector:")
    for idx, amplitude in enumerate(final_state):
        if abs(amplitude) > threshold:
            n = idx
            digits = []
            for dim in reversed(dimensions):
                digits.insert(0, str(n % dim))
                n = n // dim
            state = '|' + ''.join(digits) + '⟩'
            print(f"{state}: {amplitude}")

def tensor_product(*arrays):

    if not arrays:
        raise ValueError("At least one array must be provided.")

    result = arrays[0]
    for array in arrays[1:]:
        result = np.kron(result, array)
    return result
