from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    # locators
    CRS_BTN = (By.ID, "menu-item-3954") #(By.XPATH, "//li[@class='menu-item menu-item-type-post_type menu-item-object-page menu-item-3954']")
    QA_ENG_MIA = (By.XPATH, "//a[@ns-qa='QA Automation Engineer']")
    QA_TXT_HR = (By.ID, "gnewtonJobDescriptionText")

    def click_crs_btn(self):
        """
        click on careers button
        """
        self.click(*self.CRS_BTN)

    def click_qa_eng_mia(self):
        """
        click on QA Automation Engineer in Miami button inside the iframe
        """
        self.driver.switch_to.frame(self.driver.find_element_by_id("gnewtonIframe"))
        self.click(*self.QA_ENG_MIA)
        sleep(4)

    def qa_txt_hr(self, text):
        """
        verify page has a text 'As QA Automation Engineer you will develop automated test solutions'
        """
        self.verify_text(text, *self.QA_TXT_HR)