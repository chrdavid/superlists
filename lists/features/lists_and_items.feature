Feature: Lists And Items Model Test

  Scenario: Save and load items, default order on load is ('-text',)
    Given server is running
    When creating an item with text "First Item"
    And creating an item with text "Second Item"
    Then there are 2 item(s) in the database
    And the item at position 0 has the text "Second Item"
    And the item at position 1 has the text "First Item"
