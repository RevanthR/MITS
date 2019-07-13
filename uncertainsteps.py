def iterative_doubling_l2r(n):
    assert n >= 0
    a, b, c = 0, 0, 1  # T(0), T(1), T(2)
    for i in range(n.bit_length() - 1, -1, -1):  # Left (MSB) to right (LSB).
        x = b*b + a*(2*(c - b) - a)
        y = a*a + b*(2*c - b)
        z = c*c + b*(2*a + b)
        bit = (n >> i) & 1
        a, b, c = (y, z, x+y+z) if bit else (x, y, z)
    return c

n=int(input())
print(iterative_doubling_l2r(n))