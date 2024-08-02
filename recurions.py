


# recursion = When a thing is defined in terms of itself. - Wikipedia
#             Apply the result of a procedure, to a procedure.
#             A recursive method calls itself. Can be a substitute for iteration.
#             Divide a problem into sub-problems of the same type as the original.
#             Commonly used with advanced sorting algorithms and navigation trees.

# Advantages
# ----------
# easier to read/write
# easier to debug

# Disadvantages
# -------------
# sometimes slower
# uses more memory



def walk(n_steps):
    for i in range(n_steps):
        print('You take a step')

# walk(5)

def walk_r(n_steps):
    if n_steps == 0:
        return
    else:
        print('You take a step__recursive')
        walk_r(n_steps-1)


# walk_r(5)


def factorial(n):
    if n < 1:
        return 1
    
    return n * factorial(n-1)


# print(factorial(7))



def power(base, exponent):
    if exponent < 1: return 1
    return base * power(base, exponent-1)


print(power(2, 8))
