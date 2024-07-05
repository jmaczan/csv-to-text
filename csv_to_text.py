import pandas as pd
import argparse


def csv_to_text(path, column, output):
    file = pd.read_csv(filepath_or_buffer=path)
    concatenated = file[column].str.cat(sep=" \n ")

    with open(output, "w") as output_file:
        output_file.write(concatenated)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str)
    parser.add_argument("--column", type=str)
    parser.add_argument("--output", type=str)

    args = parser.parse_args()

    csv_to_text(path=args.path, column=args.column, output=args.output)
