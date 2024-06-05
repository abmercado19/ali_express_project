# Created by anita at 05/06/2024
Feature: Search products
  # This file is going to have all the tests related to searching a product and verify product details

  Scenario: Search for a product and verify it has items available
    Given I open Aliexpress page
    When I search for "instax mini"
    And I navigate to 2nd page
    And I click on the 2nd item in the list
    Then I see at least 1 item to buy