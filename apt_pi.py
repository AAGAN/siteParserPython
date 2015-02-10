import urllib2
from bs4 import BeautifulSoup
import winsound
import time
import email
import smtplib
import random

def getPage(url):
    pageContents = urllib2.urlopen(url).read()
    return pageContents

def getDataFromPage(htmlPage):
    soup = BeautifulSoup(htmlPage)
    tag = soup.html.body.table
    availability = tag.contents[3].contents[3].contents[3].contents[5]
    return availability

def sendEmail(availability):
    msg = email.message_from_string(availability)
    msg['from'] = "email@address.com"
    msg['To'] = "email@address.com"
    msg['Subject']="Hellooo"
    s = smtplib.SMTP("smtp.live.com",587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('email@address.com', 'pass')
    s.sendmail("email@address.com", "email@address.com", msg.as_string())

    
freq = 2500
duration = 10000
url = "https://usvisa-info.com/en-ir/selfservice/ss_country_welcome"
page = getPage(url)
availability = getDataFromPage(page)
print availability
previousAvailability = availability
sendEmail(str(availability))
i = 1
    
while True:
    try:
        page = getPage(url)
    except:
        pass
    availability = getDataFromPage(page)
    if previousAvailability != availability:
        winsound.Beep(freq,duration)
        sendEmail(str(availability))
        print availability
    print i
    i = i+1
    print availability
    previousAvailability = availability
    delaySecs = random.randint(100,500)
    print delaySecs
    time.sleep(delaySecs)