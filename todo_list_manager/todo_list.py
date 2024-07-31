# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Pending"})

    def add_multiple_tasks(self, tasks):
        task_list = tasks.split(';')
        for task in task_list:
            self.add_task(task.strip())

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["status"] = "Completed"
                break

    def clear_tasks(self):
        self.tasks = []

if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Add Multiple Tasks")
        print("3. List Tasks")
        print("4. Mark Task as Completed")
        print("5. Clear Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            tasks = input("Enter multiple tasks separated by ';': ")
            todo_list.add_multiple_tasks(tasks)
        elif choice == '3':
            tasks = todo_list.list_tasks()
            for t in tasks:
                print(f"{t['task']} - {t['status']}")
        elif choice == '4':
            task = input("Enter task to mark as completed: ")
            todo_list.mark_task_completed(task)
        elif choice == '5':
            todo_list.clear_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
