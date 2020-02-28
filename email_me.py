import getpass as gp
import smtplib
import os
import config


def send_email(msg, password, s_email):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login(config.email_address, password)
        subject = "Tutorial Example"
        _message = 'Subject: {}\n\n{}\n\n SENT BY BOT \n\n'.format(subject, msg)
        server.sendmail(config.email_address, s_email, _message)
        server.quit()
        print("Email sent!")
    except Exception as e:
        print(e)


def main():
    #pass_ = gp.getpass('Enter Email password: ')
    sender_email = input('Enter email address to send to: ')
    message = input('Enter message: ')
    send_email(msg=message, password=config.password, s_email=sender_email)


if __name__ == '__main__':
    os.system('clear')
    main()
