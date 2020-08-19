from behave import *

@given("Loginpage")
def open_homepage(context):
    context.app.main_page.open_page()

@then("Click on careers button")
def click_crs_btn(context):
    context.app.main_page.click_crs_btn()

@then("Click on QA Automation Engineer in Miami button inside the iframe")
def click_qa_eng_mia(context):
    context.app.main_page.click_qa_eng_mia()

@then("Verify page has a text as {text_here}")
def qa_txt_hr(context, text_here):
    context.app.main_page.qa_txt_hr(text_here)