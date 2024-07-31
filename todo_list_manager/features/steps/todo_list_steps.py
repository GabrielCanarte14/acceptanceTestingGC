from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_given_to_do_list_empty(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{task}"')
def step_when_user_adds_task(context, task):
    context.todo_list.add_task(task)

@then('the to-do list should contain "{task}"')
def step_then_to_do_list_should_contain_task(context, task):
    tasks = context.todo_list.list_tasks()
    task_list = [t["task"] for t in tasks]
    assert task in task_list, f'Task "{task}" not found in the to-do list'

@given('the to-do list contains tasks')
def step_given_to_do_list_contains_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row["task"])

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.output = context.todo_list.list_tasks()

@then('the output should contain')
def step_then_output_should_contain(context):
    expected_tasks = [row["task"] for row in context.table]
    actual_tasks = [t["task"] for t in context.output]
    assert expected_tasks == actual_tasks, f'Expected {expected_tasks}, but got {actual_tasks}'

@when('the user marks task "{task}" as completed')
def step_when_user_marks_task_completed(context, task):
    context.todo_list.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_then_to_do_list_should_show_task_completed(context, task):
    tasks = context.todo_list.list_tasks()
    for t in tasks:
        if t["task"] == task:
            assert t["status"] == "Completed", f'Task "{task}" is not marked as completed'
            break

@when('the user clears the to-do list')
def step_when_user_clears_to_do_list(context):
    context.todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_then_to_do_list_should_be_empty(context):
    tasks = context.todo_list.list_tasks()
    assert len(tasks) == 0, "To-Do list is not empty"
