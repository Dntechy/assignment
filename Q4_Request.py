
import requests

BASE_URL = 'https://fakestoreapi.com'
#Randomize this data
new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}
#Send a Post requesst
response = requests.post(f"{BASE_URL}/products", json=new_product)
_response = response.json()
#breakpoint()
#Not a must to print
#print(response.json())

#Set variables from the response
product_id = _response["id"]
product_title = _response["title"]

#Now we go to the browser
#First pip install selenium

from selenium import webdriver

#driver = webdriver.Chrome('./chromedriver')
#driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(BASE_URL + "/products/" + str(product_id))
#search_bar = driver.find_element_by_xpath(//pre[contains(text(),'test product')])
breakpoint()
