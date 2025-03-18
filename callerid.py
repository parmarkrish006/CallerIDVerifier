# import module
import requests
from bs4 import BeautifulSoup
 
# link for extract html data
# Making a GET request 
     
def getdata(url):
    r=requests.get(url)
    return r.text
# API key
# Enter your own API key instead of 'YOUR API KEY'
api = '2677eae8055f3d486642a017441f3bfa'

 
# number and country code
number = '919999999999'
country = 'IN'
 
# pass Your API, number and country code
# in getdata function
htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup)