import unittest
#Please put the file being tested in the same directory
import LowestCommonAncestor
from LowestCommonAncestor import Node

class TestLowestCommonAncestor(unittest.TestCase):



    def test_LCA(self):

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        answer = LowestCommonAncestor.LCA(root, 2, 7)
        self.assertEqual(answer, 1)
        answer = LowestCommonAncestor.LCA(root, 2, 5)
        self.assertEqual(answer, 2)
        answer = LowestCommonAncestor.LCA(root, 4, 6)
        self.assertEqual(answer, 1)
        answer = LowestCommonAncestor.LCA(root, 6, 7)
        self.assertEqual(answer, 3)
        answer = LowestCommonAncestor.LCA(root, 4, 5)
        self.assertEqual(answer, 2)
        answer = LowestCommonAncestor.LCA(root, 5, 6)
        self.assertEqual(answer, 1)