# Created by rapid at 2/4/2020
Feature: Open mian page, go to careers, click QA Automation Engineer Miami button

  Scenario: QA Automation Engineer Miami is here
    Given Loginpage
    Then Click on careers button
    Then Click on QA Automation Engineer in Miami button inside the iframe
    Then Verify page has a text As QA Automation Engineer you will develop automated test solutions