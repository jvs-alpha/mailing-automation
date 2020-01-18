import smtplib
from email.message import EmailMessage
import sys
import os

def MailService(recv,id):
    try:
        msg = EmailMessage()
        msg["Subject"] = "test"
        msg["From"] = os.environ.get("EMAIL_USER")
        msg["To"] = recv
        msg.set_content("PDF")
        path = os.path.join(os.getcwd(),"images/")
        file = "{}{}.pdf".format(path,id)
        f = open(file,"rb")
        file_data = f.read()
        f.close()
        msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename="{}.pdf".format(id))
        mail = smtplib.SMTP_SSL("smtp.gmail.com",465)
        mail.login(os.environ.get("EMAIL_USER"),os.environ.get("EMAIL_PASSWD"))
        mail.send_message(msg)
        mail.quit()
        return True
    except:
        return False


if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print("not enough arguments")
        print("Try:")
        print("python mailservice.py <receiver_email> <Register_ID>")
        sys.exit(0)
    MailService(sys.argv[1],sys.argv[2])
