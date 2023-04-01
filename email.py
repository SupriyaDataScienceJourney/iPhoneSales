import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("ersupriya13@gmail.com", "******")
 
# message to be sent
# todo I need to provide the details about of the mail.
message = "Sales and Rating of Iphone "
 
# sending the mail
s.sendmail("ersupriya13@gmail.com", "abhishek.choudharry@gmail.com", message)
 
# terminating the session
s.quit()