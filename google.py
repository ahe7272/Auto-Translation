import webbrowser
from selenium import webdriver
import time
import pandas as pd 
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys
from googleTranslator import googleTranslator

Multi_lines = []

g_translated = []

def indexer(file):
  with open(file, 'r') as f:
    for i in f.read().split('\n'):
      Multi_lines.append(i)
         
indexer(input('어떤 파일을 번역할까요?(확장명까지 입력해 주세요) '))

savename = input('저장할 파일명을 지정해 주세요(확장명을 .xlsx로 지정해 주세요) ')
googledriver = googleTranslator(input('어떤 언어로 번역할까요? (입력 가능 언어: ar, de, en, fr, it, ja, ko, mn, ru, sv, vi, zh) '))
  
trlen = input('몇 줄 씩 번역할까요?(숫자만 입력해 주세요) ')
        
def translator():
  try:
    while Multi_lines != []:
      google_input = googledriver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
      google_input.send_keys("\n".join(Multi_lines[:int(trlen)]))
      time.sleep(1)
      translated = googledriver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div').text.split('\n')
      g_translated.append(translated)
      time.sleep(1)
      googledriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
      time.sleep(1)
      googledriver.find_element_by_xpath('//button[@jsname="X5DuWc"]').click()
      del Multi_lines[:int(trlen)] 
  
    googledriver.close()  
    df = DataFrame(g_translated).transpose()
    df.to_excel(savename)      

  except:
    print('뭔가 잘못되었어!')
    df = DataFrame(g_translated).transpose()
    df.to_excel(savename) 
    googledriver.close()
 
translator()
