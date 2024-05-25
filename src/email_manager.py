from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from model import EmailModel

env_set = load_dotenv()

def send(email: EmailModel):
    if not env_set: 
        raise Exception("Environment variables are not set. ")
    
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv('EMAIL_PASSWORD')

    # Create the email headers and body
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email.to
    msg["Subject"] = email.subject
    msg.attach(MIMEText(email.body, "plain"))

    # Connect to the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, email.to, msg.as_string())
    server.quit()
