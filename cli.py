import os
import argparse
import pandas as pd
import json
import time


def generate():
    print("generate()")

def main(args=None):
    print("CLI Arguments:", args)

    if args.generate:
        generate()


if __name__ == "__main__":
    # Generate the inputs arguments parser
    # if you type into the terminal '--help', it will provide the description
    parser = argparse.ArgumentParser(description="CLI")

    parser.add_argument(
        "--generate",
        action="store_true",
        help="Generate data",
    )

    args = parser.parse_args()

    main(args)