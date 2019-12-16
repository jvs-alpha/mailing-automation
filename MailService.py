import smtplib
import sys

def send_mail(sender,recv,passwd,msg):
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.starttls()
        mail.login(sender,passwd)
        mail.sendmail(sender,recv,msg)
        mail.quit()
    except SMTPException:
        print("mailing service not working")


if __name__ == "__main__":
    if(len(sys.argv) < 5):
        print("not enough arguments")
        print("Try:")
        print("python mailservice.py <sender_mail_id> <receiver_mail_id> <sender_password>")
        sys.exit(0)
    send_mail(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
