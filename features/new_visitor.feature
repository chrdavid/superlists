@e2e
Feature: TODO list
  In order to manage our daily work
  As an employee
  We'll implement a simple todo list

  @layout
  Scenario: Layout And Styling
    Given Edith has opened a browser
    When Edith goes to the home page
    Then she notices the input box nicely centered
    And she starts a new list and sees the input is nicely centered there, too

  Scenario: Start A List For One User
    Given Edith has opened a browser
    When Edith goes to the home page
    Then she notices the page title and header mention to-do lists
    Then she is invited to enter a to-do item straight away
    Then she types "Buy peacock feathers" into the text box and hit's enter
    Then the page now lists "1: Buy peacock feathers" as an item
    And there is still a text box inviting her to add another item.
    Then she types "Use peacock feathers to make a fly" into the text box and hit's enter
    And the page now lists "1: Use peacock feathers to make a fly" as an item
    And the page now lists "2: Buy peacock feathers" as an item

  Scenario: Multiple users can start lists
    Given Edith has opened a browser
    When Edith starts a new todo list
    Then She notices that her list has a unique URL
    Given Francis has opened a browser
    When Francis visits the home page, there is no sign of Edith's list
    Then Francis starts a new list by entering a new item.
    And Francis gehts his own unique URL
    And again, there is no trace of Edith's list
