import smtplib
from email.message import EmailMessage

sender_email = "umesh.yadav6623@gmail.com"
sender_password = "fljy kiqn rghq ahdb"

receiver_email = "umesh.yadav6623@gmail.com"

msg = EmailMessage()

msg["Subject"] = "Business Insights Report"
msg["From"] = sender_email
msg["To"] = receiver_email

msg.set_content(
    "Hello,\n\nPlease find the attached Business Insights Report."
)

# Attach Report
with open("reports/Business_Insights_Report.pdf", "rb") as f:
    pdf_data = f.read()

msg.add_attachment(
    pdf_data,
    maintype="application",
    subtype="pdf",
    filename="Business_Insights_Report.pdf"
)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.send_message(msg)

print("Email with attachment sent successfully!")