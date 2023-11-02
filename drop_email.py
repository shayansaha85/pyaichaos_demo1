import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

sender_email = 'shayan851997@outlook.com'
receiver_email = 'shayan851997@gmail.com'
subject = f"Chaos Experiment Report | {datetime.now().strftime('%H:%M:%S')} IST"

file_report = open("report.html", "r")
dcontent = file_report.readlines()
file_report.close()

content = ""
for x in dcontent:
    content = content + x.strip() + "\n"

html_content = str(content)
# print(html_content)

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

html_mime = MIMEText(html_content, 'html')
message.attach(html_mime)

with smtplib.SMTP('smtp.outlook.com', 587) as server:
    server.starttls()
    server.login(sender_email, 'Shayan97@')
    server.send_message(message)

print("Email sent successfully!")
