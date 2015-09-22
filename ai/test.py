from unittest import TestCase
from ai.minimax import MinNode, MaxNode, INF, minimax

# Test tree extracted from this minimax video -> https://www.youtube.com/watch?v=J1GoI5WHBto
TEST_TREE = (
    None, (
        (
            None, (
                (
                    None, (
                        (
                            None, (
                                (10, []),
                                (11, []),
                            ),
                        ),
                        (
                            None, (
                                (9, []),
                                (12, []),
                            ),
                        ),
                    ),
                ),
                (
                    None, (
                        (
                            None, (
                                (14, []),
                                (15, []),
                            ),
                        ),
                        (
                            None, (
                                (13, []),
                                (14, []),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        (
            None, (
                (
                    None, (
                        (
                            None, (
                                (5, []),
                                (2, []),
                            ),
                        ),
                        (
                            None, (
                                (4, []),
                                (1, []),
                            ),
                        ),
                    ),
                ),
                (
                    None, (
                        (
                            None, (
                                (3, []),
                                (22, []),
                            ),
                        ),
                        (
                            None, (
                                (20, []),
                                (21, []),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
)


class MinimaxNodeTestMixin(object):
    child1_value = 3
    child2_value = 22
    small_child_value = child1_value
    big_child_value = child2_value
    test_tuple = None, (
        (child1_value, ()),
        (child2_value, ()),
    )


class MaxNodeTest(TestCase, MinimaxNodeTestMixin):
    def test_creates_min_nodes_from_tuple(self):
        result = MaxNode.from_tuple(self.test_tuple)
        self.assertEqual(-INF, result.value)
        child1, child2 = result.children
        self.assertIsInstance(child1, MinNode)
        self.assertEqual(self.child1_value, child1.value)
        self.assertIsInstance(child2, MinNode)
        self.assertEqual(self.child2_value, child2.value)

    def test_max_node_returns_big_child_when_visited(self):
        node = MaxNode.from_tuple(self.test_tuple)
        self.assertEqual(self.big_child_value, node.visit())


class MinNodeTest(TestCase, MinimaxNodeTestMixin):
    def test_creates_max_nodes_from_tuple(self):
        result = MinNode.from_tuple(self.test_tuple)
        self.assertEqual(INF, result.value)
        child1, child2 = result.children
        self.assertIsInstance(child1, MaxNode)
        self.assertEqual(self.child1_value, child1.value)
        self.assertIsInstance(child2, MaxNode)
        self.assertEqual(self.child2_value, child2.value)

    def test_min_node_returns_child_when_visited(self):
        node = MinNode.from_tuple(self.test_tuple)
        self.assertEqual(self.small_child_value, node.visit())


class MinimaxTest(TestCase):
    def check_tree_from_video_is_resolved_correctly(self):
        expected_result = 10
        actual_result = minimax(TEST_TREE)
        self.assertEqual(expected_result, actual_result)
