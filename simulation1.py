import random

def schnorr_honest(p, q, g, x, r, c):
    y = pow(g, x, p)
    R = pow(g, r, p)
    s = (r + c * x) % q

    lhs = pow(g, s, p)
    rhs = (R * pow(y, c, p)) % p

    return lhs == rhs

def schnorr_dishonest(p, q, g, y, c):
    s_fake = random.randrange(1, q)

    y_inv_c = pow(pow(y, c, p), p - 2, p)
    R_fake = (pow(g, s_fake, p) * y_inv_c) % p

    c_verifier = random.randrange(1, q)
    lhs = pow(g, s_fake, p)
    rhs = (R_fake * pow(y, c_verifier, p)) % p
    return lhs == rhs

if __name__ == "__main__":
    # Honest prover test case
    p, q, g = 23, 11, 2
    x, r, c = 3, 7, 4
    status = schnorr_honest(p, q, g, x, r, c)

    print(f"Honest status: {status}")

    # Dishonest prover test case
    p, q, g = 23, 11, 2
    c = 4
    y = pow(g, x, p)
    correct = sum(schnorr_dishonest(p, q, g, y, c) for _ in range(1000))

    print(f"Dishonest success rate: {correct / 1000:.4f} (theoretical 1/q ≈ {1 / q:.4f})")
