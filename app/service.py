class TaskService:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def get_all_tasks(self):
        return list(self.tasks.values())

    def create_task(self, title):
        task = {'id': self.counter, 'title': title}
        self.tasks[self.counter] = task
        self.counter += 1
        return task

    def update_task(self, task_id, title):
        if task_id not in self.tasks:
            return None
        self.tasks[task_id]['title'] = title
        return self.tasks[task_id]

    def delete_task(self, task_id):
        return self.tasks.pop(task_id, None)
