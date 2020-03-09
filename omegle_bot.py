import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException






interest = "love hate rock lol games bf cool happy sad music movies science psychology " #input("interests")#Life love hate rock lol games bf cool happy sad music movies netflix chill programming java c# c++ c discord friends girls boys people interesting science network camera instruments piano guitar mouse keyboard everything travel hiding hiking sports family finding losing win lose relation chat converstaion 
msg1 = "Hey" #input("msg1 >> ")#Hey 
msg3 = "Btw , i'm just a dude , and i made a discord ( https://discord.gg/Uj9tub ) join and you will find what you look for" #input("msg3 >> ")#Btw , i'm just a dude , and i made a discord ( https://discord.gg/Uj9tub ) join and you will find what you look for  
msg2 = "i really want to make friends and change the world" #input("msg2 >> ")#i really want to make friends and change the world
msg4 = "if you like what i did ; join and you can message me there" #input("msg4 >>")#if you like what i did ; join and you can message me there 
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Users/amino/Desktop/PythonBot/chromedriver', options=options)

def main():
      try:
            
            driver.get('https://soundcloud.com/kickthegeek/timeframe')
            time.sleep(3)
            driver.find_element_by_class_name('playControl sc-ir playControls__control playControls__play playing').click()
            time.sleep(10)
            driver.execute_script("location.reload();")
      except (InvalidElementStateException, UnexpectedAlertPresentException):
            main()                      
          
   
while True:
            main()
      
