import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time
import hidden

# Your Gmail credentials
email_address = hidden.gmail  # Replace with your Gmail address
email_password = hidden.password  # Replace with your Gmail password

emails = hidden.mailids

def send_email(receiver_email, subject, message_text, image_path):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the message to the email
    message.attach(MIMEText(message_text, 'plain'))

    # Attach the image
    with open(image_path, 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-Disposition', 'attachment', filename='image.jpg')
        message.attach(img)

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your Gmail account
    server.login(email_address, email_password)

    # Send the email
    server.sendmail(email_address, receiver_email, message.as_string())

    # Quit the SMTP server
    server.quit()

subject = hidden.sub

message_text = hidden.message

image_path = 'img.jpg'  # Replace with the path to your image file

for email in emails:
    time.sleep(2)
    try:
        send_email(email, subject, message_text, image_path)
        print(f"Email sent to {email}")
    except Exception as e:
        print(f"Failed to send email to {email}: {str(e)}")
