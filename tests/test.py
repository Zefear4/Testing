import unittest
from main import find_roots


class TestQuadraticRoots(unittest.TestCase):
    def test_two_roots(self):
        root1, root2 = find_roots(1, -3, 2)
        self.assertAlmostEqual(root1, 1.0)
        self.assertAlmostEqual(root2, 2.0)

    def test_one_root(self):
        root1, root2 = find_roots(1, -2, 1)
        self.assertAlmostEqual(root1, 1.0)
        self.assertAlmostEqual(root2, 1.0)

    def test_no_roots(self):
        root1, root2 = find_roots(1, 1, 1)
        self.assertIsNone(root1)
        self.assertIsNone(root2)

    def test_zero_a(self):
      with self.assertRaises(ZeroDivisionError):
        find_roots(0, 1, 1)

if __name__ == '__main__':
    unittest.main()