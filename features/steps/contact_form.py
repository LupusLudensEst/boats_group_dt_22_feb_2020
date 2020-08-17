from behave import *


@then("Click on About Us button")
def click_ors_abtus(context):
    """
    Click on About Us
    """
    context.app.main_page.click_ors_abtus()


@then("Click on Contact button")
def click_cntct_btn(context):
    """
    Click on Contact button
    """
    context.app.main_page.click_cntct_btn()


@then("Fill the Full Name field by Randomizer")
def fill_fullname_fld(context):
    """
    Fill the Full Name field by Randomizer
    """
    context.app.main_page.fill_fullname_fld()


@then("Fill the Company Name field by Randomizer")
def fill_company_name_fld(context):
    """
    Fill the Company Name field by Randomizer
    """
    context.app.main_page.fill_company_name_fld()


@then("Fill the Email Address field by Randomizer")
def fill_email_fld(context):
    """
    Fill the Email Address field by Randomizer
    """
    context.app.main_page.fill_email_fld()


@then("Fill the Telephone Number field by Randomizer 10 digits")
def fill_telephone_fld(context):
    """
    Fill the Telephone Number field by Randomizer 10 digits
    """
    context.app.main_page.fill_telephone_fld()


@then("Click on Region to Contact/US button")
def clck_region_to_contact(context):
    """
    Click on Region to Contact/US button
    """
    context.app.main_page.clck_region_to_contact()


@then("Click on Interested In drop-out menu, choose Boat Group All Brands")
def clck_on_interested_in(context):
    """
    Click on Interested In drop-out menu, choose Boat Group All Brands
    """
    context.app.main_page.clck_on_interested_in()


@then("Fill the Message field by {txt}")
def fill_message_fld(context, txt):
    """
    Fill the Message field by Test Message Text
    """
    context.app.main_page.fill_message_fld(txt)


@then("Fill the Enter the key field Randomizer 5 digits")
def fill_entr_key_fld(context):
    """
    Fill the Enter the key field Randomizer 5 digits
    """
    context.app.main_page.fill_entr_key_fld()


@then("Click on Send message button")
def clck_send_mess_btn(context):
    """
    Click on Send message button
    """
    context.app.main_page.clck_send_mess_btn()


@then("Assert text is here {txt}")
def qa_txt_here(context, txt):
    """
    Assert text is here The captcha field appears to be incorrect
    """
    context.app.main_page.qa_txt_here(txt)