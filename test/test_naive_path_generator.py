from DDPathGenerator.naive_path_generator import generate_sequential_path_shifted
import pytest

TEST_PATH_SEQUENTIAL_SHIFTED = "SEQ_SHIFTED"


pytestmark = pytest.mark.parametrize("pos_tensor_list,shift_end,expected_paths",
                                     [
                                         (   # Equivalent of having a 4 gate circuit and simulate them in open - open
                                             [0, 1, 2, 3],
                                             0,
                                             {
                                                 TEST_PATH_SEQUENTIAL_SHIFTED: [(0, 1), (0, 2), (0, 1)]
                                             }
                                         ),
                                         (   # Equivalent of having a 4 gate circuit and simulate them in open - close
                                             [0, 1, 2, 3],
                                             1,
                                             {
                                                 TEST_PATH_SEQUENTIAL_SHIFTED: [(0, 1), (0, 3), (0, 2)]
                                             }
                                         ),
                                         (   # Equivalent of having a 4 gate circuit and simulate them in close - open
                                             [1, 2, 3, 4],
                                             0,
                                             {
                                                 TEST_PATH_SEQUENTIAL_SHIFTED: [(1, 2), (1, 3), (1, 2)]
                                             }
                                         ),
                                         (   # Equivalent of having a 4 gate circuit and simulate them in close - close
                                             [1, 2, 3, 4],
                                             1,
                                             {
                                                 TEST_PATH_SEQUENTIAL_SHIFTED: [(1, 2), (1, 4), (1, 3)]
                                             }
                                         )
                                     ])


class TestNaivePathGenerator:
    def test_sequential_path_shifted(self, pos_tensor_list, shift_end, expected_paths):
        path = generate_sequential_path_shifted(pos_tensor_list, shift_end)
        assert path, expected_paths[TEST_PATH_SEQUENTIAL_SHIFTED]

