from .data import TensorNetwork


def generate_sequential_path(pg: TensorNetwork):
    path = [(0, 1)]
    n = len(pg.tensor_list) - 2
    while n > 0:
        path.append((0, n))
        n -= 1
    return path
