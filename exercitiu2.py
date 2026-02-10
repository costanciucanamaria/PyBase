from encodings.punycode import selective_find


# Scrieti o clasa TaskManager, care stocheaza o lista de task-uri in ea, si care are mai multe functii pentru management-ul task-urilor

# Puteti folosi un array simplu [] ca o variabila in clasa, pentru a stoca task-urile.
# Un task este un dictionar care contine urmatoarele informatii:
# { description: "test description", done: False }
# description este descrierea task-ului
# done, care poate fi True sau False, este starea unui task, daca a fost completata inca, sau nu.

# Creati urmatoarele functii:
# .add_task(task), care adauga un task in lista de task-uri, in aceasta clasa
# .remove_task(task_description), care sterge un task din lista
# .mark_as_done(task_description), care gaseste un task dupa description, si ii schimba proprietatea "done" din False in True
# .get_pending_tasks(), care returneaza o lista de task-uri care nu au fost copmletate, deci care au proprietatea "done" ca fiind False.

# Exemplu cod:

# manager = TaskManager()
# manager.add_task({"description": "task 1 to be done", "done": False})
# manager.add_task({"description": "t2 task", "done": False})
# manager.add_task({"description": "t3333 task", "done": False})
#
# manager.remove_task("task 1 to be done")
# manager.mark_as_done("t2 task")
# manager.get_pending_tasks() -> [{"description": "t3333 task", "done": False}]

class TaskManager:
    def __init__(self):
        self.tasks = []

    def __str__(self):
        return str(self.tasks)

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_description):
        self.tasks = [
            task for task in self.tasks
            if task["description"] != task_description
        ]

    def mark_as_done(self, task_description):
        for task in self.tasks:
            if task.get("description") == task_description:
                task["done"] = True
                break
    def get_pending_tasks(self):
        return [
            task for task in self.tasks
            if task.get("done") is False
        ]

manager = TaskManager()


manager.add_task({"description": "task 1 to be done", "done": False})
manager.add_task({"description": "t2 task", "done": False})
manager.add_task({"description": "t3333 task", "done": False})

manager.remove_task("task 1 to be done")
manager.mark_as_done("t2 task")

print(manager.get_pending_tasks())


