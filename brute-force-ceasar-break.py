import itertools

generator=itertools.combinations_with_replacement('abcdefghijklmnop',16)

for password in generator:
    ''.join(password)
    print(password)