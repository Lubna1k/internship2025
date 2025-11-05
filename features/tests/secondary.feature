# Created by lubna khan at 10/29/2025
Feature: Test for secondary page

  Scenario: User can filter the Secondary deals by the “want to buy” option
    Given Open Reelly main page
    Given User is signed into page with email "lubnakh786@gmail.com" and password "123456"
    When Click Secondary tab on side menu
    Then Verify Secondary page opend
    When Clicks on Filters
    Then step Selects the Want to buy option
    When Clicks on Apply Filter button
    Then Verify all cards have the Want to buy tag
   # Examples:
    # Enter steps here