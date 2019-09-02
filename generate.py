import argparse
from TextGenerator import TextGenerator
import sys


parser = argparse.ArgumentParser(description="ArgumentParser")
parser.add_argument(
    '--length',
    type=int,
    default=1,
    help='length of sequence, 1 by default'
    )

parser.add_argument(
    '--model',
    type=str,
    default=None,
    help="name of the '.pkl' file to load the model from"
    )

parser.add_argument(
    '--seed',
    type=str,
    default=None,
    help='a word to start the sequence with, an optional argument'
    )

args = parser.parse_args()

text_generator = TextGenerator()
try:
    text_generator.load_model(args.model)
except FileNotFoundError as err:
    print("{}:".format(err))
    print("{} not found, please try again".format(args.model))

if args.seed:
    print(text_generator.generate_text(args.length, args.seed))
else:
    print(text_generator.generate_text(args.length))
