"""Load a text file as a list.

Arguments:
- text file name (and directory path, if needed)

Returns:
- A list of all words in a text file in lower case

Requires-import sys

"""
import sys


def load(file):
    """Open a text file & return a list of lower case strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\nError opening {file}")
        sys.exit(1)

if __name__ == "__main__":
    load("./chap2/2of4brif.txt")
