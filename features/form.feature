Feature: FormPage

    Scenario: Correctly fill out form gives success.
      Given I am on the Form page
      When I fill out the form
      And i click Submit
      Then I am redirected to the Thanks page
      And I get a success message


      Scenario:  Submitting a blank form returns success message.
      Given I am on the Form page
      When I clear out the form
      And I click Submit
      Then I am redirected to the Thanks page
      And I get a success message

