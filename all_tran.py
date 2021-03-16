import webbrowser
from selenium import webdriver
import time
import pandas as pd 
from pandas import DataFrame
from selenium.webdriver.common.keys import Keys
from googleTranslator import googleTranslator

g_translated = []
p_translated = []
f_translated = []

#Papago 언어 설정 변수
papago_de = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[8]/a/span'
papago_en = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[2]/a/span'
papago_fr = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[7]/a/span'
papago_it = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[11]/a/span'
papago_ja = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[3]/a/span'
papago_ko = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[1]/a/span'
papago_ru = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[9]/a/span'
papago_vi = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[12]/a/span'
papago_zh = '//*[@id="ddTargetLanguage"]/div[2]/ul/li[4]/a/span'

#Flitto 언어 설정 변수
flitto_ar = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[9]/span'
flitto_de = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[2]/span'
flitto_en = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[10]/span'
flitto_fr = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[22]/span'
flitto_it = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[11]/span'
flitto_ja = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[13]/span'
flitto_ko = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[24]/span'
flitto_ru = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[3]/span'
flitto_sv = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[7]/span'
flitto_vi = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[5]/span'
flitto_zh = '//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/div/div[2]/ul/li[14]/span'

while True:
  vendors = input('어떤 번역기를 사용할까요?(gp:google + papago, gf:google + flitto, pf: papago + flitto  a:all)')
  if vendors == 'gp':
    google = True
    papago = True
    flitto = False
    break
  elif vendors == 'gf':
    google = True
    papago = False
    flitto = True
    break
  elif vendors == 'pf':
    google = False
    papago = True
    flitto = True
    break
  elif vendors == 'a':
    google = True
    papago = True
    flitto = True
    break
  else:
    print('가능한 옵션을 다시 입력해주세요.')

trans_lan = input('어떤 언어로 번역할까요? (입력 가능 언어: ar(papago불가), de, en, fr, it, ja, ko, mn(papago, flitto불가), ru, sv(papago불가), vi, zh)')

while papago == True:
  if trans_lan == 'ar':
    print('Papago는 아랍어를 지원하지 않습니다. 프로그램을 종료합니다.')
    exit()
  elif trans_lan == 'de':
    papago_lan = papago_de 
    break
  elif trans_lan == 'en':
    papago_lan = papago_en 
    break    
  elif trans_lan == 'fr':
    papago_lan = papago_fr 
    break
  elif trans_lan == 'it':
    papago_lan = papago_it 
    break
  elif trans_lan == 'ja':
    papago_lan = papago_ja 
    break
  elif trans_lan == 'ko':
    papago_lan = papago_ko 
    break
  elif trans_lan == 'mn':
    print('Papago는  몽골어를 지원하지 않습니다. 프로그램을 종료합니다.')
    exit()      
  elif trans_lan == 'ru':
    papago_lan = papago_ru 
    break    
  elif trans_lan == 'vi':
    papago_lan = papago_vi 
    break
  elif trans_lan == 'zh':
    papago_lan = papago_zh 
    break
  else:
    print('가능한 언어로 다시 입력해주세요.')

while flitto == True:
  if trans_lan == 'ar':
    flitto_lan = flitto_ar 
    break
  elif trans_lan == 'de':
    flitto_lan = flitto_de 
    break
  elif trans_lan == 'en':
    flitto_lan = flitto_en 
    break    
  elif trans_lan == 'fr':
    flitto_lan = flitto_fr 
    break
  elif trans_lan == 'it':
    flitto_lan = flitto_it 
    break
  elif trans_lan == 'ja':
    flitto_lan = flitto_ja 
    break
  elif trans_lan == 'ko':
    flitto_lan = flitto_ko 
    break
  elif trans_lan == 'mn':
    print('Flitto는 몽골어를 지원하지 않습니다. 프로그램을 종료합니다.')
    exit()
  elif trans_lan == 'ru':
    flitto_lan = flitto_ru 
    break    
  elif trans_lan == 'sv':
    flitto_lan = flitto_sv 
    break
  elif trans_lan == 'vi':
    flitto_lan = flitto_vi 
    break
  elif trans_lan == 'zh':
    flitto_lan = flitto_zh 
    break
  else:
    print('가능한 언어로 다시 입력해주세요.')

