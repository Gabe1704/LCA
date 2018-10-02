import unittest
#Please put the file being tested in the same directory
import LowestCommonAncestor
from LowestCommonAncestor import Node

class TestLowestCommonAncestor(unittest.TestCase):

#                     1
#             2               3
#        4       5         6       7
# look of tree

# testing normal functionality
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

# testing what happens if I just use the same node
    def test_LCASame(self):

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        answer = LowestCommonAncestor.LCA(root, 7, 7)
        self.assertEqual(answer, 7)
        answer = LowestCommonAncestor.LCA(root, 4, 4)
        self.assertEqual(answer, 4)

# testing what happens if I just use the root
    def test_LCARoot(self):

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        answer = LowestCommonAncestor.LCA(root, 1, 1)
        self.assertEqual(answer, 1)

# testing what happens if I just use a tree with only a root
    def test_LCAOnlyRoot(self):

        root = Node(1)

        answer = LowestCommonAncestor.LCA(root, 1, 1)
        self.assertEqual(answer, 1)

# testing to see if my invalid tree failsafe works
    def test_LCANone(self):

        root = None

        answer = LowestCommonAncestor.LCA(root, 7, 7)
        self.assertEqual(answer, -1)

#testing failsafe of findRoute
    def test_findRoute(self):

        root = None
        route = None
        x = None

        answer = LowestCommonAncestor.findRoute(root, route, x)
        self.assertIs(answer, False)
