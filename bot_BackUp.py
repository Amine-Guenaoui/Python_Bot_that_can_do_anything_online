import time
from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Users/amino/Desktop/PythonBo/chromedriver', options=options)
driver.maximize_window()
driver.get('https://www.omegle.com/');
time.sleep(3)
driver.find_elements_by_xpath('//*[@name="your-name"]')[0].send_keys("selenium bot")
driver.find_elements_by_xpath('//*[@name="your-email"]')[0].send_keys("selenium@bot.com")
driver.find_elements_by_xpath('//*[@name="your-message"]')[0].send_keys("Hello! =)")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.find_elements_by_xpath('//*[@value="Send"]')[0].click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.quit()
