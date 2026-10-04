#Extended Euclidean Algorithm

def EEA(a, b):

    if b == 0:
        return a, 1, 0
    else:
        d_prime, x_prime, y_prime = EEA(b, a % b)
        q = a // b
        d, x, y = d_prime, y_prime, x_prime - q * y_prime
        print(a, b, q, d, x, y)
        return d, x, y


a, b = 53, 26
d, x, y = EEA(53, 26)

print(f"GCD: {d}, x: {x}, y: {y}")