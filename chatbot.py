from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your WebDriver
driver_path = '/usr/bin/chromedriver'

# Instagram credentials
username = 'ahuramine'
password = 'Ehsan1402'

# Predefined response
response_message = 'Thank you for your message!'

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# Log in to Instagram
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)

username_input = driver.find_element_by_name('username')
password_input = driver.find_element_by_name('password')

username_input.send_keys(username)
password_input.send_keys(password)

password_input.send_keys(Keys.ENTER)
time.sleep(3)

# Navigate to direct messages
driver.get('https://www.instagram.com/direct/inbox/')
time.sleep(3)

# Check for new messages and reply
try:
    new_message_button = driver.find_element_by_xpath('//div[text()="New Message"]')
    new_message_button.click()
    time.sleep(2)

    # Select the first user (you might want to improve this logic)
    user_element = driver.find_element_by_xpath('//div[@role="dialog"]//div[@role="presentation"]//a')
    user_element.click()

    # Type and send the response
    message_input = driver.find_element_by_tag_name('textarea')
    message_input.send_keys(response_message)
    message_input.send_keys(Keys.ENTER)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
