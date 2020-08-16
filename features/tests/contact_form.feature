# Created by rapid at 8/16/2020
Feature: Fill the contact us form

  Scenario: Fill the contact us form
    Given Loginpage
    Then Click on About Us button
    Then Click on Contact button
    Then Fill the Full Name field by Randomizer
    Then Fill the Company Name field by Randomizer
    Then Fill the Email Address field by Randomizer
    Then Fill the Telephone Number field by Randomizer 10 digits
    Then Click on Region to Contact/US button
    Then Click on Interested In drop-out menu, choose Boat Group All Brands
    Then Fill the Message field by Test Message Text
    Then Fill the Enter the key field Randomizer 5 digits
    Then Click on Send message button
    Then Assert text is here The captcha field appears to be incorrect
