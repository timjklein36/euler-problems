from fib import fib


def main():

    print('Sum of even-valued Fibonacci numbers: {}'.format(
        sum([i for i in fib() if not i % 2])
    ))


if __name__ == '__main__':
    main()
