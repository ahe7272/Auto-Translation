import webbrowser
from selenium import webdriver
import time
import pandas as pd 
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys

Multi_lines = []

def indexer(file):
    with open(file, 'r') as f:
        for i in f.read().split('\n'):
            Multi_lines.append(i)
         
indexer(input('어떤 파일을 번역할까요?'))

g_translated = []

def googleTranslator(language):
    urls = {
        'ar' : 'https://translate.google.co.kr/?sl=auto&tl=ar&op=translate',
        'de' : 'https://translate.google.co.kr/?sl=auto&tl=de&op=translate',
        'en' : 'https://translate.google.co.kr/?sl=auto&tl=en&op=translate',
        'fr' : 'https://translate.google.co.kr/?sl=auto&tl=fr&op=translate',
        'it' : 'https://translate.google.co.kr/?sl=auto&tl=it&op=translate',
        'ja' : 'https://translate.google.co.kr/?sl=auto&tl=ja&op=translate',
        'ko' : 'https://translate.google.co.kr/?sl=auto&tl=ko&op=translate',
        'mn' : 'https://translate.google.co.kr/?sl=auto&tl=mn&op=translate',
        'ru' : 'https://translate.google.co.kr/?sl=auto&tl=ru&op=translate',
        'sv' : 'https://translate.google.co.kr/?sl=auto&tl=sv&op=translate',
        'vi' : 'https://translate.google.co.kr/?sl=auto&tl=vi&op=translate',
        'zh' : 'https://translate.google.co.kr/?sl=auto&tl=zh-CN&op=translate'
    }
    driver  = webdriver.Chrome(executable_path='/Users/HeewonLee/Desktop/COMPUTER/CODING/chromedriver')
    driver.get(urls[language])
    
    time.sleep(3)    
    
    trlen = input('몇 줄 씩 번역할까요?(숫자만 입력해 주세요)')    
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
    
googleTranslator(input('어떤 언어로 번역할까요? (입력 가능 언어: ar, de, en, fr, it, ja, ko, mn, ru, sv, vi, zh)'))
  
time.sleep(3)
        

