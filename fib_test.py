from unittest import main, TestCase
from fib import fib


class FibTest(TestCase):
    def test_below(self):
        self.assertTrue(len(fib(below=4e6)) > 5)

    def test_nth(self):
        self.assertEqual(fib(n=1), 1)
        self.assertEqual(fib(n=5), 8)

    def test_invalid_nth(self):
        with self.assertRaises(IndexError):
            fib(n=-3)


if __name__ == '__main__':
    main()
