import timeit

def show_timeit(command, setup):
    print(setup + '; ' + command + ':')
    print(timeit.timeit(command, setup))
    print()

# Comparing small integers
show_timeit('a ** b', 'a = 3; b = 4')
show_timeit('pow(a, b)', 'a = 3; b = 4')
show_timeit('math.pow(a, b)', 'import math; a = 3; b = 4')

# Compare large integers to demonstrate non-constant complexity
show_timeit('a ** b', 'a = 3; b = 400')
show_timeit('pow(a, b)', 'a = 3; b = 400')
show_timeit('math.pow(a, b)', 'import math; a = 3; b = 400')

# Compare floating point to demonstrate O(1) throughout
show_timeit('a ** b', 'a = 3.; b = 400.')
show_timeit('pow(a, b)', 'a = 3.; b = 400.')
show_timeit('math.pow(a, b)', 'import math; a = 3.; b = 400.')

a = (0,0)
b = (-1,2)
print(a+b)


x = 1
print(x in [0,2])

print(10%5)

