x = input("")


def list(x):
    if x == 0:
        return []
    else:
        return [x] + list(x-1)
