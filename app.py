from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

opcoes = Options()
argumentos = ['--start-maximized' , '--allow-running-insecure-content' , '--disable-notifications' ]
for argument in argumentos:
   opcoes.add_argument(argument)
driver = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()),options=opcoes )
driver.get('https://pt-br.facebook.com/')
sleep(3)
e = driver.find_element(By.XPATH,'//input[@id="email"]')
sleep(2)
e.click()
email = ['s','e','u',' ','e','m','a','i','l']
senha = ['s','u','a',' ','s','e','n','h','a']
def z():
   for l in email:
     sleep(random.randint(1,2))
     e.send_keys([l])    
z()
sleep(2)
s = driver.find_element(By.XPATH,"//input[@placeholder='Senha']")
s.click()
def y():
   for l in senha:
      sleep(random.randint(1,2))
      s.send_keys([l]) 
y()
sleep(1)
botao = driver.find_element(By.XPATH,'//button[@type="submit"]')
botao.click()
sleep(10)
driver.execute_script('window.scrollTo(0,200)')
sleep(5)
postar = driver.find_element(By.XPATH,"//div[@class= 'x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe xi81zsa']")
postar.click()
sleep(5)
pronto = driver.find_element(By.XPATH,"//div[@style='user-select: text; white-space: pre-wrap; word-break: break-word; font-size: 24px;']")
pronto.click()
palavras = ['e', 's', 't','o','u',' ','p','u','b','l','i','c','a','n','d','o']
def publique():
   for l in palavras:
      sleep(random.randint(1,2))
      pronto.send_keys(l)
publique()
sleep(1)
botao = driver.find_element(By.XPATH ,"//div[@aria-label='Publicar']")
botao.click()
input('..')




