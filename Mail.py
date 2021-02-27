import smtplib, ssl


class Mail:
    def __init__(self,
                 senderEmail,
                 senderPassword,
                 *kargs,
                 PORT=587,
                 SMTP_SERVER="smtp.gmail.com"):

        self.senderEmail = senderEmail
        self.senderPassword = senderPassword
        self.PORT = PORT
        self.SMTP_SERVER = SMTP_SERVER

    def sendMail(self, message, reciverEmail):

        context = ssl.create_default_context()
        with smtplib.SMTP(self.SMTP_SERVER, self.PORT) as server:
        
            try:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(self.senderEmail, self.senderPassword)

                server.sendmail(self.senderEmail, reciverEmail, message)

                return f"Mail sent : {reciverEmail}"
            except:
                return f"Mail not sent : {reciverEmail}"


if __name__ == "__main__":

    newMail = Mail("Email", "Password")
    print(newMail.sendMail("Hi", "Email"))