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

from constants import SUBJECT, BODY

data = None
smtp_server = "smtp.gmail.com"        
port = 587                            
sender_email = None                   
password = None                       
context = ssl.create_default_context()
server = None   

# Email class
class Email:
    '''class representing an email'''    

    def __init__(self, recepient, subject, body):
        '''Email constructor'''
        self.recepient = recepient
        self.subject = subject
        self.body = body

    def __str__(self):
        '''returns a string representation of the email'''
        return "----------------------\n" + \
            f"Recipient: {self.recepient} \n\n" + \
            f"Subject: {self.subject} \n\n" + \
            f"Body: {self.body}\n" + \
            "----------------------\n\n"

    def send(self):
        '''sends email using a mail object'''
        global sender_email, server
        msg = email.mime.multipart.MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = self.recepient
        recipients = [self.recepient]
        msg['Subject'] = self.subject
        msg.attach(email.mime.text.MIMEText(self.body, 'plain'))
        server.sendmail(sender_email, self.recepient, msg.as_string())

    def send_test(self):
        '''tests sends email using a mail object'''
        global sender_email, server
        msg = email.mime.multipart.MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email
        recipients = [sender_email]
        msg['Subject'] = self.subject
        msg.attach(email.mime.text.MIMEText(self.body, 'plain'))
        server.sendmail(sender_email, sender_email, msg.as_string())

# parse data.csv
def parse():
    global data
    if not path.isfile("data.csv"):
        raise Exception("cannot find data.csv file")
    result = pandas.read_csv("data.csv")
    if len(result) <= 1:
        raise Exception("data.csv should have  more than one row")
    if "email" not in list(result.columns):
        raise Exception("data.csv does not contain email field")
    data = result

# generates a sample mail from the data
def generate():
    '''creates a 3 sample emails to display'''
    emails = []
    records = data.to_dict('records')
    for i in range(min(3, len(data))):
        r = records[i]
        e = Email(e["email"], SUBJECT.format(**r), BODY.format(**r))
        emails.append(e)
    return emails

# run the sample
def run():
    emails = generate()
    print("Sample emails:")
    for e in emails:
        print(e)
    print("**************************************************")

# test run
def test_run():
    print("Sending sample emails to sender email")
    emails = generate()
    for e in emails:
        e.send_test()
    print("Success!")
    print("**************************************************")
    
def init_email():
    '''initializes SMTP gmail server'''
    global sender_email, password, server, port, context
    print("Please enter the appropriate information to login to email.")
    time.sleep(0.5)
    sender_email = input("Please enter your gmail. ")
    while(type(sender_email) != str 
        or len(sender_email) < 10  
        or sender_email[-10:] != "@gmail.com"):
        sender_email = input("Please enter a valid gmail. ")
    password = getpass()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls(context=context) # Secure the connection
        server.ehlo()
        server.login(sender_email, password)
        # TODO: Send email here
        # print("hi")
    except Exception as e:
        raise Exception("Invalid gmail and password combination or insecure apps disallowed\n \
        visit https://myaccount.google.com/u/3/lesssecureapps to allow less secure apps")
    print("Successfully connected to mail server")
    print("**************************************************")
    
def run_mass_emailer():
    '''run mass emailer including checks'''
    print("Running mass emailer and checks")
    global server
    if server == None:
        raise Exception("email server has not been initialized")
    run()
    confirmation = input("Is this sample correct? [y/n] ")
    if len(str(confirmation)) < 1 or str(confirmation)[0].lower() != "y":
        print("Confirmation on samples failed, please make edits and try again. ")
        return
    records = data.to_dict('records')
    for i in range(len(data)):
        r = records[i]
        e = Email(r['email'], SUBJECT.format(**r), BODY.format(**r))
        e.send()
        print(f"Email successfully sent to {r['email']}, sent {i+1}/{len(data)}")
        time.sleep(2) # google limits 80 emails a minute
    
    print(f"Successfully sent {len(data)} emails!")
    print("**************************************************")
    return 

# function for getting command line arguments
def getOptions():
    parser = argparse.ArgumentParser(description = "email parameters")
    parser.add_argument('-sample', action="store_true", help = "view sample emails")
    parser.add_argument('-test', action="store_true", help = "test emai")

    opts = vars(parser.parse_args())

    return opts

def main():
    '''entry point to program'''
    opts = getOptions()
    parse()

    if opts["sample"]:
        run()
        return
    else:
        init_email()
        if opts["test"]:
            test_run()
        else:
            run_mass_emailer()
        server.quit()
    
    
if __name__ == "__main__":
    main()
