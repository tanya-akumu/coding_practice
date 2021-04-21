import unittest
from Eventual_safe_State import Solution

S = Solution()

class MyTestCase(unittest.TestCase):
    def test_empty_graph(self):
        graph = []
        safe_node = S.eventual_safe_nodes(graph)
        self.assertEqual(safe_node, [])

    def test_example_1(self):
        graph = [[1,2],[2,3],[5],[],[]]
        safe_node = S.eventual_safe_nodes(graph)
        self.assertEqual(safe_node, [2,4,5,6])


if __name__ == '__main__':
    unittest.main()
