import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
    #Setting up URL of Apartment website, changing the HTML to text in order to parse through it.
    result = requests.get('https://gilberttowncommons.securecafe.com/onlineleasing/town-commons/oleapplication.aspx?stepname=Apartments&myOlePropertyId=564812&floorPlans=2203157')
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    soup_text = (soup.get_text())


    if 'Floor Plan : A3' not in soup_text:
        print("No A3s")
        # create an email message with just a subject line,
        msg1 = 'Subject: No A3 Floor Plans Available!'
        # set the 'from' address,
        fromaddr = 'pythonfrericks@gmail.com'
        # set the 'to' addresses,
        toaddrs = ['frericks@asu.edu']

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("pythonfrericks@gmail.com", "password")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg1)
        # send the email
        server.sendmail(fromaddr, toaddrs, msg1)
        # disconnect from the server
        server.quit()
        #waits 12 hours to check again
        time.sleep(43200)

    #If there is A3 available, the else executes below to notify me.
    else:
        # create an email message with just a subject line,
        msg = 'Subject: A3 Floor Plan Available!'
        # set the 'from' address,
        fromaddr = 'pythonfrericks@gmail.com'
        # set the 'to' addresses,
        toaddrs = ['frericks@asu.edu']

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("pythonfrericks@gmail.com", "password")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()