#!/usr/bin/python3


def evens(n):
    return list(filter(lambda n: n % 2 == 0, range(n + 1)))
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
