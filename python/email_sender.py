###### Email Sender #####

# 1. Set up 2-step authentication
# 2. Create app password: 
# 3. Create a program to send email 

from email.message import EmailMessage
import ssl 
import smtplib 

email_sender = " "  # Add email sender
email_password = " "    # Add password 

email_receiver = " "    # Receiving email 

subject = "Test Email from Pyhon" 
body = """
Hello for the other side.
"""

em = EmailMessage() 
em["From"] = email_sender
em["To"] = email_receiver 
em["subject"] = subject 
em.set_content(body) 

context = ssl.create_default_context() 

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password) 
    smtp.sendmail(email_sender, email_receiver, em.as_string())


