import argparse
import pandas
from os import path

data = None

# parse data.csv
def parse():
    if not path.isfile("data.csv"):
        raise Exception("cannot find data.csv file")
    result = pandas.read_csv("data.csv")
    print(result)
    print(len(result))

# generates a sample mail from the data
def generate():
    parse()
    return

# function for getting command line arguments
def getOptions():
    parser = argparse.ArgumentParser(description = "email parameters")
    parser.add_argument('-sample', action="store_true", help = "view sample emails")
    parser.add_argument('-test', action="store_true", help = "test emai")

    opts = vars(parser.parse_args())

    return opts

def main():
    opts = getOptions()

    if opts["sample"]:
        s = generate()
        print("sample")
    
    if opts["test"]:
        print("test")
    
if __name__ == "__main__":
    main()
