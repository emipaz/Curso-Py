#!/usr/bin/python3.10

# Import the Argparse package for later
import argparse

# Trigger a string output from the terminal
print('Hello from the command line!')

# Instantiate the Argparse package.
parser = argparse.ArgumentParser()
# Create an argument called name.
parser.add_argument("--name", help="Creates a new name.")
args = parser.parse_args()

# Output the name within the terminal upon calling the argument.
if args.name:
    print(f"My name is {args.name}.")