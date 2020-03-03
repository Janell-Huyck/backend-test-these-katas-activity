import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(5, 7), 12)
        self.assertEqual(katas.add(5, -5), 0)

    def test_multiply(self):
        self.assertEqual(katas.multiply(6, -2), -12)
        self.assertEqual(katas.multiply(-6, 2), -12)
        self.assertEqual(katas.multiply(6, 2), 12)
        self.assertEqual(katas.multiply(-6, -2), 12)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), 8)

    def test_factorial(self):
        self.assertEqual(katas.factorial(3), 6)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(4), 2)


if __name__ == '__main__':
    unittest.main()
