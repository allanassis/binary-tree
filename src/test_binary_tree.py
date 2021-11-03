from unittest import TestCase
import unittest

from binary_tree import BinaryTree, BinaryTreeNode


class TestBinaryTree(TestCase):
    def setUp(self):
        self.root_value = "42"
        self.some_value = "Gomu Gomu No!"

    def test_instance(self):
        # arrange/act
        tree = BinaryTree()
        # assert
        self.assertIsInstance(tree, BinaryTree)

    def test_insert_root(self):
        # arrange
        tree = BinaryTree()
        # act
        tree.insert(self.root_value)
        # assert
        self.assertIsInstance(tree.root, BinaryTreeNode)
        self.assertEqual(tree.root.value, self.root_value)

    def test_insert_first_root_child_in_level_order(self):
        # arrange
        tree = BinaryTree()
        tree.insert(self.root_value)
        # act
        tree.insert(self.some_value)
        # assert
        self.assertIsInstance(tree.root.left, BinaryTreeNode)
        self.assertEqual(tree.root.left.value, self.some_value)

    def test_get_level_order_list(self):
        # arrange
        tree = BinaryTree()
        tree.insert(self.root_value)
        tree.insert(self.some_value)
        tree.insert(f"{self.some_value}-2")
        tree.insert(f"{self.some_value}-3")
        tree.insert(f"{self.some_value}-4")
        tree.insert(f"{self.some_value}-5")
        expected = [
            self.root_value,
            self.some_value,
            f"{self.some_value}-2",
            f"{self.some_value}-3",
            f"{self.some_value}-4",
            f"{self.some_value}-5",
        ]
        # act
        level_ordered_list = tree.get_level_order_list()
        # assert
        self.assertListEqual(level_ordered_list, expected)

    def test_find(self):
        # arrange
        tree = BinaryTree()
        tree.insert(self.root_value)
        tree.insert(self.some_value)
        # act
        node = tree.find(self.some_value)
        # assert
        self.assertIsInstance(node, BinaryTreeNode)
        self.assertEqual(node.value, self.some_value)

    def test_find(self):
        # arrange
        tree = BinaryTree()
        tree.insert(self.root_value)
        tree.insert(self.some_value)
        # act
        node = tree.find(self.some_value)
        # assert
        self.assertIsInstance(node, BinaryTreeNode)
        self.assertEqual(node.value, self.some_value)

    def test_delete(self):
        # arrange
        tree = BinaryTree()
        tree.insert(self.root_value)
        tree.insert(self.some_value)
        tree.insert(f"{self.some_value}-2")
        tree.insert(f"{self.some_value}-3")
        tree.insert(f"{self.some_value}-4")
        tree.insert(f"{self.some_value}-5")

        expected = [
            self.root_value,
            self.some_value,
            f"{self.some_value}-2",
            f"{self.some_value}-4",
            f"{self.some_value}-5"
        ]

        # act
        tree.delete(f"{self.some_value}-3")

        # arrange
        self.assertListEqual(tree.get_level_order_list(), expected)
if __name__ == "__main__":
    unittest.main()
