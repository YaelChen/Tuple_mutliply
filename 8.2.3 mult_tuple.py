def mult_tuple(tuple1, tuple2):
    """
    the function makes a tuple of all the possible pairs of numbers from the given tuples.
    :param tuple1: a given tuple.
    :param tuple2: a given tuple.
    :type tuple1: tuple
    :type tuple2: tuple
    :return tuples_tuple: tuple of all the possible pairs of numbers from the given tuples.
    :rtype tuples_tuple: tuple
    """
    tuples_list = []
    for first in tuple1:
        for second in tuple2:
            tuples_list.append((first, second))
            tuples_list.append((second, first))
    tuples_tuple = tuple(tuples_list)
    return tuples_tuple


print(mult_tuple((1, 2, 3), (4, 5, 6)))
