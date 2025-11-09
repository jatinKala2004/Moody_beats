import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_contact_email(name, email, message):
    sender_email = 'kalajatin94@gmail.com'
    sender_password = 'pmkhosujeifruwkx'
    receiver_email = 'kalajatin94@gmail.com'

    subject = f'Contact Us Form Submission from {name}'
    body = f"""
    Name: {name}
    Email: {email}
    Message: {message}
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f'Error sending email: {e}')
        return False 