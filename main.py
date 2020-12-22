from BinaryAccessTree import BinaryAccessTree


def Lewko_Waters_algorithm(root):
    counter = 1
    matrix = []
    rho = []
    root.vector = [1]

    def recursion_func(node):
        nonlocal counter
        nonlocal matrix
        nonlocal rho
        if node.value == 'or':
            node.left.vector = node.vector.copy()
            node.right.vector = node.vector.copy()
        elif node.value == 'and':
            node.left.vector_pad_to(counter)
            node.left.vector.append(-1)
            node.right.vector = node.vector.copy()
            node.right.vector_pad_to(counter)
            node.right.vector.append(1)
            counter += 1
        else:
            matrix.append(node.vector.copy())
            rho.append(node.value)
            return
        recursion_func(node.left)
        recursion_func(node.right)
    recursion_func(root)
    for line in matrix:
        for i in range(counter - len(line)):
            line.append(0)
    return matrix, rho


def run_test():
    example_trees, formulas = BinaryAccessTree.get_examples()
    for i in range(len(example_trees)):
        matrix, rho = Lewko_Waters_algorithm(example_trees[i])
        print('Access formula:', formulas[i])
        print('ρ(i)', 'Matrix')
        for j in range(len(matrix)):
            print(rho[j], '  ', matrix[j])
        print()


run_test()
