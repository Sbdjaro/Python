import cowsay
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("-l")

parser.parse_args()
from cowsay import cowsay

message = """
The most remarkable thing about my mother is that for thirty years she served
the family nothing but leftovers.  The original meal has never been found.
		-- Calvin Trillin
""".strip()
print(cowsay(message))