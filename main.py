import random

from decorator.convert_to_number import convert_to_numeric
from decorator.retry import retry


@convert_to_numeric
def first_func(x):
    return x ** 2


@convert_to_numeric
def second_func(x):
    return x - 2


print(first_func('2'))

print(second_func('4'))


# retry
@retry(Exception, total_tries=4)
def test_func(*args, **kwargs):
    rnd = random.random()
    if rnd < .2:
        raise ConnectionAbortedError('Connection was aborted :(')
    elif rnd < .4:
        raise ConnectionRefusedError('Connection was refused :/')
    elif rnd < .8:
        raise ConnectionResetError('Guess the connection was reset')
    else:
        return 'Yay!!'


print(test_func('hi', 'bye', hi='ciao'))
