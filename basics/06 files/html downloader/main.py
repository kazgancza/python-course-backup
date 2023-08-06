
import os
import sys
import urllib.parse
import validators
import requests
from datetime import datetime

print(f"Number of arguments: {len(sys.argv)}")
print(f"Arguments list: {sys.argv}")

url = "https://duckduckgo.com"
if len(sys.argv) > 1:
    url = sys.argv[1]

print(f"Website to download: {url}")

scprit_dir = os.path.dirname(__file__)
os.chdir(scprit_dir)
print(f"Current working dir: {os.getcwd()}")

if not os.path.exists("./websites"):
    os.mkdir("websites")

parsed_url = urllib.parse.urlparse(url)
print(parsed_url)

valid_flag = validators.url(url)
if valid_flag:
    print(f"URL {url} is valid")
else:    
    print(f"URL {url} is not valid")
    raise Exception("Bad URL!")


response = requests.get(url, allow_redirects=True)
if response.ok == True:
    print(f"Response ok from: {parsed_url.netloc}")
    now = datetime.now()
    date_str = now.strftime("%d.%m.%Y %H.%M.%S")
    print(date_str)
    file_name = f"./websites/{parsed_url.netloc} {date_str}.html"
    print(file_name)
    fh = open(file_name, "wb")
    fh.write(response.content)
    fh.close()
    