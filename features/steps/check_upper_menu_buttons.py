from behave import *

@then("Click on Our Brands")
def click_urs_brnds(context):
    """
    Click on Our Brands
    """
    context.app.main_page.click_ors_brnds()


@then("Click on Our Solutions")
def click_ors_sltns(context):
    """
    Click on Our Solutions
    """
    context.app.main_page.click_ors_sltns()


@then("Click on Latest Releases")
def click_ors_rlss(context):
    """
    Click on Latest Releases
    """
    context.app.main_page.click_ors_rlss()


@then("Click on About Us")
def click_ors_abtus(context):
    """
    Click on About Us
    """
    context.app.main_page.click_ors_abtus()
