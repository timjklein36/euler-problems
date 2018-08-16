

def main():
    print('Sum of multiples of 3 or 5 below 1000: {}'.format(
        sum([i for i in range(1, 1000) if not (i % 3 and i % 5)])
    ))


if __name__ == '__main__':
    main()
