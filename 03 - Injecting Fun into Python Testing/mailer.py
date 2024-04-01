from smtplib import SMTP


class Mailer:
    def __init__(self, smtp_server: SMTP):
        self.smtp_server = smtp_server

    def send(self, to_address: str, message: str):
        self.smtp_server.sendmail("from@example.com", to_address, message)
