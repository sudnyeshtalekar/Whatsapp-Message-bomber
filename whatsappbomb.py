# Import selenium and other necessary libs.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# Setting up webdriver

# Uncomment below line if your using Safari web driver.
# driver = webdriver.Safari()

driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)


# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"VIT-CSE Freshers etc..."'

# Replace the below string with your own message
string = 'You are hacked!!!!'
#increase the count as many times you want to bomb the message
count=int(10)

# Getting xpath for the search menu.
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

for i in range(count):
    # xpath for typing the message
	message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
	message.send_keys(string)

    # xpath for clicking send button
	sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
	sendbutton.click()

# Closing webdriver after the sending messages.
driver.close()
