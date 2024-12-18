from typing import Any, Dict, List, Tuple, Union
import cirq
from qudit_cirq.qudit import qudit_measure 

# Function to create the circuit:

def create_circuit(*args: Any) -> Tuple[cirq.Circuit, Dict[str, cirq.Qid], List[cirq.Qid]]:
    circuit = cirq.Circuit()
    qudits: Dict[str, cirq.Qid] = {}
    qudit_order: List[cirq.Qid] = []
    current_dimension: Union[int, None] = None

    for arg in args:
        if isinstance(arg, int):
            current_dimension = arg
            continue

        if not isinstance(arg, tuple):
            raise ValueError(f"Invalid argument format: {arg}")

        if len(arg) == 3 and isinstance(arg[0], int):
            # Tuple like (dimension, gate_type, qudit_names)
            gate_dimension, gate_type, qudit_names = arg
            current_dimension = gate_dimension
        elif len(arg) == 2:
            # Tuple like (gate_type, qudit_names)
            if current_dimension is None:
                raise ValueError("Dimension must be specified before gate tuples without dimension")
            gate_dimension = current_dimension
            gate_type, qudit_names = arg
        else:
            raise ValueError(f"Invalid tuple format: {arg}")

        # Ensure qudit_names is a list
        if isinstance(qudit_names, str):
            qudit_names = [qudit_names]
        elif not isinstance(qudit_names, list):
            raise ValueError(f"qudit_names must be a string or a list of strings, got {type(qudit_names)}")

        # Ensure the qudits are initialised and validate dimensions
        qudit_objects = []
        for name in qudit_names:
            if name not in qudits:
                qudit = cirq.NamedQid(name, dimension=gate_dimension)
                qudits[name] = qudit
                qudit_order.append(qudit)
            else:
                qudit = qudits[name]
                if qudit.dimension != gate_dimension:
                    raise ValueError(f"Qudit '{name}' was previously defined with dimension {qudit.dimension}, "
                                     f"but now is used with dimension {gate_dimension}")
            qudit_objects.append(qudit)

        # Handle measurements separately
        if gate_type == qudit_measure:
            if len(qudit_objects) != 1:
                raise ValueError("qudit_measure can only measure one qudit at a time.")
            qudit_name = qudit_names[0]
            unique_key = f"m_{qudit_name}"
            measurement_operation = qudit_measure(qudit_objects[0], key=unique_key)
            circuit.append(measurement_operation)
        else:
            if not isinstance(gate_type, type) or not issubclass(gate_type, cirq.Gate):
                raise ValueError(f"Invalid gate type: {gate_type}. Must be a subclass of cirq.Gate.")
            gate = gate_type(gate_dimension)
            circuit.append(gate.on(*qudit_objects))

    return circuit, qudits, qudit_order
