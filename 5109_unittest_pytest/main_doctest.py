def square_root(x):
    """
    >>> square_root(4)
    2.0
    >>> [square_root(x) for x in range(10)]
    [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0]
    >>> square_root(-1)
    Traceback (most recent call last):
        ...
    ValueError: Argument must be greater than 0
    >>> square_root("yandexlyceum")
    Traceback (most recent call last):
        ...
    TypeError: yandexlyceum is not valid int or float value
    """
    if not isinstance(x, int) and not isinstance(x, float):
        raise TypeError(f"{x} is not valid int or float value")
    if x >= 0:
        return x ** 0.5
    else:
        raise ValueError("Argument must be greater than 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()