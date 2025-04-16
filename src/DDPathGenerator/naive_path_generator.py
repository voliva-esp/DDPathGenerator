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
    path = []
    for i in range(len(pos_tensor_list)):
        pos_tensor = pos_tensor_list[i]
        path.append((pos_tensor - i - 1, shift_ini + shift_end + len(pos_tensor_list) - i))
    return path


def generate_sequential_path(pg: TensorNetwork):
    """
    Calculates the path for a given TensorNetwork using the sequential heuristic
    :param pg: Object of the TensorNetwork containing all the relevant information of the circuit to contract
    :return: The generated path for the given TensorNetwork using the sequential path
    """
    return generate_sequential_path_shifted(list(range(len(pg.tensor_list))))
