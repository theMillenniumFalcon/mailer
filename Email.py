class Email:
    '''class representing an email'''

    def __init__(self, recepient, subject, body):
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
        '''sends email'''
        
    def send_test(self):
        '''sends email'''