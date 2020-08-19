from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class MainPage(Page):

    # locators
    CRS_BTN = (By.ID, "menu-item-3954")
    QA_ENG_MIA = (By.XPATH, "//a[@ns-qa='QA Automation Engineer']")
    QA_TXT_HR = (By.ID, "gnewtonJobDescriptionText")
    OUR_BRANDS = (By.ID, "menu-item-12654")
    OUR_SOLUTIONS = (By.ID, "menu-item-12656")
    LATEST_RELEASES = (By.ID, "menu-item-12657")
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

    def click_crs_btn(self):
        """
        Click on careers button/Click on Careers
        """
        self.click(*self.CRS_BTN)
        sleep(2)

    def click_qa_eng_mia(self):
        """
        Click on QA Automation Engineer in Miami button inside the iframe
        """
        self.driver.switch_to.frame(self.driver.find_element_by_id("gnewtonIframe"))
        sleep(8)
        self.click(*self.QA_ENG_MIA)

    def qa_txt_hr(self, text):
        """
        Verify page has a text 'As QA Automation Engineer you will develop automated test solutions'
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

    def click_cntct_btn(self):
        """
        Click on Contact button
        """
        self.click(*self.CONTACT_BTN)

    def fill_fullname_fld(self):
        """
        Fill the Full Name field by Randomizer
        """
        # Randomizer
        password = str(randint(999, 9999))
        name = 'name' + password
        print(f'Name: {name}')
        self.driver.find_element(*self.FULL_NAME).clear()
        self.driver.find_element(*self.FULL_NAME).send_keys(name)

    def fill_company_name_fld(self):
        """
        Fill the Company Name field by Randomizer
        """
        # Randomizer
        password = str(randint(999, 9999))
        comp_name = 'name' + password
        print(f"Company Name: {((comp_name + ' ') * 2).strip(' ')}")
        self.driver.find_element(*self.COMPANY_NAME).clear()
        self.driver.find_element(*self.COMPANY_NAME).send_keys(((comp_name + ' ') * 2).strip(' '))

    def fill_email_fld(self):
        """
        Fill the Email Address field by Randomizer
        """
        # Randomizer
        password = str(randint(999, 9999))
        name = 'name' + password
        email = (name + '@sample.com')
        print(f'Email: {email}')
        self.driver.find_element(*self.EMAIL_FLD).clear()
        self.driver.find_element(*self.EMAIL_FLD).send_keys(email)

    def fill_telephone_fld(self):
        """
        Fill the Telephone Number field by Randomizer 10 digits
        """
        phone_number = str(randint(10000000000, 99999999999))
        print(f'Telephone Number: {phone_number}')
        self.driver.find_element(*self.PHN_NMBR).clear()
        self.driver.find_element(*self.PHN_NMBR).send_keys(phone_number)

    def clck_region_to_contact(self):
        """
        Click on Region to Contact/US button
        """
        self.click(*self.US_BTN)

    def clck_on_interested_in(self):
        """
        Click on Interested In drop-out menu, choose Boat Group All Brands
        """
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(*self.INTERSTED_IN).click()
        # If item has a select option
        element = wait.until(EC.visibility_of_element_located((By.ID, "interested")))
        select = Select(element)
        select.select_by_visible_text("Boats Group (All Brands)")

    def fill_message_fld(self, txt):
        """
        Fill the Message field by Test Message Text
        """
        self.input_text(txt, *self.MESSAGE_FLD)

    def fill_entr_key_fld(self):
        """
        Fill the Enter the key field Randomizer 5 digits
        """
        # Randomizer
        key = str(randint(10000, 99999))
        print(f'Key: {key}')
        self.driver.find_element(*self.ENTER_KEY_FLD).clear()
        self.driver.find_element(*self.ENTER_KEY_FLD).send_keys(key)

    def clck_send_mess_btn(self):
        """
        Click on Send message button
        """
        self.click(*self.SEND_MSG_BTN)
        sleep(4)

    def qa_txt_here(self, txt):
        """
        Assert text is here The captcha field appears to be incorrect
        """
        self.verify_text(txt, *self.ERROR)
        sleep(2)

