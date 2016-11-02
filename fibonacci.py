def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    #n > 2
    a = 1
    b = 1
    #First two members of the series
    series = [a, b]
    for each_item in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c

    return series

if __name__ == '__main__':
    print(fibo(2))
