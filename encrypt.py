import argparse
import sys
def encode(m: str) -> int:
    c = 0
    power = 1

    for char in m:
        c += ord(char) * power
        power *= 256

    return c

def encrypt(m: int, N: int) -> int:
  c = pow(m, N, N)
  return c

def main():
  parser = argparse.ArgumentParser(description="Encrypts a file using Schmidt-Samoa")
  parser.add_argument(
    '-i',
    help="File to encrpyt",
    metavar="input",
    # required=True
  )
  parser.add_argument(
    '-o',
    help="File to write the ciphertext to",
    metavar="output",
    # required=True
  )
  parser.add_argument(
    '-N',
    help="Public key to use",
    metavar="pubkey",
    default="key.pub"
  )
  args = parser.parse_args()
  
  try:
    with open(args.i, "r") as file:
      text = file.read()
  except:
    sys.stderr.write("Input file does not exist\n")
    sys.exit(1)

  try:
    with open(args.N, "r") as file:
      pubkey = file.read().strip()
  except:
    sys.stderr.write("Public key file does not exist\n")
    sys.exit(1)
  # text = int.from_bytes(text.encode(), byteorder="big")
  
  try:
    with open(args.o, "w") as file:
      cipertext = encrypt(encode(text), int(pubkey))
      file.write(str(cipertext))
  except:
    sys.stderr.write("something went wrong idk\n")
    sys.exit(1)

if __name__ == "__main__":
  main()