"""
Nested For Loop:
    A nested loop is a loop inside a loop.
==> The "inner loop" will be executed one time for each iteration of the "outer loop":

"""
# Example:01
for i in range(0, 5):
    for j in range(0, 5):
        print(f'i values {i} and j values {j}')



# Example:02:Tables for 0 to 9
for s in range(0, 10):
    print('x' * 20)
    print(f'This is table of {s}')
    print('x' * 20)
    for k in range(0, 10):
        print(f'{k} multiplied by {s} is equal to {s * k}')
