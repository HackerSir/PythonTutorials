n = int(input('n = '))

for r in range(n * 2 - 1):
    for i in range(abs(r - (n - 1))):
        print(' ', end='')
    for i in range(((n - 1) - abs(r - (n - 1))) * 2 + 1):
        print('*', end='')
    print()

# for r in range(n * 2 - 1):
#     print(' ' * abs(r - (n - 1)), end='')
#     print('*' * (((n - 1) - abs(r - (n - 1))) * 2 + 1), end='')
#     print()
