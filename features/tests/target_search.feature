# Created by joker at 6/8/2025
Feature: Target.com navigation
  # Enter feature description here
  Scenario: Cart is empty
    Given open target.com
    When click cart icon
    Then verify cart empty

  Scenario: Sign in opened
    Given open target.com
    When click account dropdown
    When click sign in button
    Then verify sign in page loaded