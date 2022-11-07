Feature: Homepage

  Scenario: Redirect to Complete Web Form page
    Given I am on the Homepage
    When I click the "Complete Web Form" link
    Then I am redirected to Form page

  Scenario: Components menu displays a drop down menu with 14 options
    Given I am on the Homepage
    When I click the "Components"
    Then Drop down menu with 14 items is displayed