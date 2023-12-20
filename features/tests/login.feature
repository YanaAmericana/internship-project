# Created by yanaamericana at 12/19/23
Feature: Login
  # Enter feature description here

  Scenario: User can open change password page
    Given Open the login page
    Then Log in to the page
    When Click on settings option
    And Click on Change password option
    Then Verify the right page opens
    And Add some test password to the input fields
    And Verify the “Change password” button is available