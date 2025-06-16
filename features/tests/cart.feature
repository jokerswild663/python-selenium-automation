# Created by joker at 6/16/2025
Feature: testing target cart
  # Enter feature description here

  Scenario: Cart is empty
    Given open target page target.com
    When click cart icon
    Then verify cart empty