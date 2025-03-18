
import requests
from bs4 import BeautifulSoup
 

     
def getdata(url):
    r=requests.get(url)
    return r.text

api = '2677eae8055f3d486642a017441f3bfa'


number = '919999999999'
country = 'IN'

htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup)
