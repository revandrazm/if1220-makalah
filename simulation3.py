import random
import hashlib

def nizk_prove(p, q, g, x):
    r = random.randrange(1, q)
    y = pow(g, x, p)
    R = pow(g, r, p)
    
    c = int(hashlib.sha256(f"{y}{R}".encode()).hexdigest(), 16) % q
    s = (r + c * x) % q
    return y, R, c, s

def nizk_verify(p, q, g, y, R, c, s):
    lhs = pow(g, s, p)
    rhs = (R * pow(y, c, p)) % p
    return lhs == rhs

p, q, g = 23, 11, 2
x = random.randrange(1, q)

y, R, c, s = nizk_prove(p, q, g, x)
status = nizk_verify(p, q, g, y, R, c, s)

print(f"NIZK Fiat-Shamir status: {status}")
print(f"p: {p}, q: {q}, g: {g}")
print(f"x: {x}, y: {y}, R: {R}, c: {c}, s: {s}")
