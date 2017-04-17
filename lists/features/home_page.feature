Feature: Home Page

  Scenario: Use home template
    Given server is running
    When requesting '/'
    Then server renders 'lists/home.html' template

  Scenario: Only save items when necessary
    Given server is running
    When requesting '/'
    Then item count is 0