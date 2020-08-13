from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    # locators
    CRS_BTN = (By.ID, "menu-item-3954")
    QA_ENG_MIA = (By.XPATH, "//a[@ns-qa='QA Automation Engineer']")
    QA_TXT_HR = (By.ID, "gnewtonJobDescriptionText")
    OUR_BRANDS = (By.ID, "menu-item-12654")
    OUR_SOLUTIONS = (By.ID, "menu-item-12656")
    LATEST_RELEASES = (By.ID, "menu-item-12657")
    ABOUT_US = (By.ID, "menu-item-12658")

    def click_crs_btn(self):
        """
        click on careers button/Click on Careers
        """
        self.click(*self.CRS_BTN)
        sleep(2)

    def click_qa_eng_mia(self):
        """
        click on QA Automation Engineer in Miami button inside the iframe
        """
        self.driver.switch_to.frame(self.driver.find_element_by_id("gnewtonIframe"))
        self.click(*self.QA_ENG_MIA)
        sleep(2)

    def qa_txt_hr(self, text):
        """
        verify page has a text 'As QA Automation Engineer you will develop automated test solutions'
        """
        self.verify_text(text, *self.QA_TXT_HR)
        sleep(2)

    def click_ors_brnds(self):
        """
        Click on Our Brands
        """
        self.click(*self.OUR_BRANDS)

    def click_ors_sltns(self):
        """
        Click on Our Solutions
        """
        self.click(*self.OUR_SOLUTIONS)

    def click_ors_rlss(self):
        """
        Click on Latest Releases
        """
        self.click(*self.LATEST_RELEASES)

    def click_ors_abtus(self):
        """
        Click on About Us
        """
        self.click(*self.ABOUT_US)