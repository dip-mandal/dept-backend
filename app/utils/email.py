import smtplib
from email.mime.text import MIMEText
from app.core.config import settings


def send_contact_email(name, email, subject, message):
    msg = MIMEText(f"""
New Contact Message:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
""")

    msg["Subject"] = f"Website Contact: {subject}"
    msg["From"] = settings.smtp_user
    msg["To"] = settings.admin_email

    with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as server:
        server.starttls()
        server.login(settings.smtp_user, settings.smtp_password)
        server.send_message(msg)