import getpass as gp
import smtplib
import os

email_address = "spicetala@gmail.com"


def send_email(msg, password, s_email):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login(email_address, password)
        subject = "Tutorial Example"
        _message = 'Subject: {}\n\n{}\n\n SENT BY RIHANNA \n\n'.format(subject, msg)
        server.sendmail(email_address, s_email, _message)
        server.quit()
        print("Email sent!")
    except Exception as e:
        print(e)


def main():
    pass_ = gp.getpass('Enter Email password: ')
    sender_email = input('Enter email address to send to: ')
    message = input('Enter message: ')
    #x = input('password: ')
    send_email(msg=message, password=pass_, s_email=sender_email)


if __name__ == '__main__':
    os.system('clear')
    main()
