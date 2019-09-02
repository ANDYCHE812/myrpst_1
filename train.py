import argparse
from TextGenerator import TextGenerator


parser = argparse.ArgumentParser(description="")
parser.add_argument(
    '--input-dir',
    type=str,
    default=None,
    help='path to the text files'
    )

parser.add_argument(
    '--model',
    type=str,
    default=None,
    help='path to a file, to save the model in'
    )


args = parser.parse_args()

text_generator = TextGenerator()

if args.input_dir:
    text_generator.train(args.input_dir)
else:
    text_generator.train()

text_generator.save_model(args.model)
