# Created by joker at 6/25/2025
Feature: Terms and conditions page
  # Enter feature description here

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page for terms and conditions
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
