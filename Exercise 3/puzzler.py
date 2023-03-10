from hashlib import sha256
import random
import string
import time

def solve(p, d):
    result = ""
    ran = ""
    
    while result[:d] != "0" * d:
        ran = "".join([random.choice(string.ascii_letters) for n in range(16)])
        result = sha256((p + ran).encode()).hexdigest()
    
    print(f"Found {ran} with hash {result}.")
    return ran

def verify(p, nonce):
    i = 0
    for c in sha256((p + nonce).encode()).hexdigest():
        if c != "0":
            return i
        i += 1


for i in range(1, 10):
    now = time.time()
    input = "puzzle"
    print(f"Starting round {i}...")
    solution = solve(input, i)
    print(f"Solution: {solution}, {'Verified!' if (verify(input, solution) == i) else 'Not Verified!'}")
    print(f"Round {i} took {time.time() - now} seconds.")
