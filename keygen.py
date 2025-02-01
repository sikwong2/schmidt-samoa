import numtheory
import argparse

def main():
  parser = argparse.ArgumentParser(description="Generates a public and private key")
  parser.add_argument(
    '-N',
    help="File to write the private key to",
    default="key.pub",
    metavar="pubkey")
  parser.add_argument(
    '-d', 
    help="File to write the public key to",
    default="key.priv",
    metavar="privkey")
  args = parser.parse_args()
  p = numtheory.make_prime()
  q = numtheory.make_prime()

  N = (p**2) * q
  d  = pow(N, -1, numtheory.lcm(p - 1, q -1))

  with open(args.N, 'w') as file:
    file.write(str(N))
  with open(args.d, "w") as file:
    file.write("$$".join([str(d), str(p*q)]))


if __name__ == "__main__":
  main()