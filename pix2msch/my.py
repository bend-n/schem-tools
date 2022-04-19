#!/bin/env python
import argparse

try:
    import core
except ImportError:
    print("Could not import!")


parser = argparse.ArgumentParser()
parser.add_argument("-input", "-i", help="Input file", required=True)
parser.add_argument("-output", "-o", help="Output directory", required=True)
parser.add_argument("-name", "-n", help="Name", required=True)

args = parser.parse_args()

core.pix2msch(
    args.input,
    args.name,
    args.output, 
    False,
    200,
    "path")
