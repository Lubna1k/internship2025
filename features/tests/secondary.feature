# Created by lubna khan at 10/29/2025
Feature: Test for secondary page

  Scenario: User can filter the Secondary deals by the “want to buy” option

    Given Open Reelly main page

   #Given User is signed into page with email "lubnakh786@gmail.com" and password "123456"
   Given User is signed into page with email "lubnakh786@gmail.com" and password "123456"
    When Click on the Secondary tab on side menu
    Then Verify the right page opens
    When Clicks on Filters
    And Selects the Want to buy option
    And Clicks on Apply Filter button
   # Then Verify all cards have the Want to buy tag
    # Enter steps here