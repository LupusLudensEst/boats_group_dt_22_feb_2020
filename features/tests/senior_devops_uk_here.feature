# Created by rapid at 2/4/2020
Feature: Open main page, go to careers, click Senior DevOps Engineer Fareham, United Kingdom button

  Scenario: Senior DevOps Engineer Fareham, United Kingdom is here
    Given Loginpage
    Then Click on careers button
    Then Click on Senior DevOps Engineer Fareham, United Kingdom button inside the iframe
    Then Verify page has a text as Senior DevOps