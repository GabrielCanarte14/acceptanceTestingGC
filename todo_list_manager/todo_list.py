# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Pending"})

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
        print("\n1. Add Task\n2. List Tasks\n3. Mark Task as Completed\n4. Clear Tasks\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            tasks = todo_list.list_tasks()
            for t in tasks:
                print(f"{t['task']} - {t['status']}")
        elif choice == '3':
            task = input("Enter task to mark as completed: ")
            todo_list.mark_task_completed(task)
        elif choice == '4':
            todo_list.clear_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
