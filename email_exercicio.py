import os
import smtplib
from email.message import EmailMessage

from Segredos import password

# conf. email y seña
EMAIL_ADDRESS = 'diveanafletesyamarte@gmail.com'
EMAIL_PASSWORD = password

# crear un email
msg = EmailMessage()
msg['Subject'] = 'Cargo #35 arrived at the port'
msg['From'] = 'diveanafletesyamarte@gmail.com'
msg['To'] = 'diveanaflettes2@gmail.com'
msg.set_content(
    'Please look for package number 35 that just arrived at the porters office')

# enviar
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
