from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import datetime
import time


def generate_email_body():
    today = datetime.date.today()
    body = f"""
    <html>
        <body style="font-family: Arial, sans-serif; font-size: 14px; color: #333;">
            <p>Dear Team,</p>

            <p>This is a friendly reminder to <strong>save any updates made on the feature layers in the SDE</strong> before <strong>11:30 AM</strong> today.</p>

            <p>The automated DWG conversion process will run at that time, and any unsaved edits will not be included in the export.</p>

            <p><strong>Date:</strong> {today.strftime('%B %d, %Y')}</p>

            <p>Thank you for your cooperation and attention to this task.</p>

            <p>Best regards,<br>
            <em>Your Automated Reminder System</em></p>
        </body>
    </html>
    """
    return body


def send_email(
    body,
):
    from_email = "CorporateGIS@regina.ca"
    smtp_server = "smtp.city.regina.ca"
    subject = "🔔 Reminder: Save your SDE edits before 11:30 AM — automated DWG conversion scheduled"
    to_email = [
        "AZHANG@regina.ca",
        "RFAROOQ@regina.ca",
        "QWANG@regina.ca",
        "RALEJAND@regina.ca",
        "MGOODWIN@regina.ca",
        "DJORDAN@regina.ca",
        "SKICKLEY@regina.ca",
    ]
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = ", ".join(to_email)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))
    with smtplib.SMTP(smtp_server) as server:
        server.starttls()
        server.send_message(msg)


if __name__ == "__main__":
    current_time = time.localtime()

    if current_time.tm_hour == 18:
        print("6 PM, exiting.")
        exit()

    email_body = generate_email_body()
    send_email(email_body)
    print("Email sent successfully.")
    exit()
