import random

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(min_val, max_val):
    """Generates a random prime number within a specified range."""
    while True:
        num = random.randint(min_val, max_val)
        if is_prime(num):
            return num

def power(base, exp, mod):
    """Calculates (base^exp) % mod efficiently."""
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return res

def find_primitive_root(p):
    """Finds a primitive root modulo p."""
    if not is_prime(p):
        return None
    phi = p - 1
    factors = set()
    d = 2
    temp_phi = phi
    while d * d <= temp_phi:
        if temp_phi % d == 0:
            factors.add(d)
            while temp_phi % d == 0:
                temp_phi //= d
        d += 1
    if temp_phi > 1:
        factors.add(temp_phi)

    for res in range(2, p):
        is_primitive_root = True
        for factor in factors:
            if power(res, phi // factor, p) == 1:
                is_primitive_root = False
                break
        if is_primitive_root:
            return res
    return None

def diffie_hellman_key_exchange():
    """Performs the Diffie-Hellman key exchange."""
    # 1. Agree on a public prime number (p) and a primitive root (g)
    p = generate_prime(100, 500)
    g = find_primitive_root(p)

    if g is None:
        print(f"Could not find a primitive root for {p}. Aborting.")
        return

    print(f"Publicly agreed prime number (p): {p}")
    print(f"Publicly agreed primitive root (g): {g}")

    # 2. Alice's secret key (a) and public key (A)
    alice_secret = random.randint(1, p - 1)
    alice_public = power(g, alice_secret, p)
    print(f"\nAlice's secret key (a): {alice_secret}")
    print(f"Alice's public key (A): {alice_public}")

    # 3. Bob's secret key (b) and public key (B)
    bob_secret = random.randint(1, p - 1)
    bob_public = power(g, bob_secret, p)
    print(f"Bob's secret key (b): {bob_secret}")
    print(f"Bob's public key (B): {bob_public}")

    # 4. Exchange public keys (A and B)

    # 5. Alice calculates the shared secret key (s_a)
    alice_shared_secret = power(bob_public, alice_secret, p)
    print(f"\nAlice calculates shared secret (s_a): {alice_shared_secret}")

    # 6. Bob calculates the shared secret key (s_b)
    bob_shared_secret = power(alice_public, bob_secret, p)
    print(f"Bob calculates shared secret (s_b): {bob_shared_secret}")

    # Verify that the shared secrets are the same
    if alice_shared_secret == bob_shared_secret:
        print("\nShared secret key established successfully!")
        print(f"Shared secret: {alice_shared_secret}")
    else:
        print("\nError: Shared secret keys do not match!")

if __name__ == "__main__":
    diffie_hellman_key_exchange()