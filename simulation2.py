import random
import time
from simulation1 import schnorr_honest

PARAMETERS = [
    ("Small", 23, 11, 2),
    ("Medium", 1009, 7, 105),
    ("Large", 7919, 107, 6451)
    ]

print("Prime Size, Avg Time (μs)\n")

for label, p, q, g in PARAMETERS:
    x = random.randrange(1, q)

    times = []
    for _ in range(1000):
        r = random.randrange(1, q)
        c = random.randrange(1, q)
        t0 = time.perf_counter()
        schnorr_honest(p, q, g, x, r, c)
        times.append((time.perf_counter() - t0) * 1_000_000)

    avg = sum(times) / len(times)
    print(f"{label:<20} {avg:.3f}")
