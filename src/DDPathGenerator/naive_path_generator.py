from qiskit import QuantumCircuit


def generate_sequential_path(qc: QuantumCircuit):
    path = [(0, 1)]
    n = qc.size() - 2
    while n > 0:
        path.append((0, n))
        n -= 1
    return path
