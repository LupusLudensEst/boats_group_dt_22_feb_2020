from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# locators
ABOUT_US = (By.ID, "menu-item-12658")
CONTACT_BTN = (By.ID, "menu-item-190")
FULL_NAME = (By.ID, "name")
COMPANY_NAME = (By.ID, "company")
EMAIL_FLD = (By.ID, "email")
PHN_NMBR = (By.ID, "phone")
US_BTN = (By.CLASS_NAME, "us-label")
INTERSTED_IN = (By.ID, "interested")
MESSAGE_FLD = (By.ID, "message")
ENTER_KEY_FLD = (By.ID, "verify")
SEND_MSG_BTN = (By.ID, "send_message")
ERROR = (By.ID, "error")

# open the url
driver.get( 'https://www.boatsgroup.com/' )


# click on About Us button
driver.find_element( *ABOUT_US ).click()
sleep(2)

# click on Contact button
driver.find_element( *CONTACT_BTN ).click()
sleep(2)

# fill the Full Name field
# Randomizer
password = str(randint(999, 9999))
name = 'name' + password
print(f'Name: {name}')
driver.find_element(*FULL_NAME).clear()
driver.find_element(*FULL_NAME).send_keys(name)
sleep(2)

# fill the Company Name field
# Randomizer
password = str(randint(999, 9999))
comp_name = 'name' + password
print(f"Company Name: {((comp_name + ' ') * 2).strip(' ')}")
driver.find_element(*COMPANY_NAME).clear()
driver.find_element(*COMPANY_NAME).send_keys(((comp_name + ' ') * 2).strip(' '))
sleep(2)

# fill the Email Address field
# Randomizer
password = str(randint(999, 9999))
name = 'name' + password
email = (name + '@sample.com')
print(f'Email: {email}')
driver.find_element(*EMAIL_FLD).clear()
driver.find_element(*EMAIL_FLD).send_keys(email)
sleep(2)

# fill the Telephone Number field
# Randomizer
phone_number = str(randint(10000000000, 99999999999))
print(f'Telephone Number: {phone_number}')
driver.find_element(*PHN_NMBR).clear()
driver.find_element(*PHN_NMBR).send_keys(phone_number)
sleep(2)

# click on Region to Contact/US button
driver.find_element( *US_BTN ).click()
sleep(2)

# click on Interested In? drop-out menu, choose Boat Group (All Brands)
wait = WebDriverWait(driver, 10)
driver.find_element(*INTERSTED_IN).click()
# If item has a select option
element = wait.until(EC.visibility_of_element_located((By.ID, "interested")))
select = Select(element)
select.select_by_visible_text("Boats Group (All Brands)")

# fill the Message field by Test Message Text
driver.find_element(*MESSAGE_FLD).clear()
driver.find_element(*MESSAGE_FLD).send_keys('Test Message Text')
sleep(2)

# fill the Enter the key field
# Randomizer
key = str(randint(10000, 99999))
print(f'Key: {key}')
driver.find_element(*ENTER_KEY_FLD).clear()
driver.find_element(*ENTER_KEY_FLD).send_keys(key)
sleep(2)

# click on Send message button
driver.find_element( *SEND_MSG_BTN ).click()
sleep(2)

# assert text is here The captcha field appears to be incorrect
text = 'The captcha field appears to be incorrect'
actual_text = wait.until(EC.visibility_of_element_located((By.ID, "error"))).text
assert text in actual_text
print(f'Text is here: "{actual_text}" ')
sleep(2)

# driver quit
driver.quit()