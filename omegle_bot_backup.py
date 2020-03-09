import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException






interest = input("Enter the interests seperate by a comma ")
msg1 = input("Enter your first message (1/4) >> ")
msg2 = input("Enter your second message (2/4) >> ")
msg3 = input("Enter your third message (3/4) >> ")
msg4 = input("Enter your fourth message (4/4) >> ")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Users/amino/Desktop/PythonBot/chromedriver', options=options)
input_text = input("do you want to launch the Bot ? yes/no")
while input_text == "yes":
    #driver.maximize_window()
    driver.get('https://www.omegle.com/');
    time.sleep(3)
    #driver.find_elements_by_xpath('//*[@name="your-name"]')[0].send_keys("selenium bot")
    #driver.find_elements_by_xpath('//*[@name="your-email"]')[0].send_keys("selenium@bot.com")
    #driver.find_elements_by_xpath('//*[@name="your-message"]')[0].send_keys("Hello! =)")
    #time.sleep(3)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #time.sleep(3)
    driver.find_elements_by_xpath('//*[@id="chattypetextcell"]')[0].click()
    time.sleep(5)
    textarea = driver.find_element_by_tag_name('textarea')
    textarea.send_keys("Hello ")
    time.sleep(1)
    textarea.send_keys(Keys.RETURN)
    time.sleep(5)
    #driver.find_element_by_tag_name('sendbtn').click()
    time.sleep(7)
    textarea.send_keys("i always wanted to make friends :/ ,if you have discord join this server and you will find me there /n https://discord.gg/Uj9tub ")
    time.sleep(1)
    textarea.send_keys(Keys.RETURN)
    time.sleep(5)
    textarea.send_keys("i think i will have to leave ")
    textarea.send_keys(Keys.RETURN)
    time.sleep(5)
    textarea.send_keys(Keys.ESCAPE)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.quit()
    input_text = input("do you want to repeat")
