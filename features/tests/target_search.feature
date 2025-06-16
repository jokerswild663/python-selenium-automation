# Created by joker at 6/8/2025
Feature: Target.com navigation
  # Enter feature description here

  Scenario Outline: Target search <entry>
    Given open target page target.com
    When target search <entry>
    Then verify search <entry>
    Examples:
    |entry|
    |chair|
    |tea  |
    |beds |