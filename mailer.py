import argparse
from re import I

# generates a sample mail from the data
def generate():
    return

# function for getting command line arguments
def getOptions():
    parser = argparse.ArgumentParser(description = "email parameters")
    parser.add_argument('-s', '--sample', required = False, type = bool, help = 'view sample emails')
    parser.add_argument('-t', '--test', required = False, type = bool, help = 'test email')

    opts = vars(parser.parse_args())

    return opts

def main():
    opts = getOptions()

    if opts["sample"]:
        print("sample")
    
    if opts["test"]:
        print("test")
    
if __name__ == "__main__":
    main()
