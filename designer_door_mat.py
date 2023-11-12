n, m = 7, 21

for i in range(0, int(n / 2)):
    print( ('.|.' * (2*i + 1)).center(m, '-') )

print('Welcome'.center(m, '-'))

for i in range(int(n / 2) - 1, -1, -1):
    print( ('.|.' * (2*i + 1)).center(m, '-') )