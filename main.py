import smtplib
from getpass import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

email = input("Enter your email: ")
password = getpass("Enter your password: ")
