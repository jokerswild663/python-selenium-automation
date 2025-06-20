# Created by joker at 6/16/2025
Feature: testing target cart
  # Enter feature description here

  Scenario: Cart is empty
    Given open target page target.com
    When click cart icon
    Then verify cart empty

  Scenario: Add product to Cart
    Given open target page target.com
    When target search tea
    And click add to cart from search
    And click add to cart panel
    Then verify tea in cart