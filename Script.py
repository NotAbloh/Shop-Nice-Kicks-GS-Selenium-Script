import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# def snk_api():
#     r = requests.get('https://shopnicekicks.com/products.json') #list of product items
#     list_loaded = json.loads(r.text)['products'] #loads list of items
#
#     for product in list_loaded:
#         pro_title = product['title']
#
#         if pro_title == 'whatever shoe u want lol':
#
#             pro_url = 'https://shopnicekicks.com/products/' + product['handle']
#             print('item is found')
#             return pro_url
#     else:
#         return False



def checkout_flow(url):
    driver= webdriver.Chrome(executable_path=r'C:\Users\Tae\Desktop\chromedriver.exe') #opens selenium
    driver.get(str(url)) #opens link
    size_wanted = input(str("What size do you want?:")) #input size
    if size_wanted == "4":
        driver.find_element_by_xpath('//label[@for="option-0-0"]').click() #size 4

    elif size_wanted == "4.5":
        driver.find_element_by_xpath('//label[@for="option-0-1"]').click() #size 4.5

    elif size_wanted == "5":
        driver.find_element_by_xpath('//label[@for="option-0-2"]').click() #size 5

    elif size_wanted == "5.5":
        driver.find_element_by_xpath('//label[@for="option-0-3"]').click() #size 5.5

    elif size_wanted == "6":
        driver.find_element_by_xpath('//label[@for="option-0-4"]').click() #size 6

    elif size_wanted == "6.5":
        driver.find_element_by_xpath('//label[@for="option-0-5"]').click() #size 6.5

    driver.find_element_by_xpath('//button[@data-action="add-to-cart"]').click() #adds to cart
    time.sleep(1)
    driver.find_element_by_xpath('(//button[@class="Cart__Checkout Button Button--primary Button--full"])[2]').click() #clicks checkout
    time.sleep(.1)
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(email) #inputs email
    time.sleep(.1)
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys(f_name) #inputs first name
    time.sleep(.1)
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys(l_name) #inputs last name
    time.sleep(.1)
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys(addy) #inputs address
    time.sleep(.1)
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys(city) #inputs city
    time.sleep(.1)
    driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys(zippy) #inputs zip code
    time.sleep(.1)
    driver.find_element_by_xpath('//input[@data-backup="phone"]').send_keys(phone + u'\ue007') #inputs phone number and clicks enter
    time.sleep(1)
    driver.find_element_by_xpath('//button[@id="btn-proceed-address"]').click() #proceeds to shipping
    time.sleep(.6)
    driver.find_element_by_xpath('//button[@class="step__footer__continue-btn btn"]').click() #proceeds to payment
    time.sleep(.6)
    driver.find_element_by_xpath('//iframe[@class="card-fields-iframe"]').send_keys(card_1)# card numero
    driver.find_element_by_xpath('//iframe[@class="card-fields-iframe"]').send_keys(card_2)
    driver.find_element_by_xpath('//iframe[@class="card-fields-iframe"]').send_keys(card_3)
    driver.find_element_by_xpath('//iframe[@class="card-fields-iframe"]').send_keys(card_4)
    time.sleep(.1)
    driver.find_element_by_xpath('(//iframe[@class="card-fields-iframe"])[2]').send_keys(card_name) # card name
    time.sleep(.1)
    driver.find_element_by_xpath('(//iframe[@class="card-fields-iframe"])[3]').send_keys(month) #month
    driver.find_element_by_xpath('(//iframe[@class="card-fields-iframe"])[3]').send_keys(year) #year
    time.sleep(.1)
    driver.find_element_by_xpath('(//iframe[@class="card-fields-iframe"])[4]').send_keys(cvv) #cvv
    time.sleep(.1)
    driver.find_element_by_xpath('//button[@type = "submit"]').click() #checkout fin
    print("Script has been ran successfully")

snk_gs_link = input(str("Enter a link from SNK:"))
email = input("Enter an email:")
f_name = input("Enter your First Name:")
l_name = input("Enter your Last Name:")
addy = input("Enter your Address:")
city = input("Enter your city:")
zippy = input("Enter your zipcode:")
phone = input("Enter your phone number:")
card_1 = input("Enter your first 4 digits of your card:")
card_2 = input("Enter your second 4 digits of your card:")
card_3 = input("Enter your third 4 digits of your card:")
card_4 = input("Enter your fourth 4 digits of your card:")
card_name = input("Enter your card name:")
month = input("Enter your expiration date month:")
year = input("Enter your expiration date year:")
cvv = input("Enter your cvv (3 numbers in the back):")
print(checkout_flow(snk_gs_link))