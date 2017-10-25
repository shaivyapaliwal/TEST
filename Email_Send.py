import smtplib
#saanidhi version 
ss = smtplib.SMTP("smtp.gmail.com", 587)
ss.ehlo()
ss.starttls()
ss.login("shaivyapaliwal@gmail.com", "minionslovebapples2409")

msg="Subject: Yello.\nTest mail"
to:["shaivyapaliwal@gmail.com", "shaivya_bt2k16@dtu.ac.in", "samarthgupta1011@gmail.com"]
for i in to:

    ss.sendmail("shaivyapaliwal@gmail.com" ,to ,msg)
ss.close()
