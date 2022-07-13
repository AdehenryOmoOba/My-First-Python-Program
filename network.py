import re

# Extract emails and urls

url_regex = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
email_regex = '[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+\.[\w]+'


fhandle = open('myInfo.txt')
emails_handle = open('emails.text', 'w')
url_handle = open('urls.text', 'w')

for line in fhandle:
    line = line.rstrip()
    email = re.findall(email_regex, line)
    url = re.findall(url_regex, line)
    if len(email) == 0 and len(url) == 0:
        continue
    if len(email) > 0:
        for email_address in email:
            emails_handle.write(email_address)
            emails_handle.write('\n')
    if len(url) > 0:
        for url_address in url:
            url_handle.write(url_address)
            url_handle.write('\n')
