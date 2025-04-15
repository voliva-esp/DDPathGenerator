from DDPathGenerator import QiskitPathGenerator, PATH_SEQUENTIAL
import pytest


pytestmark = pytest.mark.parametrize("tensor_list,open_indices,expected_paths",
                                     [
                                         (   # Simple circuit with 2 qubits and 2 cx simulated open - open
                                             (
                                                ('x0', 'y0', 'x1', 'x1_1'),
                                                ('x2', 'y2', 'x1_1', 'y1'),
                                             ),
                                             ('x0', 'x1', 'x2', 'y0', 'y1', 'y2'),
                                             {
                                                PATH_SEQUENTIAL: [(0, 1)],
                                             }
                                         ),
                                         (   # Simple circuit with 2 qubits and 2 cx simulated close - open
                                             (
                                                ('x0',),
                                                ('x1',),
                                                ('x2',),
                                                ('x0', 'y0', 'x1', 'x1_1'),
                                                ('x2', 'y2', 'x1_1', 'y1'),
                                             ),
                                             ('y0', 'y1', 'y2'),
                                             {
                                                PATH_SEQUENTIAL: [(0, 1), (0, 3), (0, 2), (0, 1)],
                                             }
                                         ),
                                         (   # Simple circuit with 2 qubits and 2 cx simulated open - close
                                             (
                                                ('x0', 'y0', 'x1', 'x1_1'),
                                                ('x2', 'y2', 'x1_1', 'y1'),
                                                ('y0',),
                                                ('y1',),
                                                ('y2',),
                                             ),
                                             ('x0', 'x1', 'x2'),
                                             {
                                                PATH_SEQUENTIAL: [(0, 1), (0, 3), (0, 2), (0, 1)],
                                             }
                                         ),
                                         (   # Simple circuit with 2 qubits and 2 cx simulated close - close
                                             (
                                                ('x0',),
                                                ('x1',),
                                                ('x2',),
                                                ('x0', 'y0', 'x1', 'x1_1'),
                                                ('x2', 'y2', 'x1_1', 'y1'),
                                                ('y0',),
                                                ('y1',),
                                                ('y2',),
                                             ),
                                             (),
                                             {
                                                PATH_SEQUENTIAL: [
                                                    (0, 1), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1)
                                                ],
                                             }
                                         )
                                     ])


class ITest:
    def assert_path(self, tensor_list, open_indices, expected_paths, path_name):
        pg = QiskitPathGenerator(tensor_list, open_indices)
        path = pg.generate_path(path_name)
        assert path, expected_paths[path_name]


class TestPathGenerator(ITest):
    def test_sequential_path(self, tensor_list, open_indices, expected_paths):
        self.assert_path(tensor_list, open_indices, expected_paths, PATH_SEQUENTIAL)
