#!/usr/bin/python

"""
This is the second revision of this script, now using MIME segments instead of
a raw body. It's basic, but *structured* basic.

Written targeting Python 2, sometime in 2008. <barney@anchor.net.au>
"""

# Uses standard python libraries to make an email and send it
# Sure beats using telnet manually to send messages for testing dkim signing, etc
# this creates a 3.1KiB plain text message at the recipient's end

import smtplib
import datetime
from optparse import OptionParser

from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

parser = OptionParser()
parser.add_option("-n", type="int", dest="howmany", default=1, help="Specify how many messages to send")
parser.add_option("--from", dest="fromaddr", default='support@anchor.net.au', help="What email address should the message appear to come from")
parser.add_option("--host", "--server", dest="server", default='localhost', help="Specify the SMTP server to connect to")
parser.add_option("-p", "--port", type="int", dest="port", default=25, help="What port should the SMTP server be contacted on")
(options, args) = parser.parse_args()

if len(args) != 1:
	print "I want one recipient email address"
	import sys
	sys.exit(2)
options.toaddr = args[0]


TIMESTAMP = datetime.datetime.now().ctime()
FROM        = options.fromaddr
TO          = options.toaddr
SMTP_SERVER = options.server
SMTP_PORT   = options.port


# setup the message
mail = MIMEMultipart()
mail['Subject'] = 'Test message from Anchor - run started at %s' % TIMESTAMP
mail['From'] = FROM
mail['To'] = TO
MESSAGE_BODY = '''This is a test message.

This email is a test to ensure mail is getting through.
No action is required, please go ahead and delete it.

Thank you,
The Anchor Support team

--
We're putting in some content to bulk up the body a bit. This is some of the
Python documentation about the SMTP libraries, used in this script.


The smtplib module defines an SMTP client session object that can be used to
send mail to any Internet machine with an SMTP or ESMTP listener daemon. For 
details of SMTP and ESMTP operation, consult RFC 821 (Simple Mail Transfer 
Protocol) and RFC 1869 (SMTP Service Extensions).

class SMTP(     [host[, port[, local_hostname]]])
    A SMTP instance encapsulates an SMTP connection. It has methods that 
support a full repertoire of SMTP and ESMTP operations. If the optional host 
and port parameters are given, the SMTP connect() method is called with those 
parameters during initialization. An SMTPConnectError is raised if the 
specified host doesn't respond correctly.

    For normal use, you should only require the initialization/connect, 
sendmail(), and quit() methods. An example is included below. 

A nice selection of exceptions is defined as well:

-- This has been an autogenerated test mail --

'''
txt = MIMEText(MESSAGE_BODY)
mail.attach(txt)


# send it
mailer = smtplib.SMTP()
mailer.connect(SMTP_SERVER, SMTP_PORT) # localhost:25 is the default
print "Send emails: ",
for i in range(options.howmany):
	mailer.sendmail(FROM, TO, mail.as_string())
	print i+1
mailer.close()
