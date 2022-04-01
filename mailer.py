import argparse
import pandas
import ssl
import smtplib
import time
import email
import email.mime.multipart
import email.mime.text

from getpass import getpass
from os import path

data = None
smtp_server = "smtp.gmail.com"        
port = 587                            
sender_email = None                   
password = None                       
context = ssl.create_default_context()
server = None   

# parse data.csv
def parse():
    global data
    if not path.isfile("data.csv"):
        raise Exception("cannot find data.csv file")
    result = pandas.read_csv("data.csv")
    if len(result) <= 1:
        raise Exception("data.csv should have  more than one row")
    data = result

# generates a sample mail from the data
def generate():
    '''creates a 3 sample emails to display'''
    emails = []
    records = data.to_dict('records')
    return emails

# run the sample
def run():
    emails = generate()
    print("Sample emails:")
    for e in emails:
        print(e)

# test run
def test_run():
    print("Sending sample emails to sender email")
    emails = generate()
    for e in emails:
        e.se

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
