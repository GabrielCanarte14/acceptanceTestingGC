# features/todo_list.feature

Feature: To-Do List Management

  Scenario: Add a single task to the to-do list
    Given the to-do list is empty
    When the user adds a task "buy groceries"
    Then the to-do list should contain "buy groceries"

  Scenario: Add multiple tasks to the to-do list
    Given the to-do list is empty
    When the user adds multiple tasks "buy groceries;wash dishes;clean room"
    Then the to-do list should contain "buy groceries"
    And the to-do list should contain "wash dishes"
    And the to-do list should contain "clean room"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks
      | task          |
      | buy groceries |
      | wash dishes   |
    When the user lists all tasks
    Then the output should contain
      | task          |
      | buy groceries |
      | wash dishes   |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks
      | task          |
      | buy groceries |
    When the user marks task "buy groceries" as completed
    Then the to-do list should show task "buy groceries" as completed

  Scenario: Clear the to-do list
    Given the to-do list contains tasks
      | task          |
      | buy groceries |
      | wash dishes   |
    When the user clears the to-do list
    Then the to-do list should be empty
