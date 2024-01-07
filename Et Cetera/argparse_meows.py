# ArgumentParser
# The ' argparse' module in Python helps create a program in a command-line-environment
# in a way that appears not only easy to code but also improves interaction.

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
# Add an argument with the name "--name" and its description as "The person'

parser.add_argument("--n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print('meow')