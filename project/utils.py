import numpy as np
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