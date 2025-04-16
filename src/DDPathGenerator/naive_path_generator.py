import math

from .data import TensorNetwork


def generate_sequential_path_shifted(pos_tensor_list: list, shift_end=0):
    """
        Generalization for calculating the contraction path using the sequential heuristic. Can calculate the
        path for a given list of tensors of the tensor network, without the need of including all of them.
        Input:
        :param pos_tensor_list: Int list containing the position of all the tensors to contract
        :param shift_end: Number of tensor to be ignored that are at the right of the pos_tensor_list tensors
        Output:
        :return: The generated path for the pos_tensor_list tensors
    """
    if len(pos_tensor_list) < 2:
        return []
    shift_ini = min(pos_tensor_list)
    pos_tensor_list.remove(shift_ini)
    path = [(shift_ini, pos_tensor_list[0])]
    pos_tensor_list.remove(pos_tensor_list[0])
    for i in range(len(pos_tensor_list)):
        pos_tensor = pos_tensor_list[i]
        path.append((pos_tensor - i - 2, shift_ini + shift_end + len(pos_tensor_list) - i))
    return path


def generate_sequential_path(pg: TensorNetwork):
    """
    Calculates the path for a given TensorNetwork using the sequential heuristic
    :param pg: Object of the TensorNetwork containing all the relevant information of the circuit to contract
    :return: The generated path for the given TensorNetwork using the sequential path
    """
    return generate_sequential_path_shifted(list(range(len(pg.tensor_list))))


def generate_k_ops_path(pg: TensorNetwork, k=4):
    """
    Calculates the path for a given TensorNetwork using the K-Ops heuristic
    :param pg: Object of the TensorNetwork containing all the relevant information of the circuit to contract
    :param k: int value that set the number of contractions per operation block
    :return: The generated path for the given TensorNetwork using the sequential path
    """
    n = len(pg.tensor_list)
    shift_ini = 0
    while len(pg.tensor_list[shift_ini]) == 1:
        shift_ini += 1
    shift_end = 0
    while len(pg.tensor_list[n - shift_end - 1]) == 1:
        shift_end += 1
    n_gates = n - shift_ini - shift_end
    n_block = math.ceil((n_gates / k))
    path = []
    pos_tensors = [shift_ini + i for i in range(k)]
    for i in range(n_block):
        n_remain_gates = n_gates - k * i
        n_gates_interval = min(n_remain_gates, k)
        block_shift_end = shift_end + (n_remain_gates - n_gates_interval)
        path = path + generate_sequential_path_shifted(pos_tensors[0:n_gates_interval], block_shift_end + i)
    end_interval_first_pos = shift_ini
    end_interval = [end_interval_first_pos + i for i in range(shift_end)]
    path = path + generate_sequential_path_shifted(end_interval, n_block)
    final_interval = [i for i in range(shift_ini + n_block + (1 if shift_end != 0 else 0))]
    path = path + generate_sequential_path_shifted(final_interval, 0)
    return path



