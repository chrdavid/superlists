Feature: List View Test

  Scenario: Use list template
    Given server is running
    When creating a list
    And opening the view for the list
    Then server renders 'lists/list.html' template

  Scenario: Display only items for one list
    Given server is running
    When creating a list
    And adding an item with text "first list - item 1" to the list
    And adding an item with text "first list - item 2" to the list
    And creating another list
    And adding an item with text "second list - item 1" to the other list
    And adding an item with text "second list - item 2" to the other list
    And opening the view for the other list
    Then the response contains "second list - item 1"
    And the response contains "second list - item 2"
    And the response does not contain "first list - item 1"
    And the response does not contain "first list - item 2"

  Scenario: Pass correct list item to template
    Given server is running
    When creating a list
    And opening the view for the list
    Then the response context references this list
