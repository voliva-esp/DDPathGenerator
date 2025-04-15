from DDPathGenerator import QiskitPathGenerator, PATH_SEQUENTIAL

from qiskit import QuantumCircuit
import pytest


pytestmark = pytest.mark.parametrize("file_name,expected_paths",
                                     [
                                         ("small_2_2g", {
                                             PATH_SEQUENTIAL: [(0, 1)],
                                         })
                                     ])


class ITest:
    def generate_path_file(self, file_name):
        return f"./test/circuits/{file_name}.qasm"

    def assert_path(self, file_name, expected_paths, path_name):
        file_path = self.generate_path_file(file_name)
        qc = QuantumCircuit.from_qasm_file(file_path)
        pg = QiskitPathGenerator(qc)
        path = pg.generate_path(path_name)
        assert path, expected_paths[path_name]


class TestPathGenerator(ITest):
    def test_sequential_path(self, file_name, expected_paths):
        self.assert_path(file_name, expected_paths, PATH_SEQUENTIAL)
