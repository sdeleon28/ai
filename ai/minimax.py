from abc import abstractmethod, ABCMeta
INF = float('inf')


# noinspection PyPep8Naming
class classproperty(object):
    def __init__(self, getter):
        self.getter = getter

    # noinspection PyUnusedLocal
    def __get__(self, instance_, owner):
        return self.getter(owner)


class MinimaxNode(object, metaclass=ABCMeta):
    other_node_type = None

    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def visit(self):
        for child in self.children:
            result = child.visit()
            self.value = self.min_or_max(result)
        return self.value

    @abstractmethod
    def min_or_max(self, value):
        pass

    @classmethod
    def from_tuple(cls, t):
        value, children = t
        child_nodes = []
        for child in children:
            child_nodes.append(cls.other_node_type.from_tuple(child))
        return cls(value, child_nodes)


# noinspection PyAbstractClass
class MinNode(MinimaxNode):
    @classproperty
    def other_node_type(self):
        return MaxNode

    def __init__(self, value=None, children=None):
        super().__init__(value if value is not None else INF, children)

    def min_or_max(self, value):
        return min(self.value, value)


# noinspection PyAbstractClass
class MaxNode(MinimaxNode):
    @classproperty
    def other_node_type(self):
        return MinNode

    def __init__(self, value=None, children=None):
        super().__init__(value if value is not None else -INF, children)

    def min_or_max(self, value):
        return max(self.value, value)


def minimax(tree):
    tree = MaxNode.from_tuple(tree)
    return tree.visit()
