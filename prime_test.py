from unittest import main, TestCase
from prime import is_prime, primes, nth_prime
from util import suffix


class PrimeTest(TestCase):
    def test_is_prime(self):
        prime_nums = [5, 7, 11, 13, 17, 29]
        not_primes = [4, 6, 8, 10, 25, 50, 75, 102]

        for n in prime_nums:
            self.assertTrue(is_prime(n), '{} is not prime'.format(n))

        for n in not_primes:
            self.assertFalse(is_prime(n), '{} is actually prime'.format(n))

    def test_primes(self):
        n = 20
        prime_nums = primes(n)

        self.assertTrue(11 in prime_nums)
        self.assertFalse(12 in prime_nums)

    def test_nth_prime(self):
        n = 10

        self.assertEqual(
            nth_prime(n),
            29,
            '{} is not the {}{} prime'.format(
                29, n, suffix(n)
            )
        )


if __name__ == '__main__':
    main()
