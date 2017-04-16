@todo
Feature: TODO list
  In order to manage our daily work
  As an employee
  We'll implement a simple todo list

  @layout
  Scenario: Layout And Styling
    Given Edith has opened her browser
    When Edith goes to the home page
    Then She notices the input box nicely centered
    And She starts a new list and sees the input is nicely centered there, too

  @ux
  Scenario: Start A List For One User
    Given Edith has opened her browser
    When Edith goes to the home page
    Then She notices the page title and header mention to-do lists
    Then She is invited to enter a to-do item straight away
    Then She types "Buy peacock feathers" into the text box and hit's enter
    Then The page now lists "1: Buy peacock feathers" as an item
    And There is still a text box inviting her to add another item.
    Then She types "Use peacock feathers to make a fly" into the text box and hit's enter
    And The page now lists "1: Use peacock feathers to make a fly" as an item
    And The page now lists "2: Buy peacock feathers" as an item
