import os
import smtplib
import requests
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

dog_info = requests.get('https://api.thedogapi.com/v1/images/search').json()[0]
dog_image_url = dog_info['url']

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
MAIL_TO = os.environ.get('MAIL_TO')

msg = EmailMessage()
msg['Subject'] = 'Your dog of the day!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = [MAIL_TO]

msg.set_content(f"Have a great day :)!\n{dog_image_url}")
msg.add_alternative(f'Here is a dog image to cheer you up<br><br><img src="{dog_image_url}" width="300px"><br><br>Have a great day :)', subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
