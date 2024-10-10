"""List addition program."""


def main():
    """"""
    print(add_memberwise([1, 2, 3], [4, 5, 6]))
    print(add_memberwise([1, 2, 3], [1, 2, 3, 4]))


def add_memberwise(first, second):
    """Returns element by element sum of two lists."""
    lists = [first, second]
    maximum_length = max(len(first), len(second))
    result = [0 for i in range(maximum_length)]
    for item in lists:
        for i in range(maximum_length):
            try:
                result[i] += item[i]
            except IndexError:
                pass

    return result


main()
