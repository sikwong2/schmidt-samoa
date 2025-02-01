import argparse
import sys

def decode(c: int) -> str:
    m = ""

    while c > 0:
        m += chr(c % 256)
        c //= 256

    return m
def decrypt(c: int, d: int, n: int) -> int:
  m = pow(c, d, n)
  return m

def main():
  parser = argparse.ArgumentParser(description="Decrypts a file using Schmidt-Samoa")
  parser.add_argument(
    '-i',
    help="File to decrypt",
    metavar="input",
    # required=True
  )
  parser.add_argument(
    '-o',
    help="File to write the text to",
    metavar="output",
    # required=True
  )
  parser.add_argument(
    '-N',
    help="Public key to use",
    metavar="pubkey",
    default="key.pub"
  )
  parser.add_argument(
    '-d',
    help="Private key to use",
    metavar="privkey",
    default="key.priv"
  )
  args = parser.parse_args()
  
  try:
    with open(args.i, "r") as file:
      ciphertext = file.read().strip()
  except:
    sys.stderr.write("Input file does not exist\n")
    sys.exit(1)

  try:
    with open(args.N, "r") as file:
      pubkey = file.read().strip()
  except:
    sys.stderr.write("Public key file does not exist\n")
    sys.exit(1)

  try:
    with open(args.d, "r") as file:
      d, n = file.read().split("$$")

  except: 
    sys.stderr.write("Private key file does not exist\n")
    sys.exit(1)

  with open(args.o, "w") as file:
    text = decrypt(int(ciphertext), int(d), int(n))
    decoded_message = decode(text)
    file.write(decoded_message)

if __name__ == "__main__":
  main()