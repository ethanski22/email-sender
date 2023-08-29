import os
import smtplib

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()

	smtp.login("ethanski22donotreply@gmail.com", "Donotreply@22")

	subject = "this is the subject"
	body = "this is the body"

	msg = f"Subject: {subject}\n\n{body}"

	smtp.sendmail("ethanski22donotreply@gmail.com", "ethanski22donotreply@gmail.com", msg)