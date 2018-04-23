def get_signal_power(matr):
    res = []

    for arr in matr:
        res.append(get_avg_positive_nums(arr) + abs(get_avg_negative_nums(arr)))
        # print(get_avg_positive_nums(arr) + abs(get_avg_negative_nums(arr)))

    return get_avg(res)


def get_avg_positive_nums(arr):
    positives = [x for x in arr if x > 0]
    return get_avg(positives)


def get_avg_negative_nums(arr):
    negatives = [x for x in arr if x < 0]
    return get_avg(negatives)


def get_avg(arr):
    if (len(arr) != 0):
        return sum(arr) / len(arr)
    return 0

if __name__ == '__main__':
    matrix = [[10, -10, 20, -20], 
        [10, -10, 20, -20, 30, -30, 40],
        [10, -10, 20, -20, 30, -30, 40, 50, 60],
        [-10, -20, -30, -40, -50],
        [10, 20, 30]]

    print('power = ', get_signal_power(matrix))
