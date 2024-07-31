# features/todo_list.feature

Feature: To-Do List Management
  In order to manage my tasks
  As a user
  I want to add, list, mark as complete, and clear tasks

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | task        |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      | task        |
      | Buy groceries |
      | Pay bills     |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | task        | status   |
      | Buy groceries | Pending  |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | task        |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty
