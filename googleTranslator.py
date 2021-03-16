import webbrowser
from selenium import webdriver
import time
import pandas as pd 
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys

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

    return driver  

time.sleep(3)
        