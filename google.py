import webbrowser
from selenium import webdriver
import time
import pandas as pd 
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys

g_translated = []

auto_ar = 'https://translate.google.co.kr/?sl=auto&tl=ar&op=translate'
auto_de = 'https://translate.google.co.kr/?sl=auto&tl=de&op=translate'
auto_en = 'https://translate.google.co.kr/?sl=auto&tl=en&op=translate'
auto_fr = 'https://translate.google.co.kr/?sl=auto&tl=fr&op=translate'
auto_it = 'https://translate.google.co.kr/?sl=auto&tl=it&op=translate'
auto_ja = 'https://translate.google.co.kr/?sl=auto&tl=ja&op=translate'
auto_ko = 'https://translate.google.co.kr/?sl=auto&tl=ko&op=translate'
auto_mn = 'https://translate.google.co.kr/?sl=auto&tl=mn&op=translate'
auto_ru = 'https://translate.google.co.kr/?sl=auto&tl=ru&op=translate'
auto_sv = 'https://translate.google.co.kr/?sl=auto&tl=sv&op=translate'
auto_vi = 'https://translate.google.co.kr/?sl=auto&tl=vi&op=translate'
auto_zh = 'https://translate.google.co.kr/?sl=auto&tl=zh-CN&op=translate'

driver = webdriver.Chrome(r'/mnt/c/Users/ccc/Desktop/DATA/DATA_EXTRACT/TED Parsing/chromedriver.exe')

while True:
  outputlan = input('어떤 언어로 번역할까요? (입력 가능 언어: ar, de, en, fr, it, ja, ko, mn, ru, sv, vi, zh)')
  if outputlan == 'ar':
    driver.get(auto_ar)
    break
  elif outputlan == 'de': 
    driver.get(auto_de)
    break  
  elif outputlan == 'en': 
    driver.get(auto_en)
    break
  elif outputlan == 'fr': 
    driver.get(auto_fr)
    break
  elif outputlan == 'it': 
    driver.get(auto_it)
    break
  elif outputlan == 'ja': 
    driver.get(auto_ja)
    break
  elif outputlan == 'ko': 
    driver.get(auto_ko)
    break    
  elif outputlan == 'mn': 
    driver.get(auto_mn)
    break
  elif outputlan == 'ru': 
    driver.get(auto_ru)
    break
  elif outputlan == 'sv': 
    driver.get(auto_sv)
    break
  elif outputlan == 'vi': 
    driver.get(auto_vi)
    break
  elif outputlan == 'zh': 
    driver.get(auto_zh)
    break    
  else:
    print('가능한 언어로 다시 입력해주세요.')
time.sleep(10)
        
Multi_lines = []

def indexer(file):
  with open(file, 'r') as f:
    for i in f.read().split('\n'):
      Multi_lines.append(i)
         
indexer('lines.txt')
  
trlen = input('몇 줄 씩 번역할까요?(숫자만 입력해 주세요)')
        
def translator():
  try:
    while Multi_lines != []:
      google_input = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
      google_input.send_keys("\n".join(Multi_lines[:int(trlen)]))
      time.sleep(3)
      translated = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[3]').get_attribute('data-text').split('\n')
      g_translated.append(translated)
      time.sleep(3)
      driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
      time.sleep(1)
      driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[2]').click()
      del Multi_lines[:int(trlen)] 
  
    driver.close()  
    df = DataFrame(g_translated).transpose()
    df.to_excel('Gtranslated.xlsx')      
    
  except:
    print('뭔가 잘못되었어!')
    df = DataFrame(g_translated).transpose()
    df.to_excel('Gtranslated.xlsx') 
    driver.close()
     
translator()
