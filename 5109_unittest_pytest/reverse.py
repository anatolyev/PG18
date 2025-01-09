
def reverse(s):
    if type(s) != str:
        raise TypeError(f'Нужно было получить str, а получено {type(s)}')
    return s[::-1]
    # return "asdf"

