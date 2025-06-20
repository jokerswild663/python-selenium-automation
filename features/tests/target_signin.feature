# Created by joker at 6/16/2025
Feature: Testing Target Signin
  # Enter feature description here

  Scenario: Sign in opened
    Given open target page target.com
    When click account dropdown
    When click sign in button
    Then verify sign in page loaded