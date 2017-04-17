Feature: New List Tests

  Scenario: Create a list and an item via POST request
    Given server is running
    When sending a POST request to '/lists/new' with item_text 'A new list item'
    Then there are 1 item(s) in the database
    And the item's text is 'A new list item'

  Scenario: Redirect after POST request
    Given server is running
    When sending a POST request to '/lists/new' with item_text 'A new list item'
    Then the server redirects to the list's view

  Scenario: Redirect on GET request
    Given server is running
    When send a GET request to '/lists/new'
    Then the server redirects to '/' without saving an item

  Scenario: Add item to an existing list
    Given server is running
    When creating a list
    And sending a POST request to '/lists/%d/add_item' with item_text 'Item for existing list'
    Then there are 1 item(s) in the database
    And the item's text is 'Item for existing list'
    And the item's list is our earlier created list

  Scenario: Redirect to list view after adding an item
    Given server is running
    When creating a list
    And sending a POST request to '/lists/%d/add_item' with item_text 'Item for existing list'
    Then the server redirects to the list's view