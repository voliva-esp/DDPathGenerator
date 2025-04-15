from src.DDPathGenerator import QiskitPathGenerator, PATH_SEQUENTIAL

PATH = "test/circuit/"

if __name__ == '__main__':
    tensor_list = [('x0',), ('x1',), ('x2',), ('x0', 'y0', 'x1', 'x1_1'), ('x2', 'y2', 'x1_1', 'y1'),
                   ('y0',), ('y1',), ('y2',)]
    open_indices = []
    pg = QiskitPathGenerator(tensor_list, open_indices)
    path = pg.generate_path(PATH_SEQUENTIAL)
    print(path)


