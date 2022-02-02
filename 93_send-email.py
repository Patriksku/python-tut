import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "scriptMail"
body = "hey\n my name"

# header
# Triple-quote string can span multiple lines of text
message = f"""From: Putin Rosja{sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in")
    server.sendmail(sender, receiver, message)
    print("Email has been sent.")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")

