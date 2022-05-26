import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


service = Service('d:\\Users\\Bruno\\Desktop\\Python\\python_projects\\auto\\chromedriver.exe')
id = 'bruno'
password = 'bbc111kira'


def get_driver():
  #set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  options.add_argument('disable-blink-features=AutomationControlled')

  driver = webdriver.Chrome(service=service, options=options)
  driver.get('http://automated.pythonanywhere.com/login/')
  return driver

def main():
  driver = get_driver()
  time.sleep(3)
  idd = driver.find_element(by= 'id', value='id_username').send_keys(id)
  driver.find_element(by= 'id', value='id_password').send_keys(password + Keys.RETURN)
  
  return

print(main())