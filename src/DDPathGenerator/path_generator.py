from .naive_path_generator import generate_sequential_path
from .literal import PATH_SEQUENTIAL
from qiskit import QuantumCircuit


class QiskitPathGenerator:
    def __init__(self, qc: QuantumCircuit):
        self.qc = qc

    def generate_path(self, selected_path: str):
        path = None
        if selected_path == PATH_SEQUENTIAL:
            path = generate_sequential_path(self.qc)
        return path



