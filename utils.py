import time
from functools import wraps


def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f'Temps écoulé: {te - ts} pour l\'execution de: {method.__name__}')
        return result

    return timed
