import webbrowser
from selenium import webdriver
import time
import pandas as pd
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys

f_translated = []

ar = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[9]/span'
de = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[2]/span'
en = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[10]/span'
fr = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[22]/span'
it = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[11]/span'
ja = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[13]/span'
ko = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[24]/span'
ru = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[3]/span'
sv = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[7]/span'
vi = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[5]/span'
zh = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[14]/span'

while True:
  outputlan = input('어떤 언어로 번역할까요? (입력 가능 언어: ar, de, en, fr, it, ja, ko, ru, sv, vi, zh)')
  if outputlan == 'ar':
    flitto_lan = ar 
    break
  elif outputlan == 'de':
    flitto_lan = de 
    break
  elif outputlan == 'en':
    flitto_lan = en 
    break    
  elif outputlan == 'fr':
    flitto_lan = fr 
    break
  elif outputlan == 'it':
    flitto_lan = it 
    break
  elif outputlan == 'ja':
    flitto_lan = ja 
    break
  elif outputlan == 'ko':
    flitto_lan = ko 
    break
  elif outputlan == 'ru':
    flitto_lan = ru 
    break    
  elif outputlan == 'sv':
    flitto_lan = sv 
    break
  elif outputlan == 'vi':
    flitto_lan = vi 
    break
  elif outputlan == 'zh':
    flitto_lan = zh 
    break
  else:
    print('가능한 언어로 다시 입력해주세요.')
    
driver = webdriver.Chrome(r'/mnt/c/Users/ccc/Desktop/DATA/DATA_EXTRACT/TED Parsing/chromedriver.exe')
driver.get('https://www.flitto.com/language/translation/text')
time.sleep(10)

Multi_lines = []

def indexer(file):
  with open(file, 'r') as f:
    for i in f.read().split('\n'):
      Multi_lines.append(i)
         
indexer('lines.txt')
  
trlen = input('몇 줄 씩 번역할까요?(숫자만 입력해 주세요)')

def translator():
  language_setting = 0
  try:
    while Multi_lines != []:
      flitto_input = driver.find_element_by_id("textContent")
      flitto_input.send_keys("\n".join(Multi_lines[:int(trlen)]))
      time.sleep(3)        
      while language_setting < 1:
        driver.find_element_by_xpath('//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/label/span').click()
        driver.find_element_by_xpath(flitto_lan).click()
        time.sleep(3)
        language_setting = 1
      translated = driver.find_element_by_id("ai-result").text.split('\n')
      f_translated.append(translated)
      time.sleep(2)
      driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
      time.sleep(1)
      driver.find_element_by_xpath('//*[@id="app"]/main/section/section/section[1]/div/div[1]/article/article/div[2]/span').click()
      del Multi_lines[:int(trlen)] 

    driver.close()
    df = DataFrame(f_translated).transpose()
    df.to_excel('Ftranslated.xlsx')
    
  except:
    print('뭔가 잘못되었어!')
    df = DataFrame(f_translated).transpose()
    df.to_excel('Ftranslated.xlsx')   
    driver.close()    

translator()




