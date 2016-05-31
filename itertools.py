import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

l = list(itertools.chain(letters, booleans, numbers, decimals))
print l

print list(itertools.compress(letters, booleans))

# returns for which it is true
