
class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.status = status
        self.completed = (status == "Done")

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"

class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        tasks = [
            Task("Create GitHub repository"),
            Task("Develop Python application"),
            Task("Write unit tests"),
            Task("Create Dockerfile"),
            Task("Configure GitHub Actions"),
            Task("Test CI/CD pipeline")
        ]

        for task in tasks[:3]:
            task.mark_completed()

        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]

def main():
    task_pool = TaskPool()
    task_pool.populate()

    open_tasks = task_pool.get_open_tasks()
    print("ToDo Tasks:")
    for task in open_tasks:
        print(task.title)

    print()

    done_tasks = task_pool.get_done_tasks()
    print("Done Tasks:")
    for task in done_tasks:
        print(task.title)


if __name__ == "__main__":
    main()
