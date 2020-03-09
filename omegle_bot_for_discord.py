import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException


interest = "hate,rock,lol,games,cool,happy,sad,motivation,science,psychology,technology,computers,programming,gaming,unity,blender,godot," #input("interests")#Life love hate rock lol games bf cool happy sad music movies netflix chill programming java c# c++ c discord friends girls boys people interesting science network camera instruments piano guitar mouse keyboard everything travel hiding hiking sports family finding losing win lose relation chat converstaion 
msg0 = "F"
msg1 = "Hey ( and don't ask about age or i will leave the conversation)" #input("msg1 >> ")#Hey 
msg2 = "i hate to be rude " #input("msg3 >> ")#Btw , i'm just a dude , and i made a discord ( https://discord.gg/Uj9tub ) join and you will find what you look for  
msg3 = "xD we got the same tag that's cool" #input("msg2 >> ")#i really want to make friends and change the world
msg4 = "(if i find that you are a cool person i will share with you stuff)" #input("msg4 >>")#if you like what i did ; join and you can message me there 
msg5 = "look, i have an idea , but it's not worth sharing to anyone"
msg6 = "but if you trust me , i will tell you everything "
msg7 = "the truth is ..."
msg8 = "( my conx is a bit weird , so you may think i fast type )"
msg9 = "you know .."
msg10 = "all i wanted is to make a change , i would be really happy if you help me ."
msg11 = "oh no ! , i have to leave ASAP"
msg12 = "if you want , join my discord ( https://discord.gg/hQVnbj ) , we can keep in touch"
msg13 = "i think that you are a cool person , i like special people"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Users/amino/Desktop/PythonBot/chromedriver', options=options)

waiting_time = 20
def send(textarea,msg):
      time.sleep(5)
      textarea.send_keys(" ")      
      time.sleep(5)
      textarea.send_keys(msg)
      textarea.send_keys(Keys.RETURN)
      time.sleep(waiting_time)
      
def main():
      try:
            driver.get('http://www.omegle.com')
            time.sleep(2)
            driver.find_element_by_tag_name('textarea').clear()
            textarea = driver.find_element_by_tag_name('textarea')
            time.sleep(4)
            textarea.send_keys(" ")      
            time.sleep(5)
            textarea.send_keys(msg0)
            textarea.send_keys(Keys.RETURN)
            time.sleep(waiting_time)
            textarea.send_keys(" ")      
            time.sleep(5)
            textarea.send_keys(msg1)
            textarea.send_keys(Keys.RETURN)
            time.sleep(waiting_time)
            textarea.send_keys(" ")      
            time.sleep(5)
            textarea.send_keys(msg2)
            textarea.send_keys(Keys.RETURN)
            textarea.send_keys(" ")      
            time.sleep(5)
            textarea.send_keys(msg3)
            textarea.send_keys(Keys.RETURN)
            send(textarea,msg3)
            send(textarea,msg4)
            send(textarea,msg5)
            send(textarea,msg6)
            send(textarea,msg7)
            send(textarea,msg8)
            send(textarea,msg9)
            send(textarea,msg10)
            send(textarea,msg11)
            send(textarea,msg12)
            send(textarea,msg13)
            time.sleep(20)
            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()
            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()
            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()
      except (InvalidElementStateException, UnexpectedAlertPresentException):
            main2()
     
   
                         
   
def main2():
      try:
           
            driver.get('http://www.omegle.com')
            interest1 = driver.find_element_by_xpath('//input[@class="newtopicinput"]')
            interest1.send_keys(interest)
            time.sleep(3)
            driver.find_elements_by_xpath('//*[@id="chattypetextcell"]')[0].click()
            time.sleep(5)
            textarea = driver.find_element_by_tag_name('textarea')
            time.sleep(5)
            textarea.send_keys(" ")      
            time.sleep(5)
            textarea.send_keys(msg0)
            textarea.send_keys(Keys.RETURN)
            time.sleep(waiting_time)
            textarea.send_keys(" ")      
            time.sleep(5)
            textarea.send_keys(msg1)
            textarea.send_keys(Keys.RETURN)
            time.sleep(waiting_time)
            textarea.send_keys(" ")      
            time.sleep(5)
            textarea.send_keys(msg2)
            textarea.send_keys(Keys.RETURN)
            textarea.send_keys(" ")      
            time.sleep(5)
            textarea.send_keys(msg3)
            textarea.send_keys(Keys.RETURN)
##            send(textarea,msg3)
            send(textarea,msg4)
            send(textarea,msg5)
            send(textarea,msg6)
            send(textarea,msg7)
            send(textarea,msg8)
            send(textarea,msg9)
            send(textarea,msg10)
            send(textarea,msg11)
            send(textarea,msg12)
            send(textarea,msg13)
            time.sleep(20)
            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()
           
      except (InvalidElementStateException,UnexpectedAlertPresentException) :
            disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
            disconnect.click()
      else:
            main2()       
   
while True:
      try:
            main2()
      except (InvalidElementStateException,UnexpectedAlertPresentException) :
            main()
