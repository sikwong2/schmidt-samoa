import random

def is_prime(n: int, k: int) -> bool:
  if n <= 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  
  s, d = 0, n - 1
  while d % 2 == 0:
    d //= 2
    s += 1

  for _ in range(k):
    a = random.randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
      continue
    for _ in range(s - 1):
      x = pow(x, 2, n)
      if x == n - 1:
        break
    else:
      return False
  return True 

def make_prime() -> int:
  n = random.getrandbits(256)

  while not is_prime(n, 100):
    n = random.getrandbits(256)
  return n

def gcd(p, q):
  while q != 0:
    p, q = q, p % q
  return p

def lcm(p, q):
  return abs(p * q) // gcd(p, q)
