import webbrowser
from selenium import webdriver
import time
import pandas as pd 
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys

p_translated = []

de = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[8]/a/span'
en = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[2]/a/span'
fr = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[7]/a/span'
it = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[11]/a/span'
ja = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[3]/a/span'
ko = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[1]/a/span'
ru = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[9]/a/span'
vi = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[12]/a/span'
zh = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[4]/a/span'

while True:
  outputlan = input('어떤 언어로 번역할까요? (입력 가능 언어: de, en, fr, it, ja, ko, mn, ru, vi, zh)')
  if outputlan == 'de':
    papago_lan = de 
    break
  elif outputlan == 'en':
    papago_lan = en 
    break    
  elif outputlan == 'fr':
    papago_lan = fr 
    break
  elif outputlan == 'it':
    papago_lan = it 
    break
  elif outputlan == 'ja':
    papago_lan = ja 
    break
  elif outputlan == 'ko':
    papago_lan = ko 
    break
  elif outputlan == 'mn':
    papago_lan = mn 
    break      
  elif outputlan == 'ru':
    papago_lan = ru 
    break    
  elif outputlan == 'vi':
    papago_lan = vi 
    break
  elif outputlan == 'zh':
    papago_lan = zh 
    break
  else:
    print('가능한 언어로 다시 입력해주세요.')

driver = webdriver.Chrome(r'/mnt/c/Users/ccc/Desktop/DATA/DATA_EXTRACT/TED Parsing/chromedriver.exe')
driver.get('https://papago.naver.com')
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
      papago_input = driver.find_element_by_css_selector('textarea#txtSource')
      papago_input.send_keys("\n".join(Multi_lines[:int(trlen)]))
      time.sleep(5)
      while language_setting < 1:
        driver.find_element_by_xpath('//*[@id="ddTargetLanguageButton"]').click()
        time.sleep(2)
        driver.find_element_by_xpath(papago_lan).click()
        time.sleep(1)
        language_setting = 1
      translated = driver.find_element_by_css_selector('div#txtTarget').text.split('\n')
      time.sleep(2)
      p_translated.append(translated)
      driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
      time.sleep(1)
      refreshInput = driver.find_element_by_xpath('//*[@id="sourceEditArea"]/button').click()
      del Multi_lines[:int(trlen)] 

    driver.close()  
    df = DataFrame(p_translated).transpose()
    df.to_excel('Ptranslated.xlsx')
  
  except:
    print('뭔가 잘못되었어!')
    df = DataFrame(p_translated).transpose()
    df.to_excel('Ptranslated.xlsx')
    driver.close()

translator()



           
