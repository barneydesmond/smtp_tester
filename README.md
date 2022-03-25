quick-mail
====

This is a script I wrote for work at my first job. The idea is to replace a
manual telnet session with something scripted, with a little bit of flexibility
for targeting different SMTP servers with different parameters.

The main usage is for checking that your SMTP server is listening, reachable,
and will accept mail using to/from addresses that you expect to work. I've also
used it for poking DKIM services, to make sure they're signing the messages as
expected.
