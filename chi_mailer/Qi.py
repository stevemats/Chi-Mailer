#!/usr/bin/env/python
# -*- coding: utf-8 -*-
from __future__ import print_function

try:
    import smtplib
except:
    print("{ smtplib module is missing. Try installing it and try again }\n")
    exit(-1)
import time
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
from string import Template

'''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$                                                                              $$
$$ This project was written for EDUCATION PURPOSE ONLY to understand the SMTP   $$
$$ functionality as part of python programming. Any illegal use of the tool     $$
$$ such as spamming is strictly prohibited without the users consent/knowledge  $$
$$                      STAY SAFE AND KEEP CODING                               $$
$$         !THE FUTURE IS IN THE HANDS OF OPEN SOURCE DEVELOPERS!               $$
$$                                                                              $$
$$                                                                              $$
$$                                                       By Stevemats &fkinaro  $$
$$                                                                              $$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
'''
print('''


                                            __
      o                 /' ) 
                      /'   (                          ,
                  __/'     )                        .' `;
   o      _.-~~~~'          ``---..__             .'   ;
     _.--'  b)                       ``--...____.'   .'
    (     _.      )).      `-._                     <  The green shark world!!
     `\|\|\|\|)-.....___.-     `-.         __...--'-.'.
 stv   `---......____...---`.___.'----... .'         `.;
                                        `-`           `  
''')
try:
    SERVER_MAIL = input("\n >>>Enter your server email_address:".lower())
    PASSWORD = getpass(">>>Input your password:")  # 'Your server email password'
except NameError:
    input = raw_input  # python 2


def slowprint(thrasher):
    for n in thrasher + '\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(10. / 100)


slowprint("Congratulation! Now you can Take a sip of coffee as we automate your mail delivery... ")
time.sleep(5)


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():
    """ TODO: code functionality to lower all input mails to lowercase $ validate"""
    names, emails = get_contacts('contacts.txt')  # read contacts(email and username)
    message_template = read_template('message.txt')  # read message(your mail content)

    # Highly define your SMTP server here
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(SERVER_MAIL, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake(not necessary)
        print(message)

        # setup the parameters of the message
        msg['From'] = SERVER_MAIL
        msg['To'] = email
        msg['Subject'] = "This is Just A Sample Mail Test"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        """ TODO: code functionality to send mails at an interval to avoid red flags $ meet limits"""
        s.send_message(msg)
        del msg

    # s = your_server
    s.quit()
    print("Email successfully sent.")


if __name__ == '__main__':
    main()
