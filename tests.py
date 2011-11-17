import unittest
import collections

import search

class TestBfs(unittest.TestCase):

    def setUp(self):
        self.start = 'A'
        self.stop  = 'C'
        self.tree  = {'A': ['B'],
                     'B': ['A', 'C'],
                     'C': ['B', 'F', 'D', 'E'],
                     'D': ['C', 'E'],
                     'E': ['C', 'D', 'H'],
                     'F': ['C', 'G'],
                     'G': ['F', 'I'],
                     'H': ['E', 'I'],
                     'I': ['G', 'H']}
        self.s     = search.Bfs(self.start, self.stop, self.tree)

    def test_stepTwice(self):
        self.assertFalse(self.s.step(), False)
        self.assertTrue(self.s.step(), True)

    def test_searchTwoSteps(self):
        self.assertEqual(self.s.search(), collections.deque([['A', 'B', 'C']]))

    def test_searchOneStep(self):
        self.s = search.Bfs('A', 'B', self.tree)
        self.assertEqual(self.s.search(), collections.deque([['A', 'B']]))

    def test_searchToEnd(self):
        self.s = search.Bfs('A', 'I', self.tree)
        self.assertEqual(self.s.search(), collections.deque([
            ['A', 'B', 'C', 'F', 'G', 'I'],
            ['A', 'B', 'C', 'E', 'H', 'I'],
            ['A', 'B', 'C', 'D', 'E', 'H', 'I']]))


if __name__ == '__main__':
    unittest.main()
