#!/usr/bin/python

"""
Uses standard python libraries to make an SMTP connection and attempt auth.
Sure beats using telnet manually and figuring out your own AUTH strings

Written targeting Python 2, sometime in 2009. <barney@anchor.net.au>
"""

import smtplib
import datetime
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--host", "--server", dest="server", default='localhost', help="Specify the SMTP server to connect to")
parser.add_option("--user", "--username", dest="username", default='', help="Username to authenticate as")
parser.add_option("--pass", "--password", dest="password", default='', help="Password to authenticate with")
parser.add_option("-p", "--port", type="int", dest="port", default=25, help="What port should the SMTP server be contacted on")
(options, args) = parser.parse_args()

TIMESTAMP = datetime.datetime.now().ctime()
SMTP_SERVER = options.server
SMTP_PORT   = options.port
USERNAME    = options.username
PASSWORD    = options.password


# Let's go!
mailer = smtplib.SMTP()
mailer.set_debuglevel(True)
mailer.connect(SMTP_SERVER, SMTP_PORT) # localhost:25 is the default
mailer.starttls() # Assumes the server only allows AUTH once you've STARTTLS'd
mailer.login(USERNAME, PASSWORD)
mailer.close()
