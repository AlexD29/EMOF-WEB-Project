# import requests

# api_key = 'tKyDx4oX.yanftbHH7G5eeJRORwC6SlzOGczpRhGp' # Generated in your User Profile it shows at the top in a green bar once
# team_slug = "otelul" # when you sign up you have a team, its in the URL then use that
# email_address = "stirbu.larisa@yahoo.com" # the test email


# response = requests.post(
#     "https://app.mailvalidation.io/a/" + team_slug + "/validate/api/validate/",
#     json={'email': email_address},
#     headers={
#             'content-type': 'application/json',
#              'accept': 'application/json',
#             'Authorization': 'Api-Key ' + api_key,
#              },
# )

# valid = response.json()['is_valid']
# if valid:
#     print("Valid")
# else:
#     print("Invalid")

#asta nu merge
# from ipaddress import IPv4Address, IPv6Address
# from validate_email import validate_email
# is_valid = validate_email(
#     email_address='stirbu.larisa@yahoo.com',
#     check_format=True,
#     check_blacklist=True,
#     check_dns=True,
#     dns_timeout=10,
#     check_smtp=True,
#     smtp_timeout=10,
#     smtp_helo_host='my.host.name',
#     smtp_from_address='alexandruduca29@yahoo.com',
#     smtp_skip_tls=False,
#     smtp_tls_context=None,
#     smtp_debug=False,
#     address_types=frozenset([IPv4Address]))

# print(is_valid)

# import re
# import dns.resolver
   
# addressToVerify ='stirbu.larisa@yahoo.com'
# match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

# if match == None:
#     print('Bad Syntax')
#     raise ValueError('Bad Syntax')
   
# records = dns.resolver.resolve('yahoo.com', 'MX')
# mxRecord = records[0].exchange
# mxRecord = str(mxRecord)

# print(mxRecord)

# # Get local server hostname
# host = socket.gethostname()

# # SMTP lib setup (use debug level for full output)
# server = smtplib.SMTP()
# server.set_debuglevel(0)

# # SMTP Conversation
# server.connect(mxRecord)
# server.helo(host)
# server.mail('alexandruduca29@yahoo.com')
# code, message = server.rcpt(str(addressToVerify))
# server.quit()

# # Assume 250 as Success
# if code == 250:
#     print('Success')
# else:
#     print('Bad')



#asta merge dar valideaza doar sintaxa si domeniul, nu si adresa
# from email_validator import validate_email, EmailNotValidError

# email = "sdsa83284hwensdjsjaddkskdksdk@yahoo.com"

# try:

#   # Check that the email address is valid. Turn on check_deliverability
#   # for first-time validations like on account creation pages (but not
#   # login pages).
#   emailinfo = validate_email(email, check_deliverability=False)

#   # After this point, use only the normalized form of the email address,
#   # especially before going to a database query.
#   email = emailinfo.normalized

# except EmailNotValidError as e:

#   # The exception message is human-readable explanation of why it's
#   # not a valid (or deliverable) email address.
#   print(str(e))

# print(emailinfo)

#merge dar la fel, doar domeniul si sintaxa
# from pyisemail import is_email

# address = "d@yahosdsdsd.com"
# bool_result_with_check = is_email(address, allow_gtld=False)
# detailed_result_with_check = is_email(address, allow_gtld=False, diagnose=True)
# print(detailed_result_with_check)



#asta da eroare de conexiune
# from dns import resolver
# import re
# import smtplib
# import dns.resolver

# try:
#     mx_record = resolver.resolve('yahoo.com', 'MX')

#     exchanges = [exchange.to_text().split() for exchange in mx_record]
# except (resolver.NoAnswer, resolver.NXDOMAIN, resolver.NoNameservers):
#     exchanges = []


# fromAddress = 'alexandsadsadsadsadruduca29@yahoo.com'
# #Simple Regex for syntax checking
# regex = '^[_a-z0–9-]+(.[_a-z0–9-]+)@[a-z0–9-]+(.[a-z0–9-]+)(.[a-z]{2,})$'
# # Email address to verify
# inputAddress = fromAddress
# addressToVerify = str(inputAddress)
# # # Syntax check
# match = re.match(regex, addressToVerify)
# if match == None:
#     print('Bad Syntax')
#     raise ValueError('Bad Syntax')
# # Get domain for DNS lookup
# splitAddress = addressToVerify.split('@')
# domain = str(splitAddress[1])
# print('Domain:', domain)
# # MX record lookup
# records = dns.resolver.resolve(domain, 'MX')
# mxRecord = records[0].exchange
# mxRecord = str(mxRecord)
# # SMTP lib setup (use debug level for full output)
# server = smtplib.SMTP()
# server.set_debuglevel(0)
# # SMTP Conversation
# mailserver = smtplib.SMTP('mail.gmx.com',587)
# server.connect(mxRecord)
# server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
# server.mail(fromAddress)
# code, message = server.rcpt(str(addressToVerify))
# server.quit()

# if code == 250:
#     print('Success')
# else: 
#     print('Bad')