import requests

from bs4 import BeautifulSoup

url = "https://quiz-partie3.oc"

response = requests.get(url)

html = response.content


print(html)
soup = BeautifulSoup(html, "html.parser")
