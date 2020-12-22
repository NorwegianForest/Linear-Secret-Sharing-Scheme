import copy


class BinaryAccessTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.vector = []

    def vector_pad_to(self, counter):
        for i in range(counter - len(self.vector)):
            self.vector.append(0)

    def copy(self):
        return copy.deepcopy(self)

    @staticmethod
    def get_examples():
        boolean_formulas = []
        example_trees = []
        boolean_formulas.append('(A or B)')  # 0
        example_trees.append(BinaryAccessTree('or', BinaryAccessTree('A'), BinaryAccessTree('B')))
        boolean_formulas.append('(A and B)')  # 1
        example_trees.append(BinaryAccessTree('and', BinaryAccessTree('A'), BinaryAccessTree('B')))
        boolean_formulas.append('(B or C)')  # 2
        example_trees.append(BinaryAccessTree('or', BinaryAccessTree('B'), BinaryAccessTree('C')))
        boolean_formulas.append('(B and C)')  # 3
        example_trees.append(BinaryAccessTree('and', BinaryAccessTree('B'), BinaryAccessTree('C')))
        boolean_formulas.append('((A or B) or C)')  # 4
        example_trees.append(BinaryAccessTree('or', example_trees[0].copy(), BinaryAccessTree('C')))
        boolean_formulas.append('((A and B) and C)')  # 5
        example_trees.append(BinaryAccessTree('and', example_trees[1].copy(), BinaryAccessTree('C')))
        boolean_formulas.append('(A or (B or C))')  # 6
        example_trees.append(BinaryAccessTree('or', BinaryAccessTree('A'), example_trees[2].copy()))
        boolean_formulas.append('(A and (B and C))')  # 7
        example_trees.append(BinaryAccessTree('and', BinaryAccessTree('A'), example_trees[3].copy()))
        boolean_formulas.append('((A or B) and C)')  # 8
        example_trees.append(BinaryAccessTree('and', example_trees[0].copy(), BinaryAccessTree('C')))
        boolean_formulas.append('(A or (B and C))')  # 9
        example_trees.append(BinaryAccessTree('or', BinaryAccessTree('A'), example_trees[3].copy()))
        boolean_formulas.append('(C or D)')  # 10
        example_trees.append(BinaryAccessTree('or', BinaryAccessTree('C'), BinaryAccessTree('D')))
        boolean_formulas.append('(C and D)')  # 11
        example_trees.append(BinaryAccessTree('and', BinaryAccessTree('C'), BinaryAccessTree('D')))
        boolean_formulas.append('((A and B) or (C and D))')  # 12
        example_trees.append(BinaryAccessTree('or', example_trees[1].copy(), example_trees[11].copy()))
        boolean_formulas.append('((A or B) and (C or D))')  # 13
        example_trees.append(BinaryAccessTree('and', example_trees[0].copy(), example_trees[10].copy()))
        boolean_formulas.append('(((A and B) or (C and D)) or ((A or B) and (C or D)))')  # 14
        example_trees.append(BinaryAccessTree('or', example_trees[12].copy(), example_trees[13].copy()))
        boolean_formulas.append('(E and (((A and B) or (C and D)) or ((A or B) and (C or D))))')  # 15
        example_trees.append(BinaryAccessTree('and', BinaryAccessTree('E'), example_trees[14].copy()))
        return example_trees, boolean_formulas
