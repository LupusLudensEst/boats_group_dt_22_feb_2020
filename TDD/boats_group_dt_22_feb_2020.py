from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# locators
CRS_BTN = (By.XPATH, "//li[@class='menu-item menu-item-type-post_type menu-item-object-page menu-item-3954']")
QA_ENG_MIA = (By.XPATH, "//a[@ns-qa='QA Automation Engineer']")
QA_TXT_HR = (By.ID, "gnewtonJobDescriptionText")

# open the url
driver.get( 'https://www.boatsgroup.com/' )

# click on careers button
driver.find_element( *CRS_BTN ).click()

# click on QA Automation Engineer in Miami button inside the iframe
driver.switch_to.frame(driver.find_element_by_id("gnewtonIframe"))
sleep(2)
driver.find_element( *QA_ENG_MIA ).click()

# verify page has a text 'As QA Automation Engineer you will develop automated test solutions'
actual_text = driver.find_element( *QA_TXT_HR ).text
assert 'As QA Automation Engineer you will develop automated test solutions' in actual_text
print(f'Text is here:\n {actual_text[:150]}...to be continued!')

# driver quit
driver.quit()
