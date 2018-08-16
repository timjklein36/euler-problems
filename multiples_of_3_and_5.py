# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def main():
    print('Sum of multiples of 3 or 5 below 1000: {}'.format(
        sum([i for i in range(1, 1000) if not (i % 3 and i % 5)])
    ))


if __name__ == '__main__':
    main()
