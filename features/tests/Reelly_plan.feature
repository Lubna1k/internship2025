# Created by lubna khan at 10/31/2025
Feature: Reelly site plan

  Scenario:User can filter Off-plan projects by Announced status
    Given Open Reelly site page
    And Log in to Reelly account
    When Click on "Off-plan" in left side menu
    Then Verify Off-plan page is opened
    When Filter by sale status "Announced"
    Then Verify all projects have status "Announced"
     # Enter scenario name here
    # Enter steps here