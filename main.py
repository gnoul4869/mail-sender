import smtplib
import re

EMAIL_REGEX = r"^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$"

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()


while True:
    email = input("Enter your email: ")

    if not re.match(EMAIL_REGEX, email):
        print("Invalid email")
        continue

    while True:
        password = input("Enter your password: ")
        if not password:
            print("Password cannot be empty")
            continue
        break

    print('Logging in...')
    try:
        smtp_object.login(email, password)
        print('Login successful!')
        break

    except:
        print('Login failed!')


while True:
    to_address = input("Enter the email you want to send to: ")
    if not re.match(EMAIL_REGEX, to_address):
        print("Invalid email")
        continue
    break

while True:
    subject = input("Enter the subject: ")
    if not subject:
        print("Subject cannot be empty")
        continue

    break

while True:
    message = input("Enter the message: ")
    if not message:
        print("Message cannot be empty")
        continue
    break


from_address = email
email_content = f'Subject: {subject}\n{message}'
try:
    print('Sending email...')
    smtp_object.sendmail(from_address, to_address, email_content)
    print('Email sent!')
except:
    print('Email failed to send!')
finally:
    smtp_object.quit()
    exit()
