import smtplib
#saanidhi version 
ss = smtplib.SMTP("smtp.gmail.com", 587)
ss.ehlo()
ss.starttls()
ss.login("EMAIL", "PASSWORD")

msg="Subject: Yello.\nTest mail"
to:["SENDER", "SENDER", "SENDER"]
for i in to:

    ss.sendmail("shaivyapaliwal@gmail.com" ,to ,msg)
ss.close()
