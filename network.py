import urllib.request
import re

url = 'https://www.dr-chuck.com/page1.html'
url_regex = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'


url_handle = urllib.request.urlopen(url)

for line in url_handle:
    new_url = re.findall(url_regex, line.decode().strip())
    if len(new_url) > 0:
        print(new_url)
    print(line.decode().strip())
