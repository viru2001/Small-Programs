
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
sender_mailID="sender@gmail.com"
receiver_mailID="receiver@gmail.com"
password="password"
s.login(sender_mailID,password)
message = "Enter your message here"
s.sendmail(sender_mailID,receiver_mailID , message)
s.quit()


