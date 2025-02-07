import sys
import argparse

parser = argparse.ArgumentParser(description="Hello, World")
parser.add_argument('say', type=str, help="print something")

args = parser.parse_args()

def main():
    if args.say:
        print(args.say)

if __name__ == "__main__":
    main()
