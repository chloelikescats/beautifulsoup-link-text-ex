#Import BeautifulSoup
from bs4 import BeautifulSoup
#import requests
import requests

#Url as variable so it can easily be changed
url = "https://sfbay.craigslist.org/search/zip"

#Get page content
page = requests.get(url)

#covert to text
data = page.text

#Parse page text using html.parser (another parser could also be used here)
soup = BeautifulSoup(data, 'html.parser')

#for all a tags with class result-title, if specified text in a tag text, 
#print a tag text.
for a_tag in soup.find_all('a', class_='result-title'):
    if 'dirt' in a_tag.text.lower():
        print a_tag.text


