from src.DDPathGenerator import QiskitPathGenerator, PATH_SEQUENTIAL
from qiskit import QuantumCircuit

PATH = "test/circuit/"

if __name__ == '__main__':
    file_name = "small_2_5g"
    qc = QuantumCircuit.from_qasm_file(PATH + file_name + ".qasm")
    pg = QiskitPathGenerator(qc)
    path = pg.generate_path(PATH_SEQUENTIAL)
    print(path)

