Feature: Home Page

  @unittest
  Scenario: Use home page template
    Given Server is running
    When Requesting '/'
    Then Server renders 'lists/home.html' template.

  @unittest
  Scenario: Only save item when necessary
    Given Server is running
    When Requesting '/'
    Then Item count is 0.