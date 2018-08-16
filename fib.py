def fib(below=4e6, n=0):
    seq = [1, 2]
    index = 1
    val = 2
    if n == 0:
        while val < below:
            val += seq[index - 1]
            seq.append(val)
            index += 1
        return seq
    elif n > 0:
        while index <= n:
            val += seq[index - 1]
            seq.append(val)
            index += 1
        return seq[n - 1]
    else:
        raise IndexError('n={} is not a valid fibonacci index'.format(n))
