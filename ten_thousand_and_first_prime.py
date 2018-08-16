# Problem 7:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

from prime import nth_prime


def main():
    print('10,001st prime number: {}'.format(nth_prime(10001)))


if __name__ == '__main__':
    main()