if google == True:
  google_driver = googleTranslator(trans_lan)
time.sleep(5)
    
if papago == True:
  #Papago 기본 설정
  papago_link = 'https://papago.naver.com'
  papago_driver = webdriver.Chrome(executable_path='/Users/HeewonLee/Desktop/COMPUTER/CODING/chromedriver')

  papago_driver.get(papago_link)
  time.sleep(5)
  
if flitto == True:
  #Flitto 기본 설정
  flitto_link = 'https://www.flitto.com/language/translation/text'
  flitto_driver = webdriver.Chrome(executable_path='/Users/HeewonLee/Desktop/COMPUTER/CODING/chromedriver')

  flitto_driver.get(flitto_link)
  time.sleep(5)

Multi_lines = []

def indexer(file):
  with open(file, 'r') as f:
    for i in f.read().split('\n'):
      Multi_lines.append(i)
         
indexer(input('어떤 파일을 번역할까요?'))
  
trlen = input('몇 줄 씩 번역할까요?(숫자만 입력해 주세요)')
  
def translator():
  p_language_setting = 0
  f_language_setting = 0
  try:
    while Multi_lines != []:
      if google == True:         
        google_input = google_driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
        google_input.send_keys("\n".join(Multi_lines[:int(trlen)]))
        time.sleep(2)
        google_output = google_driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[3]').get_attribute('data-text').split('\n')
        g_translated.append(google_output)
        google_driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        g_refresh = google_driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[2]').click()
  
      if papago == True:
        papago_input = papago_driver.find_element_by_css_selector('textarea#txtSource')
        papago_input.send_keys("\n".join(Multi_lines[:int(trlen)]))
        time.sleep(5)      
        papago_driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        while p_language_setting < 1:
          papago_driver.find_element_by_xpath('//*[@id="ddTargetLanguageButton"]').click()
          time.sleep(2)
          papago_driver.find_element_by_xpath(papago_lan).click()
          time.sleep(2)
          p_language_setting = 1        
        papago_output = papago_driver.find_element_by_css_selector('div#txtTarget').text.split('\n')
        p_translated.append(papago_output)
        p_refresh = papago_driver.find_element_by_xpath('//*[@id="sourceEditArea"]/button').click()

      if flitto == True:
        flitto_input = flitto_driver.find_element_by_id("textContent")
        flitto_input.send_keys("\n".join(Multi_lines[:int(trlen)]))
        time.sleep(2)
        flitto_driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        while f_language_setting < 1:
          flitto_driver.find_element_by_xpath('//*[@id="app"]/main/section/section/section[1]/div/div[2]/article/article/div[1]/div[1]/label/span').click()
          flitto_driver.find_element_by_xpath(flitto_lan).click()
          time.sleep(2)
          f_language_setting = 1
        flitto_output = flitto_driver.find_element_by_id("ai-result").text.split('\n')
        f_translated.append(flitto_output)
        f_refresh = flitto_driver.find_element_by_xpath('//*[@id="app"]/main/section/section/section[1]/div/div[1]/article/article/div[2]/span').click()
      del Multi_lines[:int(trlen)] 
        
    if google == True:
      GoogleExcel = DataFrame(g_translated).transpose()
      GoogleExcel.to_excel('Gtranslated.xlsx')
      google_driver.close()
    if papago == True:
      PapagoExcel = DataFrame(p_translated).transpose()
      PapagoExcel.to_excel('Ptranslated.xlsx')   
      papago_driver.close()      
    if flitto == True:  
      FlittoExcel = DataFrame(f_translated).transpose()
      FlittoExcel.to_excel('Ftranslated.xlsx') 
      flitto_driver.close()   
  except:
    print('뭔가 잘못되었어!')
    if google == True:
      GoogleExcel = DataFrame(g_translated).transpose()
      GoogleExcel.to_excel('Gtranslated.xlsx')
      google_driver.close()
    if papago == True:
      PapagoExcel = DataFrame(p_translated).transpose()
      PapagoExcel.to_excel('Ptranslated.xlsx')   
      papago_driver.close()      
    if flitto == True:  
      FlittoExcel = DataFrame(f_translated).transpose()
      FlittoExcel.to_excel('Ftranslated.xlsx') 
      flitto_driver.close()  
      
translator()
